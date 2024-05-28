#!/usr/bin/env python3
"""Serializing Deserializing with XML"""

import xml.etree.ElementTree as ET
import task_03_xml as xml_serialize


def serialize_to_xml(dictionary, filename):
    """Serializes Python dictionary to XML file."""

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
