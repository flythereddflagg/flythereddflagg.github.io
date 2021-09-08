import subprocess as sp
import threading as th
import webbrowser


start_server = lambda: sp.call(['mkdocs', 'serve'])
start_browser = lambda: webbrowser.open_new_tab('http://localhost:8000')

th.Thread(None, start_server).start()
th.Thread(None, start_browser).start()
# start_browser()
