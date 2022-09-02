from core.utils.excel.reader import ExcelReader
from core.utils.config.reader import ConfigReader
import openpyxl
from PIL import Image


config = ConfigReader()

width = 900
height = 900

img = Image.open(r'C:\Users\medvi\IdeaProjects\CelleniumProject\core\utils\screenshots\img.png')
img = img.resize((width, height), Image.NEAREST)
img.save(config.read('path', 'page_base'))

wb = openpyxl.Workbook()
ws = wb.worksheets[0]
img = openpyxl.drawing.image.Image(r'C:\Users\medvi\IdeaProjects\CelleniumProject\core\utils\screenshots\img.png')
ws.add_image(img,'F10')
wb.save(config.read('path', 'page_base'))
