import json
import xml.etree.ElementTree as ET


def process_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        return [entry['valor'] for entry in data if entry['valor'] > 0]


def process_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    values = []
    for row in root.findall('row'):
        value = float(row.find('valor').text)
        if value > 0:
            values.append(value)
    return values


def calculate_metrics(values):
    menor = min(values)
    maior = max(values)
    media = sum(values) / len(values)
    acima_da_media = len([v for v in values if v > media])
    return menor, maior, media, acima_da_media


json_values = process_json('dados1.json')
json_metrics = calculate_metrics(json_values)
print(f"JSON - Menor: {json_metrics[0]}, Maior: {json_metrics[1]}, Média: {json_metrics[2]:.2f}, Dias acima da média: {json_metrics[3]}")

xml_values = process_xml('dados2.xml')
xml_metrics = calculate_metrics(xml_values)
print(f"XML - Menor: {xml_metrics[0]}, Maior: {xml_metrics[1]}, Média: {xml_metrics[2]:.2f}, Dias acima da média: {xml_metrics[3]}")
