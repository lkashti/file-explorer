import tkinter as tk


class StatusBarView:
    MARGIN_X = 4
    MARGIN_Y = 5
    '''
    Status bar widget - display number of items and current selected item
    '''
    def __init__(self, root, controller):
        self.controller = controller
        self.frame = tk.Frame(root, bg="lavender")
        # Initializing internal widgets - labels and parameters
        self.item_count = ""
        self.selected_label = tk.Label(self.frame, text="Selected item:", bg="lavender")
        self.item_label = tk.Label(self.frame, text="None", bg="lavender")
        self.item_count_label = tk.Label(self.frame,
                                         textvariable=self.item_count, bg="lavender")
        self.items_label = tk.Label(self.frame, text="Items:", bg="lavender")
        self.items_label.pack(side=tk.LEFT, padx=(StatusBarView.MARGIN_X * 68, StatusBarView.MARGIN_X))
        self.item_count_label.pack(side=tk.LEFT)
        self.selected_label.pack(side=tk.LEFT, padx=(StatusBarView.MARGIN_X * 20, StatusBarView.MARGIN_X))
        self.item_label.pack(side=tk.LEFT)
        # Locate current frame in main's window frame grid
        self.frame.grid(row=2, column=0, sticky="ew",
                        ipadx=StatusBarView.MARGIN_X, ipady=StatusBarView.MARGIN_Y)

