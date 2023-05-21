# import dependencies
import sys
from auto_gui import auto


# define the main function
def main(argv: list) -> None:
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
            -c, --count: count the number of times the tasks need to be executed
        
        Example: python app.py -p tasks.json -c 10

    Returns
    -------
    None
    """

    # verify that an argument is passed to the program
    if len(argv) == 0:
        raise ValueError("An argument must be passed to the program, check the help message for more information -h, --help")
    
    # verify that the maximum number of arguments passed is two
    if len(argv) > 4:
        raise ValueError("A maximum of two arguments can be passed to the program, check the help message for more information -h, --help")
    
    # verify that the argument passed is valid
    if argv[0] not in ("-h", "--help", "-p", "--path", "-l", "--locate"):
        raise ValueError("Invalid argument passed to the program, check the help message for more information -h, --help")
    
    # verify that the arguments -l or --locate and -h or --help are not passed together
    if len(argv) > 1:    
        if argv[0] in ("-l", "--locate", "-h", "--help") and argv[1]:
            raise ValueError("There is no need to pass any value with -l or --locate or -h or --help, check the help message for more information -h, --help")
    
    # verify that the argument -p or --path is only passed with -c or --count and no more than one argument is passed with any other argument other than -p or --path
    if len(argv) > 2:
        if argv[0] not in ("-p", "--path"):
            raise ValueError("Cannot pass more than one argument other than with -p or --path, check the help message for more information -h, --help")
        
        if argv[0] in ("-p", "--path") and argv[2] not in ("-c", "--count"):
            raise ValueError("The argument -p or --path cannot be passed with other than -c or --count, check the help message for more information -h, --help")
        else:
            try:
                count = int(float(argv[3]))        # number of times the tasks need to be executed
            except:
                raise ValueError("The argument -c or --count must have an integer or float value, check the help message for more information -h, --help")
    else:
        count = 1
    
        
    
    # the help message
    if argv[0] in ("-h", "--help"):
        print("Usage: python app.py [options]")
        print("Options:")
        print("-h, --help: display help message")
        print("-p, --path: path to the json file containing the GUI tasks")
        print("-l, --locate: locate the mouse pointer")
        print("-c, --count: count the number of times the tasks need to be executed")
        print("Example: python app.py -p tasks.json -c 10\n\n")
        print("----------------------------------------")
        print("Note:")
        print("1) -c or --count must be passed with -p or --path only")
        print("2) -l or --locate cannot be passed with any other argument")
        print("3) -h or --help cannot be passed with any other argument")
        print("4) -c or --count if not passed, the tasks will be executed only once")
        print("5) The argument -c or --count cannot be passed first, it can only be passed after -p or --path", end="\n\n")


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
        i = 0
        while i < count:
            automate.execute()
            i += 1



if __name__ == "__main__":
    main(sys.argv[1:])