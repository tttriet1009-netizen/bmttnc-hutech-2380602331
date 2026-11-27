from SinhVien import SinhVien


class QuanLySinhVien:
    def __init__(self):
        self.listSinhVien = []
        self._nextId = 1

    def generateID(self):
        newId = self._nextId
        self._nextId += 1
        return newId

    def soLuongSinhVien(self):
        return len(self.listSinhVien)

    def nhapSinhVien(self):
        svId = self.generateID()
        name = input("Nhập tên sinh viên: ")
        sex = input("Nhập giới tính sinh viên: ")
        major = input("Nhập chuyên ngành của sinh viên: ")
        diemTB = float(input("Nhập điểm của sinh viên: "))
        sv = SinhVien(svId, name, sex, major, diemTB)
        self.xepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)

    def updateSinhVien(self, ID):
        sv = self.findByID(ID)
        if sv is not None:
            sv._name = input("Nhập tên sinh viên: ")
            sv._sex = input("Nhập giới tính sinh viên: ")
            sv._major = input("Nhập chuyên ngành của sinh viên: ")
            sv._diemTB = float(input("Nhập điểm của sinh viên: "))
            self.xepLoaiHocLuc(sv)
        else:
            print(f"Sinh viên có ID = {ID} không tồn tại.")

    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda x: x._diemTB, reverse=False)

    def sortByMajor(self):
        self.listSinhVien.sort(key=lambda x: x._major.upper(), reverse=False)

    def findByID(self, ID):
        for sv in self.listSinhVien:
            if sv._id == ID:
                return sv
        return None

    def findByName(self, keyword):
        return [sv for sv in self.listSinhVien if keyword.upper() in sv._name.upper()]

    def deleteById(self, ID):
        sv = self.findByID(ID)
        if sv is not None:
            self.listSinhVien.remove(sv)
            return True
        return False

    def xepLoaiHocLuc(self, sv):
        if sv._diemTB >= 8:
            sv._hocLuc = "Giỏi"
        elif sv._diemTB >= 6.5:
            sv._hocLuc = "Khá"
        elif sv._diemTB >= 5:
            sv._hocLuc = "Trung bình"
        else:
            sv._hocLuc = "Yếu"

    def showSinhVien(self, listSV):
        print(f"{'ID':<6}{'Tên':<20}{'Giới tính':<12}{'Chuyên ngành':<18}{'Điểm TB':<10}{'Học lực':<12}")
        for sv in listSV:
            print(f"{sv._id:<6}{sv._name:<20}{sv._sex:<12}{sv._major:<18}{sv._diemTB:<10}{sv._hocLuc:<12}")
        print()

    def getListSinhVien(self):
        return self.listSinhVien
