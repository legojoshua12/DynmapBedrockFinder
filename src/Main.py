import cv2 as cv
import numpy as np
import os
import stitchtiles as st

print('Running script')
dirname = os.path.dirname(__file__)
dirname = dirname[:-4]

sample = os.path.join(dirname, r'images\-10_-6.jpg')
sample = sample.replace(os.sep, '/')

sample2 = os.path.join(dirname, r'images\-10_-5.jpg')
sample2 = sample2.replace(os.sep, '/')

bedrock = os.path.join(dirname, r'images\bedrock.jpg')
bedrock = bedrock.replace(os.sep, '/')

img_rgb = cv.imread(sample)
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

cv.imwrite('export/result.png', st.merge_images(img_array[0], img_array[1]))
