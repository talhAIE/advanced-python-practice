import zipfile
import pathlib

def create_zip(file_paths,folder_path):
    dest_path=pathlib.Path(folder_path,"compressed.zip")
    with zipfile.ZipFile(dest_path,'w') as zip:
        for file_path in file_paths:
            file_path=pathlib.Path(file_path)
            zip.write(file_path,arcname=file_path.name)

if __name__=="__main__":
    create_zip(file_paths=['./bonusExamples/bonus1.py','./bonusExamples/bonus3.py'],folder_path='./bonusExamples/dest')