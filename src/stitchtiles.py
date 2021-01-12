from PIL import Image
import numpy as np


def merge_images(image1, image2):
    image1 = Image.fromarray(image1)
    image2 = Image.fromarray(image2)

    (width1, height1) = image1.size
    (width2, height2) = image2.size

    result_width = max(width1, width2)
    result_height = height1 + height2

    result = Image.new('RGB', (result_width, result_height))
    result.paste(im=image1, box=(0, 0))
    result.paste(im=image2, box=(0, height1))

    result = np.asarray(result)
    return result


def merge_images_reverse(image1, image2):
    image1 = Image.fromarray(image1)
    image2 = Image.fromarray(image2)

    (width1, height1) = image1.size
    (width2, height2) = image2.size

    result_width = max(width1, width2)
    result_height = height1 + height2

    result = Image.new('RGB', (result_width, result_height))
    result.paste(im=image2, box=(0, 0))
    result.paste(im=image1, box=(0, height2))

    result = np.asarray(result)
    return result


def merge_columns(image1, image2):
    image1 = Image.fromarray(image1)
    image2 = Image.fromarray(image2)

    (width1, height1) = image1.size
    (width2, height2) = image2.size

    result_width = width1 + width2
    result_height = max(height1, height2)

    result = Image.new('RGB', (result_width, result_height))
    result.paste(im=image2, box=(0, 0))
    result.paste(im=image1, box=(width2, 0))

    result = np.asarray(result)
    return result


def merge_columns_reverse(image1, image2):
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


def stitchQuadrants(sw, se, nw, ne):
    sw = Image.open(sw)
    se = Image.open(se)
    nw = Image.open(nw)
    ne = Image.open(ne)

    (width1, height1) = sw.size
    (width2, height2) = se.size
    (width3, height3) = nw.size
    (width4, height4) = ne.size

    result_width = width1 + width2
    result_height = max(height1, height2)

    result = Image.new('RGB', (result_width, result_height))
    result.paste(im=sw, box=(0, 0))
    result.paste(im=se, box=(width1-128, 0))
    result = Image.fromarray(np.array(result)[:,:,::-1])

    result2_width = width3 + width4
    result2_height = max(height3, height4)

    result2 = Image.new('RGB', (result2_width, result2_height))
    result2.paste(im=nw, box=(0, 0))
    result2.paste(im=ne, box=(width3 - 128, 0))
    result2 = Image.fromarray(np.array(result2)[:, :, ::-1])

    totalResult = stitchQuadrantRows(result, result2)

    return np.asarray(totalResult)


def stitchQuadrantRows(img1, img2):

    (width1, height1) = img1.size
    (width2, height2) = img2.size

    result_width = max(width1, width2)
    result_height = height1 + height2

    result = Image.new('RGB', (result_width-128, result_height-128))
    result.paste(im=img2, box=(0, 0))
    result.paste(im=img1, box=(0, height2-128))

    return result
