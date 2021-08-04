CC = pdflatex
SRC_MD = ./docs/index.md
SRC_TEX = ./build_pdf/Mark_Redd_Resume_Printable
SRC = ./build_pdf/main

ifeq ($(OS), Windows_NT)
	RM = del
	MV = move
	CLEAN_META = clean-meta-win
	CLEAN = clean-win
	MOVE_PDF = move_pdf_win
else
	RM = rm -f
	MV = mv
	CLEAN_META = clean-meta-unix
	CLEAN = clean-unix
	MOVE_PDF = move_pdf_unix
endif

all: build_site md edit_tex to_pdf clean-meta move_pdf
	
md:
	pandoc -r markdown $(SRC_MD) -o $(SRC_TEX).tex

edit_tex:
	python ./build_pdf/comment_lines.py $(SRC_TEX).tex

to_pdf:
	$(CC) -jobname=$(SRC_TEX) $(SRC).tex
	$(CC) -jobname=$(SRC_TEX) $(SRC).tex
    
build_site:
	mkdocs build
    
    
move_pdf_win:
	$(MV) .\build_pdf\Mark_Redd_Resume_Printable.pdf ..\media

move_pdf_unix:
	$(MV) ./build_pdf/Mark_Redd_Resume_Printable.pdf ../media

move_pdf: $(MOVE_PDF)


clean-meta-win:
	$(RM) .\build_pdf\*.aux
	$(RM) .\build_pdf\*.log

clean-meta-unix:
	$(RM) ./build_pdf/*.aux
	$(RM) ./build_pdf/*.log

clean-meta: $(CLEAN_META)


clean-win:
	$(RM) ..\media\Mark_Redd_Resume_Printable.pdf

clean-unix:
	$(RM) ../media/Mark_Redd_Resume_Printable.pdf

clean: clean-meta $(CLEAN)
