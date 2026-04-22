import matplotlib.pyplot as plt

my_dict = {"Thang 1": 45.5, "Thang 2": 112.0, "Thang 3": 89.5}
sum = 0
for month in my_dict.values():
    sum = sum + month

min_month = min(my_dict, key=my_dict.get)
print("Thang co luong mua it nhat la %s" % min_month)
print("Tong luong mua = %f" % sum)

x = list(my_dict.keys())
y = list(my_dict.values())

plt.plot(x, y)
plt.xlabel("Thang")
plt.ylabel("Luong mua")
plt.title("Luong mua trong quy 1")
plt.show()
