import timeElapser
import locateBedrockInTile
import cv2 as cv
import json
import os

print('Starting script')
timeElapser.print_elapsed_time()
dirname = os.path.dirname(__file__)
dirname = dirname[:-4]

## Test code, will remove
sample = os.path.join(dirname, r'images\-10_-')
sample = sample.replace(os.sep, '/')

bedrock = os.path.join(dirname, r'images\bedrock.jpg')
bedrock = bedrock.replace(os.sep, '/')

with open(dirname+"/src/config.json") as json_data_file:
    data = json.load(json_data_file)

result = None
for i in range(data["range"]):
    sample = sample + str((i + 1)) + ".jpg"
    if result is None:
        result = locateBedrockInTile.locateBedrockFirstTime(sample, bedrock)
    else:
        result = locateBedrockInTile.locateBedrock(result, sample, bedrock)
    cv.imwrite('export/result.png', result)
    sample = sample[:-5]

timeElapser.print_elapsed_time('Ending Script:')
