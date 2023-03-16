from faker import Faker
fake = Faker()

class BaseContact:
    def __init__(self, first_name, last_name, email, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number

        self._label_lenght = 0
    
    def contact(self):
        return f'Wybieram numer {self.phone_number} i dzwonię do {self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.email}'
    
    @property
    def label_lenght(self):
        return (len(self.first_name) + len(self.last_name)) 
    
class BusinessContact(BaseContact):
    def __init__(self, business_phone_number, company, job, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.business_phone_number = business_phone_number
        self.company = company
        self.job = job

        self._label_lenght = 0
    
    def businesscontact(self):
        return f'Wybieram numer {self.business_phone_number} i dzwonię do {self.first_name} {self.last_name}'
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.job}, {self.email}'
    
    @property
    def label_lenght(self):
        return (len(self.first_name) + len(self.last_name)) 
        
person1 = BaseContact(first_name='Adam', last_name='Sandler', phone_number=123456789, email='adam@sand.star')
person2 = BusinessContact(first_name ='Basia', last_name='Bęben', phone_number=123123123, email='basia@beben.be', 
                          company='Company', job='worker', business_phone_number= 345234345)

def create_contact():



