import os
import shutil

PROJECT_NAME = "{project-name}"
PROJECT_CREATOR = "{project-creator}"
PROJECT_TITLE = "{project-title}"

def setup():
    updateFolders()
    updateFiles()
    updateInfo()
    build()
    export()
    updateLayout()
    
        
def updateFolders():
    for root, dirs, files in os.walk(os.getcwd(), topdown=False):
        for folder in dirs:
            if '{project-name}' in folder:
                old_path = os.path.join(root, folder)
                new_folder = folder.replace('{project-name}', PROJECT_NAME)
                new_path = os.path.join(root, new_folder)
                os.rename(old_path, new_path)

def updateFiles():
    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if '{project-name}' in file:
                new_name = file.replace('{project-name}', PROJECT_NAME)
                os.rename(os.path.join(root, file), os.path.join(root, new_name))

def updateInfo():
    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if file.endswith('.xml') or file.endswith('.json'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    content = f.read()

                content = content.replace('{project-name}', PROJECT_NAME)
                content = content.replace('{project-creator}', PROJECT_CREATOR)
                content = content.replace('{project-title}', PROJECT_TITLE)

                with open(file_path, 'w') as f:
                    f.write(content)

def updateLayout():
    dir = ".\\Community\\" + PROJECT_NAME + "\\" + "layout.json"
    os.system("npm run generate -- " + dir)
    

def build():
    dir = ".\\Project\\" + PROJECT_NAME + ".xml"
    os.system("npm run fspackagetool -- " + dir)

def export():
    spb = PROJECT_NAME + ".spb"
    shutil.copyfile("Project/Packages/" + PROJECT_NAME + "/Packages/" + spb, "Community/" + PROJECT_NAME +"/InGamePanels/" + spb)

setup()