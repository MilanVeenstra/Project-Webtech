import re
class EmailValidator:
    def __init__(self, email):
        self.email = email

    def validate_email(self):
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if re.match(email_regex, self.email):
            return self.email
        else:
            return False