import numpy as np
import cv2
from skimage.metrics import structural_similarity
import os


class Logic:

    @staticmethod
    def _get_image_name(actual_image_path: str) -> dict[str]:
        image_name = os.path.split(actual_image_path)
        return {
            "folder_path": image_name[0],
            "image_name": image_name[1]
        }

    def compare_images(self,
                       original_image_path: str,
                       actual_image_path: str,
                       image_resolution: list[int, int]) -> float:

        before = cv2.imread(original_image_path)
        after = cv2.imread(actual_image_path)
        # log.info(f" Test: {test_name}, load and resize images")

        before = cv2.resize(before, image_resolution)
        after = cv2.resize(after, image_resolution)
        # log.debug(f"Test: {test_name}, resolution is set to: {image_resolution}")

        before_gray = cv2.cvtColor(before, cv2.COLOR_BGR2GRAY)
        after_gray = cv2.cvtColor(after, cv2.COLOR_BGR2GRAY)
        # log.debug(f"Test: {test_name}, "
        #           f"converting images to grayscale, before: \n{before}, after: \n{after}]")

        score, diff = structural_similarity(before_gray, after_gray, full=True)
        # log.debug(f"Test: {test_name}, "
        #           f"calculating structural similarity differences, score: {score}, diff: {diff}")

        diff = (diff * 255).astype("uint8")
        diff_box = cv2.merge([diff, diff, diff])

        thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = contours[0] if len(contours) == 2 else contours[1]
        # log.debug(f"Test: {test_name}, "
        #           f"threshold the difference image, followed by finding"
        #           f"contours to obtain the regions of the two input images that differ {contours}")

        mask = np.zeros(before.shape, dtype='uint8')
        filled_after = after.copy()
        # log.debug(f'Test: {test_name}, filler: {filled_after}')

        for i in contours:
            area = cv2.contourArea(i)
            if area > 40:
                x, y, w, h = cv2.boundingRect(i)
                cv2.rectangle(before, (x, y), (x + w, y + h), (36, 255, 12), 1)
                cv2.rectangle(after, (x, y), (x + w, y + h), (36, 255, 12), 1)
                cv2.rectangle(diff_box, (x, y), (x + w, y + h), (0, 255, 0), 1)
                cv2.drawContours(mask, [i], 0, (255, 255, 255), -1)
                cv2.drawContours(filled_after, [i], 0, (250, 0, 0), -1)
            # log.debug(f'{test_name}, {area}')

        cv2.imshow('before', before)
        cv2.imshow('after', after)
        image_name = self._get_image_name(actual_image_path)['image_name']
        image_path_folder = self._get_image_name(actual_image_path)['folder_path']
        cv2.imwrite(f'{image_path_folder}\\rectangle_result_{image_name}', before)
        # log.debug(f'Test: {test_name}, saving images in: {image_path_folder}')
        result = score * 100
        cv2.destroyAllWindows()

        return result

    @staticmethod
    def generate_rectangles(result: float, success_rate: int, break_test: bool) -> str:

        if result >= success_rate:
            print(f'Image similarity between both images is: {result:.1f}%')
            return f'Image similarity between both images is: {result:.1f}%'
        else:
            if break_test:
                print(f'Test Stopped due to low similarity, result is {result}/100%')
                raise Exception(f"Test Stopped due to low similarity, result is {result}/100%")
            else:
                ...

    def generate_shadow(self, original_image_path: str, actual_image_path: str) -> None:

        original_image = cv2.imread(original_image_path)
        actual_image = cv2.imread(actual_image_path)

        before_gray = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
        after_gray = cv2.cvtColor(actual_image_path, cv2.COLOR_BGR2GRAY)
        score, diff = structural_similarity(before_gray, after_gray, full=True)
        result = score * 100

        to_gray = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(to_gray, 127, 255, 0)
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(actual_image, contours, -1, (255, 0, 0), 1)

        print(f'result is {result}%')

        image_name = self._get_image_name(actual_image_path)['image_name']
        image_path_folder = self._get_image_name(actual_image_path)['folder_path']
        cv2.imwrite(f'{image_path_folder}\\shadow_result_{image_name}', actual_image)