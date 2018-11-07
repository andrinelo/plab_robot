from behaviour import Behaviour
from sensob import ReflectanceSensob

class FollowLine(Behaviour):

    def __init__(self, sensobs, bbcon=None, recommendations=[]):
        self.priority = 0.5

        Behaviour.__init__(self, sensobs, bbcon, recommendations)
        self.name = "FollowLine"
        self.treshold = 0.3
        

    def consider_activation(self):
        print("hvilken sensor er det?")
        print(self.sensobs[0])
        value = self.sensobs[0].update()
        print("Value array med tall fra 0-1 for dark eller light")
        print(value)
        for num in value:
            if num < self.treshold:
                self.bbcon.activate_behavior(self)
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

        valueArray = self.sensobs[0].update()
        #problemet er at denne returnerer None
        #finne ut hvorfor

        if valueArray[1] < self.treshold:
            self.motor_recommendations = ["l"]
            self.match_degree = 0.8

        elif valueArray[4] < self.treshold:
            self.motor_recommendations = ["r"]
            self.match_degree = 0.8

        else:
            self.motor_recommendations = ["f"]
            self.match_degree = 0.5








