import cv2 as cv
import numpy as np
import stitchtiles as st


def locateBedrockFirstTime(sample, bedrock, bedrock2, bedrock3, threshold=0.8, boxthickness=2):
    img_rgb = cv.imread(sample)
    template = cv.imread(bedrock)
    template2 = cv.imread(bedrock2)
    template3 = cv.imread(bedrock3)
    h, w = template.shape[:-1]
    h2, w2 = template2.shape[:-1]
    h3, w3 = template3.shape[:-1]

    try:
        img_rgb.shape[:-1]
    except:
        img_rgb = np.zeros((128,128,3), np.uint8)

    res = cv.matchTemplate(img_rgb, template, cv.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), boxthickness)

    res = cv.matchTemplate(img_rgb, template2, cv.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        cv.rectangle(img_rgb, pt, (pt[0] + w2, pt[1] + h2), (0, 0, 255), boxthickness)

    res = cv.matchTemplate(img_rgb, template3, cv.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        cv.rectangle(img_rgb, pt, (pt[0] + w3, pt[1] + h3), (0, 0, 255), boxthickness)

    return np.asarray(img_rgb)


def locateBedrock(sample, sample2, bedrock, bedrock2, bedrock3, threshold=0.8, boxthickness=2, flipFunction=False):
    img_rgb = np.asarray(sample)
    img2_rgb = cv.imread(sample2)
    template = cv.imread(bedrock)
    template2 = cv.imread(bedrock2)
    template3 = cv.imread(bedrock3)
    h, w = template.shape[:-1]
    h2, w2 = template2.shape[:-1]
    h3, w3 = template3.shape[:-1]

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

    for img in img_array:
        res = cv.matchTemplate(img, template2, cv.TM_CCOEFF_NORMED)
        loc = np.where(res >= threshold)
        for pt in zip(*loc[::-1]):
            cv.rectangle(img, pt, (pt[0] + w2, pt[1] + h2), (0, 0, 255), boxthickness)

    for img in img_array:
        res = cv.matchTemplate(img, template3, cv.TM_CCOEFF_NORMED)
        loc = np.where(res >= threshold)
        for pt in zip(*loc[::-1]):
            cv.rectangle(img, pt, (pt[0] + w3, pt[1] + h3), (0, 0, 255), boxthickness)

    if flipFunction:
        return st.merge_images_reverse(img_array[0], img_array[1])
    else:
        return st.merge_images(img_array[0], img_array[1])
