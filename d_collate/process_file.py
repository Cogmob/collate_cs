import add_close_braces
import add_semicolon
import process_line
import join_lines

def _(src):
    raw_lines = src.split("\n")
    indent = 0

    lines = [[0,'','-']]
    for line in raw_lines:
        line = line.split('    ')
        if (len(line) == 1 and line[0] == ''):
            add_semicolon._(lines)
            lines.append([indent, line, '-'])
            continue
        indent = process_line._(lines, line, indent)
    add_semicolon._(lines)
    add_close_braces._(lines, indent, 0)
    lines = lines[1:-1]

    return join_lines._(lines)
