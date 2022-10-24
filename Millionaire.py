qstn_1 = 'Ո՞րն է Ֆրանսիայի մայրաքաղաքը'
qstn_2 = 'Ո՞վ է հայտնաբերել Ամերիկան'
qstn_3 = 'Ո՞վ է գծել Երևանի հատակագիծը'
qstn_4 = 'Ո՞րն է 12-ի և 24-ի ամենամեծ ընդհանուր բաժանարարը '
qstn_5 = 'Ո՞վ է ստեղծել այբուբենը'
qstn_6 = 'Ո՞րն է Պյութագորասի թեորեմը'
qstn_7 = 'question7'
qstn_8 = 'question8'
qstn_9 = 'question9'
qstn_10 = 'question10'

optns_1 = {1: "Լոնդոն", 2: "Փարիզ", 3: "Երևան", 4: "Բեռլին"}
optns_2 = {1: "Կոլումբոսը", 2: "Վասկո դա Գամա", 3: "Ամերիգո Վեսպուչիին", 4: "Լեյֆ Էրիքսոն"}
optns_3 = {1: "Երվանդ Թամանյան", 2: "Ալեքսանդր Թումանյան", 3: "Ալեքսանդր Գասպարյան", 4: "Ալեքսանդր Թամանյան"}
optns_4 = {1: "6", 2: "2", 3: "12", 4: "4"}
optns_5 = {1: "Կորյուն", 2: "Վռամշապուհը", 3: "Մեսրոպ Մաշտոց", 4: "Սահակ Պարթևը"}
optns_6 = {1: "c^2 = a^2 + b^2", 2: "a^2 = b^2", 3: "c^2 = a^2 - b^2", 4: " a^2 = c^2 + b^2"}
optns_7 = {1: 1, 2: 2, 3: 3, 4: 4}
optns_8 = {1: 1, 2: 2, 3: 3, 4: 4}
optns_9 = {1: 1, 2: 2, 3: 3, 4: 4}
optns_10 = {1: 1, 2: 2, 3: 3, 4: 4}
options = [optns_1, optns_2, optns_3, optns_4, optns_5, optns_6, optns_7, optns_8, optns_9, optns_10]
questions = {0: qstn_1, 1: qstn_2, 2: qstn_3, 3: qstn_4, 4: qstn_5, 5: qstn_6, 6: qstn_7, 7: qstn_8, 8: qstn_9, 9: qstn_10}
coins = 0
for i in questions:
    if i == 0:
        print(i + 1, ".", questions[i])
        print(options[i])
        answer_1 = int(input("your answer is: "))
        if answer_1 == list(optns_1.keys())[list(optns_1.values()).index('Փարիզ')]:
            coins += 500
            print("I'ts wright", 'you have', coins, 'coins')
        else:
            print("YOU LOSE!!!")
            break
    elif i == 1:
        print(i + 1, ".", questions[i])
        print(options[i])
        answer_2 = int(input("your answer is: "))
        if answer_2 == list(optns_2.keys())[list(optns_2.values()).index('Կոլումբոսը')]:
            coins += 500
            print("Yess", 'you have', coins, 'coins')
        else:
            print("YOU LOSE!!!!!!")
            break
    elif i == 2:
        print(i + 1, ".", questions[i])
        print(options[i])
        answer_3 = int(input("your answer is: "))
        if answer_3 == list(optns_3.keys())[list(optns_3.values()).index('Ալեքսանդր Թամանյան')]:
            coins += 500
            print("Yess", 'you have', coins, 'coins')
        else:
            print("YOU LOSE!!!!!!")
            break
    elif i == 3:
        print(i + 1, ".", questions[i])
        print(options[i])
        answer_4 = int(input("your answer is: "))
        if answer_4 == list(optns_4.keys())[list(optns_4.values()).index('12')]:
            coins += 500
            print("Yess", 'you have', coins, 'coins')
        else:
            print("YOU LOSE!!!!!!")
            break
    elif i == 4:
        print(i + 1, ".", questions[i])
        print(options[i])
        answer_5 = int(input("your answer is: "))
        if answer_5 == list(optns_5.keys())[list(optns_5.values()).index('Մեսրոպ Մաշտոց')]:
            coins += 500
            print("Yess", 'you have', coins, 'coins')
        else:
            print("YOU LOSE!!!!!!")
            break
    elif i == 5:
        answer = input("Do you want to continue the game? YES/NO ")
        if answer.upper() == 'YES':
            print(i + 1, ".", questions[i])
            print(options[i])
        else:
            print("The game is over", 'you have', coins, 'coins')
            break
        answer_6 = int(input("your answer is: "))
        if answer_6 == list(optns_6.keys())[list(optns_6.values()).index('c^2 = a^2 + b^2')]:
            coins += 500
            print("Yess", 'you have', coins, 'coins')
        else:
            print("YOU LOSE!!!!!!")
            break
    elif i == 6:
        print(i + 1, ".", questions[i])
        print(options[i])
        answer_7 = int(input("your answer is: "))
        if answer_7 == optns_7[2]:
            coins += 500
            print("Yess", 'you have', coins, 'coins')
        else:
            print("YOU LOSE!!!!!!")
            break
    elif i == 7:
        answer_8 = int(input("your answer is: "))
        if answer_8 == optns_8[3]:
            coins += 500
            print("Yess", 'you have', coins, 'coins')
        else:
            print("YOU LOSE!!!!!!")
            break
    elif i == 8:
        answer_9 = int(input("your answer is: "))
        if answer_9 == optns_9[4]:
            coins += 500
            print("Yess", 'you have', coins, 'coins')
        else:
            print("YOU LOSE!!!")
            break
    elif i == 9:
        answer_10 = int(input("your answer is: "))
        if answer_10 == optns_10[2]:
            coins += 500
            print("YOU WIN THE GAME!!!"'\n', 'YOU WON', coins, 'COINS!!!')
        else:
            print("YOU LOSE!!!")
            break


