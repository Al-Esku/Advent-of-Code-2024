'''
Part 1:

Maybe the lists are only off by a small amount! To find out, pair up the numbers and measure how far apart they are.
Pair up the smallest number in the left list with the smallest number in the right list, then the second-smallest left
number with the second-smallest right number, and so on.

Within each pair, figure out how far apart the two numbers are; you'll need to add up all of those distances. For
example, if you pair up a 3 from the left list with a 7 from the right list, the distance apart is 4; if you pair up a
9 with a 3, the distance apart is 6.

To find the total distance between the left list and the right list, add up the distances between all of the pairs you
found.

Your actual left and right lists contain many location IDs. What is the total distance between your lists?
'''

input = open("input.txt")
lines = input.readlines()

list1 = []
list2 = []

for line in lines:
    num1, num2 = line.split("   ")
    list1.append(int(num1))
    list2.append(int(num2))

sum = 0

list1.sort()
list2.sort()

for i in range(len(list1)):
    id1 = list1.pop()
    id2 = list2.pop()
    sum += abs(id1 - id2)

input.close()
output = open("output1.txt", 'w')
output.write(str(sum))
output.close()
