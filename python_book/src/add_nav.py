import os

# define constants
FILE_PATH = os.path.dirname(os.path.abspath(__file__))
TO_DOCS = "/../docs"
TO_YML = "/../mkdocs.yml"
TOC_TXT = "00-Table-of-Contents"
IND_TXT = "index"
MD_EXT = ".md"
START_YML = "# start nav"
END_YML = "# end nav"
TO_TOC = TO_DOCS + '/' + TOC_TXT + '.md'
HTML_COMMENT_NAV = "<!-- Navigation -->"
HTML_COMMENT_NAVEND = "<!-- End Navigation -->"
HEAD_FOOT_TEMPLATE = """<!-- Navigation -->

---

{previous} | [Table of Contents](./00-Table-of-Contents.md) | {next_}

---
<!-- End Navigation -->
"""

def edit_section(
    psec, pfile, csec, cfile, nsec, nfile
):
    if not csec: return
    previous = f"[Previous: {psec}](./{pfile})" if psec else ""
    next_ = f"[Next: {nsec}](./{nfile})" if nsec else ""
    with open(FILE_PATH + TO_DOCS + "/" + cfile) as f:
        lines = f.readlines()
    
    outlines = []
    keepline = True
    for line in lines:
        if any([
            HTML_COMMENT_NAV in line,
            HTML_COMMENT_NAVEND in line
        ]): 
            keepline = not keepline
        if all([
            keepline,
            HTML_COMMENT_NAV not in line,
            HTML_COMMENT_NAVEND not in line
        ]):
            outlines.append(line)
    
    # head_foot = HEAD_FOOT_TEMPLATE.format(
        # previous=previous, 
        # next_=next_
    # )  
    head_foot = ""
    out_txt = head_foot + "".join(outlines) + head_foot
    with open(FILE_PATH + TO_DOCS + "/" + cfile, 'w') as f:
        f.write(out_txt)

print("collecting and sorting files...")
sec_file = []

# get list of files in docs that apply and sort
for root, dirs, files in os.walk(FILE_PATH+TO_DOCS):
    for file_ in files:
        if TOC_TXT in file_ or\
            IND_TXT in file_ or\
            not file_.endswith(MD_EXT): continue
        
        section_name = file_[:-3]
        section_name_lst = section_name.split('-')
        section_name = " - ".join(section_name_lst[:2]) + \
            " " + " ".join(section_name_lst[2:])
        sec_file.append([section_name, file_])
    break


sec_file = sorted(
    sec_file, 
    key=lambda x: x[0]
)

# make the list for mkdocs.yml
print("Updating YML navigation...")
nav_yml = []
for i in range(len(sec_file)):
    try:
        index_num = int(sec_file[i][0][:2])
        title = sec_file[i][0][5:]
    except ValueError:
        index_num = f"{sec_file[i][0][0]}{int(sec_file[i][0][1:3])}"
        title = sec_file[i][0][6:]
        
    line = f"    - {index_num}. {title}: './{sec_file[i][1]}'"
    nav_yml.append(line)

nav_yml_txt = "\n".join(nav_yml)

# edit/update the yaml file

with open(FILE_PATH+TO_YML) as f:
    lines = f.readlines()

for i in range(len(lines)):
    line = lines[i]
    if START_YML in line: startline = i
    if END_YML in line: endline = i

pre_text = "".join(lines[:startline+1])
post_text = "".join(lines[endline:])
yml_txt = pre_text + nav_yml_txt + '\n' + post_text

with open(FILE_PATH+TO_YML, "w") as f:
    f.write(yml_txt)

# update the TOC
print("updating TOC...")
toc_f_txt = "# Table of Contents\n"

for sec, file_ in sec_file:
    toc_f_txt += f"1. [{sec[5:]}](./{file_})\n"

with open(FILE_PATH+TO_TOC,"w") as f:
    f.write(toc_f_txt)

# update each file navigation
print("updating per file navigation...")
psec, pfile, csec, cfile, nsec, nfile = "", "", "", "", "", ""

for sec, file_ in sec_file:
    nsec, nfile = sec, file_
    print(f"editing {cfile} ...")
    edit_section(
        psec, pfile, csec, cfile, nsec, nfile
    )
    psec, pfile = csec, cfile
    csec, cfile = nsec, nfile

nsec, nfile = "", ""
print(f"editing {cfile} ...")
edit_section(psec, pfile, csec, cfile, nsec, nfile)

print("Navigation Update Complete.")
