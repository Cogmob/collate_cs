import sys

printing = False
for line in sys.stdin:
    if 'Run Settings' in line:
        printing = False
    if printing:
        sys.stdout.write(line)
    if 'Test Files' in line:
        printing = True
