from time import sleep
from motob import Motob
from camera import Camera
from sensob import *

from irproximity_sensor import IRProximitySensor
from reflectance_sensors import ReflectanceSensors
from ultrasonic import Ultrasonic
from zumo_button import ZumoButton
from arbitrator import Arbitrator
from cameraBehaviour import cameraBehaviour
from followline import FollowLine
from behaviour import Behaviour

class BBCON:

    def __init__(self):
        self.behaviours = [] #list of all behavior objects (BHRs)
        self.active_behaviours = [] #a list of all currently-active BHRs.
        self.sensobs = [] #a list of all sensory objects
        self.motobs = [Motob()] #a list of all motor objects
        self.arb = Arbitrator() #this resolves motor requests produced by the behaviors.

    def add_behaviour(self, behaviour):
        #append a newly-created behavior onto the behaviors list.
        self.behaviours.append(behaviour)


    def add_sensob(self, sensob):
        #append a newly-created sensob onto the sensobs list.
        self.sensobs.append(sensob)


    def activate_behaviour(self, behaviour):
        #add an existing behavior onto the active-behaviors list.
        if behaviour not in self.active_behaviours:
            self.active_behaviours.append(behaviour)


    def deactivate_behaviour(self, behaviour):
        #remove an existing behavior from the active behaviors list.
        self.active_behaviours.remove(behaviour)


    def update_sensobs(self):
        #Update all sensobs
        for sensob in self.sensobs:
            sensob.update()



    def update_behaviours(self):
        for behaviour in self.behaviours:
            behaviour.update()


    def invoke_arb(self):
        #Invoke the arbitrator by calling arbitrator.choose action.
        return self.arb.choose_action(self.active_behaviours) #usikker på om den kun skal velge mellom de aktive eller alle




    def update_motobs(self, behaviour, haltflag):
        #Update motobs based on the winning motor recommendations.
        for motob in self.motobs:
            motob.update(behaviour, haltflag)


    def wait(self):
        #Allows motor settings to work for a timestep.
        sleep(0.5)


    def reset_sensobs(self):
        for sensob in self.sensobs:
            sensob.reset()


    def run_one_timestep(self):
        #Does methods 1-6 in sequence
        self.update_sensobs()
        self.update_behaviours()
        setting, haltflag = self.invoke_arb()
        self.update_motobs(setting, haltflag)
        self.wait()
        self.reset_sensobs()

if __name__ == '__main__':
    ZumoButton().wait_for_press()
    bbcon = BBCON()
    #makin sensobObjects 
    camsensob = CameraSensob(Camera())
    ultsens = UltrasonicSensob(Ultrasonic())
    refsens = ReflectanceSensob(ReflectanceSensors())

    #adding sensobs
    bbcon.add_sensob(camsensob)
    bbcon.add_sensob(ultsens)
    bbcon.add_sensob(refsens)

    #adding behaviours
    bbcon.add_behaviour(cameraBehaviour([bbcon.sensobs[0],bbcon.sensobs[1]], bbcon))
    bbcon.add_behaviour(FollowLine([bbcon.sensobs[2]], bbcon))

    #calling loop 
    #hello @
    while True:
        bbcon.run_one_timestep()


