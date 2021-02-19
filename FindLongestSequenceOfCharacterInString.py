s = input()
result = 0
hold = 0
for i in s:
    if i != "0":
        if hold > result:
            result = hold
        hold = 0
    else:
        hold += 1

if hold > result:
    result = hold
print(result)
