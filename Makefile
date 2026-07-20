PANDOC_HTMLOPT := --mathjax -t html --template=template

MD := $(wildcard log/*.md)
HTML := $(patsubst log/%.md,docs/%.html,$(MD))

.PHONY: all clean

all: $(HTML)
	rm -rf docs/images
	cp -R log/images docs/images

docs/index_in.md: log/index.md
	sed -e 's/\.md)/.html)/g' $< > $@

docs/index.html: docs/index_in.md template.html
	pandoc -s $< -o $@ $(PANDOC_HTMLOPT) --metadata pagetitle='log'
	rm docs/index_in.md

docs/%.html: log/%.md template.html
	TITLE=$$(head -1 $< | sed -e '1 s/^# \(.*\)$$/\1/g'); pandoc -s $< -o $@ $(PANDOC_HTMLOPT) --metadata pagetitle="$$TITLE"

clean:
	rm -f $(HTML)
	rm -rf docs/images
