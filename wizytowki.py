# Klasa podstawowa
class BaseContact:
    def __init__(self, name, ascii_emai, phone_number):
        self.name = name
        self.ascii_emai = ascii_emai
        self.phone_number = phone_number
    
    def __repr__(self):
        return f"{self.name} {self.ascii_emai} {self.phone_number}"
    @property
    def contact(self):
        print(f"Wybieram numer {self.phone_number} i dzwonię do {self.name}")
    @property
    def label_length(self):
        name_surname = self.name.split(' ')
        print("Ilość liter imienia = %d i nazwiska = %d" % (len(name_surname[0]),len(name_surname[1])))

# Klasa dziedziczona
class BusinessContact(BaseContact):
    def __init__(self, job, company, *arg, **kwarg):
        super().__init__(*arg, **kwarg)
        self.job = job
        self.company = company

# Kreator tożsamości
def create_contacts(namecard_kind, amount):
    from faker import Faker 
    fake = Faker("pl_PL")  
    namecard = []

    for i in range(amount):
        if namecard_kind == 'BaseContact':
            namecard.append(BaseContact(
                fake.name(),
                fake.ascii_email(),
                fake.phone_number()
            ))
        elif namecard_kind == 'BusinessContact':
            namecard.append(BusinessContact(
                fake.company(),
                fake.job(),
                fake.name(),
                fake.ascii_company_email(),
                fake.phone_number()
            ))
        else:
            raise Error(f'{namecard_kind} isn\'t excepted value. You can choose \'BaseContact\' or \'BusinessContact\'')
    return namecard

# Wyświetlanie metod contact dla wizytówek
for i in create_contacts('BusinessContact', 3):
    i.contact
