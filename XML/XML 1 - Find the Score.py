import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    # your code goes here
    s=len(node.attrib)
    for i in node:
        s+=get_attr_number(i)
    return s

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
