class Contact:
    def __init__(self, name = '', phone= '', email = ''):
        self.__name = name
        self.__phone = phone
        self.__email = email
        
    def set_phone(self, phone):
        self.__phone = phone

    def set_email(self, email):
      self.__email = email

    def get_contact(self):
        return(self.__name, self.__phone, self.__email)