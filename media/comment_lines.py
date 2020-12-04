from sys import argv

bad_lines = [
    "orcid",
    "linkedin",
    "github",
    "printable",
]


with open(argv[1], 'r') as f:
    lines = f.readlines()

for i in range(len(lines)):
    for key in bad_lines:
        if key in lines[i].lower():
            lines[i] = "% " + lines[i]


for line in lines:
    print(line)

with open(argv[1], 'w') as f:
    f.write("".join(lines))
