import json
import urllib

def getData(url):
    with open('files/static/'+url) as file_:
        contents = file_.read()
        if contents:
            contents = json.loads(contents)
        else:
            contents = []
        return contents

def saveData(url,saveData):
    with open('files/static/'+url,'w') as file_:
        contents = file_.write(saveData)
