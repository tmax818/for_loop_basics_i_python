## TODO Basic - Print all integers from 0 to 150.

for i in range(151):
    print(i)

## TODO Multiples of Five - Print all the multiples of 5 from 5 to 1,000

for i in range(1001):
    if i % 5 == 0:
        print(i)

## TODO Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".

for i in range(101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

## TODO Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.

total = 0

for i in range(500001):
    total += i

print(total)

## TODO Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.

for i in range(2018, 0, -4):
    if i % 2 == 0:
        print(i)

# # TODO Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum,
#  print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3,
#  the loop should print 3, 6, 9 (on successive lines)

lowNum = 2
highNum = 9
mult = 3

for i in range(highNum + 1):
    if i % mult == 0:
        print(i)
