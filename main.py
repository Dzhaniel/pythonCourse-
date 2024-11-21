san1=int(input("Санды енгіз:"))
amaldar=(input("Амалды енгіз(+,-,*,/)="))
san2=int(input("Санды енгіз:"))
if amaldar=="+":
    print("Жауабы:",san1+san2)
elif amaldar=="-":
    print("Жауабы:", san1- san2)
elif amaldar=="*":
    print("Жауабы:", san1 * san2)
elif amaldar=="/":
    if san2!=0:
        print("Жауабы:", san1 / san2)
    else:
        print("Қате:0-ге бөлу")
else:
    print("Қате операция")