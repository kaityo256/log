PANDOC_HTMLOPT=--mathjax -t html --template=template

all: d202011.html index.html

d202011.html: d202011.md template.html

%.html: %.md
	pandoc -s $< -o $@ $(PANDOC_HTMLOPT)
