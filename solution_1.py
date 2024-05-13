class AirConditioning:

    def __init__(self):
        self.__status = False
        self.__temperature = None
        self.setup = True

    status = property()
    temperature = property()

    @status.setter
    def status(self, value):
        if self.setup and self.__status:
            self.__status = value

    @status.getter
    def status(self):
        return self.__status
    
    @temperature.setter
    def temperature(self, value):
        if self.setup and self.__status:
            if value >= 0 and value <= 43:
                self.__temperature = value

    @temperature.getter
    def temperature(self):
        return self.__temperature

    def switch_on(self):
        self.__status = True
        self.setup = True
        self.__temperature = 18
        self.setup = False

    def switch_off(self):
        self.__status = False
        self.__temperature = None

    def reset(self):
        if self.__status:
            self.__temperature = 18

    def get_temperature(self):
        return self.__temperature

    def raise_temperature(self):
        if self.__status:
            if self.__temperature < 43:
                self.__temperature += 1

    def lower_temperature(self):
        if self.__status:
            if self.__temperature > 0:
                self.__temperature -= 1

    def __str__(self):
        if not self.__status:
            return f'Кондиционер выключен.' 
        return f'Кондиционер включен. \
Температурный режим: {self.__temperature} градусов.'