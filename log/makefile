PANDOC_HTMLOPT=--mathjax -t html --template=template

MD=$(shell ls *.md)
HTML=$(MD:.md=.html)

all: $(HTML)

d202011.html: d202011.md template.html

index_in.md: index.md
	sed -e 's/\(^\*.*\)\(d*\)\.md/\1\2.html/g' $< > $@

index.html: index_in.md
	pandoc -s $< -o $@ $(PANDOC_HTMLOPT)
	rm index_in.md

%.html: %.md
	pandoc -s $< -o $@ $(PANDOC_HTMLOPT)

.PHONY: clean

clean:
	rm $(HTML)
