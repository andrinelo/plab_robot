from behaviour import Behaviour
from sensob import ReflectanceSensob

class FollowLine(Behaviour):

    def __init__(self, sensobs, bbcon=None, recommendations=[]):
        
        super().__init__(sensobs, bbcon, recommendations)
        self.priority = 0.5
        self.sensobs = self.bbcon.sensobs[2]
        self.name = "FollowLine"
        self.treshold = 0.3
        print(self.sensobs)
        

    def consider_activation(self):
        print("hvilken sensor er det?")
        print(self.sensobs)
        value = self.sensobs.get_value()
        print("Value array med tall fra 0-1 for dark eller light")
        print(value)
        for num in value:
            if num < self.treshold:
                self.bbcon.activate_behaviour(self)
                self.active_flag = True
                return

    def consider_deactivation(self):
        # deactivating
        self.weight = 0
        self.bbcon.deactivate_behaviour(self)
        print("slettet behaviour inni Followline")
        self.active_flag = False
        
    def update(self):

        self.consider_activation()
        self.sense_and_act()
        self.weight = self.priority * self.match_degree

    def sense_and_act(self):

        valueArray = self.sensobs.get_value()
        #problemet er at denne returnerer None
        #finne ut hvorfor

        if valueArray[1] < self.treshold:
            self.motor_recommendations = ["f", 3]
            self.match_degree = 0.8

        elif valueArray[4] < self.treshold:
            self.motor_recommendations = ["r", 1]
            self.match_degree = 0.8

        else:
            self.motor_recommendations = ["f", 1]
            self.match_degree = 0.5








