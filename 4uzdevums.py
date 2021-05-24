"""
Uzrakstiet programmu Python, lai pārbaudītu, vai norādītā
vērtība ir vērtību grupā.

Testa dati:
3 -> [1, 5, 8, 3]: taisnība
-1 -> [1, 5, 8, 3]: nepatiesa
  """

vertiba=int(input("Ievadiet vērtību: "))


if vertiba == 1 or vertiba == 5 or vertiba == 8 or vertiba ==3:
  print("taisnība") 

else:
  print("nepatiesība")