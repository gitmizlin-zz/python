#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
from datetime import datetime
import getopt
import pdb
import requests

#
# Add some stuff about this script
#
PROGRAM = os.path.basename(sys.argv[0])
AUTHOR = "Mi"
EMAIL = "miis15@student.bth.se"
VERSION = "1.0"
USAGE = """{program} - AUTHOER: {author} ({email}), version {version}

Usage:
  {program} [options] name

Options:
    -h, --help skriver ut en beskrivning av kommandot och vilka parameterar som fungerar.
    -i, --info skriver ut en beskrivning av spelet och spelets idé.
    -v, --version skriver ut versionen av spelet.
    -a, --about skriver ut en kort beskrivning av dig själv, du som gjort spelet.
    -c, --cheat skriver ut minsta möjliga väg för att klara spelet och berättar hur du kan fuska dig fram.
""".format(program=PROGRAM, author=AUTHOR, email=EMAIL, version=VERSION)

MSG_VERSION = "{program} version {version}.".format(program=PROGRAM, version=VERSION)
MSG_USAGE = "Use {program} --help to get usage.\n".format(program=PROGRAM)

#
# Global default settings affecting behaviour of script in several places
#
SILENT = False
VERBOSE = True
NAME = ""

EXIT_SUCCESS = 0
EXIT_USAGE = 1
EXIT_FAILED = 2

def printUsage(exitStatus):
    """
    Print usage information about the script and exit.
    """
    print(USAGE)
    sys.exit(exitStatus)

def printVersion():
    """
    Print version information and exit.
    """
    print(MSG_VERSION)
    sys.exit(EXIT_SUCCESS)

def printMi():
    """
    Print info about Mi.
    """
    print("Det är jag som gjort detta spel och jag heter Mi.")

# def cheat():


def parseOptions():
    """
    Merge default options with incoming options and arguments and return them as a dictionary.
    """

    # Switch through all options
    try:
        global VERBOSE

        opts, args = getopt.getopt(sys.argv[1:], "d:hr:svp:", ["ping", "help", "version", "silent", "verbose"])

        for opt, arg in opts:
            if opt in ("-h", "--help"):
                printUsage(EXIT_SUCCESS)

            elif opt in ("-p", "--ping", "ping"):
                pingWebsite()

            elif opt in ("-v", "--version"):
                printVersion()

            elif opt in ("--verbose"):
                VERBOSE = True

            elif opt in ("-s", "--silent"):
                VERBOSE = False

            else:
                assert False, "Unhandled option"

        if len(args) != 1:
            assert False, "Missing name"

        print(args)

        # The name passed as a required argument
        global NAME
        NAME = args[0]

    except Exception as err:
        print(err)
        print(MSG_USAGE)
        # Prints the callstack, good for debugging, comment out for production
        #traceback.print_exception(Exception, err, None)
        sys.exit(EXIT_USAGE)


def main():
    """
    Main function to carry out the work.
    """
    startTime = datetime.now()

    parseOptions()

    timediff = datetime.now()-startTime
    if VERBOSE:
        sys.stderr.write("Script executed in {}.{} seconds\n".format(timediff.seconds, timediff.microseconds))

    sys.exit(EXIT_SUCCESS)



if __name__ == "__main__":
    main()

