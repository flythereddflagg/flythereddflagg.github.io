"""
file: make_html.py
author: Mark Redd
about:
    Converts select markdown files in the current folder to lahtml files in an
    already-existing folder called 'html'. Does not search sub folders.
"""
import subprocess
import os

begin_html = """<!doctype html>
<html>
<head>
<meta charset='UTF-8'><meta name='viewport' content='width=device-width initial-scale=1'>
<link rel="stylesheet" href="style.css">
</head>
<body class='typora-export os-windows' >
<div  id='write'  class = 'is-node'>
"""

end_html = """
</body>
</html>
"""

for root, dirs, files in os.walk('.'):
    for filename in files:
        if filename.endswith(".md"):
            html_name = f"{root}/html/{filename[:-3]}.html"
            print(f'generating: {html_name}...')
            subprocess.call([
                'pandoc', 
                '-f',
                'markdown_mmd',
                '-t',
                'html',
                '--mathjax',
                filename,
                '-o',
                html_name])
            
            print(f"Making minor edits to {html_name}...")
            with open(html_name, 'r') as f:
                lines = f.readlines()
            
            for i, line in enumerate(lines):
                if ".md" in line:
                    newline = line.replace(
                        ".md",
                        ".html")
                    
                    lines[i] = newline
            
            filestring = ''.join(lines)
            filestring = begin_html + filestring + end_html
            
            with open(html_name, 'w') as f:
                f.write(filestring)
    break
    
#input("press ENTER to end...")