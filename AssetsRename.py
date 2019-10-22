#coding:utf-8


import os
import json
import io

# asset 目录路径
assets_path = '/Users/chenying/Desktop/ufoto/facefoto/CSYCamera/Assets.xcassets'

# 项目目录
project_path = '/Users/chenying/Desktop/ufoto/facefoto/CSYCamera'
config_path = '/Users/chenying/Desktop/ufoto/facefoto/CSYCamera/Assets.xcassets/ConvertDirs.json'
suf_set = ('.h', '.m', '.xib', '.storyboard', '.mm', '.pch', '.swift')

#改变路径字典
change_paths = {}

#目录
log_path_change = {}

#文件修改信息
log_file_change = {}


#重命名子文件夹
def rename_path():
    for (root, dirs, files) in os.walk(assets_path):
        # 文件夹加前缀
        for dir_name in dirs:
            if os.path.splitext(dir_name)[1] != '.imageset' or root.split('/')[-1] == 'Assets.xcassets' or root.split('/')[-1] == 'AppIcon.appiconset':
                continue
            super_dir_name = root.split('/')[-1]
#            to_name = super_dir_name + "_CY" + dir_name
            to_name = "CY0x1F48B" + dir_name
#            print ("rootDir---%s--tagnaPath-%s" %(super_dir_name, dir_name))
            if dir_name.startswith(super_dir_name):
                continue
            if dir_name.startswith(super_dir_name.lower()):
                to_name = dir_name.replace(super_dir_name.lower(), super_dir_name)
            old_path = os.path.join(root, dir_name)
            new_path = os.path.join(root, to_name)
            change_paths[old_path] = new_path
            log_path_change[old_path.replace(assets_path, '')] = new_path.replace(assets_path, '')
            print(old_path)
            print("--->")
            print(new_path)
            print("-------------")

    for key in change_paths:
#        print ("rootDir---%s--tagnaPath-%s" %(key, change_paths[key]))
        os.renames(key, change_paths[key])
    #写入文件夹更改记录
    json_obj = json.dumps(log_path_change)
    fo = open(os.path.join(assets_path, "ConvertDirs.json"), "w+")
    fo.write(json_obj)
    fo.close()


def file_name_in_path(file_path):
    return file_path.split('/')[-1]


# 文件重命名函数，返回新的文件名
def file_rename(file_path, oldName = "", newName = ""):
    root_path = os.path.split(file_path)[0]     # 文件目录
    root_name = os.path.split(file_path)[1]     # 文件名包含扩展名
    filename = os.path.splitext(root_name)[0]  # 文件名
    filetype = os.path.splitext(root_name)[1]  # 文件扩展名
    new_path = os.path.join(root_path, filename.replace(oldName, newName) + filetype)    # 拼接新路径
    os.renames(file_path, new_path)             # 文件重命名
    # print(file_path)
    # print("--->")
    # print(new_path)
    # print("-------------")
    return filename.replace(oldName, newName)


# 统一文件夹与图片资源名
def correct_imageset():
    for (root, dirs, files) in os.walk(assets_path):
        # for dir_name in dirs:
        #     if os.path.splitext(dir_name)[1] != '.imageset' or root.split('/')[-1] == 'Assets.xcassets':
        #         continue
        for file_name in files:
            if not os.path.isfile(os.path.join(root, file_name)) or os.path.splitext(file_name)[1] == ".json" :
                continue
            super_dir_name_prefix = os.path.splitext(root.split('/')[-1])[0]
            # print(f)
            os.path.splitext(root)
            # print(root)
            img_scale = ""
            if os.path.splitext(file_name)[0].split('@').__len__() > 1:
                img_scale = "@" + os.path.splitext(file_name)[0].split('@')[1]
            old_key = os.path.splitext(file_name)[0]
            new_key = super_dir_name_prefix + img_scale
            log_file_change[os.path.join(root, old_key).replace(assets_path, '')] = os.path.join(root, new_key).replace(assets_path, '')
            file_rename(os.path.join(root, file_name),old_key, new_key)
            #替换json内容
            json_path = os.path.join(root,'Contents.json')
            if os.path.exists(json_path):
                with open(json_path  , 'r+') as f:
                    s0 = f.read()
                    f.close()
                    if old_key in s0:
                        with open(json_path, 'r+') as f2:
                            s = f2.read().replace(old_key, new_key,1)
                            f2.seek(0)
                            f2.write(s)
                            f2.truncate()
                            f2.close()
    json_obj = json.dumps(log_file_change)
    fo = open(os.path.join(assets_path, "correct_imageset.json"), "w+")
    fo.write(json_obj)
    fo.close()


# 修改代码文件中的图片名
def replace_image_name_in_code():
    with io.open(config_path, 'r+', encoding='utf-8') as f:
        config = json.load(f, encoding='utf-8')
        print(config)
        for (root, dirs, files) in os.walk(project_path):
            for file_name in files:
                if not file_name.endswith(suf_set):
                    continue
                print(file_name)
                with io.open(os.path.join(root, file_name), 'r+', encoding='utf-8') as f:
#                    s0 = f.read()
#                    s0 = unicode(f.read(), 'utf-8')
                    try:
                        s0 = f.read()
                    except:
                        with io.open(os.path.join(root, file_name), 'r+', encoding='ISO-8859-1') as f:
                            s0 = f.read()
                            
                    f.close()
                    for key in config:
                        from_name = os.path.splitext(key)[0].split('/')[-1]
                        to_name = os.path.splitext(config[key])[0].split('/')[-1]
                        print ("rootDir->%s--to_name->%s" %(from_name, file_name))
                        if from_name in s0:
                            with io.open(os.path.join(root, file_name), 'r+', encoding='utf-8') as f4:
#                                s1 = f4.read().replace("\"" + from_name + "\"", "\"" + to_name + "\"")
                                try:
                                    s1 = f4.read().replace("\"" + from_name + "\"", "\"" + to_name + "\"")
                                    
                                    f4.seek(0)
                                    f4.write(s1)
                                    f4.truncate()
                                    f4.close()
                                except:
                                    with io.open(os.path.join(root, file_name), 'r+', encoding='ISO-8859-1') as f4:
                                        s1 = f4.read().replace("\"" + from_name + "\"", "\"" + to_name + "\"")
                                        
                                        f4.seek(0)
                                        f4.write(s1)
                                        f4.truncate()
                                        f4.close()
                                        
#                                f4.seek(0)
#                                f4.write(s1)
#                                f4.truncate()
#                                f4.close()

# 一个一个执行
if __name__ == '__main__':

#    rename_path()
#    correct_imageset() //暂时不用
    replace_image_name_in_code()
