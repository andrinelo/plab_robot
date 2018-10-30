from time import sleep
from motob import Motob
from camera import Camera
from sensob import Sensob
from irproximity_sensor import IRProximitySensor
from reflectance_sensors import ReflectanceSensors
from ultrasonic import Ultrasonic
from zumo_button import ZumoButton
from arbitrator import Arbitrator


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
        #Update all behaviors
        pass


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
        self.update_motobs(behaviour, haltflag)
        self.wait()
        self.reset_sensobs()

if __name__ == '__main__':
    bbcon = BBCON()
    #adding sensobs
    bbcon.add_sensob(Sensob(Camera()))
    bbcon.add_sensob(Sensob(Ultrasonic()))
    bbcon.add_sensob(Sensob(IRProximitySensor()))
    bbcon.add_sensob(Sensob(ReflectanceSensors()))
    bbcon.add_sensob(Sensob(ZumoButton()))
    #adding behaviours

