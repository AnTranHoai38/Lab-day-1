lst = []
num = 10
sum = 0
for i in range(num):
    i = float(input("Enter the score:"))
    lst.append(i)
    sum += i
lst.sort()
print(f"Highest score: {lst[num-1]}\nLowest score: {lst[0]}")
print("Average score:", sum / num)
print("The second largest score:", lst[num-2])
for i in lst:
    if (i > 100):
        print("A value over 100 has been entered!")
print("Average score after droping two lowest score:", (sum - lst[0]-lst[1])/(num -2))



