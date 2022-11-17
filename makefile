PANDOC_HTMLOPT=--mathjax -t html --template=template 

MD=$(shell ls log/*.md | sed 's/log/docs/g')
HTML=$(MD:.md=.html)

all: $(HTML)
	cp -r log/images docs

docs/index_in.md: log/index.md
	sed -e 's/\(^\*.*\)\(d*\)\.md/\1\2.html/g' $< > $@

docs/index.html: docs/index_in.md
	pandoc -s $< -o $@ $(PANDOC_HTMLOPT) --metadata pagetitle='log'
	rm docs/index_in.md

docs/%.html: log/%.md
	TITLE=$(shell head -1 $< | sed -e '1 s/^# \(.*\)$$/\1/g'); pandoc -s $< -o $@ $(PANDOC_HTMLOPT) --metadata pagetitle=$$TITLE

.PHONY: clean

hoge:
	TITLE=$(shell head -1 log/d202211.md | sed -e '1 s/^# \(.*\)$$/\1/g'); echo $$TITLE

clean:
	rm $(HTML)
	rm -rf docs/images
