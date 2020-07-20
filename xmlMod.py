#!/usr/bin/python3
#-*- coding:utf-8 -*-

# Modulos para validar xml con xsd.
import xmlschema, lxml
# Modulos para tratar archivo xstl.
from lxml import etree
# Modulos para accesar a datos de archivo xml.
import xml.etree.ElementTree as ET

def countElements(xml):
    """ Cuenta los elementos que tiene la raiz de un archivo xml.

    Devueleve el total de elementos que se tienen a partir
    de un elemento raiz xml en forma:

                root
            -------------
            |           |
         element1    element2
                    ----------
                    |        | 
            subelement1  subelement2
            |
         ......
    Parámetros:
    xml -- ruta del archivo xml a tratar
    """
    # Se obtiene el archivo xml como objeto Parser.
    tree = ET.parse(xml)
    root = tree.getroot()# se obtiene la raiz del documento
    # Se accede a los nodos hijos del elemento raíz.
    childs = root.getchildren()
    return len(childs)

def mkhtml(xslt, xml, html_file):
    # -----------------------------------------------------
    # Crea un archivo html a partir de un xslt.
    # Parámetros:
    # xslt -- ruta del archivo xslt
    # xml -- ruta del archivo xml
    # html_file -- ruta del archiv htmla crear
    # -----------------------------------------------------
    # Tratamiento de archivo de tranformación usando un parse.
    xsl_doc = etree.parse(xslt)
    xsl_trans = etree.XSLT(xsl_doc)
    # Tratamiento de archivo xml usando el parse.
    xml_doc = etree.parse(xml)
    # Se genera la salida para el archivo HTML
    outputDoc = xsl_trans(xml_doc)
    # Se escribe el archivo HTML
    outputDoc.write(
       html_file,
        pretty_print = True
    )
def validateXML(xml,xsd):
    """valida un xml con su xsd

    Devuele falso o verdadero si el archivo xml cumple con
    lo establecido en su schema (archivo xsd).

    parámetros:
    xml -- ruta del archivo xml.
    xsd -- ruta del archivo xsd.
    """
    schema = xmlschema.XMLSchema(xsd)
    state = False
    if schema.is_valid(xml):
        state = True
    return state