import tkinter as tk


class NavBar:
    """
    Top bar widget - navigation buttons, path and search fields
    """
    PAD = 3
    MARGIN_X = 5
    MARGIN_Y = 10

    def __init__(self, root, controller, width):
        self.controller = controller
        self.navbar_frame = tk.Frame(root, bg="lavender")
        self.navbar_frame.grid_rowconfigure(1, weight=1)
        self.navbar_frame.grid_columnconfigure(0, weight=1)
        self.navbar_frame.grid(row=0, column=0, sticky="ew",
                               ipady=NavBar.MARGIN_Y, ipadx=NavBar.PAD)
        # Initializing buttons
        self.home_btn = tk.Button(self.navbar_frame, text="Home", font="Arial 9 bold")
        self.home_btn.pack(side=tk.LEFT, padx=NavBar.MARGIN_X)
        self.back_btn = tk.Button(self.navbar_frame, text="Back", font="Arial 9 bold")
        self.back_btn.pack(side=tk.LEFT, padx=NavBar.MARGIN_X)
        self.forward_btn = tk.Button(self.navbar_frame, text="Forward", font="Arial 9 bold")
        self.forward_btn.pack(side=tk.LEFT, padx=NavBar.MARGIN_X)
        # Initializing text fields
        self.path_field = tk.Entry(self.navbar_frame, width=int(0.1 * width))
        self.path = tk.StringVar()
        self.path_field.configure(textvariable=self.path)
        self.path_field.pack(side=tk.LEFT, ipady=NavBar.PAD)
        self.search_field = tk.Entry(self.navbar_frame,
                                     width=int(0.04 * width))
        self.search_text = tk.StringVar()
        self.search_field.configure(textvariable=self.search_text)
        self.search_field.pack(side=tk.LEFT, ipady=NavBar.PAD,
                               padx=NavBar.MARGIN_X)
        self.search_field.insert(0, "Search...")
        # Bind to functionality
        self.search_field.bind("<FocusIn>",
                               self.controller.handle_focus_in_search_bar)

        self.search_field.bind("<FocusOut>",
                               lambda e: self.search_text.set("Search..."))
        self.home_btn.bind("<ButtonRelease>", self.controller.handle_home_event)
        self.back_btn.bind("<ButtonRelease>", self.controller.handle_back_event)
        self.forward_btn.bind("<ButtonRelease>",
                              self.controller.handle_forward_event)
        self.path_field.bind('<Return>', self.controller.handle_enter_path)
        self.search_field.bind('<Return>', self.controller.handle_search_path)