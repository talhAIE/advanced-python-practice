import zipfile

def extract_archive(file_path,dest_folder):
    with zipfile.ZipFile(file_path,'r') as zip_ref:
        zip_ref.extractall(dest_folder)

