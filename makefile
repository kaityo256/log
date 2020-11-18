PANDOC_HTMLOPT=--mathjax -t html --template=template

MD=$(shell ls log/*.md | sed 's/log/docs/g')
HTML=$(MD:.md=.html)

all: $(HTML)

docs/index_in.md: log/index.md
	sed -e 's/\(^\*.*\)\(d*\)\.md/\1\2.html/g' $< > $@

docs/index.html: docs/index_in.md
	pandoc -s $< -o $@ $(PANDOC_HTMLOPT)
	rm docs/index_in.md

docs/%.html: log/%.md
	pandoc -s $< -o $@ $(PANDOC_HTMLOPT)

.PHONY: clean

clean:
	rm $(HTML)
