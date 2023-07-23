# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

some_list = [1, 3, 3, 5, 6, 7, 4, 3, 2, 1, 7, 'A', 'A']
new_list = []

for item in some_list:
    if some_list.count(item) >= 2 and item not in new_list:
        new_list.append(item)

print(new_list)
