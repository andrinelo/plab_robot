class BBCON:

    def __init__(self):
        self.behaviours = [] #list of all behavior objects (BHRs)
        self.active_behaviours = [] #a list of all currently-active BHRs.
        self.sensobs = [] #a list of all sensory objects
        self.motobs = [] #a list of all motor objects
        self.arb = None #this resolves motor requests produced by the behaviors.

    def update_sensobs(self):
        #Update all sensobs
        pass


    def update_behaviours(self):
        #Update all behaviors
        pass


    def invoke_arb(self):
        #Invoke the arbitrator by calling arbitrator.choose action.
        self.arb.choose_action()


    def update_motobs(self):
        #Update motobs based on the winning motor recommendations.
        pass


    def wait(self):
        #Allows motor settings to work for a timestep.
        pass


    def reset_sensobs(self):
        #6 Reset all sensobs
        pass


    def run_one_timestep(self):
        #Does methods 1-6 in sequence
        self.update_sensobs()
        self.update_behaviours()
        self.invoke_arb()
        self.update_motobs()
        self.wait()
        self.reset_sensobs()