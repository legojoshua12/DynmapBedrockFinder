# Written by legojoshua12

import timeElapser
import locateBedrockInTile
import stitchtiles as st
import fetchTiles as ft
import cv2 as cv
import json
import os

print('Starting script')
timeElapser.print_elapsed_time()
dirname = os.path.dirname(__file__)
dirname = dirname[:-4]

# Test code, will remove
sample = os.path.join(dirname, r'images')
sample = sample.replace(os.sep, '/')

bedrock = os.path.join(dirname, r'src\bedrock.jpg')
bedrock = bedrock.replace(os.sep, '/')

bedrock2 = os.path.join(dirname, r'src\bedrock2.jpg')
bedrock2 = bedrock2.replace(os.sep, '/')

bedrock3 = os.path.join(dirname, r'src\bedrock3.jpg')
bedrock3 = bedrock3.replace(os.sep, '/')

with open(dirname + "/src/config.json") as json_data_file:
    data = json.load(json_data_file)

timeElapser.print_elapsed_time('Initialization:')


def NegativeNegative():
    print("Running Negative, Negative Tiles Compute")
    global sample
    global bedrock
    ft.pullImages(data["dynmapSourceUrl"], data["vertical start"], data["vertical end"], data["horizontal start"],
                  data["horizontal end"], 'tiles/world/flat/-1_-1/', '-', '_-')
    timeElapser.print_elapsed_time('Download Images:')
    totalResult = None
    for i in range(data["horizontal start"], data["horizontal end"] + 1):
        result = None
        for j in range(data["vertical start"], data["vertical end"] + 1):
            sample = sample + '/-' + str(i) + '_-' + str(j) + ".jpg"
            if result is None:
                result = locateBedrockInTile.locateBedrockFirstTime(sample, bedrock, bedrock2, bedrock3, data["threshold"],
                                                                    data["boxthickness"])
            else:
                result = locateBedrockInTile.locateBedrock(result, sample, bedrock, bedrock2, bedrock3, data["threshold"],
                                                           data["boxthickness"])

            # TODO: This needs fixing, just a hacky way for now within double digits of tile names, need to come up with a better method later
            if j <= 9 and i <= 9:
                sample = sample[:-10]
            elif j <= 9 and i >= 10:
                sample = sample[:-11]
            elif j >= 10 and i <= 9:
                sample = sample[:-11]
            elif j >= 10 and i >= 10:
                sample = sample[:-12]

        if totalResult is None:
            totalResult = result
        else:
            totalResult = st.merge_columns(totalResult, result)
        cv.imwrite('export/result.png', totalResult)
    timeElapser.print_elapsed_time('Located Bedrock:')


def PositiveNegative():
    print("Running Positive, Negative Tiles Compute")
    global sample
    global bedrock
    ft.pullImages(data["dynmapSourceUrl"], data["vertical start"], data["vertical end"], data["horizontal start"],
                  data["horizontal end"], 'tiles/world/flat/0_-1/', '', '_-')
    timeElapser.print_elapsed_time('Download Images:')
    totalResult = None
    for i in range(data["horizontal start"], data["horizontal end"] + 1):
        result = None
        for j in range(data["vertical start"], data["vertical end"] + 1):
            sample = sample + '/' + str(i) + '_-' + str(j) + ".jpg"
            if result is None:
                result = locateBedrockInTile.locateBedrockFirstTime(sample, bedrock, bedrock2, bedrock3, data["threshold"],
                                                                    data["boxthickness"])
            else:
                result = locateBedrockInTile.locateBedrock(result, sample, bedrock, bedrock2, bedrock3, data["threshold"],
                                                           data["boxthickness"])

            # TODO: This needs fixing, just a hacky way for now within double digits of tile names, need to come up with a better method later
            if j <= 9 and i <= 9:
                sample = sample[:-9]
            elif j <= 9 and i >= 10:
                sample = sample[:-10]
            elif j >= 10 and i <= 9:
                sample = sample[:-10]
            elif j >= 10 and i >= 10:
                sample = sample[:-11]

        if totalResult is None:
            totalResult = result
        else:
            totalResult = st.merge_columns_reverse(totalResult, result)
        cv.imwrite('export/result2.png', totalResult)
    timeElapser.print_elapsed_time('Located Bedrock:')


