import os
from datetime import datetime as dt


def is_old(item: str, delete_before: int) -> bool:
	"""Checks if the file was modified before the specified time"""
	now = dt.now().timestamp()
	item_last_update_time = os.path.getmtime(item)
	return (now - item_last_update_time) > delete_before * 3600


def get_old_files(folder_path: str, delete_before: int) -> list:
	"""Gets the `list` of files from the input path."""
	file_list = []
	for root, sub_folder, items in os.walk(folder_path, topdown=False):
		for i in range(len(items)):
			item = os.path.join(root, items[i])
			if is_old(item, delete_before):
				file_list.append(item)
	return file_list


def get_old_folders(folder_path: str, delete_before: int) -> list:
	"""Gets the `list` of folders from the input path."""
	folder_list = []
	for root, sub_folder, items in os.walk(folder_path, topdown=False):
		if is_old(root, delete_before):
			folder_list.append(root)
	return folder_list[:-1]


def temp_file_deleter():
	"""Deletes items in the path as per to the last modification time"""
	path = input(print("Please enter the main folder path: "))
	hours = int(input("Files will be deleted which are not updated since x hours. Please enter 'x': "))
	files = get_old_files(path, hours)
	folders = get_old_folders(path, hours)
	for i in range(len(files)):
		os.remove(files[i])
	for i in range(len(folders)):
		os.rmdir(folders[i])
	return folders + files


deleted_items = temp_file_deleter()
source_file = open('deleted_file_list.txt', 'a')
print(f"{len(deleted_items)} items were deleted at: " + str(dt.now()) + " " + str(deleted_items), file=source_file)
source_file.close()
