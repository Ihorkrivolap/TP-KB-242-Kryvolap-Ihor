
nums = [1, 2, 3, 4, 5, 6]

a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))
c = int(input("Введіть третє число: "))

for num in [a, b, c]:
    inserted = False
    for i in range(len(nums)):
        if nums[i] >= num:
            nums.insert(i, num)
            inserted = True
            break
    if not inserted:
        nums.append(num)

print("Оновлений список:", nums)