start:
	python twitter_/start.py &

install-language-packs:
	polyglot download sentiment2.en embeddings2.en ner2.en
