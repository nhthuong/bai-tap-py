'''
Created on May 26, 2018

@author: thuong
'''
import json
import urllib.request

def read_json_from_internet_unicode(url1):
    DEFAULT_ENCODING = 'utf-8'
    urlResponse = urllib.request.urlopen(url1)
    
    encoding = DEFAULT_ENCODING
    noi_dung = json.loads(urlResponse.read().decode(encoding))
    return noi_dung

def doc_noi_dung_json(filename):
    data_file = open(filename, encoding = "utf-8")
    data = json.load(data_file)
    data_file.close()
    return data