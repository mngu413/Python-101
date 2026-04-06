import math

end_num = 0
num = int(input('Enter a number (0 to quit): '))
num_list = []
while num != end_num:
    num_list.append(num)
    num = int(input('Enter a number (0 to quit): '))

#count
count = len(num_list)

#sum
summ = 0
for guess in num_list:
    summ += float(guess)
    
#average
avg = summ/count

#max & min
mini = float(min(num_list))
maxi = float(max(num_list))

sd = []
for guess in num_list:
    total = float(guess) - avg
    new_total = total ** 2
    sd.append(float(new_total))

val = 0
for num in sd:
    val += float(num)
    
third_step = val/count

standard_deviation = math.sqrt(third_step)

print(f'count               :     {count:.2f}')
print(f'sum                 :    {summ:.2f}')
print(f'average             :     {avg:.2f}')
print(f'min                 :     {mini:.2f}')
print(f'max                 :     {maxi:.2f}')
print(f'standard deviation  :     {standard_deviation:.2f}')
