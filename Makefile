HUGO ?= hugo
PYTHON ?= python3
HUGO_VERSION := 0.159.2
LOCAL_BASE_URL ?= http://localhost:1313/log/
LOCAL_PORT ?= 1313

.PHONY: all generate generate-all check serve build clean test version

all: build

generate:
	$(PYTHON) scripts/split_diary.py

generate-all:
	$(PYTHON) scripts/split_diary.py --all

test:
	$(PYTHON) -m unittest discover -s tests -v

check: test
	$(PYTHON) scripts/split_diary.py --check
	$(HUGO) --panicOnWarning --cleanDestinationDir
	$(PYTHON) scripts/check_site.py public

serve: generate
	$(HUGO) server --baseURL $(LOCAL_BASE_URL) --port $(LOCAL_PORT) --appendPort=false --navigateToChanged

build: generate
	$(HUGO) --gc --minify --cleanDestinationDir

clean:
	$(RM) -r -- public resources/_gen
	$(RM) -- .hugo_build.lock

version:
	@echo "Expected Hugo: $(HUGO_VERSION)"
	@$(HUGO) version
	@$(PYTHON) --version
