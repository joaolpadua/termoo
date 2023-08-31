import json , random

f = open("words.json" ,encoding = "Utf8")

words = json.load(f)
choice_c = random.choice(list(words.keys()))

print("###########################################")
print("Bem vindo ao jogo de adivinhação das datas!")
print("###########################################")

n_choices = 5
win = False

while n_choices > 0:
    print("Dica: " + words[choice_c])
    answer_user = input("Data : DDMMAAAA \n")
    if len(answer_user) != 8:
        print("Erro na entrada! Digite novamente: ")
        continue
    if answer_user.isdigit():
        check = []
        pontuation = 0
        for i in range(8):
            if answer_user[i] == choice_c[i]:
                check.append("✔️")
                pontuation += 1
            else:
                check.append("❌")

        print("Resposta: \n")
        print("|".join(check))
        print(" |".join(answer_user))
        print("#########################")

        if pontuation == 8:
            win = True

if win == True:
    print("VITÓRIA!!")
else:
    print("DERROTA!")
    print("A resposta era: " + choice_c)