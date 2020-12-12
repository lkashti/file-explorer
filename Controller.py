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
        self.update_all_views(self.model.get_home_path())
        self.root.mainloop()

    def handle_home_event(self, event):
        # event.widget# Pass data to view
        if self.view.navbar.path.get() != self.model.get_home_path():
            self.model.nav_stack.push(os.getcwd())
            self.update_all_views(self.model.get_home_path())

    def handle_back_event(self, event):
        if len(self.model.nav_stack.stack) > 0:
            self.update_all_views(self.model.nav_stack.pop())

    def on_double_click(self, event):
        # get selected item
        try:
            item = self.view.viewer.viewer_tree.selection()[0]
            item_text = self.view.viewer.viewer_tree.item(item, "text")
        except IndexError:

            return
        # clear tree before update
        if os.path.isdir(item_text):
            new_path = os.path.join(self.view.navbar.path.get(), item_text)
            self.model.nav_stack.push(self.view.navbar.path.get())
            print(self.model.nav_stack.stack)
            self.update_all_views(new_path)

    def update_treeview(self, path):
        self.view.viewer.viewer_tree.delete(*self.view.viewer.viewer_tree.get_children())
        folder_details, file_details = self.model.get_content_from_path(path)
        self.view.viewer.show_folders_and_files(folder_details, file_details)

    def update_all_views(self, path):
        print(path)
        self.update_treeview(path)
        self.view.navbar.path.set(path)


if __name__ == '__main__':
    c = Controller()
