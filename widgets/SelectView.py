import tkinter as tk
import tkinter.ttk as ttk

class SelectView:
    PAD = 3
    MARGIN_X = 5
    MARGIN_Y = 10

    def __init__(self, root, controller):
        self.controller = controller
        self.frame = tk.Frame(root)
        self.select_label = tk.Label(self.frame, text="Select Items",
                                     font="Arial 12 bold")
        self.select_label.pack(side=tk.LEFT)
        self.all_var = tk.IntVar()
        self.none_var = tk.IntVar()
        self.all_checkbox = tk.Checkbutton(self.frame,text="All",font="Arial 10",variable=self.all_var)
        self.none_checkbox = tk.Checkbutton(self.frame, text="None",font="Arial 10",variable=self.none_var)
        self.all_checkbox.pack(side=tk.LEFT, padx=(10, 4))
        self.none_checkbox.pack(side=tk.LEFT, padx=(4, 4))
        self.all_checkbox.bind("<Button-1>", controller.print_all_selected)
        self.none_checkbox.bind("<Button-1>", controller.print_none_selected)
        self.frame.grid(row=0, column=0,
                        sticky=tk.NSEW,
                        padx=SelectView.MARGIN_X,
                        pady=SelectView.MARGIN_Y)