def NegativePositive():
    print("Running Negative, Positive Tiles Compute")
    global sample
    global bedrock
    ft.pullImages(data["dynmapSourceUrl"], data["vertical start"], data["vertical end"], data["horizontal start"], data["horizontal end"], 'tiles/world/flat/-1_0/', '-', '_')
    timeElapser.print_elapsed_time('Download Images:')
    totalResult = None
    for i in range(data["horizontal start"], data["horizontal end"] + 1):
        result = None
        for j in range(data["vertical start"], data["vertical end"] + 1):
            sample = sample + '/-' + str(i) + '_' + str(j) + ".jpg"
            if result is None:
                result = locateBedrockInTile.locateBedrockFirstTime(sample, bedrock, bedrock2, bedrock3, data["threshold"],
                                                                    data["boxthickness"])
            else:
                result = locateBedrockInTile.locateBedrock(result, sample, bedrock, bedrock2, bedrock3, data["threshold"],
                                                           data["boxthickness"], True)

            # TODO: This needs fixing, just a hacky way for now within double digits of tile names, need to come up with a better method later
            if j <= 9 and i <= 9:
                sample = sample[:-9]
            elif j <= 9 and i >= 10:
                sample = sample[:-10]
            elif j >= 10 and i <= 9:
                sample = sample[:-10]
            elif j >= 10 and i >= 10:
                sample = sample[:-11]

        if totalResult is None:
            totalResult = result
        else:
            totalResult = st.merge_columns(totalResult, result)
        cv.imwrite('export/result3.png', totalResult)
    timeElapser.print_elapsed_time('Located Bedrock:')


def PositivePositive():
    print("Running Positive, Positive Tiles Compute")
    global sample
    global bedrock
    ft.pullImages(data["dynmapSourceUrl"], data["vertical start"], data["vertical end"], data["horizontal start"], data["horizontal end"], 'tiles/world/flat/-1_0/', '', '_')
    timeElapser.print_elapsed_time('Download Images:')
    totalResult = None
    for i in range(data["horizontal start"], data["horizontal end"] + 1):
        result = None
        for j in range(data["vertical start"], data["vertical end"] + 1):
            sample = sample + '/' + str(i) + '_' + str(j) + ".jpg"
            if result is None:
                result = locateBedrockInTile.locateBedrockFirstTime(sample, bedrock, bedrock2, bedrock3, data["threshold"],
                                                                    data["boxthickness"])
            else:
                result = locateBedrockInTile.locateBedrock(result, sample, bedrock, bedrock2, bedrock3, data["threshold"],
                                                           data["boxthickness"], True)

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
            totalResult = st.merge_columns_reverse(totalResult, result)
        cv.imwrite('export/result4.png', totalResult)
    timeElapser.print_elapsed_time('Located Bedrock:')


NegativeNegative()
PositiveNegative()
NegativePositive()
PositivePositive()

result = os.path.join(dirname, r'export\result.png')
result = result.replace(os.sep, '/')
result2 = os.path.join(dirname, r'export\result2.png')
result2 = result2.replace(os.sep, '/')
result3 = os.path.join(dirname, r'export\result3.png')
result3 = result3.replace(os.sep, '/')
result4 = os.path.join(dirname, r'export\result4.png')
result4 = result4.replace(os.sep, '/')
cv.imwrite('export/finalresult.png', st.stitchQuadrants(result, result2, result3, result4))

if data["removeLeftOverImages"]:
    imagesLocation = os.path.join(dirname, r'images')
    imagesLocation = imagesLocation.replace(os.sep, '/')
    ft.emptyImages(imagesLocation)
    timeElapser.print_elapsed_time('RemoveImages:')
