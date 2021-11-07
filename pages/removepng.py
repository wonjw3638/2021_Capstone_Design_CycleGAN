import os 

def removefile():

    def removeExtensionFile(filePath, fileExtension):
        if os.path.exists(filePath):
            for file in os.scandir(filePath):
                if file.name.endswith(fileExtension):
                    os.remove(file.path)
            return 'Remove File : ' + fileExtension
        else:
            return 'Directory Not Found'

    img_path_1 = r'C:\Users\BTLsub\realsite\media\input'
    img_path_2 = r'C:\Users\BTLsub\realsite\media\output'


    removeExtensionFile(img_path_1, '.png')
    removeExtensionFile(img_path_2, '.png')