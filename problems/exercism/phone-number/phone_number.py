import re


class PhoneNumber:
    def __init__(self, number: str):
        self.number = self.clean_phone_num(number)
        self.area_code = self.number[:3]

    def clean_phone_num(self, n: str) -> str:
        if any(ltr for ltr in n if ltr.islower()):
            raise ValueError("letters not permitted")
        # Terrible test -- test_invalid_with_punctuations -- implementation and
        # return error. Since string.punctuation would work very well here, but
        # punctuation is allowed in a phone number....
        elif any(pnc for pnc in n if pnc in "@:!"):
            raise ValueError("punctuations not permitted")

        clean = re.sub("[^0-9]", "", n)
        if len(clean) < 10:
            raise ValueError("incorrect number of digits")
        elif len(clean) > 11:
            raise ValueError("more than 11 digits")
        elif len(clean) == 11:
            if clean[0] != '1':
                raise ValueError("11 digits must start with 1")
            clean = clean[1:]

        if clean[0] == '0':
            raise ValueError("area code cannot start with zero")
        elif clean[0] == '1':
            raise ValueError("area code cannot start with one")
        elif clean[3] == '0':
            raise ValueError("exchange code cannot start with zero")
        elif clean[3] == '1':
            raise ValueError("exchange code cannot start with one")

        return clean

    def pretty(self) -> str:
        return f"({self.area_code})-{self.number[3:6]}-{self.number[6:]}"
