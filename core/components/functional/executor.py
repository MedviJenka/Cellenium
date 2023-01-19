from abc import ABC, abstractmethod
from core.components.functional.methods import read_json
from core.components.tools.image_compare.image_compare import Logic
from core.components.tools.image_compare.input_data import InputData


class Executor(ABC):

    @abstractmethod
    def execute(self, *args: any, **kwargs: any) -> None:
        ...


class CompareImages(Logic, Executor):

    def execute(self, path: str) -> None:
        data = InputData(**read_json(path))
        self.compare_images(original_image_path=data.original_image_path,
                            actual_image_path=data.actual_image_path,
                            success_rate=data.success_rate,
                            resolution=data.resolution,
                            break_test=data.break_test)
