import tkinter as tk


class FavoritesView:
    """
    Favorites widget - user can add and remove his favorite directories to a list
    """
    PAD = 3
    MARGIN_X = 5
    MARGIN_Y = 10

    def __init__(self, root, controller):
        self.controller = controller
        self.frame = tk.Frame(root, bg="lavender")
        # Initializing internal widgets - labels and buttons
        self.label = tk.Label(self.frame, text="Favorites",
                              font="Arial 12 bold", anchor="w",
                              padx=FavoritesView.MARGIN_X, bg="lavender")
        self.add_btn = tk.Button(self.frame, text="✚", font="Arial 9")
        self.rmv_btn = tk.Button(self.frame, text="▬", font="Arial 9")
        # Locate internal widgets in a grid
        self.label.grid(row=0, column=0,
                        padx=(FavoritesView.PAD, FavoritesView.PAD * 5))
        self.add_btn.grid(row=0, column=1,
                          padx=(FavoritesView.PAD, FavoritesView.PAD))
        self.rmv_btn.grid(row=0, column=2,
                          padx=(FavoritesView.PAD, FavoritesView.PAD))
        self.add_btn.bind("<Button-1>", self.controller.add_to_favorites)
        self.rmv_btn.bind("<Button-1>", self.controller.rmv_from_favorites)
        # Locate current frame in left's side frame grid
        self.frame.grid(row=4, column=0, sticky="nsew",
                        padx=FavoritesView.MARGIN_X,
                        pady=FavoritesView.MARGIN_Y)

    # Load saved favorites from a json file
    def load_favorites(self):
        favorites = self.controller.model.favorites.get()
        fav_listbox = self.controller.view.center_frame.favorites_lb_view.listbox
        for fav in favorites:
            fav_listbox.insert("end",
                               " ⭐ " + fav.get("name"))
