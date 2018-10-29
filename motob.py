class Motob:

    def __init__(self):
        self.motors = [] #list of all motors whose values it sets
        self.value = None #most recent motor recommendation sent to the motob.

    def update(self):
        #load new motor recommendation into the value slot and operationalize it.
        pass

    def operationalize(self):
        #convert value into motor settings and send to the corresponding motor(s).
        pass

    