import tkinter as tk
import tkinter.ttk as ttk


class TreeView:
    """Representation of the files and folders in the system"""

    def __init__(self, root, controller):
        """Init tree view and set tree's columns"""
        self.controller = controller
        self.frame = tk.Frame(root, bg="lavender")
        # Initializing internal widget
        self.tree = ttk.Treeview(self.frame, height=26)
        self.tree["columns"] = ("#1", "#2", "#3", "#4", "#5")
        self.tree["show"] = "headings"
        self.exclusion_list = ["#2"]
        self.tree.column("#1", width=300, minwidth=170, stretch=tk.NO)
        self.tree.column("#2", width=300, minwidth=170, stretch=tk.NO)
        self.tree.column("#3", width=200, minwidth=120, stretch=tk.NO)
        self.tree.column("#4", width=150, minwidth=50)
        self.tree.column("#5", width=150, minwidth=50, stretch=tk.NO)
        self.tree.heading("#1", text="Name", anchor=tk.W,
                          command=lambda: self.controller.sort_tree_view(0))
        self.tree.heading("#2", text="Path", anchor=tk.W,
                          command=lambda: self.controller.sort_tree_view(3))
        self.tree.heading("#3", text="Date modified", anchor=tk.W,
                          command=lambda: self.controller.sort_tree_view(1))
        self.tree.heading("#4", text="Type", anchor=tk.W,
                          command=lambda: self.controller.sort_tree_view(2))
        self.tree.heading("#5", text="Size", anchor=tk.W,
                          command=lambda: self.controller.sort_tree_view(3))
        self.display_columns = []
        for col in self.tree["columns"]:
            if not "%s" % col in self.exclusion_list:
                self.display_columns.append(col)
        self.tree["displaycolumns"] = self.display_columns
        # Bind to functionality
        self.tree.bind("<Double-1>", self.controller.on_double_click)
        self.tree.bind("<<TreeviewSelect>>", self.controller.on_tree_select)
        # Locate current frame in right's side frame grid
        self.tree.pack()
