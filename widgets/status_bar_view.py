import tkinter as tk
import tkinter.ttk as ttk


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
        self.items_label.pack(side=tk.LEFT,
                              padx=(StatusBarView.MARGIN_X * 68, StatusBarView.MARGIN_X))
        self.item_count_label.pack(side=tk.LEFT)
        self.selected_label.pack(side=tk.LEFT,
                                 padx=(StatusBarView.MARGIN_X * 20, StatusBarView.MARGIN_X))
        self.item_label.pack(side=tk.LEFT)
        # progressbar for search feature
        self.progress = tk.IntVar()
        self.progressbar = ttk.Progressbar(self.frame, length=200, orient=tk.HORIZONTAL,
                                           variable=self.progress, mode='determinate')

        # Locate current frame in main's window frame grid
        self.frame.grid(row=2, column=0, sticky="ew",
                        ipadx=StatusBarView.MARGIN_X, ipady=StatusBarView.MARGIN_Y)

    def show_progressbar(self):
        """ used to indicate a long computation"""
        from random import randint
        self.progressbar.pack(side=tk.RIGHT, padx=StatusBarView.MARGIN_X * 2)
        self.progress.set(randint(30, 70))
        self.controller.root.update_idletasks()

    def hide_progressbar(self):
        """ used to hide progressbar when a long computation is done"""
        from time import sleep
        self.progress.set(100)
        self.controller.root.update_idletasks()
        sleep(0.2)
        self.progressbar.stop()
        self.progressbar.pack_forget()
