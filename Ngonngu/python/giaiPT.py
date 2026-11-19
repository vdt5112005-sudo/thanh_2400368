a = float(input("Nhap a: "))
b = float(input("Nhap b: "))
if a == 0:
    print("Vo nghiem" if b != 0 else "Vo so nghiem")
else:
    print(f"Nghiem x = {-b / a}")
