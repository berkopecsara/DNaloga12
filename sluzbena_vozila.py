class PodatkiVozila:
    def __init__(self, znamka, model, stevilo_prevozenih_kilometrov, datum_servisa):
        print ("Vozilo" + znamka + " " + model + " " + stevilo_prevozenih_kilometrov + " " + datum_servisa)
        self.znamka = znamka
        self.model = model
        self.stevilo_prevozenih_kilometrov = stevilo_prevozenih_kilometrov
        self.datum_servisa = datum_servisa

    def izpis(self):
        print (self.znamka + " " + self.model + " " + self.stevilo_prevozenih_kilometrov + " " + self.datum_servisa)

    def dodatni_kilometri(self, novi_kilometri):
        self.stevilo_prevozenih_kilometrov += novi_kilometri

    def posodobitev_datumov(self, nov_datum):
        self.datum_servisa = nov_datum

    def dodana_vozila(self):
        znamka = raw_input("Znamka vozila: ")
        model = raw_input("Model vozila: ")
        stevilo_prevozenih_kilometrov = raw_input("Stevilo prevozenih kilometrov: ")
        datum_servisa = raw_input("Datum servisa: ")

        vpis = novo_vozilo(znamka, model, stevilo_prevozenih_kilometrov, datum_servisa)

        if vpis:
            print "Vpisali se vozilo %s %s!" % (znamka, model)
        else:
            print "Kaksno je stevilo prevozenih kilometrov?"


vozilo1 = PodatkiVozila("Toyota", "4", "1234", "23.5.2016")
vozilo2 = PodatkiVozila("Polo", "10", "213", "24.6.2016")
vozilo3 = PodatkiVozila("Golf", "3", "1324", "1.1.2016")
vozilo4 = PodatkiVozila("Citroen", "4", "123", "1.1.2016")


print ("Vsa sluzbena vozila: ")
seznam_vozil = [vozilo1, vozilo2, vozilo3, vozilo4]
for v in seznam_vozil:
    v.izpis()


print "Vozila: %s" % seznam_vozil

podatki_vozil = open("podatki.txt", "wt")



print "End"