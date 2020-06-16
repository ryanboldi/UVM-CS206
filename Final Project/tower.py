import constants as c

class TOWER:
    def __init__(self,sim, y):
        #sends tower to simn
        self.b1 = sim.send_box(x=c.TL/4, y=y, z=c.TL/2, length=c.TW, width=c.TW, height=c.TL, r=0.5, g=0.5, b=0.5, collision_group="tower")
        self.b2 = sim.send_box(x=-c.TL/4, y=y, z=c.TL/2, length=c.TW, width=c.TW, height=c.TL, r=0.5, g=0.5, b=0.5, collision_group="tower")
        self.top = sim.send_box(x = 0, y = y, z=c.TL + (c.TW/2), length = c.TW, width=c.TL,height = c.TW, r=1, g = 0, b= 0, collision_group="tower")

        self.fallSensor = sim.send_position_sensor(body_id = self.top)
        