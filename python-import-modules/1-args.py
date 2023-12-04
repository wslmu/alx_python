import sys

if __name__ == "__main__":

    if len(sys.argv) == 1:
        print("0 arguments.")

    elif len(sys.argv) == 2:
        print("1 argument:")
        noofArg = -1
        for i in sys.argv:
            noofArg += 1
            if noofArg == 0:
                pass
            else:
                print("{}: {}".format(noofArg, i))
    
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
        noofArg = -1
        for i in sys.argv:
            noofArg += 1
            if noofArg == 0:
                pass
            else:
                print("{}: {}".format(noofArg, i))