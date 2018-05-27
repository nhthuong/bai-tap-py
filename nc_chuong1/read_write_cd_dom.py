'''
Created on May 27, 2018

@author: hv
'''
import os.path
import xml.dom.minidom
from xml.dom.minidom import Document
from pydoc import doc

def make_xml(ten_file,cd):
    if os.path.isfile(ten_file):
        doc = xml.dom.minidom.parse(ten_file)
        root_xml = doc.documentElement
    else:
        doc = Document
        root_xml = doc.createElement("cds")
        doc.appendChild(root_xml)
    
    child_node = doc.createElement("cd")
    child_node.setAttribute('ten', cd.ten)
    root_xml.appendChild(child_node)
    
    ca_sy = doc.createElement('ca_sy')
    ca_sy.appendChild(doc.createTextNode(cd.ca_sy))
    child_node.appendChild(ca_sy)
    
    so_bai_hat = doc.createElement('so_bai_hat')
    so_bai_hat.appendChild(doc.createTextNode(cd.so_bai_hat))
    child_node.appendChild(so_bai_hat)
    
    gia_thanh = doc.createElement('gia_thanh')
    gia_thanh.appendChild(doc.createTextNode(cd.gia_thanh))
    child_node.appendChild(gia_thanh)
    
    return doc

def read_xml(ten_file):
    DOMTree = xml.dom.minidom.parse(ten_file)
    collection = DOMTree.documentElement
    cds = collection.getElementsByTagName("cd")
    for cd in cds:
        print('---CD---')
        if cd.hasAttribute("ten"):
            print('Tên CD: %s'%cd.getAttribute("ten"))
        ca_sy = cd.getElementsByTagName('ca_sy')[0]
        print('Ca sỹ: %s'%ca_sy.childNodes[0].data)
        so_bai_hat = cd.getElementsByTagName('so_bai_hat')[0]
        print('Format: %s'%so_bai_hat.childNodes[0].data)
        gia_thanh = cd.getElementsByTagName('gia_thanh')[0]
        print('Rating: %s'%gia_thanh.childNodes[0].data)
    return

