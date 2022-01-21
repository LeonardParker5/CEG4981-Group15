# Relies on the printer propagation via CUPS
# The following program code is used in linux platform server for printing Hello World 
# This program code can be included in the wireless server
# The code demonstrates how the printing works using subprocesses 
import subprocess

lpr =  subprocess.Popen("/usr/bin/lpr", stdin=subprocess.PIPE)
lpr.stdin.write("Hello World")
lpr.stdin.close()
