class Allergies:
    ITEMS = {
        "eggs":         1,
        "peanuts":      2,
        "shellfish":    4,
        "strawberries": 8,
        "tomatoes":     16,
        "chocolate":    32,
        "pollen":       64,
        "cats":         128,
    }

    def __init__(self, score: int) -> None:
        self.score = score

    def allergic_to(self, item: str) -> bool:
        return self.score & self.ITEMS[item] != 0

    @property
    def lst(self):
        return [i for i in self.ITEMS if self.allergic_to(i)]
