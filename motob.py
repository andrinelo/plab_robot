from motors import Motors

class Motob:

    def __init__(self):
        self.motors = [Motors()] #list of all motors whose values it sets
        self.value = None #most recent motor recommendation sent to the motob.

    def update(self, setting, haltflag):
        if haltflag:
            for motor in self.motors:
                motor.stop()
        else:
            self.value = setting
            self.operationalize(setting)
        #load new motor recommendation into the value slot and operationalize it.

    def operationalize(self, setting):

        #convert value into motor settings and send to the corresponding motor(s).
        pass


'''
In the robot project, the only actuators are the wheels, so the motob and the
(wheel) motor wrapper are about the same thing. See file motors.py for
details of the motor wrapper, and then build your motob class based on that.
'''