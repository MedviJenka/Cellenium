from dataclasses import dataclass


@dataclass
class InputData:

    original_image_path: str
    actual_image_path: str
    success_rate: int
    resolution: list[int, int]
    break_test: bool
