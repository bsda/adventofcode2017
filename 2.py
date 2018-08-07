


#part 1
input = list()
position = 0
diff = 0
with open('2.txt', 'r') as f:
    for l in f.readlines():
        input.append(list())
        for n in l.split('\t'):
            input[position].append(int(n))
        input[position] = sorted(input[position])
        position += 1


for l in input:
    diff += l[-1] - l[0]

print(diff)

#part 2

#input = [[5,9,2,8], [9,4,7,3], [3,8,6,5]]

n = 0
sum = 0
for l in input:
    for n in l:
        # print(n)
        for n2 in l:
            # print(n2)
            if n != n2:
                if n % n2 == 0:
                    print(f'{n} / {n2} = {(n // n2)} ')
                    sum += (n // n2)
#
print(sum)

