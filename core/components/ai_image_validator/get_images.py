from skimage.metrics import structural_similarity
import cv2
import numpy as np
from dataclasses import dataclass


@dataclass
class CompareImages:

    """
    :param: original ................ path for original image to compare
    :param: compare ................. path for screenshot
    :param: show_full_data .......... extra data which emphasizes image difference
    """

    @staticmethod
    def find_difference(original: str, compare: str, show_full_data=False) -> str:

        # load and resize images
        before = cv2.imread(original)
        after = cv2.imread(compare)
        before = cv2.resize(before, (800, 800))
        after = cv2.resize(after, (800, 800))

        # Convert images to grayscale
        before_gray = cv2.cvtColor(before, cv2.COLOR_BGR2GRAY)
        after_gray = cv2.cvtColor(after, cv2.COLOR_BGR2GRAY)
        (score, diff) = structural_similarity(before_gray, after_gray, full=True)

        diff = (diff * 255).astype("uint8")
        diff_box = cv2.merge([diff, diff, diff])

        # Threshold the difference image, followed by finding contours to
        # obtain the regions of the two input images that differ
        thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = contours[0] if len(contours) == 2 else contours[1]

        mask = np.zeros(before.shape, dtype='uint8')
        filled_after = after.copy()

        for c in contours:
            area = cv2.contourArea(c)
            if area > 40:
                x, y, w, h = cv2.boundingRect(c)
                cv2.rectangle(before, (x, y), (x + w, y + h), (36, 255, 12), 2)
                cv2.rectangle(after, (x, y), (x + w, y + h), (36, 255, 12), 2)
                cv2.rectangle(diff_box, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.drawContours(mask, [c], 0, (255, 255, 255), -1)
                cv2.drawContours(filled_after, [c], 0, (250, 0, 0), -1)

        cv2.imshow('before', before)
        cv2.imshow('after', after)
        cv2.waitKey()

        if show_full_data:
            cv2.imshow('diff', diff)
            cv2.imshow('diff_box', diff_box)
            cv2.imshow('mask', mask)
            cv2.imshow('filled after', filled_after)
            cv2.waitKey()

        result = score * 100
        result_text = f"Image Similarity: {result:.1f}%"
        print(result_text)

        print("LOW SIMILARITY, CONSULT WITH THE DEVELOPER") if result < 95 else print("seems good")
        return result_text


def test1() -> None:
    compare_images = CompareImages()
    compare_images.find_difference(original=r"C:\Users\evgenyp\Cellenium\core\static\screenshots\reports\web.jpg",
                                   compare=r"C:\Users\evgenyp\Cellenium\core\static\screenshots\reports\web2.jpg")


def test2() -> None:
    compare_images = CompareImages()
    compare_images.find_difference(original=r"C:\Users\evgenyp\Cellenium\core\static\screenshots\reports\web.jpg",
                                   compare=r"C:\Users\evgenyp\Cellenium\core\static\screenshots\reports\web2.jpg")


def test3() -> None:
    compare_images = CompareImages()
    compare_images.find_difference(original=r"C:\Users\evgenyp\Cellenium\core\static\screenshots\reports\web.jpg",
                                   compare=r"C:\Users\evgenyp\Cellenium\core\static\screenshots\reports\web3.jpg",
                                   show_full_data=True)


def main() -> None:
    test1()
    test2()
    test3()


if __name__ == '__main__':
    main()
