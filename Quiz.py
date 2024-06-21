questions=[
    ["1)Who is known as the Father of the Nation in India?","Jawaharlal Nehru" ,"Mahatma Gandhi" ,"Subhas Chandra Bose", "Sardar Vallabhbhai Patel","B"],
    ["2)What is the largest planet in our solar system?","Earth", "Mars", "Jupiter", "Saturn", "C"],
    ["3)What is the capital of Japan?","Beijing", "Seoul", "Bangkok", "Tokyo", "D"],
    ["4)In which year did the Titanic sink?","1905", "1912", "1920", "1930", "B"],
    ["5)Which ocean is the largest?","Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean", "D"]

]


levels=[100000,200000,300000,400000,500000]
money=0

for i in range(0,len(questions)):
    question=questions[i]

    print(f"Your question for {levels[i]}")
    print(f"{question[0]}")
    print(f"A){question[1]}     B){question[2]}")
    print(f"C){question[3]}     D){question[4]}")
    reply=input('Enter your Answer or to Quit No = ')
    if(reply=="No"):
        money=levels[i-1] if i>0 else 0
        break
    if(reply==question[-1]):
        print(f"Your Answer is correct for {levels[i]}\n")
        money=levels[i]
    else:
        print("Your Answer is Wrong")
        break

print(f"Your Winning Amount is {money}")
