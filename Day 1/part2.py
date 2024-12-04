'''
Part 2:

This time, you'll need to figure out exactly how often each number from the left list appears in the right list.
Calculate a total similarity score by adding up each number in the left list after multiplying it by the number of
times that number appears in the right list.

Once again consider your left and right lists. What is their similarity score?
'''

input = open("input.txt")
lines = input.readlines()

list1 = []
list2 = []

for line in lines:
    num1, num2 = line.split("   ")
    list1.append(int(num1))
    list2.append(int(num2))

similarity = 0

for id in list1:
    similarity += list2.count(id) * id

input.close()
output = open("output2.txt", 'w')
output.write(str(similarity))
output.close()

