def calculate_grade(score):
    if score < 0 or score > 100 :
        print("Invalid score . Please enter a score between 0 and 100 ")
    elif score < 40 :
        print("You have failed . F")
    elif score < 50 :
        print("D")
    elif score < 60 :
        print("C")
    elif score < 70 :
        print("B")
    else:
        print("A")