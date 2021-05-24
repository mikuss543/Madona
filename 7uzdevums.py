"""
Uzrakstiet programmu Python, lai aprēķinātu 
četru ievadīto skaitļu summu.
Ja ievadītās vērtības ir vienādas, atgrieziet summu,
divkāršojot un paņemot tās absolūto vērtību.
"""
sk1=int(input("Ievadi pirmo skaitli: "))
sk2=int(input("Ievadi otro skaitli: "))
sk3=int(input("Ievadi trešo skaitli: "))
sk4=int(input("Ievadi ceturto skaitli: "))

if sk1==sk2==sk3==sk4:
    print(abs(sk1 * 2))

else: 
    print(sk1+sk2+sk3+sk4)