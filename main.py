from angestellter import Angestellter

angest1 = Angestellter("Zara Svensson", 20000, 3456)
angest2 = Angestellter("Manni Deutsch", 50000, 678)
print(angest1)
print(angest2)
angest2.gehalt = 44300
print(angest2)
print(Angestellter.zeige_anzahl())