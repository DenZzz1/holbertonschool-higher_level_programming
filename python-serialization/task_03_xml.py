#!/usr/bin/env python3
"""
Module for XML serialization and deserialization
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to XML and save to file

    Args:
        dictionary: Python dictionary to serialize
        filename: name of the output XML file
    """
    # Create root element
    root = ET.Element('data')

    # Add dictionary items as child elements
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    # Create tree and write to file
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserialize XML file to Python dictionary

    Args:
        filename: name of the XML file to read

    Returns:
        Python dictionary with deserialized data
    """
    # Parse XML file
    tree = ET.parse(filename)
    root = tree.getroot()

    # Reconstruct dictionary
    dictionary = {}
    for child in root:
        dictionary[child.tag] = child.text

    return dictionary
