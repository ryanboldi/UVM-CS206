import constants as c
import math
import random


class ROBOT:
    def __init__(self, sim, wts):
        self.send_objects(sim)
        self.send_joints(sim)
        self.send_sensors(sim)
        self.send_neurons(sim)
        self.send_synapses(sim, wts)


        # delete these so they're not copied with copy.deepcopy()
        del self.O
        del self.J
        del self.S
        del self.SN
        del self.MN
        

    def send_objects(self, sim):
        #create new cylinder and capture its ID in a variable
        #self.whiteObject = sim.send_cylinder(x=0, y=0, z=0.6,length=1.0, radius=0.1)
        #self.redObject = sim.send_cylinder(x=0, y=0.5, z=1.1, length=1.0, r=1, g=0, b=0, r1=0,r2=1,r3=0)
        self.O0 = sim.send_box(x=0, y=0, z=c.L + c.R, length=c.L, width=c.L, height=2 * c.R, r=0.5, g=0.5, b=0.5)
        self.O1 = sim.send_cylinder(x=0 ,y=c.L, z=c.L + c.R, length= c.L, radius = c.R, r1=0, r2=1, r3=0, r=1, g=0, b=0)
        self.O2 = sim.send_cylinder(x=c.L, y=0, z=c.L + c.R, length=c.L, radius = c.R, r1=1, r2=0, r3=0, r=0, g=1, b=0)
        self.O3 = sim.send_cylinder(x=0, y=-c.L, z = c.L + c.R, length=c.L, radius=c.R, r1=0, r2=-1, r3=0, r=0, g=0, b=1)
        self.O4 = sim.send_cylinder(x=-c.L, y=0, z = c.L + c.R, length=c.L, radius=c.R, r1=-1, r2=0, r3=0, r=1, g=0, b=1)
        self.O5 = sim.send_cylinder(x=0, y=1.5*c.L, z = (c.L/2) + c.R, length=c.L, radius=c.R, r1=0, r2=0, r3=1, r=1, g=0, b=0)
        self.O6 = sim.send_cylinder(x=1.5*c.L, y=0, z = (c.L/2) + c.R, length=c.L, radius=c.R, r1=0, r2=0, r3=1, r=0, g=1, b=0)
        self.O7 = sim.send_cylinder(x=0, y=-1.5*c.L, z = (c.L/2) + c.R, length=c.L, radius=c.R, r1=0, r2=0, r3=1, r=0, g=0, b=1)
        self.O8 = sim.send_cylinder(x=-1.5*c.L, y=0, z = (c.L/2) + c.R, length=c.L, radius=c.R, r1=0, r2=0, r3=1, r=1, g=0, b=1)
        
        #ARMS 
        self.O9 = sim.send_cylinder(x = (c.L/3), y = 0, z = (c.L  + 2 * (c.R) + c.A/2), length=c.A, radius=c.aR, r=1, g=1, b=0)
        self.O10 = sim.send_cylinder(x = -(c.L/3), y = 0, z = (c.L + 2 * (c.R) + c.A/2), length=c.A, radius=c.aR, r=1, g=1, b=0)

        self.O11 = sim.send_cylinder(x = (c.L/3), y = c.A/2, z = (c.L * (1) + 2 * (c.R) + c.A), length=c.A, radius=c.aR, r1= 0, r2 =1, r3 = 0, r=0, g=1, b=1)
        self.O12 = sim.send_cylinder(x = -(c.L/3), y = c.A/2, z = (c.L * (1) + 2 * (c.R) + c.A), length=c.A, radius=c.aR, r1= 0, r2 =1, r3 = 0, r=0, g=1, b=1)

        self.O = {} #dict of all objects    
        self.O[0] = self.O0
        self.O[1] = self.O1
        self.O[2] = self.O2
        self.O[3] = self.O3
        self.O[4] = self.O4
        self.O[5] = self.O5
        self.O[6] = self.O6
        self.O[7] = self.O7
        self.O[8] = self.O8
        self.O[9] = self.O9
        self.O[10] = self.O10
        self.O[11] = self.O11
        self.O[12] = self.O12
        


    def send_joints(self,sim):
        #adds a new joint at x,y,z swith normal vec (n1,n2,n3)
        self.J0 = sim.send_hinge_joint(first_body_id=self.O0, second_body_id=self.O1,x=0, y=c.L/2, z=c.L + c.R,n1=-1, n2=0, n3=0, hi=math.pi /2, lo=-math.pi/2)
        self.J1 = sim.send_hinge_joint(first_body_id=self.O1, second_body_id=self.O5,x=0, y=1.5* c.L, z=c.L + c.R,n1=-1, n2=0, n3=0, hi=math.pi /2, lo=-math.pi/2)
        self.J2 = sim.send_hinge_joint(first_body_id=self.O0, second_body_id=self.O2,x=c.L/2, y=0, z=c.L + c.R,n1=0, n2=1, n3=0, hi=math.pi /2, lo=-math.pi/2)
        self.J3 = sim.send_hinge_joint(first_body_id=self.O2, second_body_id=self.O6,x=1.5 * c.L, y=0, z=c.L + c.R,n1=0, n2=1, n3=0, hi=math.pi /2, lo=-math.pi/2)
        self.J4 = sim.send_hinge_joint(first_body_id=self.O0, second_body_id=self.O3,x=0, y=-c.L/2, z=c.L + c.R,n1=1, n2=0, n3=0, hi=math.pi /2, lo=-math.pi/2)
        self.J5 = sim.send_hinge_joint(first_body_id=self.O3, second_body_id=self.O7,x=0, y=-1.5*c.L, z=c.L + c.R,n1=1, n2=0, n3=0, hi=math.pi /2, lo=-math.pi/2)
        self.J6 = sim.send_hinge_joint(first_body_id=self.O0, second_body_id=self.O4,x=-c.L/2, y=0, z=c.L + c.R,n1=0, n2=-1, n3=0, hi=math.pi /2, lo=-math.pi/2)
        self.J7 = sim.send_hinge_joint(first_body_id=self.O4, second_body_id=self.O8,x=-1.5*c.L, y=0, z=c.L + c.R,n1=0, n2=-1, n3=0, hi=math.pi /2, lo=-math.pi/2)

        #shoulder joints
        self.J8 = sim.send_hinge_joint(first_body_id=self.O0, second_body_id=self.O9, x=(c.L/3), y = 0, z = (c.L * (1) + 2 * (c.R)), n1= 0, n2 = 1, n3 = 0)
        self.J9 = sim.send_hinge_joint(first_body_id=self.O0, second_body_id=self.O10, x=-(c.L/3), y = 0, z = (c.L * (1) + 2 * (c.R)), n1= 0, n2 = 1, n3 = 0)

        #elbow joints
        self.J10 = sim.send_hinge_joint(first_body_id=self.O9, second_body_id=self.O11, x = (c.L/3), y = 0, z = (c.L * (2) + 3.5 * (c.R)), n1= 1, n2 = 0, n3 = 0)
        self.J11 = sim.send_hinge_joint(first_body_id=self.O10, second_body_id=self.O12, x = -(c.L/3), y = 0, z = (c.L * (2) + 3.5 * (c.R)), n1= 1, n2 = 0, n3 = 0)

        self.J = {}
        self.J[0] = self.J0
        self.J[1] = self.J1
        self.J[2] = self.J2
        self.J[3] = self.J3
        self.J[4] = self.J4
        self.J[5] = self.J5
        self.J[6] = self.J6
        self.J[7] = self.J7
        self.J[8] = self.J8
        self.J[9] = self.J9
        self.J[10] = self.J10
        self.J[11] = self.J11



    def send_sensors(self, sim):
        self.T0 = sim.send_touch_sensor(body_id = self.O5)
        self.T1 = sim.send_touch_sensor(body_id = self.O6)
        self.T2 = sim.send_touch_sensor(body_id = self.O7)
        self.T3 = sim.send_touch_sensor(body_id = self.O8)

        self.T4 = sim.send_touch_sensor(body_id = self.O11)
        self.T5 = sim.send_touch_sensor(body_id= self.O12)

        self.S = {}
        self.S[0] = self.T0
        self.S[1] = self.T1
        self.S[2] = self.T2
        self.S[3] = self.T3
        self.S[4] = self.T4 
        self.S[5] = self.T5


        #Only used for fitness computation   
        self.P4 = sim.send_position_sensor( body_id=self.O0)

    def send_neurons(self, sim):
        self.SN = {}

        for s in self.S:
            self.SN[s] = sim.send_sensor_neuron(sensor_id=self.S[s])
        
        self.MN = {}

        for j in self.J:
            self.MN[j] = sim.send_motor_neuron(joint_id=self.J[j], tau=0.3)

         #creates sensor neurons, each one connected to one cylinder
        #self.SN0 = sim.send_sensor_neuron( sensor_id=self.T0 )
        #self.SN1 = sim.send_sensor_neuron( sensor_id=self.T1 )
        
        #self.SN2 = sim.send_sensor_neuron(sensor_id=self.P2)
        #self.SN3 = sim.send_sensor_neuron(sensor_id=self.R3)

        #create a motor neuron on the joint
        #self.MN2 = sim.send_motor_neuron( joint_id=self.joint )


    def send_synapses(self, sim, wts):
        for j in self.SN:
            for i in self.MN:
                sim.send_synapse(source_neuron_id=self.SN[j], target_neuron_id=self.MN[i], weight=wts[i][j])