import cv2
import numpy as np
from skimage.metrics import structural_similarity
import os


class Logic:

    """
    :param: original ................ path for original image to compare
    :param: compare ................. path for screenshot
    :param: success_rate ............ wanted percentage of success
    :param: resolution .............. image resolution
    :param: break_test .............. choose if the test will be stopped
    """

    @staticmethod
    def _image_name(actual_image_path: str) -> str:
        image_name = os.path.split(actual_image_path)
        return image_name[1]

    def compare_images(self,
                       original_image_path: str,
                       actual_image_path: str,
                       success_rate: int,
                       resolution: list[int, int],
                       break_test: bool) -> str:

        # load and resize images
        before = cv2.imread(original_image_path)
        after = cv2.imread(actual_image_path)

        before = cv2.resize(before, resolution)
        after = cv2.resize(after, resolution)
        before = cv2.resize(before, resolution)
        after = cv2.resize(after, resolution)

        # Convert images to grayscale
        before_gray = cv2.cvtColor(before, cv2.COLOR_BGR2GRAY)
        after_gray = cv2.cvtColor(after, cv2.COLOR_BGR2GRAY)
        score, diff = structural_similarity(before_gray, after_gray, full=True)

        diff = (diff * 255).astype("uint8")
        diff_box = cv2.merge([diff, diff, diff])

        # Threshold the difference image, followed by finding contours to
        # obtain the regions of the two input images that differ
        thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = contours[0] if len(contours) == 2 else contours[1]

        mask = np.zeros(before.shape, dtype='uint8')
        filled_after = after.copy()

        for i in contours:
            area = cv2.contourArea(i)
            if area > 40:
                x, y, w, h = cv2.boundingRect(i)
                cv2.rectangle(before, (x, y), (x + w, y + h), (36, 255, 12), 1)
                cv2.rectangle(after, (x, y), (x + w, y + h), (36, 255, 12), 1)
                cv2.rectangle(diff_box, (x, y), (x + w, y + h), (0, 255, 0), 1)
                cv2.drawContours(mask, [i], 0, (255, 255, 255), -1)
                cv2.drawContours(filled_after, [i], 0, (250, 0, 0), -1)

        cv2.imshow('before', before)
        cv2.imshow('after', after)

        result = score * 100

        cv2.imwrite(fr'{actual_image_path}/{self._image_name(actual_image_path)}.png', after)
        cv2.destroyAllWindows()

        if break_test:
            if result >= success_rate:
                return f"Image Similarity: {result:.1f}%"
            else:
                raise Exception(f"LOW SIMILARITY ({result}/100%), CONSULT WITH THE DEVELOPER")
        else:
            pass
