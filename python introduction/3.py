a = 1
b = 2
c = 3
print((a < b) and (b < c))  # True
print((a > b) and (b < c))  # False
print((a > b) or (b > c))   # True
print(not (a > b))          # True
print("" or [])

print(5 and 2)   # 5
print(3 and "")  # 返回空

# or的返回值
print(2 or 5)   # 2
print("返回值为：", "" and 3)   # 3

a = "是小怪兽"
b = "不，是奥特曼"

print(1 and a or b) # 是小怪兽
print(0 and a or b) # 不，是奥特曼

a = ""
b = "不，是奥特曼"

print(1 and a or b) # 不，是奥特曼
c = (1 and [a] or [b])
print(c[0]) # 返回空
print([a][0])

a = 0
if a:
  print("123")   # 如果是True（不为空，或者不为0），则会打印123
else:
  print("456")

main = 1
print(f"{main+1}")



a = "124xafaadfa"
b = 287381
try:
  print(x/y)
except:
  print("ok")

print("\thello\nword")



