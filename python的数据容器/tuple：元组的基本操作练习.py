aihao = [ "sing", "jump" , "rap", "basketball"]
xinxi = ("ikun", 22 , aihao)
print(xinxi.index(22))

print("--------------------------------------")

print(xinxi[0])

print("--------------------------------------")

del xinxi[2][-1]
print(xinxi)

print("----------------------------------------")

xinxi[2].append("coding")
print(xinxi)