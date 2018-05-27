'''
Created on May 27, 2018

@author: Thuong
'''
import xml.dom.minidom

def create_list_contacts(list_contact):
    DOMTree = xml.dom.minidom.parse("contact.xml")
    collection = DOMTree.documentElement
    contact_s = collection.getElementsByTagName("contact")
    for item in contact_s:
        if item.hasAttribute("phone") and item.hasAttribute("name"):
            contact = {"phone":item.getAttribute("phone"),"name":item.getAttribute("name")}
            list_contact.append(contact)
    return list_contact

list_contact = []
create_list_contacts(list_contact)
print('List of contacts:')
i=1
for item in list_contact:
    print('--- Contact ',i,' ---')
    print('Name: ',item["name"])
    print('Phone',item["phone"])
    i+=1