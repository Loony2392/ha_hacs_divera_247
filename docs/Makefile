# Makefile for Sphinx documentation

# Pfade definieren
SPHINXBUILD   = sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build

.PHONY: help clean html

help:
	@echo "Bitte benutze 'make <target>', wobei <target> eines der folgenden ist:"
	@echo "  clean    zum Löschen der generierten Dokumentation"
	@echo "  html     zum Erstellen der HTML-Dokumentation"

clean:
	rm -rf $(BUILDDIR)/*

html:
	$(SPHINXBUILD) -b html $(SOURCEDIR) $(BUILDDIR)/html
	@echo
	@echo "Build fertig. Die HTML-Dateien befinden sich in $(BUILDDIR)/html."
