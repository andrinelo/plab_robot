from time import sleep
class BBCON:

    def __init__(self):
        self.behaviours = [] #list of all behavior objects (BHRs)
        self.active_behaviours = [] #a list of all currently-active BHRs.
        self.sensobs = [] #a list of all sensory objects
        self.motobs = [] #a list of all motor objects
        self.arb = None #this resolves motor requests produced by the behaviors.


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
        self.arb.choose_action()


    def update_motobs(self):
        #Update motobs based on the winning motor recommendations.
        for motob in self.motobs:
            motob.update()


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
        self.invoke_arb()
        self.update_motobs()
        self.wait()
        self.reset_sensobs()


