 # ![](assets/icons/folder-icon.png) File Explorer 

Made with python 3.6
## Prerequisites

Please make sure you have the following interpreter on your machine:\
Python 3.6 or above


## Usage
no external libraries were used yet, only builtins.
```bash
python main.py
```

## Features
#### Buttons:
    'Home' - Navigate to root folder from any path - Single Left-Click
    'Back' - Go to the previous folder in hierarchy, into parent folder of the current folder - Single Left-Click
    'Forward' - Go to next folder in hierarchy, into child folder of the current folder - Single Left-Click
    'Add' - Create a new folder in your current location
    'Copy' - Saves a name and a path of a file/folder that the user wants to copy as a source file - Single Left-Click
    'Paste' - Copy source file/folder into the desired new path - Single Left-Click
    'Move' - Copy source file/folder into the desired new path and remove the source file/folder from its original path;
	  	       Single Left-Click to copy the source path
		       Single Right-Click, in addition, to paste and remove from the origin
    'Delete' - Remove the source file/folder from its original path;
			 Single Left-Click will display a warning on the Info view
			 Double Left-Click, in addition, to remove from the origin
	
#### Fields:
    Path-field - Displays the current path and the user can write/insert a path manually 
	Search-field - Looking for the searched file/folder in the current folder recursively

    Options:
		'All' - Select all items in the tree view
		'Hidden' - Show/Hide hidden files/folders

    Favorites:
		'+' - Add the current folder to the favorites list
		'-' - Remove the selected folder on the list view to the favorites list
		A click on an element in list view will jump to the favorite folder

    Info:
		Displays warnings, errors, and user guidelines
		 
    Status Bar:
		Displays the number of items in the current folder and the selected item in the tree view



## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to test your code, otherwise provide tests.

## Authors
[Noam Mishaeli](https://www.linkedin.com/in/noam-mishaeli-94b143183/) 
&
[Lior Kashti](https://www.linkedin.com/in/lior-kashti/)