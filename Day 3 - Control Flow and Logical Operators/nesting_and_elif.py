maths_score=int(input("Maths Score :" ))
english_score=int(input("English SCore : "))
if maths_score >= 90:
    if english_score >= 90:
        print("You're good at everything")
    else:
        print("You're good at maths")
if english_score >= 90:
    print("You're good at english")