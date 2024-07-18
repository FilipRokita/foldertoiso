import os
import sys
import shutil

def convert_folder_to_iso(folder_path, iso_path):
    try:
        shutil.make_archive(iso_path, 'zip', folder_path)
        os.rename(iso_path + '.zip', iso_path + '.iso')
        print(f"Folder '{folder_path}' converted to ISO file '{iso_path}.iso' successfully.")
    except Exception as e:
        print(f"An error occurred while converting folder to ISO: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python foldertoiso.py <path to folder> <path to iso>")
        sys.exit(1)

    folder_path = sys.argv[1]
    iso_path = sys.argv[2]

    convert_folder_to_iso(folder_path, iso_path)