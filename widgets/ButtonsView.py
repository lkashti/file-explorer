import tkinter as tk
import tkinter.ttk as ttk

class ButtonsView:
    PAD = 3
    MARGIN_X = 5
    MARGIN_Y = 10

    def __init__(self, root, controller):
        self.controller = controller
        self.frame = tk.Frame(root)
        self.copy_btn = tk.Button(self.frame, text="Copy", font="Arial 9")
        # self.copy_btn.grid(row=0, column=0, padx=5)
        self.copy_btn.pack(side=tk.LEFT, padx=(ButtonsView.MARGIN_X*2, ButtonsView.MARGIN_X))
        self.paste_btn = tk.Button(self.frame, text="Paste", font="Arial 9")
        # self.paste_btn.grid(row=0,column=1, padx=5)
        self.paste_btn.pack(side=tk.LEFT, padx=(ButtonsView.MARGIN_X, ButtonsView.MARGIN_X))
        self.move_btn = tk.Button(self.frame, text="Move", font="Arial 9")
        # self.move_btn.grid(row=0, column=2, padx=5)
        self.move_btn.pack(side=tk.LEFT, padx=(ButtonsView.MARGIN_X, ButtonsView.MARGIN_X))
        self.add_btn = tk.Button(self.frame, text="Add 2 Fav", font="Arial 9")
        # self.add_btn.grid(row=1, column=0, padx=ButtonsView.MARGIN_X, pady=ButtonsView.MARGIN_Y)
        self.add_btn.pack()
        # self.all_checkbox.bind("<Button-1>", controller.print_all_selected)
        # self.none_checkbox.bind("<Button-1>", controller.print_none_selected)
        self.frame.grid(row=3, column=0,
                        sticky=tk.NSEW,
                        padx=ButtonsView.MARGIN_X,
                        pady=ButtonsView.MARGIN_Y)
