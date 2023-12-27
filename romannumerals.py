def romanToInt():
    mydict = {"I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
        }
    s = input()
    s = s.replace("\"", "")
    sum = 0

    for i in range(len(s)-1):
        if mydict.get(s[i]) < mydict.get(s[i+1]):
            sum -= mydict.get(s[i])
        else:
            sum += (mydict.get(s[i]))
    sum += (mydict.get(s[-1]))
    return sum

print(romanToInt())