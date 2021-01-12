import requests
import shutil
import os


def pullImages(sourceurl, startv, endv, starth, endh, longStringIdentifier, index, underscore):
    sourceurl = sourceurl + longStringIdentifier
    for i in range(startv, endv+1):
        for j in range(starth, endh+1):
            pullurl = sourceurl + index + str(j) + underscore + str(i) + ".jpg"
            filename = pullurl.split("/")[-1]

            r = requests.get(pullurl, stream=True)
            if r.status_code == 200:
                r.raw.decode_content = True
                with open("images/"+filename, 'wb') as f:
                    shutil.copyfileobj(r.raw, f)

def emptyImages(path):
    shutil.rmtree(path)
    os.mkdir("images")
