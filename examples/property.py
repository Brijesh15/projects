
class Celsius(object):
    def __init__(self, temperature = 0):
        self.temperature = temperature   # call the setter method from the initialiser
        #self._temperature = temperature # we can not the setter method from the initialiser, we only call setter when we modify the values 

    def to_fahrenheit(self):
        return (self._temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value

    #temperature = property(get_temperature,set_temperature,)

c = Celsius(10)
print c.temperature
c.temperature = 370
print c.temperature
