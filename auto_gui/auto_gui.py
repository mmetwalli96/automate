# import dependencies
import os
import json
import time
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
    
    def sleep(self, time: float) -> None:
        """
        Sleep for a given time
        """

        # raise TypeError if time is not a float
        if not isinstance(time, float):
            raise TypeError("time must be a float")
        
        # sleep for the given time
        time.sleep(time)

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
        
    def move(self, x: int, y: int, time: float ) -> None:
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
    
    def navigate(self, path: str, open: bool, operating_system: str) -> None:
        """
        Navigate to a path
        """
        # verify the path is a string
        if not isinstance(path, str):
            raise TypeError("The path must be a string")
        
        # verify the open is a boolean
        if not isinstance(open, bool):
            raise TypeError("The open must be a boolean")
        
        # verify the os is a string
        if not isinstance(operating_system, str): 
            raise TypeError("The os must be a string")
        
        # navigate to the path
        if operating_system == "mac":
            if open:
                try:
                    cmd = f"open {path}"
                    os.system(cmd)
                except Exception as e:
                    raise e
            else:
                try:
                    cmd = f"cd {path}"
                    os.system(cmd)
                except Exception as e:
                    raise e
                
        elif operating_system == "win":
            if open:
                try:
                    cmd = f"explorer {path}"
                    os.system(cmd)
                except Exception as e:
                    raise e
            else:
                try:
                    cmd = f"cd {path}"
                    os.system(cmd)
                except Exception as e:
                    raise e
        else:
            raise ValueError("The os must be either mac or win. Other operating systems are not supported")

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
            elif task["task"] == "navigate":
                self.navigate(task["path"], task["open"], task["os"])
            elif task["task"] == "sleep":
                self.sleep(task["time"])
            else:
                raise ValueError(f"Invalid task {task['task']}, review sample_taks.json for how you constrcut the tasks")

        return None




        