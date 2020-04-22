from xml.etree import ElementTree as ET

# создаем тег Coordinate
root = ET.Element('Coordinate')
for i in range(10):
    sub_element = ET.SubElement(root, 'value{}'.format(i))
    # присваивание атрибуту текст значение * 10
    sub_element.text = str(i * 10)

print(ET.dump(root)) # плохой способ лучше использовать: tree.write

# создание набора данных, которые будут добавлены в xml
data = [{'x': 10, 'y': 11, 'z': 12},
        {'x': 20, 'y': 21, 'z': 22}
        ]

root = ET.Element('Coordinates')

for item in data:
    record = ET.SubElement(root, 'Coordinate')
    for key, value in item.items():
        e = ET.SubElement(record, key)
        e.text = str(value)

tree = ET.ElementTree(root)
tree.write('xml_data/output.xml', encoding='utf-8')