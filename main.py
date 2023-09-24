start = int(input("Введіть початкове число діапазону: "))

end = int(input("Введіть кінцеве число діапазону: "))

sum_even = 0

count_even = 0

sum_odd = 0

count_odd = 0

for num in range(start, end + 1):

    if num % 2 == 0:

        sum_even += num

        count_even += 1

    else:

        sum_odd += num

        count_odd += 1
average_even = sum_even / count_even if count_even > 0 else 0

average_odd = sum_odd / count_odd if count_odd > 0 else 0

print("Сума парних чисел:", sum_even)

print("Середнє арифметичне парних чисел:", average_even)

print("Сума непарних чисел:", sum_odd)

print("Середнє арифметичне непарних чисел:", average_odd)



