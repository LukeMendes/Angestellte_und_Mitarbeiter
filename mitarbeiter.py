class Mitarbeiter(object):
    anzahl = 0
    def __init__(self, name, gehalt):
        self.name = name
        self.gehalt = gehalt
        Mitarbeiter.anzahl += 1
    @staticmethod
    def zeige_anzahl():
        return "Gesamt Mitarbeiter %d" % Mitarbeiter.anzahl
    def __str__(self):
        return "Name:" + self.name + "\nGehalt:" + str(self.gehalt)
chef = Mitarbeiter("Markus Boss", 120000)
print(chef)
print(Mitarbeiter.zeige_anzahl())
chef1 = Mitarbeiter("Martina Boss", 150000)
print(chef1)
print(Mitarbeiter.zeige_anzahl())