import os
import shutil


def organize_files(folder_path):
    file_types = {
        ".jpg": "Images",
        ".png": "Images",
        ".pdf": "Documents",
        ".txt": "Documents",
        ".docx": "Documents",
        ".mp3": "Music",
        ".zip": "Compressed",
    }

    for filename in os.listdir(folder_path):
        file_ext = os.path.splitext(filename)[1].lower()
        if file_ext in file_types:
            destination_folder = os.path.join(folder_path, file_types[file_ext])
            os.makedirs(destination_folder, exist_ok=True)  # Create folders if needed
            source_file = os.path.join(folder_path, filename)
            shutil.move(source_file, destination_folder)

#Monk Fruit
# Example usage:
organize_files("C:/Users/YourName/Downloads")  # Replace with your target folder
