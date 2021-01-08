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
                                     font="Arial 12 bold", anchor="w", padx=SelectView.MARGIN_X)
        self.select_label.pack(fill=tk.X)
        self.all_var = tk.IntVar()
        self.none_var = tk.IntVar()
        self.hidden_var = tk.IntVar()
        self.checkbox_flag = False
        self.hidden_flag = False
        self.all_checkbox = tk.Checkbutton(self.frame, text="All", font="Arial 10", variable=self.all_var)
        self.none_checkbox = tk.Checkbutton(self.frame, text="None", font="Arial 10", variable=self.none_var)
        self.hidden_checkbox = tk.Checkbutton(self.frame, text="Hidden Items", font="Arial 10", variable=self.hidden_var)
        self.all_checkbox.pack(side=tk.LEFT, padx=(10, 4))
        self.none_checkbox.pack(side=tk.LEFT, padx=(4, 4))
        self.hidden_checkbox.pack(side=tk.LEFT, padx=(4, 4))
        self.all_checkbox.bind("<Button-1>", self.controller.select_all)
        self.none_checkbox.bind("<Button-1>", self.controller.select_none)
        self.hidden_checkbox.bind("<Button-1>", self.controller.show_hidden)
        self.frame.grid(row=0, column=0,
                        sticky=tk.NSEW,
                        padx=SelectView.MARGIN_X,
                        pady=SelectView.MARGIN_Y)
