##Admin
class Admin:
    ##attributes
    def __init__ (self,admin_id:int, username:str, password:str, email:str):
        self.admin_id = admin_id
        self.username = username
        self.password = password
        self.email = email
    
    ##admin_id Getter & Setter
    @property
    def admin_id(self):
        return self.__admin_id
    @admin_id.setter
    def admin_id(self, value):
        self.__admin_id = value
        if not admin_id:
            raise ValueError("admin_id ist erforderlich")
        if not isinstance(admin_id, int):
            raise ValueError("admin_id muss eine Zahl sein")
    
    ##username Getter & Setter
    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, value: str):
        if value and isinstance(value, str):
            self.__username = value
        else:
            raise ValueError("Ungültiger Username")
    
    ##password Getter & Setter
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, value):
        self.__password = value
        if not isinstance(value, str):
            raise ValueError("Passwort muss ein String sein")
        if len(value) < 8:
            raise ValueError("Passwort muss mindestens 8 Zeichen lang sein")
        has_letter = any(c.isalpha() for c in value)
        has_digit = any(c.isdigit() for c in value)
        has_special = any(not c.isalnum() for c in value)
        if not has_letter:
            raise ValueError("Passwort muss mindestens einen Buchstaben enthalten")
        if not has_digit:
            raise ValueError("Passwort muss mindestens eine Zahl enthalten")
        if not has_special:
            raise ValueError("Passwort muss mindestens ein Sonderzeichen enthalten")

    ## email Getter & Setter
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, value):
        if "@" not in value or "." not in value:
            raise ValueError("Ungültige Email")
        self.__email = value