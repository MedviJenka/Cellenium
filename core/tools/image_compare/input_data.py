from dataclasses import dataclass


@dataclass
class InputData:

    """
    :param: original_image_path ................ path for original image to compare
    :param: actual_image_path .................. path for screenshot
    :param: success_rate ....................... wanted percentage of success
    :param: break_test ......................... choose if the test will stop or continue
    :param: screen_resolution .................. set resolution, default is 800x800

    """

    original_image_path: str
    actual_image_path: str
    success_rate: int
    image_resolution: list[int, int]
    break_test: bool
