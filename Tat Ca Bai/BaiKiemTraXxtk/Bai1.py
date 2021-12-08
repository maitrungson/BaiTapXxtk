A = [1,1,2,6,8,9,4,5,6,45,34,66,44,37,78]
B = []
print("cac so nho hon 30 la: ")
for x in A:
	if x < 30:
		print(x)
		B.append(x)
print(B)
n = input("nh?p n:")
n = int(n)
print("cac so lon hon n la:")
for x in A:
	if x > n:
		print(x)
