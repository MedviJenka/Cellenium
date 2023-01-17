import cv2
import numpy as np
from core.components.functional.methods import read_json, read_config
from skimage.metrics import structural_similarity
from dataclasses import dataclass


@dataclass
class InputData:

    original: str
    actual: str
    save: str
    success_rate: int
    resolution: list[int]
    break_test: bool


class CompareImages:

    """
    :param: original ................ path for original image to compare
    :param: compare ................. path for screenshot
    :param: save .................... path for save images
    :param: success_rate ............ wanted percentage of success
    :param: resolution .............. image resolution
    :param: break_test .............. choose if the test will be stopped
    """

    @staticmethod
    def _image_name(path: str) -> str:
        image_path = path.split('\\')[-1]
        image = image_path.partition('.')[0]
        return image

    def compare_images(self, path: str) -> str:
        data = InputData(**read_json(path))
        # load and resize images
        before = cv2.imread(data.original)
        after = cv2.imread(data.actual)

        before = cv2.resize(before, data.resolution)
        after = cv2.resize(after, data.resolution)
        before = cv2.resize(before, data.resolution)
        after = cv2.resize(after, data.resolution)

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
        result_text = f"Image Similarity: {result:.1f}%"
        cv2.imwrite(fr'{data.save}/{self._image_name(data.actual)}.png', after)
        cv2.destroyAllWindows()

        if data.break_test:
            if result >= data.success_rate:
                return f"GOOD , {result_text}"
            else:
                raise Exception(f"LOW SIMILARITY ({result_text}), CONSULT WITH THE DEVELOPER")
        else:
            pass


if __name__ == '__main__':
    app = CompareImages()
    app.compare_images(read_config('json', 'image_compare_data'))
