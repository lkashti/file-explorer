import tkinter as tk
from Model import Model
from View import View
import os


class Controller:
    def __init__(self):
        self.root = tk.Tk()
        self.model = Model()
        # Pass to view links on root frame and controller object
        self.view = View(self.root, self)
        self.root.deiconify()
        # initialization
        self.view.navbar.path.set(self.model.get_home_path())
        self.update_treeview(self.model.get_home_path())
        self.root.mainloop()

    def home_btn_handler(self, event):
        # event.widget# Pass data to view
        if self.view.navbar.path.get() != self.model.get_home_path():
            self.view.navbar.path.set(self.model.get_home_path())

    def update_treeview(self, path):
        self.view.viewer.viewer_tree.delete(*self.view.viewer.viewer_tree.get_children())
        folder_details, file_details = self.model.get_content_from_path(path)
        self.view.viewer.show_folders_and_files(folder_details, file_details)

    def update_all_views(self, path):
        self.update_treeview(path)
        self.view.navbar.path.set(path)
        # os.chdir(path)
        print(os.getcwd())


if __name__ == '__main__':
    c = Controller()
