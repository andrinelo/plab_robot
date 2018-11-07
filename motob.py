from motors import Motors

class Motob:

    def __init__(self):
        self.motor = Motors() #list of all motors whose values it sets
        self.value = [] #most recent motor recommendation sent to the motob.
        self.motorsettings = {'f': self.motor.forward, 'b':self.motor.backward, 'l':self.motor.left, 'r':self.motor.right, 's':self.motor.stop}

    def update(self, setting, haltflag):
        self.value = []
        if haltflag:
            for motor in self.motors:
                motor.stop()
        else:
            if setting: 
                for comm in setting: 
                    self.value.append(comm)
            self.operationalize()
        #load new motor recommendation into the value slot and operationalize it.

    def operationalize(self):
        if len(self.value) == 2:
            self.motorsettings[self.value[0]](dur=self.value[1])
        elif len(self.value)==1:
            self.motorsettings[self.value[0]]()
        else: 
            pass
        #convert value into motor settings and send to the corresponding motor(s).
        


'''
In the robot project, the only actuators are the wheels, so the motob and the
(wheel) motor wrapper are about the same thing. See file motors.py for
details of the motor wrapper, and then build your motob class based on that.
'''