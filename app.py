# import dependencies
import sys
from auto_gui import auto


# define the main function
def main(argv) -> None:
    """
    Main program function

    Parameters
    ----------
    argv: list
        command line arguments passed to the program
        options:
            -h, --help: display help message
            -p, --path: path to the json file containing the GUI tasks
            -l, --locate: locate the mouse pointer

    Returns
    -------
    None
    """

    # verify the argument is valid
    if len(argv) == 0:
        raise ValueError("An argument must be passed to the program, check the help message for more information -h, --help")
    if len(argv) > 2:
        raise ValueError("Only one argument can be passed to the program, check the help message for more information -h, --help")
    if argv[0] not in ("-h", "--help", "-p", "--path", "-l", "--locate"):
        raise ValueError("Invalid argument passed to the program, check the help message for more information -h, --help")
    
    # the help message
    if argv[0] in ("-h", "--help"):
        print("Usage: python app.py [options]")
        print("Options:")
        print("-h, --help: display help message")
        print("-p, --path: path to the json file containing the GUI tasks")
        print("-l, --locate: locate the mouse pointer")
        return None
    
    # locate the mouse pointer
    if argv[0] in ("-l", "--locate"):
        automate = auto()
        automate.locate()
        return None
    
    # load the json file
    if argv[0] in ("-p", "--path"):

        # send error message if no path is provided
        if len(argv) == 1:
            raise ValueError("A path must be provided to the program, check the help message for more information -h, --help")
        
        # define the path to the json file containing the GUI tasks
        path = argv[1]

        # convert \ into / if exists
        if "\\" in path:
            path = path.replace("\\", "/")

        # call the auto class
        automate = auto(path)

        # load the json file
        automate.load()

        # execute the GUI tasks
        automate.execute()



if __name__ == "__main__":
    main(sys.argv[1:])