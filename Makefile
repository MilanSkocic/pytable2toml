
.PHONY: doc docs

doc: 
	make -C doc latexpdf
	make -C doc html

docs:
	cp -rf ./doc/build/html/* ./docs/
