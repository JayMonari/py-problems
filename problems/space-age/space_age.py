class SpaceAge:
    EARTH_PERIOD = 31557600
    MERCURY_PERIOD = 0.2408467 * EARTH_PERIOD
    VENUS_PERIOD = 0.61519726 * EARTH_PERIOD
    MARS_PERIOD = 1.8808158 * EARTH_PERIOD
    JUPITER_PERIOD = 11.862615 * EARTH_PERIOD
    SATURN_PERIOD = 29.447498 * EARTH_PERIOD
    URANUS_PERIOD = 84.016846 * EARTH_PERIOD
    NEPTUNE_PERIOD = 164.79132 * EARTH_PERIOD

    def __init__(self, seconds: int) -> None:
        self.seconds = seconds

    def on_mercury(self) -> float:
        return round(self.seconds / self.MERCURY_PERIOD, 2)

    def on_venus(self) -> float:
        return round(self.seconds / self.VENUS_PERIOD, 2)

    def on_earth(self) -> float:
        return round(self.seconds / self.EARTH_PERIOD, 2)

    def on_mars(self) -> float:
        return round(self.seconds / self.MARS_PERIOD, 2)

    def on_jupiter(self) -> float:
        return round(self.seconds / self.JUPITER_PERIOD, 2)

    def on_saturn(self) -> float:
        return round(self.seconds / self.SATURN_PERIOD, 2)

    def on_uranus(self) -> float:
        return round(self.seconds / self.URANUS_PERIOD, 2)

    def on_neptune(self) -> float:
        return round(self.seconds / self.NEPTUNE_PERIOD, 2)
