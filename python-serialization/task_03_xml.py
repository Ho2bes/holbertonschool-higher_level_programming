#!/usr/bin/env python3
"""Serializing and Deserializing with XML"""

import xml.etree.ElementTree as ET
import task_03_xml as xml_serialize


def serialize_to_xml(dictionary, filename):
    """Serializes a Python dictionary to an XML file."""

    root = ET.Element("data")

    def build_tree(d, parent):
        for key, value in d.items():
            if isinstance(value, dict):
                child = ET.SubElement(parent, key)
                build_tree(value, child)
            else:
                child = ET.SubElement(parent, key)
                child.text = str(value)

    build_tree(dictionary, root)
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """Deserializes an XML file to a Python dictionary"""
    tree = ET.parse(filename)
    root = tree.getroot()

    def parse_tree(element):
        d = {}
        for child in element:
            if len(child):
                d[child.tag] = parse_tree(child)
            else:
                d[child.tag] = child.text
        return d

    return parse_tree(root)
