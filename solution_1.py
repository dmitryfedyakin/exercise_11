class AirConditioning:
    '''
    Class describes AirConditioner work.
    '''
    
    def __init__(self):
        '''
        Initializes Air Conditioner data.
        '''

        self.__status = False
        self.__temperature = None
        self.setup = True

    status = property()
    temperature = property()

    @status.setter
    def status(self, value):
        '''
        Sets Air Conditioner status.

        :param value: Status value
        '''
      
        if self.setup and self.__status:
            self.__status = value

    @status.getter
    def status(self):
        '''
        Returns Air Conditioner status of work.
        '''
      
        return self.__status
    
    @temperature.setter
    def temperature(self, value):
        '''
        Sets Air Conditioner temperature.

        :param value: Temperature value
        '''
      
        if self.setup and self.__status:
            if value >= 0 and value <= 43:
                self.__temperature = value

    @temperature.getter
    def temperature(self):
        '''
        Returns Air Conditioner temperature.
        '''
        
        return self.__temperature

    def switch_on(self):
        '''
        Switches on Air Conditioner.
        '''
        
        self.__status = True
        self.setup = True
        self.__temperature = 18
        self.setup = False

    def switch_off(self):
        '''
        Switches off Air Conditioner.
        '''

        self.__status = False
        self.__temperature = None

    def reset(self):
        '''
        Resets Air Conditioner.
        '''

        if self.__status:
            self.__temperature = 18

    def get_temperature(self):
        '''
        Returns Air Conditioner temperature.
        '''

        return self.__temperature

    def raise_temperature(self):
        '''
        Increase Air Conditioner temperature.
        '''

        if self.__status:
            if self.__temperature < 43:
                self.__temperature += 1

    def lower_temperature(self):
        '''
        Decrease Air Conditioner temperature.
        '''

        if self.__status:
            if self.__temperature > 0:
                self.__temperature -= 1

    def __str__(self):
        '''
        Returns string representation of an object (for users).
        '''

        if not self.__status:
            return f'Кондиционер выключен.' 
        return f'Кондиционер включен. \
Температурный режим: {self.__temperature} градусов.'