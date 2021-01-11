import tkinter as tk
from tkinter import ttk as ttk

from widgets.buttons_view import ButtonsView
from widgets.favorites_bar_view import FavoritesView
from widgets.favorites_listbox_view import ListBox
from widgets.log_view import Log
from widgets.select_view import SelectView
from widgets.tree_view import TreeView


class CenterFrame:
    """
    Central widget - splits into two part
    Left side - features and controlling the app
    Right side - Folders and files tree view
    """
    PAD = 3
    MARGIN_X = 5
    MARGIN_Y = 10

    def __init__(self, root, controller):
        self.controller = controller
        self.center_frame = tk.Frame(root, bd=1, relief=tk.SUNKEN)
        self.center_frame.grid(row=1, column=0, sticky="nsew")
        self.center_frame.grid_rowconfigure(0, weight=1)
        self.center_frame.grid_columnconfigure(1, weight=1)
        # Right side
        self.right_frame = TreeView(self.center_frame, controller)
        self.right_frame.frame.grid(row=0, column=1, sticky="nsew")
        # Left side
        self.left_frame = tk.Frame(self.center_frame, bg="lavender")
        self.left_frame.grid(row=0, column=0, sticky="nsew")
        ttk.Separator(self.left_frame, orient=tk.HORIZONTAL).grid(row=1,
                                                                  ipadx=130)
        ttk.Separator(self.left_frame, orient=tk.HORIZONTAL).grid(row=3,
                                                                  ipadx=130)
        ttk.Separator(self.left_frame, orient=tk.HORIZONTAL).grid(row=6,
                                                                  ipadx=130)
        # Initialize widgets for left side
        self.favorites_view = FavoritesView(self.left_frame, controller)
        self.favorites_lb_view = ListBox(self.left_frame, controller)
        self.select_view = SelectView(self.left_frame, controller)
        self.buttons_view = ButtonsView(self.left_frame, controller)
        self.log = Log(self.left_frame, controller)

    # Display items
    def show_folders_and_files(self, folder_details, file_details):
        """Inserts formatted data to the treeview

        :param folder_details: list - formatted folder details to be represented in the treeview
        :param file_details: list - formatted file details to be represented in the treeview
        """
        idx = 1
        for folder_detail in folder_details:
            self.right_frame.tree.insert("", index="end", iid=idx,
                                         text=folder_detail[0],
                                         values=folder_detail[0:])
            idx += 1
        for file_detail in file_details:
            self.right_frame.tree.insert("", index="end",
                                         text=file_detail[0],
                                         values=file_detail[0:])
            idx += 1