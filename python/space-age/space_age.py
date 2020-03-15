class SpaceAge:

    def __init__(self, seconds):
        self.seconds = seconds

    def on_earth(self):
        return round(self.seconds / 31557600, 2)

    def on_mercury(self):
        x = 31557600 * 0.2408467
        return round(self.seconds / x , 2)

    def on_venus(self):
        x = 31557600 * 0.61519726
        return round(self.seconds / x, 2)

    def on_mars(self):
        x = 31557600 * 1.8808158
        return round(self.seconds / x, 2)

    def on_jupiter(self):
        x = 31557600 * 11.862615
        return round(self.seconds / x, 2)

    def on_saturn(self):
        x = 31557600 * 29.447498
        return round(self.seconds / x, 2)

    def on_uranus(self):
        x = 31557600 * 84.016846
        return round(self.seconds / x, 2)

    def on_neptune(self):
        x = 31557600 * 164.79132
        return round(self.seconds / x, 2)
