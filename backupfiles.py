import os 
import shutil
import time
def main():
    deleted_folders=0
    deleted_files=0
    path="C:/Users/Laksh/Desktop/project 99"
    days=30
    seconds=time.time()-(days*24*60*60)
    if(os.path.exists(path)):
        for rootfolder,folders,files in os.walk(path):
            if(seconds>=fileorfolderage(rootfolder)):
                removefolder(rootfolder)
                deleted_folders=deleted_folders+1
            else:
                for folder in folders:
                    folderpath=os.path.join(rootfolder,folder)
                    if(seconds>=fileorfolderage(folderpath)):
                       removefolder(folderpath)
                       deleted_folders=deleted_folders+1
                for file in files:
                    filepath=os.path.join(rootfolder,file)
                    if(seconds>=fileorfolderage(filepath)):
                        removefile(filepath)
                        deleted_files=deleted_files+1
    else:
        print("files not found")
    print(deleted_files,deleted_folders)


           

                
    
def fileorfolderage(path):
    ctime=os.stat(path).st_ctime
    return ctime
def removefile(path):
    if not os.remove(path):
        print("path is removed successfully")
    else:
        print("unable to delete the path")

def removefolder(path):
    if not shutil.rmtree(path):
        print("path is removed successfully")
    else:
        print("unable to delete the path")
main()