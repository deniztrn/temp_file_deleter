import datetime
import os
import shutil
from datetime import datetime as dt
from time import sleep


def temp_file_deleter(dir_path: str, delete_before: int) -> None:
	"""
	Gets the `list` of files and folders with the last modification time. Deletes the items which are not modified
	since specified hours.

	:param dir_path: Folder path to delete the old files.
	:param delete_before: Specified hours to keep the temp files.
	:return: list of deleted files
	"""
	global item_path, file_path, source_file
	now = dt.now().timestamp()
	items = next(os.walk(dir_path))
	folder_list = items[1]
	file_list = items[2]
	deleted_folders = []
	deleted_files = []
	# Folder deletion
	for folder in range(len(folder_list)):
		item_path = dir_path + "\\" + folder_list[folder]
		item_time = os.path.getmtime(dir_path + "\\" + folder_list[folder])
		if (now - item_time) > delete_before * 3600:
			print("Folder DELETED: " + item_path)
			deleted_folders.append(item_path)
		shutil.rmtree(item_path)

	# File deletion
	for file in range(len(file_list)):
		file_path = dir_path + "\\" + file_list[file]
		file_time = os.path.getmtime(dir_path + "\\" + file_list[file])
		if (now - file_time) > delete_before * 3600:
			print("File DELETED: " + file_path)
			deleted_files.append(file_path)
		os.remove(file_path)
	source_file = open('deleted_file_list.txt', 'a')
	print(f"{len(deleted_files)} out of {len(file_list)} files and {len(deleted_folders)} out of "
	      f"{len(folder_list)} folders are deleted" + f"{deleted_files}" f"{deleted_folders}" + str(
		datetime.datetime.now()), file=source_file)
	source_file.close()

	return None


# Input Path: The folder path which will be checked by the script for deletion
path = input(print("Please enter the path name: "))

# Input Hours: Filters the files as per to the last modification time.
# Files will be removed if the files or folders last modification time is older than the specified hours.
hours = int(input(print("Please specify the age of the files with to delete")))

temp_file_deleter(path, hours)
sleep(5)
