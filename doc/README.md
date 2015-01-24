# Boggle

This codebase implements two different solvers for the problem of searching for all words in a given dictionary that can be made on a given boggle board. The problem statement, however, is different from traditional boggle and closer to scrabble since the adjacent move restriction is not required.

The two solutions are discussed here briefly:

## Linear search

This process implements a linear search in the dictionary given a board to find all matches until the dictionary is exhausted. Uses a simple predicate function to find if a given word is possible on the board. The time complexity is linear in the size of the dictionary.

There are two different scripts which implement this method - `simple` and `ordered-counter`. The simple script uses two parallel lists to hold the boards and their corresponding word counts (we ignore the actual words). The `ordered counter' uses an example in the collections module to implement an ordered counter class. The ordered counter, unexpectedly, turns out to be significantly slower than the simple method.

## Recusrive search in a trie

This process uses a _re_trie_val_ tree to store the dictionary first. The trie is implemented as a very simple recursive data structure using Python's efficient `dict` data type. The words themselves are stored as sentinel values at the terminal leafs to allow easy retrieval later. The cost of creating the tree (a few seconds with our dictionary) will be amortized over searching a large number of boards.

Given a board then, a recursive search method is employed where the searcher fans out into the appropriate sub-tries and bubbles up the matches found from its search space bottom up. This way the whole dictionary is searched in one fell swoop. Since tries are very broad but not very deep, the recursive search prunes the search space and bubbles up quickly making searching the dictionary much more efficient than a linear search.

## Profiling

Rudimentary profiling is implemented.

The recursive search uses less than 5 seconds to finish 100 boards where the simple version of linear search takes ~92 seconds. On the other hand, the peak memory usage of the recursive search method is ~250MB as compared to 41MB for the simple linear search for a dictionary of ~235K words.
