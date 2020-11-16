from itertools import takewhile
import re

def build_tree(lines):
    is_tab = r"    ".__eq__
    lines = iter(lines)
    stack = []
    result = []
    for line in lines:
        if line == "#--------------------------------------------------":
            result.append(line+'\n')
            continue
        elif bool(re.match(r"(^echo)", line)):
            result.append(line+'\n')
            continue
        else:
            indent = len(list(takewhile(is_tab, line)))
            stack[indent:] = [line.lstrip()]
            result.append('configure '.join(stack)+'\n')
    return result

source = '''
#--------------------------------------------------
echo "System Time NTP Configuration"
#--------------------------------------------------
    system
        time
            ntp
                server 220.103.209.192 prefer
                server 220.103.209.193
            exit
        exit
    exit
#--------------------------------------------------
echo "OAM Tests Configuration"
#--------------------------------------------------
    test-oam
        twamp
            server
                prefix 172.20.51.248/30 create
                exit
                prefix 172.20.51.252/30 create
                exit
                prefix 172.20.52.252/30 create
                exit
                no shutdown
            exit
        exit
    exit
'''

a = "".join(build_tree(source.split('\n')))
print(a)

