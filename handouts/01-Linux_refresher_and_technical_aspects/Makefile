all:  Technical_aspects.pdf
Technical_aspects.pdf : Technical_aspects.md
	pandoc --indented-code-classes=bash --number-sections -V monofont:"Fira Mono" -V fontsize=12pt -V geometry:margin=1in -V mainfont="Minion Pro" --latex-engine=xelatex --toc -o Technical_aspects.pdf Technical_aspects.md
