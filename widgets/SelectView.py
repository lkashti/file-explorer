import tkinter as tk


class SelectView:
    PAD = 3
    MARGIN_X = 5
    MARGIN_Y = 10

    def __init__(self, root, controller):
        self.controller = controller

        self.frame = tk.Frame(root)

        self.select_label = tk.Label(self.frame, text="Select",
                                     font="Arial 15 bold")
        self.select_label.pack()

        self.v = tk.IntVar()
        self.v.set(1)
        self.values = {"All": 1,
                       "None": 2,
                       "Custom": 3,
                       }
        for index, btn in enumerate(self.values):
            b = tk.Radiobutton(self.frame,
                               text=btn,
                               value=index,
                               variable=self.v)
            b.pack(side=tk.LEFT)
        self.frame.grid(row=2, column=0,
                        sticky=tk.NSEW,
                        padx=SelectView.MARGIN_X,
                        pady=SelectView.MARGIN_Y)
