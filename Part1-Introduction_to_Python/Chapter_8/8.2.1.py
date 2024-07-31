res = ((1 <= 1) and (1 != 1))
print(res)

res = not (1 != 2)
print(res)

res = ("good" != "bad") or False
print(res)

res = ("good" != "Good") and not (1 == 1)
print(res)
