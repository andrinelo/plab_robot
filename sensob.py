'''
One Sensob for each of these sensors:
    Ultrasonic sensor - one larger sensor
    Infrared sensors - array of 6 small sensors on robot’s underside.
    Camera - read extra document on PIL.
'''
from camera import Camera
from reflectance_sensors import ReflectanceSensors
from ultrasonic import Ultrasonic


class Sensob:

    def __init__(self, sensor):
        self.sensors = [sensor] #list of all sensors that this sensob 'controls'
        self.value = None

    def update(self):
        raise NotImplementedError
        # fetch the relevant sensor values
        #convert into pre-processed sensob value
        pass


    def get_value(self):
        return self.value


    def reset(self):
        self.value = None

class UltrasonicSensob(Sensob):

    def __init__(self, sensor):
        super().__init__(sensor)

    def update(self):
        for sensor in self.sensors:
            if isinstance(sensor, Ultrasonic):
                value = sensor.sensor_get_value()
                self.value = value
                return self.value
                #dette er en numerisk value - returnerer distanse til objekt foran robot
            else:
                raise TypeError

class ReflectanceSensob(Sensob):

    def __init__(self, sensor):
        super().__init__(sensor)

    def update(self):
        for sensor in self.sensors:
            if isinstance(sensor, ReflectanceSensors):
                value = sensor.update()
                self.value = value
                #dette er en array av 6 values
                return self.value
            else:
                raise TypeError

class CameraSensob(Sensob):

    def __init__(self, sensor):
        super().__init__(sensor)

    def update(self):
        for sensor in self.sensors:
            if isinstance(sensor, Camera):
                rgbobj = sensor.get_value()
                self.value = rgbobj
                return self.value
                #dette er et rgb-objet, aka tre vals i en tuppel
            else:
                raise TypeError