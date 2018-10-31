from behaviour import Behaviour
from camera import Camera
import imager2 as IMR

class cameraBehaviour(Behaviour):

    def __init__(self, bbcon=None, sensob=[], recommendations=[], priority=0.5):
        Behaviour.__init__(bbcon, sensob, recommendations, priority)
        self.name = "take picture"
        self.can_take_picture = False

    def consider_activation(self):
        if self.can_take_picture: #fix IF-statement
            self.bbcon.activate_behaviour(self)
            self.active_flag = True

    def consider_deactivation(self):
        if not self.can_take_picture: #fix IF-statement
            self.bbcon.deactivate_behaviour(self)
            self.active_flag = False
        pass

    def sense_and_act(self):
        if self.can_take_picture:
            print("Taking picture now!!")
            img = IMR.Imager() #tar et bilde her??
            img.dump_image('/') #aner ikke hva denne gjor?
            self.motor_recommendations = [None] #send en motor rec vi onsker a utfore nar bildet er tatt

        self.priority = 0.9







