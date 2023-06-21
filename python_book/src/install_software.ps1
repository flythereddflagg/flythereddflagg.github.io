Set-ExecutionPolicy RemoteSigned -scope CurrentUser
Invoke-Expression (New-Object System.Net.WebClient).DownloadString('https://get.scoop.sh')
scoop install git
scoop bucket add extras
scoop update
scoop install latex make pandoc python sumatrapdf typora
pip install pandoc-tablenos pandoc-fignos pandoc-eqnos pandoc-secnos pandoc-xnos
