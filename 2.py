quantity_el = int(input("Enter quantity elements in array: "))
my_array = list(map(int, input("Enter numbers for array with SPACE: ").split(" "))) #read our array
find_num = int(input("Enter number for find: "))

index = 0
for i in range(1, quantity_el):
    if abs(my_array[i]-find_num) < abs(my_array[index]-find_num): #compare in absolute numbers differences
        index=i

print(f"The number {my_array[index]} is closest to the number {find_num}.")