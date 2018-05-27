'''
Created on May 27, 2018

@author: hv
'''
import xml.dom.minidom
import nc_chuong1.danh_sach_nhan_vien 

def tao_danh_sach_don_vi(list_don_vi):
    DOMTree = xml.dom.minidom.parse("don_vi.xml")
    collection = DOMTree.documentElement
    don_vi_s = collection.getElementsByTagName("DON_VI")
    for item in don_vi_s:
        if item.hasAttribute("ID") and item.hasAttribute("Ten"):
            don_vi = nc_chuong1.danh_sach_nhan_vien.DonVi(item.getAttribute("ID"),item.getAttribute("Ten"))
            list_don_vi.append(don_vi)
    return list_don_vi

def tao_danh_sach_nhan_vien(list_nhan_vien):
    DOMTree = xml.dom.minidom.parse("nhan_vien.xml")
    collection = DOMTree.documentElement
    nhan_vien_s = collection.getElementsByTagName("NHAN_VIEN")
    for item in nhan_vien_s:
        if item.hasAttribute("ID") and item.hasAttribute("ID_DON_VI"):
            nhan_vien = nc_chuong1.danh_sach_nhan_vien.NhanVien(item.getAttribute("ID"),item.getAttribute("Ho_ten"),\
                                                                item.getAttribute("Gioi_tinh"),item.getAttribute("Ngay_sinh"),\
                                                                item.getAttribute("CMND"),item.getAttribute("Muc_luong"),\
                                                                item.getAttribute("Dia_chi"),item.getAttribute("ID_DON_VI"))
            list_nhan_vien.append(nhan_vien)
    return list_nhan_vien

def thong_ke_don_vi(iddv,list_nhan_vien):
    count = 0
    nam = 0
    nu = 0
    for item in list_nhan_vien:
        if (int(item.iddv) == iddv):
            print(item.idnv,'-',item.ho_ten,'-',item.cmnd)
            count += 1
            if item.gioi_tinh == 'true':
                nam += 1
            else:
                nu += 1
    print('Tổng nhân viên: ',count,' - Trong đó có ',nam,' nam và ',nu,' nữ')
        
def tim_nhan_vien(ten,list_nhan_vien):
    count = 0; 
    for nv in list_nhan_vien:
        if nv.ho_ten.lower().find(ten.lower()) != -1:
            count += 1       
            print(nv.idnv,'-',nv.ho_ten,'-',nv.cmnd)
    return count;
        
list_don_vi = []
list_nhan_vien = []
list_don_vi = tao_danh_sach_don_vi(list_don_vi)
list_nhan_vien = tao_danh_sach_nhan_vien(list_nhan_vien)

print('---Danh sách đơn vi---')
for item in list_don_vi:
    print(item.iddv,'-',item.ten)

iddv = int(input('Bạn muốn xem thống kê đơn vị nào (nhập số)? '))
print('---Kết quả thống kê---')
thong_ke_don_vi(iddv, list_nhan_vien)

ten = input('Nhập tên nhân viên cần tìm: ')
print('---Kết quả tìm kiếm---')
count = tim_nhan_vien(ten, list_nhan_vien)
if count == 0:
    print('Không tìm thấy nhân viên nào!')