# Written by legojoshua12

import timeElapser
import locateBedrockInTile
import stitchtiles as st
import fetchTiles as ft
import cv2 as cv
import json
import os
import threading as thread

print('Starting script')
timeElapser.print_elapsed_time()
dirname = os.path.dirname(__file__)
dirname = dirname[:-4]

# Test code, will remove
sample = os.path.join(dirname, r'images')
sample = sample.replace(os.sep, '/')

bedrock = os.path.join(dirname, r'src\bedrockSourceImages\bedrock')
bedrock = bedrock.replace(os.sep, '/')

with open(dirname + "/src/config.json") as json_data_file:
    data = json.load(json_data_file)

bedrockArray = []
for i in range(data["bedrockSampleImageCount"]):
    bedrockArray.append(bedrock)

timeElapser.print_elapsed_time('Initialization:')


def NegativeNegative():
    print("Running Negative, Negative Tiles Compute")
    global sample
    global bedrockArray
    ft.pullImages(data["dynmapSourceUrl"], data["vertical start"], data["vertical end"], data["horizontal start"],
                  data["horizontal end"], 'tiles/world/flat/-1_-1/', '-', '_-')
    timeElapser.print_elapsed_time('Download Images:')
    totalResult = None
    for i in range(data["horizontal start"], data["horizontal end"] + 1):
        result = None
        for j in range(data["vertical start"], data["vertical end"] + 1):
            sample = sample + '/-' + str(i) + '_-' + str(j) + ".jpg"
            if result is None:
                result = locateBedrockInTile.locateBedrockFirstTime(sample, bedrockArray, data["threshold"],
                                                                    data["boxthickness"])
            else:
                result = locateBedrockInTile.locateBedrock(result, sample, bedrockArray, data["threshold"],
                                                           data["boxthickness"])
            sample = sample[:-((len(str(i))) + 8 + (len(str(j))))]

        if totalResult is None:
            totalResult = result
        else:
            totalResult = st.merge_columns(totalResult, result)
        cv.imwrite('export/result.png', totalResult)
    timeElapser.print_elapsed_time('Located Bedrock:')


def PositiveNegative():
    print("Running Positive, Negative Tiles Compute")
    global sample
    global bedrockArray
    ft.pullImages(data["dynmapSourceUrl"], data["vertical start"], data["vertical end"], data["horizontal start"],
                  data["horizontal end"], 'tiles/world/flat/0_-1/', '', '_-')
    timeElapser.print_elapsed_time('Download Images:')
    totalResult = None
    for i in range(data["horizontal start"], data["horizontal end"] + 1):
        result = None
        for j in range(data["vertical start"], data["vertical end"] + 1):
            sample = sample + '/' + str(i) + '_-' + str(j) + ".jpg"
            if result is None:
                result = locateBedrockInTile.locateBedrockFirstTime(sample, bedrockArray, data["threshold"],
                                                                    data["boxthickness"])
            else:
                result = locateBedrockInTile.locateBedrock(result, sample, bedrockArray, data["threshold"],
                                                           data["boxthickness"])
            sample = sample[:-((len(str(i))) + 7 + (len(str(j))))]

        if totalResult is None:
            totalResult = result
        else:
            totalResult = st.merge_columns_reverse(totalResult, result)
        cv.imwrite('export/result2.png', totalResult)
    timeElapser.print_elapsed_time('Located Bedrock:')


def NegativePositive():
    print("Running Negative, Positive Tiles Compute")
    global sample
    global bedrockArray
    ft.pullImages(data["dynmapSourceUrl"], data["vertical start"], data["vertical end"], data["horizontal start"],
                  data["horizontal end"], 'tiles/world/flat/-1_0/', '-', '_')
    timeElapser.print_elapsed_time('Download Images:')
    totalResult = None
    for i in range(data["horizontal start"], data["horizontal end"] + 1):
        result = None
        for j in range(data["vertical start"], data["vertical end"] + 1):
            sample = sample + '/-' + str(i) + '_' + str(j) + ".jpg"
            if result is None:
                result = locateBedrockInTile.locateBedrockFirstTime(sample, bedrockArray, data["threshold"],
                                                                    data["boxthickness"])
            else:
                result = locateBedrockInTile.locateBedrock(result, sample, bedrockArray, data["threshold"],
                                                           data["boxthickness"], True)
            sample = sample[:-((len(str(i))) + 7 + (len(str(j))))]

        if totalResult is None:
            totalResult = result
        else:
            totalResult = st.merge_columns(totalResult, result)
        cv.imwrite('export/result3.png', totalResult)
    timeElapser.print_elapsed_time('Located Bedrock:')


def PositivePositive():
    print("Running Positive, Positive Tiles Compute")
    global sample
    global bedrockArray
    ft.pullImages(data["dynmapSourceUrl"], data["vertical start"], data["vertical end"], data["horizontal start"],
                  data["horizontal end"], 'tiles/world/flat/-1_0/', '', '_')
    timeElapser.print_elapsed_time('Download Images:')
    totalResult = None
    for i in range(data["horizontal start"], data["horizontal end"] + 1):
        result = None
        for j in range(data["vertical start"], data["vertical end"] + 1):
            sample = sample + '/' + str(i) + '_' + str(j) + ".jpg"
            if result is None:
                result = locateBedrockInTile.locateBedrockFirstTime(sample, bedrockArray, data["threshold"],
                                                                    data["boxthickness"])
            else:
                result = locateBedrockInTile.locateBedrock(result, sample, bedrockArray, data["threshold"],
                                                           data["boxthickness"], True)
            sample = sample[:-((len(str(i))) + 6 + (len(str(j))))]

        if totalResult is None:
            totalResult = result
        else:
            totalResult = st.merge_columns_reverse(totalResult, result)
        cv.imwrite('export/result4.png', totalResult)
    timeElapser.print_elapsed_time('Located Bedrock:')

if data["unqiueRender"] == 0:
    NegativeNegative()
    PositiveNegative()
    NegativePositive()
    PositivePositive()
elif data["unqiueRender"] == 1:
    NegativeNegative()
elif data["unqiueRender"] == 2:
    PositiveNegative()
elif data["unqiueRender"] == 3:
    NegativePositive()
elif data["unqiueRender"] == 4:
    PositivePositive()
else:
    print("Invalid number specified")

result = os.path.join(dirname, r'export\result.png')
result = result.replace(os.sep, '/')
result2 = os.path.join(dirname, r'export\result2.png')
result2 = result2.replace(os.sep, '/')
result3 = os.path.join(dirname, r'export\result3.png')
result3 = result3.replace(os.sep, '/')
result4 = os.path.join(dirname, r'export\result4.png')
result4 = result4.replace(os.sep, '/')

if data["stitchFinalRender"] and data["unqiueRender"] == 0:
    cv.imwrite('export/finalresult.png', st.stitchQuadrants(result, result2, result3, result4))

if data["removeLeftOverImages"]:
    imagesLocation = os.path.join(dirname, r'images')
    imagesLocation = imagesLocation.replace(os.sep, '/')
    ft.emptyImages(imagesLocation)
    timeElapser.print_elapsed_time('RemoveImages:')
