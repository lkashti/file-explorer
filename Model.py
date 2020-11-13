import os


class Model:
    def __init__(self):
        pass

    @staticmethod
    def get_home_path():
        return os.path.expanduser("~")

    @staticmethod
    def get_folders_contents(path):
        os.chdir(path)
        contents = os.listdir(path)
        dirs = [item for item in contents if os.path.isdir(item)]
        files = [item for item in contents if os.path.isfile(item)]
        return dirs, files
