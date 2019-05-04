# Module 3
#   Programming Assignment 4
#     Prob-3.py

# Jonathan Ciarlo

def letterGrade(score):
    # your code here
    grade = "inavalid"
   
   
    if score == 0:
        grade = "F"
    elif score == 1:
        grade = "F"
    elif score == 2:
        grade = "D"
    elif score == 3:
        grade = "C"
    elif score == 4:
        grade = "B"
    elif score == 5:
        grade = "A"
       
    return grade
    

def unitTest():
    # your test code here
    print("Leter grade:", letterGrade(0))
    print("Leter grade:", letterGrade(1))
    print("Leter grade:", letterGrade(2))
    print("Leter grade:", letterGrade(3))
    print("Leter grade:", letterGrade(4))
    print("Leter grade:", letterGrade(5))


if __name__ == "__main__":
    unitTest()