 """
Uzrakstīt programmu Python, lai
atņemot divus norādītos veselos skaitļus. 
Tomēr, ja starpībs vērtība ir mazāka kā 10 un lielāka kā -10, 
atgriezt tekstu Poga.

"""
sk1=int(input("Ievadiet pirmo skaitli: "))
sk2=int(input("Ievadiet otro skaitli: "))

starpiba=sk1-sk2

if starpiba in range(5):
    print("Poga")
else:
    print(starpiba)