import sys

printing = False
for line in sys.stdin:
    if 'Run Settings' in line:
        printing = False
    if printing:
        if 'Microsoft (R)' in line:
            continue
        if 'Copyright (C)' in line:
            continue
        sys.stdout.write(line)
    if 'Test Files' in line:
        printing = True
