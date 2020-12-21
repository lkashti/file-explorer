import tkinter as tk
import tkinter.ttk as ttk


class SelectView:
    PAD = 3
    MARGIN_X = 5
    MARGIN_Y = 10

    def __init__(self, root, controller, height, width):
        self.controller = controller

        self.frame = tk.Frame(root, bd=1,
                              relief=tk.SUNKEN)
        self.frame.grid(row=1, column=0, sticky="nsew",
                        padx=SelectView.MARGIN_X,
                        pady=SelectView.MARGIN_Y)
        self.frame.grid_propagate(0)

        self.select_label = tk.Label(self.frame, text="Select",
                                     font="Arial 15 bold")
        self.select_label.pack()

        self.select_checkbox = tk.Checkbutton(self.frame, width=35)
        self.select_checkbox.pack()

        self.select_combobox = ttk.Combobox(self.frame, width=30)
        self.select_combobox.pack()
