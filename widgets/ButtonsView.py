import tkinter as tk
import tkinter.ttk as ttk


class ButtonsView:
    PAD = 3
    MARGIN_X = 5
    MARGIN_Y = 10

    def __init__(self, root, controller):
        self.controller = controller
        self.frame = tk.Frame(root)
        self.label = tk.Label(self.frame, text="Options",
                              font="Arial 12 bold", anchor="w", padx=ButtonsView.MARGIN_X,
                              pady=ButtonsView.MARGIN_X * 2)
        self.label.pack(fill=tk.X)
        self.copy_btn = tk.Button(self.frame, text="Copy", font="Arial 9")
        # self.copy_btn.grid(row=0, column=0, padx=5)
        # self.copy_btn.bind("<Button-1>", controller.show_hidden_files)
        self.copy_btn.pack(side=tk.LEFT, padx=(ButtonsView.MARGIN_X, ButtonsView.MARGIN_X))
        self.paste_btn = tk.Button(self.frame, text="Paste", font="Arial 9")
        # self.paste_btn.grid(row=0,column=1, padx=5)
        self.paste_btn.pack(side=tk.LEFT, padx=(ButtonsView.MARGIN_X, ButtonsView.MARGIN_X))
        self.move_btn = tk.Button(self.frame, text="Move", font="Arial 9")
        # self.move_btn.grid(row=0, column=2, padx=5)
        self.move_btn.pack(side=tk.LEFT, padx=(ButtonsView.MARGIN_X, ButtonsView.MARGIN_X))
        # self.load_to_fav(controller.model.get_home_path())
        # self.add_btn.grid(row=1, column=0, padx=ButtonsView.MARGIN_X, pady=ButtonsView.MARGIN_Y)
        # self.all_checkbox.bind("<Button-1>", controller.print_all_selected)
        # self.none_checkbox.bind("<Button-1>", controller.print_none_selected)
        self.frame.grid(row=2, column=0,
                        sticky=tk.NSEW,
                        padx=ButtonsView.MARGIN_X, pady=ButtonsView.MARGIN_Y)
