from sys import argv

bad_lines = [
    "orcid",
    "linkedin",
    "GitHub",
    "Printable",
]


with open(argv[1], 'r') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    for key in bad_lines:
        if key in line:
            lines[i] = "% " + line


# for line in lines:
    # print(line)

with open(argv[1], 'w') as f:
    f.write("".join(lines))
