import tkinter as tk
import tkinter.ttk as ttk
'''
Tree view widget - Init tree view and set tree's columns 
'''
class TreeView:
    def __init__(self, root, controller):
        self.controller = controller
        self.frame = tk.Frame(root, bg="lavender")
        # Initializing internal widget
        self.tree = ttk.Treeview(self.frame, height=26)
        self.tree["columns"] = ("one", "two", "three", "four")
        self.tree["show"] = "headings"
        self.tree.column("one", width=310, minwidth=170, stretch=tk.NO)
        self.tree.column("two", width=200, minwidth=120, stretch=tk.NO)
        self.tree.column("three", width=150, minwidth=50)
        self.tree.column("four", width=150, minwidth=50, stretch=tk.NO)
        self.tree.heading("one", text="Name", anchor=tk.W)
        self.tree.heading("two", text="Date modified", anchor=tk.W)
        self.tree.heading("three", text="Type", anchor=tk.W)
        self.tree.heading("four", text="Size", anchor=tk.W)
        # Bind to functionality
        self.tree.bind("<Double-1>", self.controller.on_double_click)
        self.tree.bind("<<TreeviewSelect>>", self.controller.on_tree_select)
        # Locate current frame in right's side frame grid
        self.tree.pack()
