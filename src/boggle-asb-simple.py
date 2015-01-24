#!/usr/bin/env python3

###############################################################################
# Purpose: Play the Akuna version of boggle.
# Author: Akhil S. Behl
# Dependencies: optparse, sys
# Created: Fri 23 Jan 2015 03:05:12 PM IST
###############################################################################

import optparse
from sys import stdout


def boardContainsWordP(board, word):
    board = list(board)
    for char in word:
        try:
            board.remove(char)
        except ValueError:
            return False
    return True


if __name__ == '__main__':

    argsParser = optparse.OptionParser()
    argsParser.add_option('-i', '--input', action="store", dest='inFile',
                          help="path to the input file")
    argsParser.add_option('-d', '--dictionary', action="store",
                          dest='dictFile', help="path to the dictionary file")
    argsParser.add_option('-o', '--output', action="store",
                          dest='outFile', help="path to the output file")
    options, remainder = argsParser.parse_args()

    try:
        inFile = options.inFile if options.inFile else remainder.pop(0)
        dictFile = options.dictFile if options.dictFile else remainder.pop(0)
    except IndexError:
        argsParser.print_help()
        argsParser.exit(status=1)

    try:
        outFile = options.outFile if options.outFile else remainder.pop(0)
    except IndexError:
        outFile = stdout

    with open(dictFile, 'r') as dictF, open(inFile, 'r') as inF:
        outF = open(outFile, 'w') if outFile is not stdout else stdout
        # Make sure to count the newline in string length as well.
        dictionary = set([word.strip().lower() for
                          word in dictF.readlines() if len(word) > 3])
        boards = [board.strip() for board in inF.readlines()]
        counter = [0] * len(boards)
        for word in dictionary:
            for i, board in enumerate(boards):
                counter[i] += boardContainsWordP(board, word)
        for board, count in zip(boards, counter):
            print("%s %d" % (board, count), file=outF)
        outF.close() if outF is not stdout else None
