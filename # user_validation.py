# user_validation.py
import re

class UserValidation:
    @staticmethod
    def validate_email(email: str) -> bool:
        """Validates if the provided email is in a proper format."""
        if not isinstance(email, str):
            return False
        email = email.strip()
        if not email:
            return False
        pattern = r'^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email, re.IGNORECASE))

    @staticmethod
    def validate_username(username: str) -> bool:
        """Validates username (3–20 chars, letters/numbers/underscore only)."""
        if not isinstance(username, str):
            return False
        username = username.strip()
        if not username:
            return False
        pattern = r'^[a-zA-Z0-9_]{3,20}$'
        return bool(re.match(pattern, username))

    @staticmethod
    def validate_phone_number(phone: str) -> bool:
        """Validates Egyptian phone number (starts with 010, 011, 012, 015 or 20 10,20 11,20 12,20 15 — 11 digits total or 12 if it starts with 2)."""
        if not isinstance(phone, str):
            return False
        phone = phone.strip()
        if not phone:
            return False
        if not phone.isdigit():
            return False
        length = len(phone)
        if length == 11:
            if phone.startswith(('010', '011', '012', '015')):
                return True
        elif length == 12:
            if phone.startswith(('2010', '2011', '2012', '2015')):
                return True
        return False

    @staticmethod
    def validate_national_id(national_id: str) -> bool:
        """Validates Egyptian national ID (14 digits with valid date and governorate code)."""
        if not isinstance(national_id, str):
            return False
        national_id = national_id.strip()
        if not national_id:
            return False
        if len(national_id) != 14 or not national_id.isdigit():
            return False
        century_code = int(national_id[0])
        if century_code not in (2, 3):
            return False
        month = int(national_id[3:5])
        if month < 1 or month > 12:
            return False
        day = int(national_id[5:7])
        if day < 1 or day > 31:
            return False
        gov_code = int(national_id[7:9])
        if gov_code < 1 or gov_code > 88:
            return False
        return True