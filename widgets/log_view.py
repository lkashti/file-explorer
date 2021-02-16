import tkinter as tk


class Log:
    """
    Log widget - display warnings, errors and guidelines to the user
    """
    PAD = 3
    MARGIN_X = 5
    MARGIN_Y = 10

    def __init__(self, root, controller):
        self.controller = controller
        self.frame = tk.Frame(root, bg="lavender")
        # Initializing internal widgets - labels
        self.label = tk.Label(self.frame, text="Info",
                              font="Arial 12 bold", anchor="w", padx=Log.MARGIN_X, bg="lavender")
        self.log_text = tk.Label(self.frame, text="-- Will be shown here --",
                                 font="Arial 10 bold", anchor="w", padx=Log.MARGIN_X, bg="lavender")
        self.label.pack(fill=tk.X)
        self.log_text.pack()
        # Locate current frame in left's side frame grid
        self.frame.grid(row=7, column=0, sticky="nsew",
                        padx=Log.MARGIN_X)
