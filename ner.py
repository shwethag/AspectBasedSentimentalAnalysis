import nltk
import sys
def extract_entities(text):
	for sent in nltk.sent_tokenize(text):
		for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
			if hasattr(chunk, 'node'):
				print chunk.node, ' '.join(c[0] for c in chunk.leaves())


def main(argv):
	f=open(argv[0], 'r')
	text=""
	for line in f:
		text=text+line

	extract_entities(text)

if __name__ == "__main__":
    main(sys.argv[1:])