from dataclasses import dataclass
from core.infrastructure.constants.data import IMAGE_COMPARE_DATA
from core.infrastructure.modules.executor import Executor
from core.infrastructure.modules.reader import read_json
from core.tools.image_compare.image_compare import Logic
from core.tools.image_compare.input_data import InputData


@dataclass
class ImageCompare(Executor, Logic):

    def execute(self, path=IMAGE_COMPARE_DATA) -> None:
        data = InputData(**read_json(path))

        result = self.compare_images(original_image_path=data.original_image_path,
                                     actual_image_path=data.actual_image_path,
                                     image_resolution=data.image_resolution)

        self.generate_rectangles(result=result,
                                 success_rate=data.success_rate,
                                 break_test=data.break_test)

        self.combine_images_into_one_image(original_image_path=data.original_image_path,
                                           actual_image_path=data.actual_image_path)


image = ImageCompare()
image.execute()
