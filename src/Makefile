all: simple ordcount trie

simple:
	./boggle-simple.py \
	  -i ../data/input.txt \
	  -d ../data/word_dictionary \
	  -o ../data/output-simple.txt

ordcount:
	./boggle-ordered-counter.py \
	  -i ../data/input.txt \
	  -d ../data/word_dictionary \
	  -o ../data/output-ordered-counter.txt

trie:
	./boggle-trie.py \
	  -i ../data/input.txt \
	  -d ../data/word_dictionary \
	  -o ../data/output-trie.txt

clean: cleansimple cleanordcount cleantrie

cleansimple:
	rm -rf ../data/output-simple.txt

cleanordcount:
	rm -rf ../data/output-ordered-counter.txt

cleantrie:
	rm -rf ../data/output-trie.txt

time: timesimple timeordcount timetrie

timesimple:
	time make simple

timeordcount:
	time make ordcount

timetrie:
	time make trie
