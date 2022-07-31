# Nhập các thông số đầu vào:
print("Mời bạn nhập số thứ 1:")
soThu1=float(input())
print("Mời bạn nhập phép tính: (+ - * /):")
phepTinh=input()
print("Mời bạn nhập số thứ 2:")
soThu2=float(input())

ketQua=0

# Tạo các hàm:
def cong(soThu1, soThu2):
	return soThu1 + soThu2

def tru(soThu1, soThu2):
	return soThu1 - soThu2

def nhan(soThu1, soThu2):
	return soThu1 * soThu2

def chia(soThu1, soThu2):
	return soThu1 / soThu2

def mayTinh(soThu1,soThu2,phepTinh):
	if phepTinh == '+':
		return cong(soThu1, soThu2)
	if phepTinh == '-':
		return tru(soThu1, soThu2)
	if phepTinh == '*':
		return nhan(soThu1, soThu2)
	if phepTinh == '/':
		if soThu2==0 :
			return "Không hợp lệ" 
		return chia(soThu1, soThu2)
ketQua=mayTinh(soThu1,soThu2,phepTinh)
if ketQua=="Không hợp lệ":
	print("Không thể chia cho 0")
else:
	print("Kết quả:" +" "+ str(soThu1)+" "+ str(phepTinh)+" "+str(soThu2) + " "+"=" +" "+ str(ketQua))