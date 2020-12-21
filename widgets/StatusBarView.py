import tkinter as tk


class StatusBarView:
    PAD = 40
    MARGIN_X = 5
    MARGIN_Y = 10

    def __init__(self, root, controller, height, width):
        self.controller = controller
        self.frame = tk.Frame(root, bd=1,
                              relief=tk.SUNKEN)
        self.frame.grid(row=2, column=0, sticky="nsew",
                        padx=StatusBarView.MARGIN_X,
                        pady=StatusBarView.MARGIN_Y)

        self.status_bar_label = tk.Label(self.frame, text="Status Bar",bg="green")

        self.status_bar_label.grid(row=0,column=0,sticky=tk.W,padx=StatusBarView.PAD)

        self.status_bar_label = tk.Label(self.frame, text="Folder Name")
        self.status_bar_label.grid(row=0,column=1,padx=StatusBarView.PAD)

        self.status_bar_label = tk.Label(self.frame, text="Items")
        self.status_bar_label.grid(row=0,column=2,sticky=tk.E)
