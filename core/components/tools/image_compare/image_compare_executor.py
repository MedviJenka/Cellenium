from core.components.functional.executor import Executor
from core.components.functional.methods import read_json
from core.components.tools.image_compare.image_compare import Logic
from core.components.tools.image_compare.input_data import InputData
from dataclasses import dataclass


@dataclass
class ImageCompare(Executor):

    logic = Logic()

    def execute(self, path: str) -> None:

        data = InputData(**read_json(path))

        result = self.logic.compare_images(original_image_path=data.original_image_path,
                                           actual_image_path=data.actual_image_path,
                                           image_resolution=data.image_resolution)

        self.logic.generate_rectangles(result=result,
                                       success_rate=data.success_rate,
                                       break_test=data.break_test)

        self.logic.generate_shadow(original_image_path=data.original_image_path,
                                   actual_image_path=data.actual_image_path)


def main() -> None:
    image_compare = ImageCompare()
    image_compare.execute(r'C:\Projects\PyBREnv\tools\image_compare\data.json')


if __name__ == '__main__':
    main()
