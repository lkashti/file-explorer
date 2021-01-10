import json
import os


class FavoritesHandler:
    def __init__(self):
        pass

    # self.favorites = []

    # init empty favorites file
    if not os.path.exists("favorites.json"):
        with open("favorites.json", "w") as fp:
            fav = {
                "favorites": [
                ]
            }

            json.dump(fav, fp)

    def get(self):
        with open("favorites.json") as fp:
            return json.load(fp).get("favorites")

    def store(self, path):
        dir_name = os.path.basename(path)
        new_favorite = {
            "name": dir_name,
            "path": path
        }

        with open("favorites.json") as fp:
            data = json.load(fp)

        # append favorite obj to file, open a new file if it does not exist
        with open("favorites.json", "w") as fp:
            favorites = data.get("favorites", None)
            if new_favorite not in favorites:
                data.get("favorites", None).append(new_favorite)
            json.dump(data, fp)

    def remove(self, path):
        with open("favorites.json") as fp:
            data = json.load(fp)
        with open("favorites.json", "w") as fp:
            favorites: list = data.get("favorites")
            if len(favorites) > 0:
                for item in favorites:
                    if item.get("path") == path:
                        data.get("favorites", None).remove(item)
            json.dump(data, fp)
