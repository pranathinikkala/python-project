#attendence calculation

attended = int(input("Classes attended: "))
total = int(input("Total classes: "))

if total > 0 and 0 <= attended <= total:
    percentage = attended / total * 100
    print("Attendance:", percentage, "%")

    if percentage >= 75:
        print("Eligible")
    else:
        print("Not Eligible")
else:
    print("Invalid attendance data")
