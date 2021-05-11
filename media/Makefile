CC = pdflatex
SRC_MD = ../resume/docs/index.md
SRC_TEX = ./Mark_Redd_Resume_Printable
SRC = main

ifeq ($(OS), Windows_NT)
	RM = del
else
	RM = rm -f
endif

all: md edit_tex to_pdf clean-meta
	
md:
	pandoc -r markdown $(SRC_MD) -o $(SRC_TEX).tex

edit_tex:
	python comment_lines.py $(SRC_TEX).tex

to_pdf:
	$(CC) -jobname=$(SRC_TEX) $(SRC).tex
	$(CC) -jobname=$(SRC_TEX) $(SRC).tex
	
clean-meta:
	$(RM) *.aux
	$(RM) *.log


clean: clean-meta
	$(RM) *.pdf
