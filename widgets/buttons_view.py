import tkinter as tk
import os
import shutil


class ButtonsView:
    PAD = 3
    MARGIN_X = 5
    MARGIN_Y = 10

    def __init__(self, root, controller):
        self.controller = controller
        self.frame = tk.Frame(root)
        self.label = tk.Label(self.frame, text="Options",
                              font="Arial 12 bold", anchor="w", padx=ButtonsView.MARGIN_X)
        self.label.pack(fill=tk.X)
        self.copy_btn = tk.Button(self.frame, text="Copy", font="Arial 9 bold")
        self.src_path = ""
        self.dst_path = ""
        self.file_name = ""
        self.copy_btn.pack(side=tk.LEFT, padx=(ButtonsView.MARGIN_X * 2, ButtonsView.MARGIN_X),
                           pady=ButtonsView.MARGIN_X)
        self.paste_btn = tk.Button(self.frame, text="Paste", font="Arial 9 bold")
        self.paste_btn.pack(side=tk.LEFT, padx=(ButtonsView.MARGIN_X, ButtonsView.MARGIN_X), pady=ButtonsView.MARGIN_X)
        self.move_btn = tk.Button(self.frame, text="Move", font="Arial 9 bold")
        self.move_btn.pack(side=tk.LEFT, padx=(ButtonsView.MARGIN_X, ButtonsView.MARGIN_X), pady=ButtonsView.MARGIN_X)
        self.delete_btn = tk.Button(self.frame, text="Delete", font="Arial 9 bold")
        self.delete_btn.pack(side=tk.LEFT, padx=(ButtonsView.MARGIN_X, ButtonsView.MARGIN_X), pady=ButtonsView.MARGIN_X)
        self.copy_btn.bind("<Button-1>", self.handle_copy_event)
        self.paste_btn.bind("<Button-1>", self.handle_paste_event)
        self.move_btn.bind("<Button-1>", self.handle_copy_event)
        self.move_btn.bind("<Button-3>", self.handle_move_event)
        self.delete_btn.bind("<Button-1>", self.handle_delete_event)
        self.frame.grid(row=2, column=0,
                        sticky=tk.NSEW,
                        padx=ButtonsView.MARGIN_X, pady=ButtonsView.MARGIN_Y)

    def handle_copy_event(self, event):
        self.src_path = self.controller.view.navbar.path.get() + "\\" + self.file_name
        print(self.src_path)

    def handle_paste_event(self, event):
        self.cpy_src_dst()
        self.controller.update_all_views(self.controller.view.navbar.path.get())

    def handle_move_event(self, event):
        self.cpy_src_dst()
        os.remove(self.src_path)
        self.controller.update_all_views(self.controller.view.navbar.path.get())

    def handle_delete_event(self, event):
        self.src_path = self.controller.view.navbar.path.get() + "\\" + self.file_name
        os.remove(self.src_path)
        self.controller.update_all_views(self.controller.view.navbar.path.get())

    def cpy_src_dst(self):
        without_extra_slash = os.path.normpath(self.src_path)
        file_to_copy = os.path.basename(without_extra_slash)
        self.dst_path = self.controller.view.navbar.path.get() + "\\" + file_to_copy
        shutil.copyfile(self.src_path, self.dst_path)
