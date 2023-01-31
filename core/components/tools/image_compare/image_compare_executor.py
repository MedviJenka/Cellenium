from core.components.functional.executor import Executor
from core.components.functional.methods import read_json
from core.components.tools.image_compare.image_compare import Logic
from core.components.tools.image_compare.input_data import InputData
from dataclasses import dataclass


@dataclass
class ImageCompare(Executor, Logic):

    def execute(self, path: str) -> None:

        data = InputData(**read_json(path))

        result = self.compare_images(original_image_path=data.original_image_path,
                                     actual_image_path=data.actual_image_path,
                                     image_resolution=data.image_resolution)

        self.generate_rectangles(result=result,
                                 success_rate=data.success_rate,
                                 break_test=data.break_test)

        self.generate_shadow(original_image_path=data.original_image_path,
                             actual_image_path=data.actual_image_path)
