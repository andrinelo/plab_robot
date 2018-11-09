from behaviour import Behaviour
from camera import Camera
#from imager2 import Imager as IMR
from sensob import *
import imager2 as IMR

class cameraBehaviour(Behaviour):

    def __init__(self, sensobs, bbcon=None,  recommendations=[]):
        self.priority = 0.2
        super().__init__(sensobs, bbcon, recommendations)
        self.sensobs = self.bbcon.sensobs
        self.name = "take picture"
        self.match_degree = 1
        super().weight = 2
        

    def consider_activation(self):
        if self.can_take_picture(): #fix IF-statement
            self.bbcon.activate_behaviour(self)
            self.active_flag = True

    def consider_deactivation(self):
        if not self.can_take_picture(): #fix IF-statement
            self.bbcon.deactivate_behaviour(self)
            print("slettet behaviour inni CB")
            self.active_flag = False
        pass

    def can_take_picture(self):
        #self.sensobs[1].compute_value()
        distance = self.sensobs[1].update()
        print(distance)

        if (distance < 10 and distance > 0):
            return True


    def sense_and_act(self):
        
        if self.can_take_picture():
            self.match_degree = 1
            self.weight = 1
            print("Taking picture now!!")
            img = self.sensobs[0].update()
            img = IMR.Imager(image = img).scale(3, 3)


            #img = IMR(image=self.sensobs[0].get_value(), mode='RGB').scale(3,3)
            img.dump_image('test.jpeg')

            if img.is_black():
                print("picture is black")
                self.motor_recommendations = ['b', 3] #kjorer bakover i 3 sec
                self.priority = 0.9
            else:
                print("picture is bright")
                self.motor_recommendations = ['f', 2] #kjorer forover i 2 sec
                self.priority = 0.2








