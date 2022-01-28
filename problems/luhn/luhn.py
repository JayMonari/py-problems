import re


class Luhn:
    def __init__(self, cardNo: str) -> None:
        self.cardNo = cardNo.strip()

    def valid(self) -> bool:
        if len(self.cardNo) == 1 or re.search("[^0-9 ]", self.cardNo):
            return False

        sum, sanitized = 0, re.sub("[^0-9]", "", self.cardNo)
        for i, digit in enumerate(reversed(sanitized), start=1):
            d = int(digit)
            if i % 2 == 0:
                d *= 2
                if d > 9:
                    d -= 9
            sum += d
        return sum % 10 == 0
