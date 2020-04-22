from xml.etree import ElementTree as ET

children = ET.parse('xml_data/menu.xml').getroot()

for menu in children:
    print('PK= ', menu.attrib)
    for child in menu:
        print('{}: {}'.format(child.tag, child.text))