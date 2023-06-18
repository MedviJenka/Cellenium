import logging
import os
import cv2
import numpy as np
from skimage.metrics import structural_similarity
from core.infrastructure.modules.methods import log
from dataclasses import dataclass
from PIL import Image


@dataclass
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

        _before = cv2.imread(original_image_path)
        _after = cv2.imread(actual_image_path)
        log(level=logging.DEBUG, text=f" Test: {__name__}, load and resize images")

        before = cv2.resize(_before, image_resolution)
        after = cv2.resize(_after, image_resolution)
        log(level=logging.DEBUG, text=f"resolution is set to: {image_resolution}")

        before_gray = cv2.cvtColor(before, cv2.COLOR_BGR2GRAY)
        after_gray = cv2.cvtColor(after, cv2.COLOR_BGR2GRAY)
        log(level=logging.DEBUG, text=f"converting images to grayscale, before: \n{before}, after: \n{after}]")

        score, diff = structural_similarity(before_gray, after_gray, full=True)
        log(level=logging.DEBUG,
            text=f"calculating structural similarity differences, score: {score}, diff: {diff}")

        diff = (diff * 255).astype("uint8")
        diff_box = cv2.merge([diff, diff, diff])

        thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = contours[0] if len(contours) == 2 else contours[1]
        log(level=logging.DEBUG,
            text=f"threshold the difference image, followed by finding"
                 f"contours to obtain the regions of the two input images that differ {contours}")

        mask = np.zeros(before.shape, dtype='uint8')
        filled_after = after.copy()
        log(text=f'filler: {filled_after}')

        for i in contours:
            area = cv2.contourArea(i)
            if area > 40:
                x, y, w, h = cv2.boundingRect(i)
                cv2.rectangle(before, (x, y), (x + w, y + h), (36, 255, 12), 1)
                cv2.rectangle(after, (x, y), (x + w, y + h), (36, 255, 12), 1)
                cv2.rectangle(diff_box, (x, y), (x + w, y + h), (0, 255, 0), 1)
                cv2.drawContours(mask, [i], 0, (255, 255, 255), -1)
                cv2.drawContours(filled_after, [i], 0, (250, 0, 0), -1)

            log(level=logging.DEBUG, text=f'area: {area}')

        cv2.imshow('before', before)
        cv2.imshow('after', after)

        image_name = self._get_image_name(actual_image_path)['image_name']
        log(text=f'generated result image name is: {image_name}')

        image_path_folder = self._get_image_name(actual_image_path)['folder_path']
        image_result = fr'{image_path_folder}\{image_name}_RESULT.png'
        cv2.imwrite(f'{image_result}', before)
        log(level=logging.DEBUG, text=f'saving images in: {image_path_folder}')
        result = score * 100
        cv2.destroyAllWindows()

        return result

    def combine_images_into_one_image(self,
                                      original_image_path: str,
                                      actual_image_path: str,) -> None:

        image_name = self._get_image_name(actual_image_path)['image_name']
        image_path_folder = self._get_image_name(actual_image_path)['folder_path']
        image_result = fr'{image_path_folder}\{image_name}_RESULT.png'

        images = [Image.open(x) for x in [original_image_path, actual_image_path, image_result]]
        widths, heights = zip(*(i.size for i in images))
        total_width = sum(widths)
        max_height = max(heights)
        new_im = Image.new('RGB', (total_width, max_height))
        x_offset = 0

        for each_image in images:
            new_im.paste(each_image, (x_offset, 0))
            x_offset += each_image.size[0]

        new_im.save(image_result)

    @staticmethod
    def generate_rectangles(result: float, success_rate: int, break_test: bool) -> None:

        if result >= success_rate:
            log(f'PASSED:\n'
                f'Image similarity between both images is: {result:.1f}%')
        else:
            if break_test:
                log(text=f'STOPPED: Test Stopped due to low similarity, result is {result:.1f}/100%',
                    level=logging.ERROR)
                raise Exception(f"Test Stopped due to low similarity, result is {result:.1f}/100%")
            else:
                log(text=f'FAILED:'
                         f'Image similarity between both images is: {result:.1f}% '
                         f'when the success rate threshold was {success_rate},'
                         f'please consult with developer or your team.',
                    level=logging.DEBUG)
