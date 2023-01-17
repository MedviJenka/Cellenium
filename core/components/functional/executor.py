from core.components.functional.service import Service
from core.components.functional.methods import read_config
from core.components.tools.image_compare import CompareImages


class CompareImagesExecutor(Service):

    def run(self) -> None:
        app = CompareImages()
        path = read_config('path', 'image_compare_data')
        app.compare_images(path)
