import os
import csv
from lxml import etree
import xml.etree.ElementTree as ET

# Validate XML files against schema
def validate_xml(schema_path, xml_files):
    with open(schema_path, 'r') as schema_file:
        schema_doc = etree.parse(schema_file)
        schema = etree.XMLSchema(schema_doc)

    for xml_file in xml_files:
        try:
            with open(xml_file, 'r') as file:
                xml_doc = etree.parse(file)
                schema.assertValid(xml_doc)
                print(f"{xml_file} is valid.")
        except (etree.XMLSchemaError, etree.XMLSyntaxError) as e:
            print(f"{xml_file} is not valid: {e}")

def parse_xml_to_csv(xml_file, csv_file, fields, root_tag, row_tag):
    """Parse XML and write data to a CSV file."""
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    # Open CSV file for writing
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(fields)  # Write header
        
        # Extract and write rows
        for row in root.findall(f".//{row_tag}"):
            writer.writerow([row.find(tag).text if row.find(tag) is not None else "" for tag in fields])

def main():
    schema_path = "C:/Users/Enric/Desktop/cw2/xml-csv/schema.xsd"
    xml_directory = "C:/Users/Enric/Desktop/cw2/task1"
    # -- schema_path and xml_directory must be changed to correctly alligned to your current directory
    xml_files = [os.path.join(xml_directory, f) for f in os.listdir(xml_directory) if f.endswith('.xml')]

    xml_configurations = [
    {
        "xml_file": "info.xml",
        "csv_file": "info.csv",
        "fields": ["symbol", "fullname", "industry"],  # Columns for CSV
        "root_tag": "companies",
        "row_tag": "company",
    },
    {
        "xml_file": "price.xml",
        "csv_file": "price.csv",
        "fields": ["date", "open", "high", "low", "close", "volume", "symbol"],  # Columns for CSV
        "root_tag": "price",
        "row_tag": "tick",
    },
    {
        "xml_file": "time.xml",
        "csv_file": "time.csv",
        "fields": ["date", "weeknum", "weekday"],  # Example fields
        "root_tag": "time",
        "row_tag": "row",
    }, ]
    
    # Validate XML files and Create the CSV copy
    validate_xml(schema_path, xml_files)
        # Process each XML configuration
    for config in xml_configurations:
        parse_xml_to_csv(
            xml_file=config["xml_file"],
            csv_file=config["csv_file"],
            fields=config["fields"],
            root_tag=config["root_tag"],
            row_tag=config["row_tag"],)

if __name__ == "__main__":
    main()
    print("done")