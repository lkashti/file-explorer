from utils.navigation_stack import NavigationStack
from utils.favorites import FavoritesHandler
import time
import glob
import enum
import os


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
    def get_folder_file_count(path, hidden):
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
            contents = os.listdir(path)
        except PermissionError or TypeError:
            contents = []
        files_time = []
        dirs_time = []
        files_paths = []
        dirs_paths = []
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
        dir_dict_details, file_dict_details = Model.create_path_lists(
            file_names, dir_names, dirs_paths, files_paths, files_time, dirs_time, path)
        dir_details = [(dir_name, dir_path, dirs_time.pop(), "File Folder",
                        "{} KB".format(
                            int(Model.get_file_size(dir_path, SizeUnit.KB))))
                       for dir_name, dir_path in dir_dict_details.items()]
        file_details = [(file_name, file_path, files_time.pop(),
                         os.path.splitext(file_name)[1].upper() + " File",
                         "{} KB".format(
                             int(Model.get_file_size(file_path, SizeUnit.KB))))
                        for file_name, file_path in file_dict_details.items()]

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
            # size = os.stat('C:\\Python27\\Lib\\genericpath.py').st_size
        except FileNotFoundError as fnf:
            return 0
        return Model.convert_unit(size, size_type)

    @staticmethod
    def create_path_lists(file_names, dir_names, dirs_paths, files_paths, files_time, dirs_time, path):
        dir_dict_details = {}
        file_dict_details = {}
        for item in dir_names:
            if os.path.isdir(os.path.join(path, item)):
                dirs_paths.append(os.path.join(path, item))
        for item in file_names:
            if os.path.isfile(os.path.join(path, item)):
                files_paths.append(os.path.join(path, item))

        for key in dir_names:
            for value in dirs_paths:
                dir_dict_details[key] = value
                dirs_paths.remove(value)
                break

        for key in file_names:
            for value in files_paths:
                file_dict_details[key] = value
                files_paths.remove(value)
                break
        for file_name, file_path in file_dict_details.items():
            try:
                files_time.append(time.strftime('%m/%d/%Y', time.gmtime(os.path.getmtime(file_path))))
            except FileNotFoundError:
                files_time.append("No Permission")

        for dirs_name, dir_path in dir_dict_details.items():
            try:
                dirs_time.append(time.strftime('%m/%d/%Y', time.gmtime(os.path.getmtime(dir_path))))
            except FileNotFoundError:
                dirs_time.append("No Permission")
        return dir_dict_details, file_dict_details
