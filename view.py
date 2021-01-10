import tkinter as tk

from widgets.center_frame_view import CenterFrame
from widgets.navbar_frame import NavBar
from widgets.status_bar_view import StatusBarView


class View:
    """Main window, holds the root element of tkinter"""

    def __init__(self, root: tk.Tk, controller):
        self.controller = controller
        root.title("File Explorer")
        # Set size to app's window
        self.width = 1092
        self.height = 614
        self.horizon_offset = 100
        self.vertical_offset = 50
        root.geometry(
            "{}x{}+{}+{}".format(self.width, self.height,
                                 self.horizon_offset, self.vertical_offset))
        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)
        root.wm_attributes("-topmost", 1)
        root.resizable(0, 0)
        # Initialize three main frames into root frame
        self.navbar = NavBar(root, controller, self.width)
        self.center_frame = CenterFrame(root, controller)
        self.status_bar = StatusBarView(root, controller)
