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
        print("Press Ctrl-C to quit or q to quit")
        try:
            while True:
                # Get and print the mouse coordinates.
                x, y = pyautogui.position()
                position_str = f"X: {x}, Y: {y}"
                print(position_str, end="  \r", flush=True)

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

            return None
        
    def move(self, x: int, y: int, time: float) -> None:
        """
        Move the mouse pointer
        """

        # raise TypeError if x or y is not an integer
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        
        # raise TypeError if time is not a float
        if not isinstance(time, float):
            raise TypeError("time must be a float")
        
        # move the mouse pointer
        pyautogui.moveTo(x, y, duration = time)

        return None
    
    def click(self, position) -> None:
        """
        Click the mouse pointer
        """

        # click the mouse pointer
        pyautogui.click(button = position)

        return None
    
    def execute(self) -> None:
        """
        Execute the GUI tasks
        """

        # verify the tasks attribute is not None
        if self.tasks is None:
            raise ValueError("The tasks attribute cannot be None")
        
        # execute the tasks
        for task in self.tasks:
            if task["task"] == "move":
                self.move(task["position"]["x"], task["position"]["y"], task["time"])
            elif task["task"] == "click":
                self.click(task["position"])
            else:
                raise ValueError("Invalid task")

        return None




        