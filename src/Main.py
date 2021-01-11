import cv2 as cv
import numpy as np
import os

print('Running script')
dirname = os.path.dirname(__file__)
dirname = dirname[:-4]

sample = os.path.join(dirname, r'images\sample.jpg')
sample = sample.replace(os.sep, '/')

bedrock = os.path.join(dirname, r'images\bedrock.jpg')
bedrock = bedrock.replace(os.sep, '/')

img_rgb = cv.imread(sample)
template = cv.imread(bedrock)
h, w = template.shape[:-1]

res = cv.matchTemplate(img_rgb, template, cv.TM_CCOEFF_NORMED)
threshold = .8
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):
    cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

cv.imwrite('export/result.png', img_rgb)