import os
# import bpy
import platform
import stat # for mac fix chmod

__QR_plugin_version__ = "1.3"

def getQREngineFolder():
    isMacOS = (platform.system()=="Darwin") or (platform.system()=="macosx")
    isLinux = (platform.system()=="Linux")
    if (isMacOS):
        engineFolder = "/Users/Shared/Exoside/QuadRemesher/Datas_Blender/QuadRemesherEngine_"+__QR_plugin_version__
    elif isLinux:
        engineFolder = os.path.expanduser("~/.local/share/Exoside/QuadRemesher/Datas_Blender/QuadRemesherEngine_"+__QR_plugin_version__)
    else:
        #appData = os.getenv('APPDATA')  windows ... UserName/../Roaming... 
        appData = os.getenv('ALLUSERSPROFILE')  # on windows : C:\Users\All Users == C:\ProgramData\
        engineFolder = os.path.join(appData, "Exoside/QuadRemesher/Datas_Blender/QuadRemesherEngine_"+__QR_plugin_version__)
    return engineFolder

def InstallQuadRemesherEngine() -> int:
    engineFolder = getQREngineFolder()
    if not os.path.exists(engineFolder):
        parent_path = os.path.dirname(engineFolder)
        if not os.path.exists(parent_path):
            os.makedirs(parent_path)
        print(engineFolder)
        dow_QREngine_path = "https://hurcaguari.top/blender/data/QuadRemesherEngine_1.3_win.zip"
        zip_file_name = os.path.join(engineFolder, "../install_engine.zip")
        import urllib.request
        urllib.request.urlretrieve(dow_QREngine_path, zip_file_name)
        if os.path.exists(zip_file_name):
            from zipfile import ZipFile
            with ZipFile(zip_file_name, 'r') as zip: 
                zip.extractall(engineFolder)
            os.remove(zip_file_name)
            return 0
        else:
            return 1
    return 0

if __name__ == "__main__":
    InstallQuadRemesherEngine()
    pass
