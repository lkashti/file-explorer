import tkinter as tk
from Model import Model
from View import View


class Controller:
    def __init__(self):
        self.root = tk.Tk()
        self.model = Model()
        # Pass to view links on root frame and controller object
        self.view = View(self.root, self)
        self.root.deiconify()
        # initialization
        self.view.NavBar.path.set(self.model.get_home_path())
        self.update_viewer(self.model.get_home_path())
        self.root.mainloop()

    def home_btn_handler(self, event):
        # event.widget# Pass data to view
        if self.view.NavBar.path.get() != self.model.get_home_path():
            self.view.NavBar.path.set(self.model.get_home_path())

    def update_viewer(self, path):
        folder_details, file_details = self.model.get_content_from_path(path)
        self.view.Viewer.show_folders_and_files(folder_details, file_details)


if __name__ == '__main__':
    c = Controller()
