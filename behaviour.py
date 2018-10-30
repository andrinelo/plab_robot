class Behaviour:

    def __init__(self, bbcon, sensob, recommendations, priority):
        self.bbcon = bbcon #pointer to the controller.
        self.sensobs = [sensob] #all sensobs that it uses.
        self.motor_recommendations = [] #a list of recommendations, one per motob, that this behavior provides to the arbitrator.
        self.active_flag = False #boolean variable indicating that the behavior is currently active or inactive.
        self.halt_request = False #request that robot halts.
        self.priority = None #a static, pre-defined value indicating the importance of this behavior.
        self.match_degree = 0 #value between [0,1] : degree to which current conditions warrant the performance of this behavior.
        self.weight = self.priority*self.match_degree #priority x match degree; the arbitrator gets this.

    def consider_deactivation(self):
        raise NotImplementedError
        #whenever a behavior is active, it should test whether it should deactivate.
        #disse implementeres i subklassene. kall på act/deact i bbcon


    def consider_activation(self):
        raise NotImplementedError
        # disse implementeres i subklassene. kall på act/deact i bbcon
        #whenever a behavior is inactive, it should test whether it should activate.

    def update(self):
        #update activity status
        #call sense_and_act
        #set weight to match degree x priority ;
        pass

    def sense_and_act(self):
        #main action of a behaviour
        #use sensob readings to produce motob recommendations (and halt requests)
        pass

    '''
    In general, behaviors can do many things, but must:
        consider activation or deactivation
        produce motor recommendations
        update match degree
    They must NOT communicate directly with other behaviors!!
    '''
