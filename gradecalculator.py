import math
print("")
print("GRADE CALCULATOR")
while True:
    current = input("Current grade (%): ")
    if (current.endswith('%')):
        current = current.rstrip(current[-1])
    current = float(current)

    final = input("Final exam (% of class): ")
    if (final.endswith('%')):
        final = final.rstrip(final[-1])
        
    if (str(final) != "0"):
        final = float(final)
        print("")
        print("Do you want to calculate the ")
        calculateForDesired = str(input("score you need for a certain grade? (y/n): "))
        if (calculateForDesired == "y"):
            desired = input("Desired grade (%): ")
            if (desired.endswith('%')):
                desired = desired.rstrip(desired[-1])
            desired = float(desired)

            currentWithFinal = current * ((100 - final) / 100)
            needed = (desired - currentWithFinal) / (final / 100)
            print("")
            print("You need a " + str(needed) + "% on the final exam")
            print("")
        else:
            print("")
            print("Put % if your input is a %. Else put fraction or decimal")
            gradeOnFinal = input("Anticipated grade on final (% or faction): ")
            if (gradeOnFinal.endswith('%')):
                gradeOnFinal = gradeOnFinal.rstrip(gradeOnFinal[-1])
                gradeOnFinal = float(gradeOnFinal)
            elif ("/" in gradeOnFinal):
                gradeOnFinal = eval(gradeOnFinal)
                gradeOnFinal = float(gradeOnFinal) * 100
            else:
                gradeOnFinal = float(gradeOnFinal)

            currentWithFinal = current * ((100 - final) / 100)
            finalGrade = currentWithFinal + (gradeOnFinal * (final / 100))
            print("")
            print("Your final grade will be " + str(finalGrade) + "%")
            print("")
    else:
        print("")
        print("It is impossible to determine your grade without")
        print("knowing how much your final exam will be worth.")
        print("")
        print("You can do the calculations manually. However, this")
        print("calculator will not speed up the process.")
#        print("")
#        categories = input("Are there grade categories in your class (y/n): ")
#        if (categories == "y"):
#            print("")
#            categoryValue = input("What is the value of the category of the final (%): ")
#            if (categoryValue.endswith('%')):
#                categoryValue = categoryValue.rstrip(categoryValue[-1])
#            categoryValue = float(categoryValue)
#            
#            categoryGrade = input("What is your grade in that category (%): ")
#            if (categoryGrade.endswith('%')):
#                categoryGrade = categoryGrade.rstrip(categoryGrade[-1])
#            categoryGrade = float(categoryGrade)
#
#            print("Do you want to calculate the ")
#            calculateForDesired = str(input("score you need for a certain grade? (y/n): "))
#            if (calculateForDesired == "y"):
#                desired = input("Desired grade (%): ")
#                if (desired.endswith('%')):
#                    desired = desired.rstrip(desired[-1])
#                desired = float(desired)
#
#                currentWithFinal = current * ((100 - categoryValue) / 100)
#                needed = (desired - currentWithFinal) / (categoryValue / 100)
#                print("")
#                print("You need a " + str(needed) + "% on the final exam")
#                print("")
#            else:
#                print("")
#        else: 
#            print("")
