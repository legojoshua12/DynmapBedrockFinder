import cv2 as cv
import numpy as np
import stitchtiles as st

def locateBedrockFirstTime(sample, bedrock):
    img_rgb = cv.imread(sample)
    template = cv.imread(bedrock)
    h, w = template.shape[:-1]

    res = cv.matchTemplate(img_rgb, template, cv.TM_CCOEFF_NORMED)
    threshold = .8
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

    return np.asarray(img_rgb)

def locateBedrock(sample, sample2, bedrock):
    img_rgb = np.asarray(sample)
    img2_rgb = cv.imread(sample2)
    template = cv.imread(bedrock)
    h, w = template.shape[:-1]

    img_array = []
    img_array.append(img_rgb)
    img_array.append(img2_rgb)

    for img in img_array:
        res = cv.matchTemplate(img, template, cv.TM_CCOEFF_NORMED)
        threshold = .8
        loc = np.where(res >= threshold)
        for pt in zip(*loc[::-1]):
            cv.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

    return st.merge_images(img_array[0], img_array[1])
