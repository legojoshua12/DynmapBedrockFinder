from PIL import Image
import numpy as np


def merge_images(image1, image2):
    image1 = Image.fromarray(image1)
    image2 = Image.fromarray(image2)

    (width1, height1) = image1.size
    (width2, height2) = image2.size

    result_width = width1 + width2
    result_height = max(height1, height2)

    result = Image.new('RGB', (result_width, result_height))
    result.paste(im=image1, box=(0, 0))
    result.paste(im=image2, box=(width1, 0))

    result = np.asarray(result)
    return result
