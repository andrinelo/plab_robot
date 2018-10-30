class Arbitrator:

    def choose_action(self, behaviourlist):
        #go through all activ behaviours and choose winner
        #choose deterministically or stochastically - our option
        #return a tuple
            #motor recommandations (one per motob) of the winning behaviour
            #halt flag: should robot halt immediately?
        setting = None
        haltflag = False
        current_weight = -1
        for behaviour in behaviourlist:
            if behaviour.weight > current_weight:
                current_weight = behaviour.weight
                haltflag = behaviour.halt_request
                setting = behaviour.motor_recommendations
        return setting, haltflag
