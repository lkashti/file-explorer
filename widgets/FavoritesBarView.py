import tkinter as tk


class FavoritesView:
    PAD = 3
    MARGIN_X = 5
    MARGIN_Y = 10

    def __init__(self, root, controller):
        self.controller = controller
        self.frame = tk.Frame(root)
        self.frame.grid(row=4, column=0, sticky="nsew",
                        padx=FavoritesView.MARGIN_X,
                        pady=FavoritesView.MARGIN_Y)
        self.label = tk.Label(self.frame, text="Favorites",
                              font="Arial 12 bold", anchor="w", padx=FavoritesView.MARGIN_X)
        self.label.grid(row=0, column=0, padx=(FavoritesView.PAD, FavoritesView.PAD * 5))
        self.add_btn = tk.Button(self.frame, text="✚", font="Arial 9")
        self.add_btn.bind("<Button-1>", controller.add_to_favorites)
        self.add_btn.grid(row=0, column=1, padx=(FavoritesView.PAD, FavoritesView.PAD))
        self.rmv_btn = tk.Button(self.frame, text="▬", font="Arial 9")
        self.rmv_btn.bind("<Button-1>", controller.add_to_favorites)
        self.rmv_btn.grid(row=0, column=2, padx=(FavoritesView.PAD, FavoritesView.PAD))
