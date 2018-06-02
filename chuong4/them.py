'''
Created on Jun 2, 2018

@author: hv
'''
import sqlite3
cnn = sqlite3.connect(r"product.db")
cnn.execute("INSERT INTO PRODUCT (NAME,PRICE,AMOUNT) VALUES ('Nho Mỹ', 32000.0, 21)")
cnn.execute("INSERT INTO PRODUCT (NAME,PRICE,AMOUNT) VALUES ('Nho khô', 15000.0, 34)")
cnn.execute("INSERT INTO PRODUCT (NAME,PRICE,AMOUNT) VALUES ('Kotex', 20000.0, 15)")
cnn.execute("INSERT INTO PRODUCT (NAME,PRICE,AMOUNT) VALUES ('Kẹo', 65000.0, 6)")
cnn.commit()
cnn.close()