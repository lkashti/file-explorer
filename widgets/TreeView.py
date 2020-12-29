import tkinter as tk
import tkinter.ttk as ttk


class TreeView:
    def __init__(self, root, controller):
        self.controller = controller
        self.frame = tk.Frame(root)
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
        self.tree.bind("<Double-1>", controller.on_double_click)
        self.tree.pack()

    # def selected(self):
    #     curItem = self.tree.focus()
    #     print(self.tree.item(curItem))
