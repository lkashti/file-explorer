import tkinter as tk
from model import Model
from view import View
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

    def print_all_selected(self):
        if self.view.center_frame.select_view.all_var.get() == 0:
            self.view.center_frame.right_frame.tree.selection_set(
                self.view.center_frame.right_frame.tree.get_children())
            self.view.center_frame.select_view.none_checkbox.config(state=tk.DISABLED)
        if self.view.center_frame.select_view.all_var.get() == 1:
            self.view.center_frame.select_view.none_checkbox.config(state=tk.NORMAL)

    def print_none_selected(self):
        if self.view.center_frame.select_view.none_var.get() == 0:
            self.view.center_frame.right_frame.tree.selection_set()
            self.view.center_frame.select_view.all_checkbox.config(state=tk.DISABLED)
        if self.view.center_frame.select_view.none_var.get() == 1:
            self.view.center_frame.select_view.all_checkbox.config(state=tk.NORMAL)

    def add_to_favorites(self, event):
        self.view.center_frame.favorites_lb_view.listbox.insert("end", " ⭐ " + self.view.navbar.path.get())

    def rmv_to_favorites(self, event):
        listbox_len = self.view.center_frame.favorites_lb_view.listbox.size() - 1
        self.view.center_frame.favorites_lb_view.listbox.delete(listbox_len)

    def show_hidden_files(self, event):
        print("asdasd")

    def handle_home_event(self, event):
        # event.widget# Pass data to view
        if self.view.navbar.path.get() != self.model.get_home_path():
            self.model.back_stack.push(os.getcwd())
            self.model.forward_stack.clear_stack()
            self.update_all_views(self.model.get_home_path())

    def handle_back_event(self, event):
        if len(self.model.back_stack.stack) > 0:
            self.model.forward_stack.push(os.getcwd())
            self.update_all_views(self.model.back_stack.pop())

    def handle_forward_event(self, event):
        if len(self.model.forward_stack.stack) > 0:
            self.model.back_stack.push(os.getcwd())
            self.update_all_views(self.model.forward_stack.pop())

    def on_double_click(self, event):
        # get selected item
        try:
            item = self.view.center_frame.right_frame.tree.selection()[0]
            item_text = self.view.center_frame.right_frame.tree.item(item,
                                                                     "text")
        except IndexError:
            return
        # clear tree before update
        if os.path.isdir(item_text):
            new_path = os.path.join(self.view.navbar.path.get(), item_text)
            self.model.back_stack.push(self.view.navbar.path.get())
            self.model.forward_stack.clear_stack()
            self.update_all_views(new_path)

    def on_tree_select(self, event):
        index = self.view.center_frame.right_frame.tree.focus()
        line_tup = self.view.center_frame.right_frame.tree.item(index)
        self.view.center_frame.buttons_view.file_name = line_tup['text']

    def update_treeview(self, path):
        self.view.center_frame.right_frame.tree.delete(
            *self.view.center_frame.right_frame.tree.get_children())
        folder_details, file_details = self.model.get_content_from_path(path)
        self.view.center_frame.show_folders_and_files(folder_details,
                                                      file_details)

    def on_click_list(self, new_path):
        print(new_path)
        if os.path.isdir(new_path):
            self.model.back_stack.push(self.view.navbar.path.get())
            self.model.forward_stack.clear_stack()
            print(os.path.normpath(new_path))
            self.update_all_views(new_path)

    def update_all_views(self, path):
        self.update_treeview(path)
        self.view.navbar.path.set(path)
        self.view.status_bar.load_item_count(path)


if __name__ == '__main__':
    # original = r'C:\Users\noami\OneDrive\Desktop\logos\back.png'
    # target = r'C:\Users\noami\OneDrive\Desktop\back.png'
    c = Controller()