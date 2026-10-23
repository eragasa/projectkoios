SHELL := /bin/sh

SOURCE := Ragasa2026_pk_a.tex
JOB := Ragasa2026_pk_a
BUILD_DIR := .build
BUILD_PDF := $(BUILD_DIR)/$(JOB).pdf
PDF := $(JOB).pdf
SOURCE_DATE_EPOCH ?= 1792674722

LATEXMK := latexmk
LATEX_FLAGS := -pdf -bibtex -interaction=nonstopmode -halt-on-error \
	-file-line-error -outdir=$(BUILD_DIR)

SOURCES := $(SOURCE) references.bib \
	figures/audit-first-workflow.tex \
	figures/evidence-authority-separation.tex

.PHONY: all clean rebuild

all: $(PDF)

$(PDF): $(SOURCES) | $(BUILD_DIR)
	TZ=UTC SOURCE_DATE_EPOCH=$(SOURCE_DATE_EPOCH) FORCE_SOURCE_DATE=1 \
		$(LATEXMK) $(LATEX_FLAGS) $(SOURCE)
	cp $(BUILD_PDF) $(PDF)

$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)

rebuild: clean all

clean:
	rm -rf $(BUILD_DIR) $(PDF)
