from behaviour import Behaviour
from sensob import *

class FollowLine(Behaviour):

    def __init__(self, bbcon, sensob, recommendations, priority):
        super().__init__(bbcon, sensob, recommendations, priority)
        self.name = "FollowLine"
        self.sensob#Ta inn riktig sensor her etterhvert
        self.treshold = 0.3

    def consider_activation(self):
        for value in self.r_sensob.update():
            if value < self.treshold:
                self.bbcon.activate_bahavior(self)
                self.active_flag = True
                return

        # deactivating
        self.weight = 0
        self.bbcon.deactive_behavior(self)
        self.active_flag = False
        pass

    def consider_deactivation(self):
        self.consider_activation()
        pass
    def update(self):

        self.consider_activation()
        self.sense_and_act()
        self.weight = self.priority * self.match_degree

    def sense_and_act(self):

        self.r_sensob.update()

        if self.r_sensob.get_value()[1] < self.treshold:
            self.motor_recommendations = ["l"]
            self.match_degree = 0.8

        elif self.r_sensob.get_value()[4] < self.treshold:
            self.motor_recommendations = ["r"]
            self.match_degree = 0.8

        else:
            self.motor_recommendations = ["f"]
            self.match_degree = 0.5

        self.priority = 0.5







