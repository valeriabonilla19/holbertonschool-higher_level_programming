#!/usr/bin/python3
"""
Module to serialize and deserialize a dictionary using XML.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a dictionary to an XML file.

    Args:
        dictionary (dict): Dictionary to serialize.
        filename (str): File to write the XML to.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        element = ET.SubElement(root, key)
        element.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserializes XML data from a file into a dictionary.

    Args:
        filename (str): XML file to read from.

    Returns:
        dict: Dictionary containing the deserialized data.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        return {child.tag: child.text for child in root}
    except (FileNotFoundError, ET.ParseError):
        return {}
