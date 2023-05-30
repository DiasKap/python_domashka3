quantity_el = int(input("Enter quantity elements in array: "))
my_array = list(map(int, input("Enter numbers for array with SPACE: ").split(" "))) #read our array
find_num = int(input("Enter number for find: "))

count = 0
for i in range(quantity_el):
    if my_array[i] == find_num:
        count +=1

print(f"Number {find_num} entered {count} times.")