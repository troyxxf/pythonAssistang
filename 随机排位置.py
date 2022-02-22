import random
with open("name.txt", encoding='utf-8') as file_object:
    lines = file_object.readlines()
print(len(lines))
a = random.sample(range(0, 101), 101)
n = 1
while n <= 101:
    b = a[n-1]
    with open("random_name.txt", "a") as file_object1:
        file_object1.write('%s : %s' % (str(n), lines[b]))
        n += 1

