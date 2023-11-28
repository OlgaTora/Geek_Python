import re


class EmailValidator:

    def __init__(self):
        self.EMAIL_REGEX: str = "^[A-Za-z0-9+_.-]+@(.+)$"

    def is_valid_email(self, email: str) -> bool:
        if re.fullmatch(self.EMAIL_REGEX, email):
            return True
        return False
