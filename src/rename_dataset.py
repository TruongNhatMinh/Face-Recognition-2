import os
path = '../Dataset/FaceData/raw/Zoky'
files = os.listdir(path)


for index, file in enumerate(files):
    os.rename(os.path.join(path, file), os.path.join(path, ''.join(['Zoky' + str(index), '.jpg'])))