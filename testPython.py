x = -3
print(abs(x)) # absolute value
print(round(3.7)) # round to nearest integer (3)
list_1 = [1, 2, 3, 4, 5]
print(max(list_1)) # 5 value max
print(min(list_1)) # 1 value min
print(sum(list_1)) # 15 value sum
print(len(list_1)) # 5 value length

list_2 = [True, True, False]
print(any(list_2)) # True if any value is true
print(all(list_2)) # True if all values are true

y = 10
print(type(y)) # int type
print(str(y))   # '10' string
print(float(y)) # 10.0 float

z = '10'
print(int(z)) # 10 int from string

print(tuple(list_1)) 



list_1 = [1, 6, 10, -2]
name = ["faniry", "elisa","Ando", "ndraina"]

dict_1 = {k:v for k,v in enumerate(name)}
print(dict_1)