
__author__ = "Bilal El Uneis"
__since__ = "August 2018"
__email__ = "bilaleluneis@gmail.com"


def logger(logger_type: str = "Default Logger:", message: str = " nothing to log!!"):
    print("{} -> {}".format(logger_type, message))


def main():
    logger()
    logger(message="something to log")  # notice the use of named parameter and able to switch order of param!
    logger(message="message parm came first!", logger_type="Message Logger")
    pass


# start of running code
if __name__ == "__main__":
    main()  # from now on, this is how I will do it, so that I can scope same named vars and not expose them outside!
