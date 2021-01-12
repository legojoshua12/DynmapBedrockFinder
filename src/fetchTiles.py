import requests
import shutil
import os


def pullImages(sourceurl, startv, endv, starth, endh):
    sourceurl = sourceurl + "tiles/world/flat/-1_-1/"
    for i in range(startv, endv):
        for j in range(starth, endh):
            pullurl = sourceurl + "-" + str(j) + "_-" + str(i) + ".jpg"
            filename = pullurl.split("/")[-1]

            r = requests.get(pullurl, stream=True)
            if r.status_code == 200:
                r.raw.decode_content = True
                with open("images/"+filename, 'wb') as f:
                    shutil.copyfileobj(r.raw, f)

def emptyImages(path):
    shutil.rmtree(path)
    os.mkdir("images")
