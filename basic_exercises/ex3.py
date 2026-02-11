temperatures = [15.5, 17.2, 14.8, 16.0, 18.3, 20.1, 19.5]

print("The temperatues in wednesday is:", temperatures[2])

max_temp = temperatures[0]
for temp in temperatures:
    if temp > max_temp:
        max_temp = temp
print("The maximun temperature is:", max_temp)

min_temp = temperatures[0]
for temp in temperatures:
    if temp < min_temp:
        min_temp = temp
print("The minimun temperature is:", min_temp)

average = round(sum(temperatures) / len(temperatures), 1)
print("The average is:", average)

count = 0
for t in temperatures:
    if t > 17:
        count += 1
print("The number of days above 17 is:", count)
print("The tempperatures from lowest to highest:", sorted(temperatures))