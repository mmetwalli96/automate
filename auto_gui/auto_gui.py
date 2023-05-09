# import dependencies
import json
import pyautogui

class auto():
    """
    Auto class is to automate GUI tasks
    
    Attributes
    ----------
    path: str
        path to the file where the json file containing the GUI tasks is located

    tasks: dict
        dictionary containing the GUI tasks

    Methods
    -------
    locate()
        locate the mouse pointer
    
    load()
        load the json file containing the GUI tasks
    """
    def __init__(self, path: str = None):
        """
        Constructor for auto class
        """

        # verify the the path is a string and a json file
        if path is not None:
            if not isinstance(path, str):
                raise TypeError("The path must be a string")
            if not path.endswith(".json"):
                raise TypeError("The path must be a json file")
            
        self.path = path

        return None
        
            
    def locate(self) -> None:
        """
        Locate the mouse pointer
        """

        # locate the mouse pointer
        print("Press Ctrl-C to quit")
        try:
            while True:
                # Get and print the mouse coordinates.
                x, y = pyautogui.position()
                position_str = "X: " + str(x).rjust(4) + " Y: " + str(y).rjust(4)
                print(position_str, end="")
                print("\b" * len(position_str), end="", flush=True)
        except KeyboardInterrupt:
            print("\nDone")
            return None

    def load(self) -> None:
        """
        Load the json file containing the GUI tasks
        """

        # verify the path is not None
        if self.path is None:
            raise ValueError("The path cannot be None")
        else:
            with open(self.path, "r") as f:
                tasks = json.load(f)

            # assign the tasks to the tasks attribute
            self.tasks = tasks
            print(self.tasks)
            return None

        