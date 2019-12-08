from pdf2image import convert_from_path, convert_from_bytes
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)
import tempfile


def pdf_2_image():
    with tempfile.TemporaryDirectory() as path:
        images_from_path = convert_from_path('/home/sharon/Desktop/Python/PyCharm/Project1/BW.pdf',
                                             output_folder='/home/sharon/Desktop/Python/PyCharm/Project1/')
