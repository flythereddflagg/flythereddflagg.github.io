CC = pdflatex
SRC_MD = ./docs/index.md
SRC_TEX = ./build_pdf/Mark_Redd_Resume_Printable
SRC = ./build_pdf/main


# ifeq ($(OS),Windows_NT)
    # CCFLAGS += -D WIN32
    # ifeq ($(PROCESSOR_ARCHITEW6432),AMD64)
        # CCFLAGS += -D AMD64
    # else
        # ifeq ($(PROCESSOR_ARCHITECTURE),AMD64)
            # CCFLAGS += -D AMD64
        # endif
        # ifeq ($(PROCESSOR_ARCHITECTURE),x86)
            # CCFLAGS += -D IA32
        # endif
    # endif
# else
    # UNAME_S := $(shell uname -s)
    # ifeq ($(UNAME_S),Linux)
        # CCFLAGS += -D LINUX
    # endif
    # ifeq ($(UNAME_S),Darwin)
        # CCFLAGS += -D OSX
    # endif
    # UNAME_P := $(shell uname -p)
    # ifeq ($(UNAME_P),x86_64)
        # CCFLAGS += -D AMD64
    # endif
    # ifneq ($(filter %86,$(UNAME_P)),)
        # CCFLAGS += -D IA32
    # endif
    # ifneq ($(filter arm%,$(UNAME_P)),)
        # CCFLAGS += -D ARM
    # endif
# endif

RM = rm -f
MV = mv
CLEAN_META = clean-meta-unix
CLEAN = clean-unix
MOVE_PDF = move_pdf_unix


all: build_site md edit_tex to_pdf move_pdf clean-meta

pdf: md edit_tex to_pdf move_pdf clean-meta
	
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
	$(MV) ./build_pdf/Mark_Redd_Resume_Printable.pdf ../media

move_pdf_unix:
	mv ./build_pdf/Mark_Redd_Resume_Printable.pdf ../media

move_pdf: $(MOVE_PDF)


clean-meta-win:
	$(RM) ./build_pdf/*.aux
	$(RM) ./build_pdf/*.log

clean-meta-unix:
	$(RM) ./build_pdf/*.aux
	$(RM) ./build_pdf/*.log

clean-meta: $(CLEAN_META)


clean-win:
	$(RM) ../media/Mark_Redd_Resume_Printable.pdf

clean-unix:
	$(RM) ../media/Mark_Redd_Resume_Printable.pdf

clean: clean-meta $(CLEAN)
