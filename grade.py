conAssmt =input("Please type your marks for the Continous Assessment : ")  #Taking input for Continous Assessment mark
conAssmt = int(conAssmt)  #Converting marks into an integer
conAssmtP = conAssmt*0.3  #convrting marks into 30%
examAssmt = input("Please type your marks for the Examination : ")  #Taking input for Examination Marks
examAssmt = int(examAssmt) #Converting Marks into integer
examAssmtP = examAssmt*0.7 # Converting Examination Marks into 70% 

marks = examAssmt+conAssmtP  # Suming Both the Continous Assessment Marks and the Examination Marks 
print("Your mark was  is ",marks)  # Displaying the total Marks 


# If statements for cheking the marks and displaying the right grade for KNUST grading system
if marks > 70:
    print(" Your Grade is  A")
elif marks >= 60 and marks <= 69:
    print("Your Grade is  B")
elif marks >= 50 and marks <= 59:
    print("Your Grade is  C")
elif marks >= 40 and marks <= 49:
    print("Your Grade is  D")
elif marks >= 1 and marks <= 39:
    print("Your Grade is  F")
