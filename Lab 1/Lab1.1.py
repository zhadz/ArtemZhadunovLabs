numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
sum_of_numbers = sum(number for number in numbers if number is not None)
total_count = len(numbers)
average = sum_of_numbers / total_count
index_of_none = numbers.index(None)
numbers[index_of_none] = average
print("Измененный список:", numbers)
