import os
import time
import enum
from utils.NavigationStack import NavigationStack


# Enum for size units
class SizeUnit(enum.Enum):
    BYTES = 1
    KB = 2
    MB = 3
    GB = 4


class Model:
    def __init__(self):
        self.back_stack = NavigationStack()
        self.forward_stack = NavigationStack()

    @staticmethod
    def get_home_path():
        return os.path.expanduser("~")

    @staticmethod
    def get_folder_file_count(path):
        try:
            num = len(os.listdir(path))
        except PermissionError or TypeError:
            num = 0
        return num

    @staticmethod
    def get_folders_contents(path):
        os.chdir(path)
        contents = os.listdir(path)
        dirs = [item for item in contents if os.path.isdir(item)]
        files = [item for item in contents if os.path.isfile(item)]
        return dirs, files

    @staticmethod
    def get_content_from_path(path):
        try:
            os.chdir(path)
            contents = os.listdir(path)
        except PermissionError or TypeError:
            contents = []
        dir_names = [item for item in contents if os.path.isdir(item)]
        file_names = [item for item in contents if os.path.isfile(item)]
        dir_details = [(dir_name,
                        # time.strftime('%m/%d/%Y', time.gmtime(
                        #     os.path.getmtime(dir_name))),
                        "File Folder",
                        "")
                       for dir_name in dir_names]
        file_details = [(file_name,
                         # time last modified
                         # time.strftime('%m/%d/%Y', time.gmtime(
                         #     os.path.getmtime(file_name))),
                         # extension
                         os.path.splitext(file_name)[1].upper() + " File",
                         # size
                         "{} KB".format(
                             int(Model.get_file_size(file_name, SizeUnit.KB))))
                        for file_name in file_names]

        return file_details, dir_details

    @staticmethod
    def convert_unit(size_in_bytes, unit):
        """ Convert the size from bytes to other units like KB, MB or GB"""
        if unit == SizeUnit.KB:
            return size_in_bytes / 1024
        elif unit == SizeUnit.MB:
            return size_in_bytes / (1024 * 1024)
        elif unit == SizeUnit.GB:
            return size_in_bytes / (1024 * 1024 * 1024)
        else:
            return size_in_bytes

    @staticmethod
    def get_file_size(file_name, size_type=SizeUnit.BYTES):
        """ Get file in size in given unit like KB, MB or GB"""
        size = os.path.getsize(file_name)
        return Model.convert_unit(size, size_type)
