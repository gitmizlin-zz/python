#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Example to show how command-line options can be handled by a script.
"""

import sys
import os
from datetime import datetime
import time
import getopt
import requests

#
# Add some stuff about this script
#
PROGRAM = os.path.basename(sys.argv[0])
AUTHOR = "Mi"
EMAIL = "miis15@student.bth.se"
VERSION = "1.0"
USAGE = """{program} - AUTHOR: {author} ({email}), version {version}


Usage:
  {program} [options] name

Options:
    -h, --help skall visa en hjälptext som beskriver ditt kommando och hur det används.
    -v, --version skall visa versionen av programmet.
    --verbose skall innebära att mer text skrivs ut, kanske bra för debugging?
    -s, --silent skall innebära att minimalt med utskrift sker, bra om man bara vill se svaret.
    -p, --ping skall hämna en webbsida.

  name                           Your name.
""".format(program=PROGRAM, author=AUTHOR, email=EMAIL, version=VERSION)
MSG_VERSION = "{program} version {version}.".format(program=PROGRAM, version=VERSION)
MSG_USAGE = "Use {program} --help to get usage.\n".format(program=PROGRAM)

#
# Global default settings affecting behaviour of script in several places
#
SILENT = False
VERBOSE = False
NAME = ""

EXIT_SUCCESS = 0
EXIT_USAGE = 1
EXIT_FAILED = 2

def exit(exitStatus):
    """
    exit Python
    """
    print("Satus code:", exitStatus)
    sys.exit(exitStatus)

def printUsage(exitStatus):
    """
    Print usage information about the script and exit.
    """
    print(USAGE)


def printVersion():
    """
    Print version information and exit.
    """
    print(MSG_VERSION)

def pingWebsite(url = "http://www.yahoo.co.jp/"):
    """
    Ping a website.
    """
    try:
        # Get current time
        rTime = time.ctime(time.time())

        # Request header from url
        print("Ready to send HTTP request to ", url, "\n(press return)", end='')
        input()
        req = requests.head(url)

        # Print result
        print("Request to ", url, " sent at ", rTime)
        print("Recieved status code: ", req.status_code)

        exit(EXIT_SUCCESS)

    except requests.ConnectionError:
        exit(EXIT_FAILED)


def parseOptions():
    """
    Merge default options with incoming options and arguments and return them as a dictionary.
    """
    global VERBOSE, SILENT

    # Switch through all options
    try:
        opts, args = getopt.getopt(sys.argv[1:], "p:hvs", ["ping", "help", "version", "silent", "verbose"])

        print(args)

        for i, arg in enumerate(args):
            if (arg == 'ping'):
                if (not args[i+1]):
                    print('you suck')
                else:
                    try:
                        pingWebsite(args[i+1])
                    except Exception as err:
                        print(err)

        for opt, arg in opts:
            print(arg)

            if opt in ("-h", "--help"):
                printUsage(EXIT_SUCCESS)

            elif opt in ("-v", "--version"):
                printVersion()

            elif opt in "--verbose":
                VERBOSE = True

            elif opt in ("-s", "--silent"):
                SILENT = True

            else:
                assert False, "Unhandled option"

        # if len(args) != 1:
        #     assert False, "Missing name"

        # The name passed as a required argument
        # global NAME
        # NAME = args[0]

    except Exception as err:
        print(err)
        print(MSG_USAGE)
        exit(EXIT_USAGE)

        # Prints the callstack, good for debugging, comment out for production
        #traceback.print_exception(Exception, err, None)

def main():
    """
    Main function to carry out the work.
    """
    startTime = datetime.now()

    try:
        parseOptions()

        timediff = datetime.now()-startTime

        if VERBOSE:
            sys.stderr.write("Script executed in {}.{} seconds\n".format(timediff.seconds, timediff.microseconds))

            print("Executed: ", time.strftime("%Y-%m-%d %H:%M"))

        if SILENT:
            exit(EXIT_SUCCESS)

        exit(EXIT_SUCCESS)

    except Exception as err:
        exit(EXIT_FAILED)


if __name__ == "__main__":
    main()
