import tkinter as tk


class FavoritesView:
    PAD = 3
    MARGIN_X = 5
    MARGIN_Y = 10

    def __init__(self, root, controller):
        self.controller = controller

        self.frame = tk.Frame(root)
        self.frame.grid(row=0, column=0, sticky="nsew",
                        padx=FavoritesView.MARGIN_X,
                        pady=FavoritesView.MARGIN_Y)

        self.label = tk.Label(self.frame, text="Favorites",
                              font="Arial 15 bold")
        self.label.pack(fill=tk.X)

        self.scrollbar = tk.Scrollbar(self.frame, orient=tk.VERTICAL)
        self.listbox = tk.Listbox(self.frame, width=40,
                                  yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)

        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
        self.listbox.pack(fill=tk.BOTH)
