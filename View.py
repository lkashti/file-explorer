import tkinter as tk
import tkinter.ttk as ttk


class View:
    def __init__(self, master, controller):
        master.title("File Explorer")
        self.width = master.winfo_screenwidth() // 2
        self.height = master.winfo_screenheight() // 2
        master.geometry("{}x{}".format(self.width, self.height))
        master.resizable(0, 0)

        self.controller = controller
        self.NavBar = NavBar(master, controller, self.width, self.height)
        self.Viewer = Viewer(master, controller, self.width, self.height)


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
        self.home_btn.bind("<Button>", controller.home_btn_handler)
        # self.back_btn.bind("<Button>", controller.btnHandler)


class Viewer:
    PAD = 10

    def __init__(self, root, controller, width, height):
        self.controller = controller
        self.viewer_tree = ttk.Treeview(root)
        self.viewer_tree["columns"] = ("one", "two", "three")
        self.viewer_tree.column("#0", width=270, minwidth=270, stretch=tk.NO)
        self.viewer_tree.column("one", width=150, minwidth=150, stretch=tk.NO)
        self.viewer_tree.column("two", width=400, minwidth=200)
        self.viewer_tree.column("three", width=300, minwidth=50, stretch=tk.NO)

        self.viewer_tree.heading("#0", text="Name", anchor=tk.W)
        self.viewer_tree.heading("one", text="Date modified", anchor=tk.W)
        self.viewer_tree.heading("two", text="Type", anchor=tk.W)
        self.viewer_tree.heading("three", text="Size", anchor=tk.W)

        self.viewer_tree.grid(row=1, column=0, padx=Viewer.PAD, sticky=tk.W)
        #####
        # self.viewer_frame = tk.Frame(root, width=width - 2 * Viewer.PADDING,
        #                              height=0.9 * height - 2 * Viewer.PADDING,
        #                              bd=2, relief=tk.SUNKEN, bg="#e5e6e4")
        # self.width = width - 2 * Viewer.PADDING
        # self.height = 0.9 * height - 2 * Viewer.PADDING
        #
        # self.folders = []
        # self.files = []
        #
        # self.viewer_frame.grid_propagate(0)
        # self.viewer_frame.grid(row=1, column=0, padx=Viewer.PADDING)
        #####

    def show_folders_and_files(self, folder_details, file_details):
        idx = 1
        for folder_detail in folder_details:
            self.viewer_tree.insert("", index="end", iid=idx,
                                    text=folder_detail[0],
                                    values=folder_detail[1:])
            idx += 1
        for file_detail in file_details:
            self.viewer_tree.insert("", index="end", text=folder_detail[0],
                                    values=file_detail[1:])
            idx += 1
    # def show_folders_and_files(self, folders, files):
    #     row = 0
    #     col = 0
    #     MAX_IN_COL = 6
    #
    #     for folder_name in folders:
    #         Folder(self.viewer_frame, folder_name, row, col)
    #         if col < MAX_IN_COL - 1:
    #             col += 1
    #         else:
    #             row += 1
    #             col = 0
    #     for file_name in files:
    #         File(self.viewer_frame, file_name, row, col)
    #         if col < MAX_IN_COL - 1:
    #             col += 1
    #         else:
    #             row += 1
    #             col = 0


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
