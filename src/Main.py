# Written by legojoshua12

import timeElapser
import locateBedrockInTile
import stitchtiles as st
import cv2 as cv
import json
import os

print('Starting script')
timeElapser.print_elapsed_time()
dirname = os.path.dirname(__file__)
dirname = dirname[:-4]

# Test code, will remove
sample = os.path.join(dirname, r'images\-')
sample = sample.replace(os.sep, '/')

bedrock = os.path.join(dirname, r'images\bedrock.jpg')
bedrock = bedrock.replace(os.sep, '/')

with open(dirname + "/src/config.json") as json_data_file:
    data = json.load(json_data_file)

totalResult = None
for i in range(data["horizontal start"], data["horizontal end"] + 1):
    result = None
    for j in range(data["vertical start"], data["vertical end"] + 1):
        sample = sample + str(i) + '_-' + str(j) + ".jpg"
        if result is None:
            result = locateBedrockInTile.locateBedrockFirstTime(sample, bedrock, data["threshold"], data["boxthickness"])
        else:
            result = locateBedrockInTile.locateBedrock(result, sample, bedrock, data["threshold"], data["boxthickness"])

        # TODO: This needs fixing, just a hacky way for now within double digits of tile names, need to come up with a better method later
        if j <= 9 and i <= 9:
            sample = sample[:-8]
        elif j <= 9 and i >= 10:
            sample = sample[:-9]
        elif j >= 10 and i <= 9:
            sample = sample[:-9]
        elif j >= 10 and i >= 10:
            sample = sample[:-10]

    if totalResult is None:
        totalResult = result
    else:
        totalResult = st.merge_columns(totalResult, result)
    cv.imwrite('export/result.png', totalResult)

timeElapser.print_elapsed_time('Ending Script:')
