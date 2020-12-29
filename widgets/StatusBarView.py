import tkinter as tk


class StatusBarView:
    PADX = 4
    PADY = 5

    def __init__(self, root, controller):
        self.controller = controller
        self.frame = tk.Frame(root,bg="lavender")
        self.frame.grid(row=2, column=0, sticky="ew",
                        padx=StatusBarView.PADX,ipady=StatusBarView.PADY)

        self.bottom_bar_label1 = tk.Label(self.frame, text="Status Bar")
        self.bottom_bar_label2 = tk.Label(self.frame, text="Folder Name:")
        self.bottom_bar_label3 = tk.Label(self.frame, text="Items:")
        self.folder_name_label = tk.Label(self.frame, text="My_Shits")
        self.items_label = tk.Label(self.frame, text="12")

        # layout the widgets in the btm frame
        self.bottom_bar_label1.pack(side=tk.LEFT, padx=StatusBarView.PADX)
        self.bottom_bar_label2.pack(side=tk.LEFT, padx=(
            StatusBarView.PADX * 57, StatusBarView.PADX))
        self.folder_name_label.pack(side=tk.LEFT, padx=StatusBarView.PADX)
        self.bottom_bar_label3.pack(side=tk.LEFT, padx=(
            StatusBarView.PADX * 25, StatusBarView.PADX))
        self.items_label.pack(side=tk.LEFT, padx=StatusBarView.PADX)
