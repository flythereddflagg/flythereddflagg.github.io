#!/usr/bin/env python3
"""
File   : add_nav.py
Author : Mark Redd
Email  : redddogjr@gmail.com

Description:
Running this script removes old navigation marked by:

<!-- Navigation --> and <!-- End Navigation -->

and puts new navigation defined below in its place.
This does this to all the .md files in whatever directory it is in.
"""

import os


def add_nav(nav_root_dir):
    nav_files = []
    toc = []

    for root, dirs, files in os.walk(nav_root_dir):
        for file in files:
            if file.endswith(".md"):
                nav_files.append(file)
        break
        
    nav_files = sorted(nav_files)
    
    yml_nav = []
    for file in nav_files:
        if "README" in nav_files[i] or \
            "Table of Contents" in nav_files[i] or \
            "index" in nav_files[i]:
            continue
        file_words = file[:-3].split('-')
        yml_nav.append(f"    - {int(file_words[0])}."\
                    f" {' '.join(file_words[1:])}: './{file}'\n")
    
    for # continue here to add to yml
    
    for i in range(len(nav_files)):
        if "README" in nav_files[i] or \
            "Table of Contents" in nav_files[i] or \
            "index" in nav_files[i]:
            continue
        
        toc_element = f"1. [{nav_files[i][3:-3]}]"\
                f"(./{nav_files[i].replace(' ', '-')})"
        
        try:
            prev = f"[Previous: {nav_files[i-1][:-3]}]"\
                f"(./{nav_files[i-1].replace(' ', '-')})"
        except:
            prev = ""
            
        try:
                
            next = f"[Next: {nav_files[i+1][:-3]}]"\
                f"(./{nav_files[i+1].replace(' ', '-')})"
        except:
            next = ""
        
        toc.append(toc_element)
        
        front_add_text = f"""<!-- Navigation -->

---

{prev} | [Table of Contents](./00-Table-of-Contents.md) | {next}

---
<!-- End Navigation -->
"""

        back_add_text = f"""<!-- Navigation -->

---

{prev} | [Table of Contents](./00-Table-of-Contents.md) | {next}

---
<!-- End Navigation -->
"""

        with open(nav_root_dir+nav_files[i], 'r') as f:
            content = f.read()
        
        with open(nav_root_dir+nav_files[i], 'w') as f:
            f.write(front_add_text + content + back_add_text)
    
    with open(nav_root_dir+"00-Table-of-Contents.md", 'w') as f:
        f.write("# Table of Contents\n")
        f.write("\n".join(toc) + "\n")
        

def rm_nav(nav_root_dir):
    nav_files = []

    for root, dirs, files in os.walk(nav_root_dir):
        for file in files:
            if file.endswith(".md"):
                nav_files.append(file)

        break
    
    for i in range(len(nav_files)):
        with open(nav_root_dir+nav_files[i], 'r') as f:
            content = f.readlines()
        
        nav = False
        new_content = []
        for line in content:
            if "<!-- Navigation -->" in line:
                nav = True
                continue
            if "<!-- End Navigation -->" in line:
                nav = False
                continue
            
            if not nav:
                new_content.append(line)
            
        new_content = "".join(new_content)
        
                
        with open(nav_root_dir+nav_files[i], 'w') as f:
            f.write(new_content)

        
        
if __name__ == "__main__":
    rm_nav("./docs/")
    add_nav("./docs/")
