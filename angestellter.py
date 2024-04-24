from mitarbeiter import Mitarbeiter

class Angestellter(Mitarbeiter):
    def __init__(self, name, gehalt, projektnummer):
        super().__init__(name, gehalt)
        self.projektnummer = projektnummer
    def __str__(self):
        return "Ausgabe Angestellte: \nName: " + self.name + "\nGehalt: " + str(self.gehalt) + "\nProjektnummer: " + str(self.projektnummer)
angestellt = Angestellter("Evelyn Müller", 34000, 12345)
print(angestellt)
print(angestellt.zeige_anzahl())