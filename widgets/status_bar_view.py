import tkinter as tk


class StatusBarView:
    PADX = 4
    PADY = 5

    def __init__(self, root, controller):
        self.controller = controller
        self.frame = tk.Frame(root)
        self.frame.grid(row=2, column=0, sticky="ew",
                        ipadx=StatusBarView.PADX, ipady=StatusBarView.PADY)

        self.selected_label = tk.Label(self.frame, text="Selected item:")
        self.item_label = tk.Label(self.frame, text="None")
        self.item_count = ""
        self.item_count_label = tk.Label(self.frame,
                                         textvariable=self.item_count)
        self.items_label = tk.Label(self.frame, text="Items:")
        self.items_label.pack(side=tk.LEFT, padx=(StatusBarView.PADX*68, StatusBarView.PADX))
        self.item_count_label.pack(side=tk.LEFT)
        self.selected_label.pack(side=tk.LEFT, padx=(StatusBarView.PADX*20, StatusBarView.PADX))
        self.item_label.pack(side=tk.LEFT)

