import cv2 as cv
import numpy as np
import stitchtiles as st


def locateBedrockFirstTime(sample, bedrock, threshold=0.8, boxthickness = 2):
    img_rgb = cv.imread(sample)
    template = cv.imread(bedrock)
    h, w = template.shape[:-1]

    try:
        img_rgb.shape[:-1]
    except:
        img_rgb = np.zeros((128,128,3), np.uint8)

    res = cv.matchTemplate(img_rgb, template, cv.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

    return np.asarray(img_rgb)


def locateBedrock(sample, sample2, bedrock, threshold=0.8, boxthickness = 2):
    img_rgb = np.asarray(sample)
    img2_rgb = cv.imread(sample2)
    template = cv.imread(bedrock)
    h, w = template.shape[:-1]

    try:
        img2_rgb.shape[:-1]
    except:
        img2_rgb = np.zeros((128,128,3), np.uint8)

    img_array = [img_rgb, img2_rgb]

    for img in img_array:
        res = cv.matchTemplate(img, template, cv.TM_CCOEFF_NORMED)
        loc = np.where(res >= threshold)
        for pt in zip(*loc[::-1]):
            cv.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), boxthickness)

    return st.merge_images(img_array[0], img_array[1])
