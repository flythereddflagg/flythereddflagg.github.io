CC = mkdocs

MOVE = cp README.md ./docs/index.md

build:
	$(MOVE)
	$(CC) build



