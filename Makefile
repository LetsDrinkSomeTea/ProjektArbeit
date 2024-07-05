all: pdf

pdf: lua bib glossary
	@echo "Generating PDF..."
	make lua
	make bib
	make glossary
	lualatex Ausarbeitung.tex
	lualatex Ausarbeitung.tex

lua:
	@echo "Running Lua..."
	lualatex Ausarbeitung.tex

glossary: Quellen/glossary.tex
	@echo "Generating glossary..."
	xindy -I xindy -M "Ausarbeitung" -t "Ausarbeitung.glg" -o "Ausarbeitung.gls" "Ausarbeitung.glo"

bib: Quellen/Literatur.bib
	@echo "Generating bibliography..."
	biber Ausarbeitung

clean:
	@echo "Cleaning up..."
	rm -f *.aux *.bbl *.bcf *.blg *.glg *.glo *.gls *.ist *.lof *.log *.lot *.out *.run.xml *.toc *.xdy *.synctex.gz *.fdb_latexmk *.fls *.pdf
