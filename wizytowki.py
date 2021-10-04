class BaseContact:
    def __init__(self,name,surname,email,number):
        self.name = name
        self.surname = surname
        self.email = email
        self.number = number
    
    @property
    def contact(self):
        print(f"Wybieram numer {self.number} i dzwonię do {self.name} {self.surname}")
    @property
    def label_length(self):
        print("Ilość liter imienia = %d i nazwiska = %d" % (len(self.name),len(self.surname)))

class BusinessContact(BaseContact):
    def __init__(self, position, firm, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        self.position = position
        self.firm = firm

S_Czarnecki = namecard("Szymon","Czarnecki","SzymonCzarnecki@dayrep.com","Standard Food","Fire fighter")
K_Wieczorek = namecard("Kasper","Wieczorek","KasperWieczorek@jourrapide.com","Peter Reeves","Architect")
L_Dudek = namecard("Lucyna","Dudek","LucynaDudek@dayrep.com","The High Heelers","Maintenance machinist")
J_Nowak = namecard("Jarek","Nowak","JarekNowak@armyspy.com","Joseph Magnin","Security officer")
M_Borkowski = namecard("Mścisław","Borkowski","MscislawBorkowski@armyspy.com","Glicks Furniture","Audio control engineer")

namecard_pack = [M_Borkowski, S_Czarnecki, L_Dudek, J_Nowak, K_Wieczorek]

for i in namecard_pack:
    print("{:10}{:12}{}".format(i.name, i.surname, i.email))

S_Czarnecki.contact
S_Czarnecki.label_length   
