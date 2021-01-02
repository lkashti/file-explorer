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
        self.view.center_frame.favorites_view.load_favorites()
        self.root.mainloop()

    def print_all_selected(self, event):
        if self.view.center_frame.select_view.all_var.get() == 0:
            self.view.center_frame.right_frame.tree.selection_set(
                self.view.center_frame.right_frame.tree.get_children())
            self.view.center_frame.select_view.none_checkbox.config(
                state=tk.DISABLED)
        if self.view.center_frame.select_view.all_var.get() == 1:
            self.view.center_frame.select_view.none_checkbox.config(
                state=tk.NORMAL)

    def print_none_selected(self, event):
        if self.view.center_frame.select_view.none_var.get() == 0:
            self.view.center_frame.right_frame.tree.selection_set()
            self.view.center_frame.select_view.all_checkbox.config(
                state=tk.DISABLED)
        if self.view.center_frame.select_view.none_var.get() == 1:
            self.view.center_frame.select_view.all_checkbox.config(
                state=tk.NORMAL)

    def add_to_favorites(self, event):
        # show addition in the view
        favs = [item.get("path") for item in self.model.favorites.get()]
        if self.view.navbar.path.get() not in favs:
            fav_listbox = self.view.center_frame.favorites_lb_view.listbox
            fav_listbox.insert("end",
                               " ⭐ " + self.view.navbar.path.get())
            # store favorite object in json file

            self.model.favorites.store(self.view.navbar.path.get())

    def rmv_from_favorites(self, event):
        # delete from view
        list_box = self.view.center_frame.favorites_lb_view.listbox
        selected = list_box.curselection()
        if selected is not ():
            # the split is used to dismiss the star icon
            selected_path = list_box.get(selected).split(" ", 2)[2]
            list_box.delete(selected)
            # remove from json file
            self.model.favorites.remove(selected_path)

    def show_hidden_files(self, event):
        pass

    def handle_home_event(self, event):
        # event.widget# Pass data to view
        if self.view.navbar.path.get() != self.model.get_home_path():
            self.model.back_stack.clear_stack()
            self.model.forward_stack.clear_stack()
            self.update_all_views(self.model.get_home_path())

    def handle_back_event(self, event):
        if len(self.model.back_stack.stack) > 0:
            self.model.forward_stack.push(self.view.navbar.path.get())
            self.update_all_views(self.model.back_stack.pop())

    def handle_forward_event(self, event):
        if len(self.model.forward_stack.stack) > 0:
            self.model.back_stack.push(self.view.navbar.path.get())
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
        if os.path.isdir(os.path.join(self.view.navbar.path.get(), item_text)):
            new_path = os.path.join(self.view.navbar.path.get(), item_text)
            self.model.back_stack.push(self.view.navbar.path.get())
            self.model.forward_stack.clear_stack()
            self.update_all_views(new_path)
            self.view.status_bar.item_label.config(text="None")

    def on_tree_select(self, event):
        index = self.view.center_frame.right_frame.tree.focus()
        line_tup = self.view.center_frame.right_frame.tree.item(index)
        self.view.center_frame.buttons_view.file_name = line_tup['text']
        self.view.status_bar.item_label.config(text=line_tup['text'])

    def update_treeview(self, path):
        self.view.center_frame.right_frame.tree.delete(
            *self.view.center_frame.right_frame.tree.get_children())
        folder_details, file_details = self.model.get_content_from_path(path)
        self.view.center_frame.show_folders_and_files(folder_details,
                                                      file_details)

    def on_favorite_click(self, new_path):
        if os.path.isdir(new_path):
            self.model.back_stack.push(self.view.navbar.path.get())
            self.model.forward_stack.clear_stack()
            self.update_all_views(new_path)

    def update_all_views(self, path):
        self.update_treeview(path)
        self.view.navbar.path.set(path)
        self.view.status_bar.load_item_count(path)


if __name__ == '__main__':
    # original = r'C:\Users\noami\OneDrive\Desktop\logos\back.png'
    # target = r'C:\Users\noami\OneDrive\Desktop\back.png'
    c = Controller()
