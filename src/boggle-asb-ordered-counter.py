#!/usr/bin/env python3

###############################################################################
# Purpose: Play the Akuna version of boggle.
# Author: Akhil S. Behl
# Dependencies: optparse, collections, sys
# Created: Fri 23 Jan 2015 03:05:12 PM IST
###############################################################################

import optparse
from collections import Counter, OrderedDict
from sys import stdout


class OrderedCounter(Counter, OrderedDict):

    '''https://docs.python.org/3/library/collections.html#ordereddict-examples-and-recipes'''

    def writeOut(self, to):
        for key, count in self.items():
            print("%s %d" % (key, count), file=to)


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
        counter = OrderedCounter()
        for word in dictionary:
            for board in boards:
                counter[board] += boardContainsWordP(board, word)
        counter.writeOut(to=outF)
        outF.close() if outF is not stdout else None
