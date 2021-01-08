import os
import time
import glob
import enum
from utils.navigation_stack import NavigationStack
from utils.favorites import FavoritesHandler


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
        self.favorites = FavoritesHandler()

    @staticmethod
    def get_home_path():
        return os.path.expanduser("~")

    @staticmethod
    def get_folder_file_count(path,hidden):
        if hidden:
            try:
                num = len(os.listdir(path))
            except PermissionError or TypeError:
                num = 0
        if not hidden:
            try:
                num = len(glob.glob(os.path.join(path, '*')))
            except PermissionError or TypeError:
                num = 0
        return num

    @staticmethod
    def get_content_from_path(path, hidden):
        try:
            # orig_path = os.getcwd()
            # os.chdir(path)
            contents = os.listdir(path)
        except PermissionError or TypeError:
            contents = []

        if hidden:
            dir_names = [item for item in contents if
                         os.path.isdir(os.path.join(path, item))]
            file_names = [item for item in contents if
                          os.path.isfile(os.path.join(path, item))]

        if not hidden:
            dir_names = [item for item in contents if
                            os.path.isdir(os.path.join(path, item)) and not item.startswith('.')]
            file_names = [item for item in contents if
                          os.path.isfile(os.path.join(path, item)) and not item.startswith('.')]

        file_paths = []
        dir_paths = []
        for item in dir_names:
            if os.path.isdir(os.path.join(path, item)):
                dir_paths.append(os.path.join(path, item))
        for item in file_names:
            if os.path.isfile(os.path.join(path, item)):
                file_paths.append(os.path.join(path, item))

        # files_time = []
        # for i in file_paths:
        #     try:
        #         files_time.append(time.strftime('%m/%d/%Y', time.gmtime(os.path.getmtime(file_paths.pop()))))
        #     except FileNotFoundError as e:
        #     # except IOError as e:
        #         print(e)
        # print(files_time)
        dir_dict_details = {}
        for key in dir_names:
            for value in dir_paths:
                dir_dict_details[key] = value
                dir_paths.remove(value)
                break
        file_dict_details = {}
        for key in file_names:
            for value in file_paths:
                file_dict_details[key] = value
                file_paths.remove(value)
                break

        dir_details = [(dir_name,
                        # files_time.pop(),
                        # time.strftime('%m/%d/%Y', time.gmtime(
                        #     os.path.getsize(str(dir_path)))),
                        "File Folder",
                        "")
                       for dir_name,dir_path in dir_dict_details.items()]
        file_details = [(file_name,
                         # time last modified
                         #     time.strftime('%m/%d/%Y', time.gmtime(
                         #         os.path.getmtime(file_name))) ,
                         # extension
                         os.path.splitext(file_name)[1].upper() + " File",
                         # size
                         "{} KB".format(
                             int(Model.get_file_size(file_name, SizeUnit.KB))))
                        for file_name in file_names]
        # os.chdir(orig_path)
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
        try:
            size = os.path.getsize(file_name)
        except FileNotFoundError as fnf:
            return 0
        return Model.convert_unit(size, size_type)
