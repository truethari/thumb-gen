def deco():
        print("""
  _______ _                     _            _____
 |__   __| |                   | |          / ____|           
    | |  | |__  _   _ _ __ ___ | |__ ______| |  __  ___ _ __
    | |  | '_ \| | | | '_ ` _ \| '_ |______| | |_ |/ _ | '_ \ 
    | |  | | | | |_| | | | | | | |_) |     | |__| |  __| | | |
    |_|  |_| |_|\__,_|_| |_| |_|_.__/       \_____|\___|_| |_|

""")

def args_error(argument_list = False):
        if argument_list == False:
                print("Usage: thumb-gen [options] path/file\n\nerror: You must provide at least one option.")
        else:
                print("ERROR: unknown command {}".format(argument_list))

def helps():
        print ("""
    -v, --version       show program's version number and exit
    -h, --help          show this help message and exit

Options:
    -f, --file          input a single video from current directory
    -w, --where         input a single video from another directory
    -d, --dir           input videos from a directory
    """)
