# import dependencies
import os
import sys
import json
import time
import pyautogui
import numpy as np


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

        

    def sleep(self, time: float) -> None:
        """
        Sleep for a given time
        """

        # raise TypeError if time is not a float
        if not isinstance(time, float):
            raise TypeError("time must be a float")

        # sleep for the given time
        time.sleep(time)

        

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
        pyautogui.moveTo(x, y, duration=time)

        

    def click(self, position) -> None:
        """
        Click the mouse pointer
        """

        # click the mouse pointer
        pyautogui.click(button=position)

        

    def read_csv(self, path: str) -> None:
        """
        Read a csv file
        """
        # verify the path is a string
        if not isinstance(path, str):
            raise TypeError("The path must be a string")

        # verify the path is a file
        if not os.path.isfile(path):
            raise TypeError("The path must be a file")

        # verify the path exists
        if not os.path.exists(path):
            raise FileNotFoundError("The path does not exist")

        # verify the path is for a csv file
        if not path.endswith(".csv"):
            raise TypeError("The path must be a csv file")

        # read the csv file
        try:
            with open(path, "r") as f:
                csv = f.read()

                # skip the first line
                header = csv.split("\n")[0]

                # number of columns
                self.n_cols = len(header.split(","))

                # number of rows
                self.n_rows = len(csv.split("\n")) - 1

                # store the csv in numpy array
                self.csv = np.array(csv.split("\n"))

        except Exception as e:
            raise e

        

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
            raise ValueError(
                "The os must be either mac or win. Other operating systems are not supported")

        

    def create_pdf(self, path: str) -> None:
        """
        Create pdf files from Word documents in a directory. Works only on Windows
        """

        # verify the path is a string
        if not isinstance(path, str):
            raise TypeError("The path must be a string")

        # verify the path is a directory
        if not os.path.isdir(path):
            raise TypeError("The path must be a directory")

        # check if the operating system is windows
        if sys.platform != "win32":
            raise Exception("This function works only on Windows")

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
                self.move(task["position"]["x"],
                          task["position"]["y"], task["time"])
            elif task["task"] == "click":
                self.click(task["position"])
            elif task["task"] == "navigate":
                self.navigate(task["path"], task["open"], task["os"])
            elif task["task"] == "sleep":
                self.sleep(task["time"])
            elif task["task"] == "read_csv":
                self.read_csv(task["path"])
            else:
                raise ValueError(
                    f"Invalid task {task['task']}, review sample_taks.json for how you constrcut the tasks")

        
