import sys

printing = True
has_errored = False
for line in sys.stdin:
    if 'Runtime Environment' in line:
        printing = False
    if 'Run Settings' in line:
        printing = False
    if printing:
        if 'Microsoft (R)' in line:
            continue
        if 'Copyright (C)' in line:
            continue
        if line.strip() == '':
            sys.stdout.write(line)
            continue
        sys.stdout.write(line)
        has_errored = True
    if 'Errors, Failures and Warnings' in line:
        printing = True

if has_errored:
    sys.exit(1)
