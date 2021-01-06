import tkinter as tk

class Log:
    PAD = 3
    MARGIN_X = 5
    MARGIN_Y = 10

    def __init__(self, root, controller):
        self.controller = controller
        self.frame = tk.Frame(root)
        self.label = tk.Label(self.frame, text="Log",
                              font="Arial 12 bold", anchor="w", padx=Log.MARGIN_X)
        self.log_text = tk.Label(self.frame, text="-- Will be show here --",
                              font="Arial 10 bold", anchor="w", padx=Log.MARGIN_X)
        self.label.pack(fill=tk.X)
        self.log_text.pack()
        self.frame.grid(row=7, column=0, sticky="nsew",
                        padx=Log.MARGIN_X)

