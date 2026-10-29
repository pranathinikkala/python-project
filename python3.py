#student marks analysics

marks = []

for i in range(3):
    m = int(input("Enter marks: "))
    marks.append(m)

total = sum(marks)
average = total / 3

print("Total:", total)
print("Average:", average)

if min(marks) >= 35:
    print("Result: PASS")
else:
    print("Result: FAIL")
