import tkinter as tk


class StatusBarView:
    PADX = 4
    PADY = 5

    def __init__(self, root, controller):
        self.controller = controller
        self.frame = tk.Frame(root)
        self.frame.grid(row=2, column=0, sticky="ew",
                        ipadx=StatusBarView.PADX, ipady=StatusBarView.PADY)

        self.item_count: tk.IntVar = tk.IntVar()
        self.load_item_count(controller.model.get_home_path())
        self.item_count_label = tk.Label(self.frame,
                                         textvariable=self.item_count)
        self.items_label = tk.Label(self.frame, text="items")

        # self.selected_item_count = tk.IntVar()
        # self.selected_items_count_label = tk.Label(
        #     self.frame,
        #     textvariable=self.selected_item_count
        # )
        # self.selected_items_label = tk.Label(self.frame, text="items selected")
        # layout the widgets in the btm frame
        self.item_count_label.pack(side=tk.LEFT, padx=(StatusBarView.PADX, 0))
        self.items_label.pack(side=tk.LEFT, padx=(0, StatusBarView.PADX))

        # self.selected_items_count_label.pack(side=tk.LEFT,
        #                                      padx=StatusBarView.PADX)
        # self.selected_items_label.pack(side=tk.LEFT, padx=StatusBarView.PADX)

    def load_item_count(self, path):
        self.item_count.set(
            self.controller.model.get_folder_file_count(path)
        )
