#coding:utf-8

import os
import re
import random
import json

## 方法重命名

#project_path = '/Users/chenying/Desktop/test/testJson'
project_path = '/Users/chenying/Desktop/ufoto/icamera-ios/iCameraApp'

name_emb = { 'timerending':'0',
            'hellh':'66',
            'hellw':'76',
            'encryptpeyd':'ales.png',
            'framewithccLayer':'0.88',
            'version_identifiers':'1',
            'withHuee':'true'
}

name_list = {'rres': 'resll.png',
            'myFramess': '20*8',
            'rres': 'resll.png',
            'readyttoReecord': 'reslle.png',
            'toupdateters': 'copyBBt.png',
            'morefouncdd': 'bundleddow.png',
            'environmentstatuee': '0',
            'geles': '2013',
            'amerycas': '1.0'
}
def file_classname_in_path(file_path = ""):
    with open(file_path, 'rb+') as f:
        
        model = json.load(f)
        f.close()
        
        if isinstance(model,list):
            model.append(name_list)
        else:
            for i in name_emb:
                print('iiiiiiiii:' + str(i) + 'item:' + name_emb[i])
                model[i] = name_emb[i]

        
        jsonObj = json.dumps(model)
        
        with open(file_path, 'w') as fww:
            fww.write(jsonObj)
            fww.close()
        

def findJsonFile():
    for (root, dirs, files) in os.walk(project_path):
            for file_name in files:
            
                pppath = os.path.join(root, file_name)
                print(pppath)
                if pppath.__contains__('Assets.xcassets'.encode()):
                    continue
                    
                if os.path.splitext(file_name)[1] == '.json':
                    file_classname_in_path(os.path.join(root, file_name))
    
    

# refactor_variable()
if __name__ == '__main__':
    findJsonFile()
