'''
One Sensob for each of these sensors:
    Ultrasonic sensor - one larger sensor
    Infrared sensors - array of 6 small sensors on robot’s underside.
    Camera - read extra document on PIL.
'''


class Sensob:

    def __init__(self):
        self.sensors = [] #list of all sensors that this sensob 'controls'
        self.value = None

    def update(self):
        for sensor in self.sensors:
            # fetch the relevant sensor values
            sensor_val = self.get_value(sensor)
            #convert into pre-processed sensob value
            pass


    def get_value(self, sensor):
        #ma sjekke hvilke type objekter det er vi far tilbake
        #skal pre-processes ulikt avhengig av type
        value = sensor.get_value()
        #TODO PRE-PROCESSING
        #if isinstance(value, xxx)

        prep_value = value
        return prep_value

    def reset(self):
        pass


    '''
    Vet ikke hvor dette skal inn
    Zumo Button
        A very simple sensor.
        The only method: wait_for_press
    
    '''
