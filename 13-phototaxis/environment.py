import constants as c

class ENVIRONMENT:
    def __init__(self, id):
        self.id = id
        
        self.l = c.L
        self.w = c.L
        self.h = c.L

        if (self.id == 0):
            self.Place_Light_Source_To_The_Front()
        if (self.id == 1):
            self.Place_Light_Source_To_The_Right()
        if (self.id == 2):
            self.Place_Light_Source_To_The_Back()
        if (self.id == 3):
            self.Place_Light_Source_To_The_Left()

        print("self.x " + str(self.x) + ", self.y " + str(self.y) + ", self.z " + str(self.z) + ", self.w " + str(self.w) + ", self.l " + str(self.l) + ", self.h " + str(self.h)) 

    def Place_Light_Source_To_The_Front(self):
        self.y = 30 * c.L
        self.x = 0
        self.z = 0

    def Place_Light_Source_To_The_Right(self):
        self.x = 30 * c.L
        self.y = 0
        self.z = 0
    
    def Place_Light_Source_To_The_Back(self):
        self.y = - 30*c.L
        self.x = 0
        self.z = 0
    
    def Place_Light_Source_To_The_Left(self):
        self.x = -30 * c.L
        self.y = 0
        self.z = 0
        
    
    def Send_To(self, sim):
        lightSource = sim.send_box(x=self.x, y=self.y, z = self.z, width = self.w, height = self.h, length = self.l)
        sim.send_light_source(body_id = lightSource)