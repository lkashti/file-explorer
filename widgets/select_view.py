import tkinter as tk


class SelectView:
    """
    Select items widget - checkboxes use to select all or none items and show/hide hidden items  
    """
    PAD = 3
    MARGIN_X = 5
    MARGIN_Y = 10

    def __init__(self, root, controller):
        self.controller = controller
        self.frame = tk.Frame(root, bg="lavender")
        # Initializing parameters
        self.select_label = tk.Label(self.frame, text="Select Items",
                                     font="Arial 12 bold", anchor="w", padx=SelectView.MARGIN_X,
                                     bg="lavender")
        self.select_label.pack(fill=tk.X)
        self.all_var = tk.IntVar()
        self.hidden_var = tk.IntVar()
        self.hidden_flag = False
        # Initializing internal widgets - checkboxes
        self.all_checkbox = tk.Checkbutton(self.frame, text="All", font="Arial 10",
                                           variable=self.all_var, bg="lavender")
        self.hidden_checkbox = tk.Checkbutton(self.frame, text="Show Hidden", font="Arial 10",
                                              variable=self.hidden_var, bg="lavender")
        self.all_checkbox.pack(side=tk.LEFT, padx=(10, 4))
        self.hidden_checkbox.pack(side=tk.LEFT, padx=(4, 4))
        # Bind to functionality
        self.all_checkbox.bind("<Button-1>", self.controller.select_all)
        self.hidden_checkbox.bind("<Button-1>", self.controller.show_hidden)
        # Locate current frame in left's side frame grid
        self.frame.grid(row=0, column=0,
                        sticky=tk.NSEW,
                        padx=SelectView.MARGIN_X,
                        pady=SelectView.MARGIN_Y)
