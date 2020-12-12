import tkinter as tk
import tkinter.ttk as ttk
import os


class View:
    def __init__(self, master, controller):
        master.title("File Explorer")
        self.width = int(master.winfo_screenwidth() * 0.8)
        self.height = int(master.winfo_screenheight() * 0.6)
        master.geometry("{}x{}".format(self.width, self.height))
        master.resizable(0, 0)
        self.controller = controller
        self.navbar = NavBar(master, controller, self.width, self.height)
        self.viewer = Viewer(master, controller, self.width, self.height)


class NavBar:
    PAD = 3
    MARGIN_X = 5
    MARGIN_Y = 10

    def __init__(self, root, controller, width, height):
        self.controller = controller
        self.navbar_frame = tk.Frame(root, width=width, height=0.05 * height)
        self.navbar_frame.grid(row=0, column=0, sticky=tk.W,
                               padx=NavBar.MARGIN_X)
        self.home_btn = tk.Button(self.navbar_frame, text="Home")
        self.home_btn.pack(side=tk.LEFT, padx=NavBar.MARGIN_X,
                           pady=NavBar.MARGIN_Y)
        self.back_btn = tk.Button(self.navbar_frame, text="Back")
        self.back_btn.pack(side=tk.LEFT, padx=NavBar.MARGIN_X,
                           pady=NavBar.MARGIN_Y)
        self.forward_btn = tk.Button(self.navbar_frame, text="Forward")
        self.forward_btn.pack(side=tk.LEFT, padx=NavBar.MARGIN_X,
                              pady=NavBar.MARGIN_Y)

        self.path_field = tk.Entry(self.navbar_frame, width=int(0.125 * width))
        self.path = tk.StringVar()
        self.path_field.configure(textvariable=self.path)
        self.path_field.pack(side=tk.RIGHT, ipady=NavBar.PAD,
                             pady=NavBar.MARGIN_Y)
        self.home_btn.bind("<Button>", controller.handle_home_event)
        self.back_btn.bind("<Button>", controller.handle_back_event)


class Viewer:
    PAD = 10

    def __init__(self, root, controller, width, height):
        self.controller = controller
        self.viewer_tree = ttk.Treeview(root)

        self.viewer_tree["columns"] = ("one", "two", "three","four")
        self.viewer_tree["show"] = "headings"
        self.viewer_tree.column("one", width=200, minwidth=170, stretch=tk.NO)
        self.viewer_tree.column("two", width=150, minwidth=120, stretch=tk.NO)
        self.viewer_tree.column("three", width=100, minwidth=50)
        self.viewer_tree.column("four", width=100, minwidth=50, stretch=tk.NO)

        self.viewer_tree.heading("one", text="Name", anchor=tk.W)
        self.viewer_tree.heading("two", text="Date modified", anchor=tk.W)
        self.viewer_tree.heading("three", text="Type", anchor=tk.W)
        self.viewer_tree.heading("four", text="Size", anchor=tk.W)

        self.viewer_tree.bind("<Double-1>", controller.on_double_click)
        self.viewer_tree.grid(row=1, column=0, padx=Viewer.PAD, sticky="nsew")

    def show_folders_and_files(self, folder_details, file_details):
        idx = 1
        for folder_detail in folder_details:
            self.viewer_tree.insert("", index="end", iid=idx,
                                    text=folder_detail[0],
                                    values=folder_detail[0:])
            idx += 1
        for file_detail in file_details:
            self.viewer_tree.insert("", index="end", text=file_detail[0],
                                    values=file_detail[0:])
            idx += 1


class Folder:
    PADDING = 10

    def __init__(self, root, folder_name, row, col):
        self.folder_frame = tk.Frame(
            root,
            width=60, height=80, bg="#e5e6e4"
        )
        self.folder_name = folder_name
        tk.Frame(self.folder_frame, width=50, height=50, bg="black").pack()
        self.folder_label = tk.Label(self.folder_frame, text=self.folder_name,
                                     bg="#e5e6e4")
        self.folder_label.pack(side=tk.BOTTOM, fill=tk.BOTH)

        self.folder_frame.grid_propagate(False)
        self.folder_frame.grid(row=row, column=col, padx=Viewer.PAD * 2,
                               pady=Viewer.PAD * 2)


class File:
    PADDING = 10

    def __init__(self, root, file_name, row, col):
        self.file_frame = tk.Frame(
            root,
            bd=2, relief=tk.SUNKEN
        )
        self.file_name = file_name
        self.file_label = tk.Label(self.file_frame, text=self.file_name)
        self.file_frame.pack_propagate(0)
        self.file_label.pack()
        self.file_frame.grid(row=row, column=col, padx=Viewer.PAD * 2,
                             pady=Viewer.PAD * 2)
