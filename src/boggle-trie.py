#!/usr/bin/env python3

###############################################################################
# Purpose: Play the Akuna version of boggle.
# Author: Akhil S. Behl
# Dependencies: optparse, sys
# Created: Fri 23 Jan 2015 03:05:12 PM IST
###############################################################################

import optparse
from sys import stdout


def makeTrieFromDictionary(dictionary, sentKey='', sentVal=None):
    '''sentVal = None implies use the original word as the sentinel value so
    that we can easily retrieve them later.'''
    trie = {}
    for word in dictionary:
        subTrie = trie
        for char in word:
            subTrie = subTrie.setdefault(char, {})
        subTrie[sentKey] = word if sentVal is None else sentVal
    return trie


def findWordsOnBoard(board, dictTrie, sentKey=''):
    '''The collection of the words from terminal nodes relies on the word
    itself being used as the sentinel value when constructing the trie.
    However, the counting will always be correct.'''
    words, count = [], 0
    if sentKey in dictTrie:
        words.append(dictTrie[sentKey])
        count += 1
    if board:
        for char in set(board):
            if char in dictTrie:
                subTrie = dictTrie[char]
                subBoard = board.replace(char, '', 1)
                _, __ = findWordsOnBoard(subBoard, subTrie)
                words += _
                count += __
    return words, count


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
        dictTrie = makeTrieFromDictionary(dictionary)
        boards = [board.strip() for board in inF.readlines()]
        for board in boards:
            _, count = findWordsOnBoard(board, dictTrie)
            print("%s %d" % (board, count), file=outF)
        outF.close() if outF is not stdout else None
