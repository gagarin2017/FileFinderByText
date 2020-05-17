import os
import argparse
# print("Usage: python hello.py --words apple banana")

# defined command line options
# this also generates --help and error handling
CLI = argparse.ArgumentParser()
CLI.add_argument(
    "--words",  # name on the CLI - drop the `--` for positional/required parameters
    help='Pass space separated list of words to be searched for in a single file. For examle, --words apple banana',
    required=True,
)

# parse the command line
args = CLI.parse_args()

# access CLI options
wordList = args.words
fileExt = ".txt"


def doesFileContainWords(theFile):
    wordsFound = set()
    fileLines = list()

    for line in theFile:
        fileLines.append(line)

    for word in wordList:
        for line in fileLines:
            if word in line:
                wordsFound.add(word)

    if (len(wordsFound) == len(wordList)):
        return True
    else:
        return False


def searchFiles():
    for dirpath, dirnames, files in os.walk("./"):
        for fileName in files:
            theFile = open(os.path.join(dirpath, fileName), "r")
            if theFile.name.endswith(fileExt):
                if doesFileContainWords(theFile):
                    print('File containing words \' %r \' [ %s ]' % (
                        wordList, os.path.abspath(theFile.name)))


if len(wordList) < 1:
    print('\nNo words passed as arguments\n')
else:
    searchFiles()
