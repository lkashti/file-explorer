from widgets.favorites_bar_view import FavoritesView
from widgets.favorites_listbox_view import ListBox
from widgets.select_view import SelectView
from widgets.status_bar_view import StatusBarView
from widgets.tree_view import TreeView
from widgets.buttons_view import ButtonsView
from widgets.log_view import Log
import tkinter.ttk as ttk
import tkinter as tk


class View:
    def __init__(self, root: tk.Tk, controller):
        self.controller = controller
        root.title("File Explorer")
        # Set size to app's window
        self.width = 1092
        self.height = 614
        self.horizon_offset = 100
        self.vertical_offset = 50
        root.geometry(
            "{}x{}+{}+{}".format(self.width, self.height,
                                 self.horizon_offset, self.vertical_offset))
        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)
        root.wm_attributes("-topmost", 1)
        root.resizable(0, 0)
        # Initialize three main frames into root frame
        self.navbar = NavBar(root, controller, self.width)
        self.center_frame = CenterFrame(root, controller)
        self.status_bar = StatusBarView(root, controller)


class NavBar:
    PAD = 3
    MARGIN_X = 5
    MARGIN_Y = 10
    '''
    Top bar widget - navigation buttons, path and search fields  
    '''
    def __init__(self, root, controller, width):
        self.controller = controller
        self.navbar_frame = tk.Frame(root, bg="lavender")
        self.navbar_frame.grid_rowconfigure(1, weight=1)
        self.navbar_frame.grid_columnconfigure(0, weight=1)
        self.navbar_frame.grid(row=0, column=0, sticky="ew",
                               ipady=NavBar.MARGIN_Y, ipadx=NavBar.PAD)
        # Initializing buttons
        self.home_btn = tk.Button(self.navbar_frame, text="Home", font="Arial 9 bold")
        self.home_btn.pack(side=tk.LEFT, padx=NavBar.MARGIN_X)
        self.back_btn = tk.Button(self.navbar_frame, text="Back", font="Arial 9 bold")
        self.back_btn.pack(side=tk.LEFT, padx=NavBar.MARGIN_X)
        self.forward_btn = tk.Button(self.navbar_frame, text="Forward", font="Arial 9 bold")
        self.forward_btn.pack(side=tk.LEFT, padx=NavBar.MARGIN_X)
        # Initializing text fields
        self.path_field = tk.Entry(self.navbar_frame, width=int(0.1 * width))
        self.path = tk.StringVar()
        self.path_field.configure(textvariable=self.path)
        self.path_field.pack(side=tk.LEFT, ipady=NavBar.PAD)
        self.search_field = tk.Entry(self.navbar_frame,
                                     width=int(0.04 * width))
        self.search_text = tk.StringVar()
        self.search_field.configure(textvariable=self.search_text)
        self.search_field.pack(side=tk.LEFT, ipady=NavBar.PAD,
                               padx=NavBar.MARGIN_X)
        self.search_field.insert(0, "Search...")
        # Bind to functionality
        self.search_field.bind("<FocusIn>",
                               lambda e: self.search_text.set(""))
        self.search_field.bind("<FocusOut>",
                               lambda e: self.search_text.set("Search..."))
        self.home_btn.bind("<ButtonRelease>", self.controller.handle_home_event)
        self.back_btn.bind("<ButtonRelease>", self.controller.handle_back_event)
        self.forward_btn.bind("<ButtonRelease>",
                              self.controller.handle_forward_event)
        self.path_field.bind('<Return>', self.controller.handle_enter_path)
        self.search_field.bind('<Return>',self.controller.handle_search_path)


class CenterFrame:
    PAD = 3
    MARGIN_X = 5
    MARGIN_Y = 10
    '''
    Central widget - splits into two part 
    Left side - features and controlling the app
    Right side - Folders and files tree view   
    '''
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
                                                                  ipadx=120)
        ttk.Separator(self.left_frame, orient=tk.HORIZONTAL).grid(row=3,
                                                                  ipadx=120)
        ttk.Separator(self.left_frame, orient=tk.HORIZONTAL).grid(row=6,
                                                                  ipadx=120)
        # Initialize widgets for left side
        self.favorites_view = FavoritesView(self.left_frame, controller)
        self.favorites_lb_view = ListBox(self.left_frame, controller)
        self.select_view = SelectView(self.left_frame, controller)
        self.buttons_view = ButtonsView(self.left_frame, controller)
        self.log = Log(self.left_frame, controller)

    # Display items
    def show_folders_and_files(self, folder_details, file_details):
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
