#coding:utf-8

import os
import re
import random


## 方法重命名

project_path = '/Users/chenying/Desktop/ufoto/SweetChatiOS/SweetChat/SCComponent/Extension'

def file_classname_in_path(file_path = ""):
    for (root, dirs, files) in os.walk(project_path):
        for file_name in files:
            print(file_name)
            with open(os.path.join(root, file_name), 'rb+') as f:
                lines = f.readlines()
                for line in lines:
                    if line.__contains__('extension'.encode()):
                        print(line.split())
                        index = 0

                        classItems = line.split()
                        for classitem in classItems:
                            index +=1
                            if classitem.__contains__('extension'.encode()):
#                                print('iiiiiiiii:' + str(index) + 'classitem:' + classitem)
                                break
                        
                        realClass = classItems[index]
                        print('realClass:' + realClass.replace("{", " ").replace("(", " "))
                        break

#                    elif line.__contains__('class'.encode()):
                    
#                    elif line.__contains__('@interface'.encode()):



# refactor_variable()
if __name__ == '__main__':
    file_classname_in_path()
