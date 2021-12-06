from typing import Tuple


class Clock:
    MINS_PER_HOUR = 60
    HOURS_PER_DAY = 24

    def __init__(self, hour: int, minute: int) -> None:
        nhours, nmins = self.__normalize(hour, minute, self.MINS_PER_HOUR)
        _, nhours = self.__normalize(0, nhours, self.HOURS_PER_DAY)
        self.hours = nhours
        self.mins = nmins

    def __repr__(self) -> str:
        return f"{str(self.hours).zfill(2)}:{str(self.mins).zfill(2)}"

    def __eq__(self, other: "Clock") -> bool:
        return str(self) == str(other)

    def __add__(self, minutes: int) -> "Clock":
        self.hours, self.mins = self.__normalize(
            self.hours, self.mins+minutes, self.MINS_PER_HOUR)
        _, self.hours = self.__normalize(0, self.hours, self.HOURS_PER_DAY)
        return self

    def __sub__(self, minutes: int) -> "Clock":
        self.hours, self.mins = self.__normalize(
            self.hours, self.mins-minutes, self.MINS_PER_HOUR)
        _, self.hours = self.__normalize(0, self.hours, self.HOURS_PER_DAY)
        return self

    def __normalize(self, hi: int, lo: int, base: int) -> Tuple[int, int]:
        if lo < 0:
            norm = (-lo-1) // base + 1
            hi -= norm
            lo += norm * base
        if lo >= base:
            norm = lo // base
            hi += norm
            lo -= norm * base
        return hi, lo
