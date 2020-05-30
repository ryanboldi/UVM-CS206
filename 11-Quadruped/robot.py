import constants as c
import math


class ROBOT:
    def __init__(self, sim, wts):
        self.send_objects(sim)
        self.send_joints(sim)
        self.send_sensors(sim)
        self.send_neurons(sim)
        #self.send_synapses(sim, wts)
        

    def send_objects(self, sim):
        #create new cylinder and capture its ID in a variable
        #self.whiteObject = sim.send_cylinder(x=0, y=0, z=0.6,length=1.0, radius=0.1)
        #self.redObject = sim.send_cylinder(x=0, y=0.5, z=1.1, length=1.0, r=1, g=0, b=0, r1=0,r2=1,r3=0)
        self.O0 = sim.send_box(x=0, y=0, z=c.L + c.R, length=c.L, width=c.L, height=2 * c.R, r=0.5, g=0.5, b=0.5)
        self.O1 = sim.send_cylinder(x=0 ,y=c.L, z=c.L + c.R, length= c.L, radius = c.R, r1=0, r2=1, r3=0, r=1, g=0, b=0)
        self.O2 = sim.send_cylinder(x=c.L, y=0, z=c.L+c.R, length=c.L, radius = c.R, r1=1, r2=0, r3=0, r=0, g=1, b=0)
        self.O3 = sim.send_cylinder(x=0, y=-c.L, z = c.L + c.R, length=c.L, radius=c.R, r1=0, r2=-1, r3=0, r=0, g=0, b=1)
        self.O4 = sim.send_cylinder(x=-c.L, y=0, z = c.L + c.R, length=c.L, radius=c.R, r1=-1, r2=0, r3=0, r=1, g=0, b=1)
        self.O5 = sim.send_cylinder(x=0, y=1.5*c.L, z = (c.L/2) + c.R, length=c.L, radius=c.R, r1=0, r2=0, r3=1, r=1, g=0, b=0)
        self.O6 = sim.send_cylinder(x=1.5*c.L, y=0, z = (c.L/2) + c.R, length=c.L, radius=c.R, r1=0, r2=0, r3=1, r=0, g=1, b=0)
        self.O7 = sim.send_cylinder(x=0, y=-1.5*c.L, z = (c.L/2) + c.R, length=c.L, radius=c.R, r1=0, r2=0, r3=1, r=0, g=0, b=1)
        self.O8 = sim.send_cylinder(x=-1.5*c.L, y=0, z = (c.L/2) + c.R, length=c.L, radius=c.R, r1=0, r2=0, r3=1, r=1, g=0, b=1)



    def send_joints(self,sim):
        #adds a new joint at x,y,z swith normal vec (n1,n2,n3)
        self.J0 = sim.send_hinge_joint(first_body_id=self.O0, second_body_id=self.O1,x=0, y=c.L/2, z=c.L + c.R,n1=-1, n2=0, n3=0, hi=math.pi /2, lo=-math.pi/2)
        self.J1 = sim.send_hinge_joint(first_body_id=self.O1, second_body_id=self.O5,x=0, y=1.5* c.L, z=c.L + c.R,n1=-1, n2=0, n3=0, hi=math.pi /2, lo=-math.pi/2)
        self.J2 = sim.send_hinge_joint(first_body_id=self.O0, second_body_id=self.O2,x=c.L/2, y=0, z=c.L + c.R,n1=0, n2=1, n3=0, hi=math.pi /2, lo=-math.pi/2)
        self.J3 = sim.send_hinge_joint(first_body_id=self.O2, second_body_id=self.O6,x=1.5 * c.L, y=0, z=c.L + c.R,n1=0, n2=1, n3=0, hi=math.pi /2, lo=-math.pi/2)
        self.J4 = sim.send_hinge_joint(first_body_id=self.O0, second_body_id=self.O3,x=0, y=-c.L/2, z=c.L + c.R,n1=1, n2=0, n3=0, hi=math.pi /2, lo=-math.pi/2)
        self.J5 = sim.send_hinge_joint(first_body_id=self.O3, second_body_id=self.O7,x=0, y=-1.5*c.L, z=c.L + c.R,n1=1, n2=0, n3=0, hi=math.pi /2, lo=-math.pi/2)
        self.J6 = sim.send_hinge_joint(first_body_id=self.O0, second_body_id=self.O4,x=-c.L/2, y=0, z=c.L + c.R,n1=0, n2=-1, n3=0, hi=math.pi /2, lo=-math.pi/2)
        self.J6 = sim.send_hinge_joint(first_body_id=self.O4, second_body_id=self.O8,x=-1.5*c.L, y=0, z=c.L + c.R,n1=0, n2=-1, n3=0, hi=math.pi /2, lo=-math.pi/2)


    def send_sensors(self, sim):
        self.T0 = sim.send_touch_sensor(body_id = self.O5)
        self.T1 = sim.send_touch_sensor(body_id = self.O6)
        self.T2 = sim.send_touch_sensor(body_id = self.O7)
        self.T3 = sim.send_touch_sensor(body_id = self.O8)

        #Only used for fitness computation   
        #self.P4 = sim.send_position_sensor( body_id=self.redObject)

    def send_neurons(self, sim):
         #creates sensor neurons, each one connected to one cylinder
        #self.SN0 = sim.send_sensor_neuron( sensor_id=self.T0 )
        #self.SN1 = sim.send_sensor_neuron( sensor_id=self.T1 )
        
        #self.SN2 = sim.send_sensor_neuron(sensor_id=self.P2)
        #self.SN3 = sim.send_sensor_neuron(sensor_id=self.R3)

        #create a motor neuron on the joint
        #self.MN2 = sim.send_motor_neuron( joint_id=self.joint )


    def send_synapses(self, sim, wts):
        sensorNeurons = {}
        sensorNeurons[0] = self.SN0
        sensorNeurons[1] = self.SN1
        sensorNeurons[2] = self.SN2
        sensorNeurons[3] = self.SN3

        motorNeurons = {}
        motorNeurons[0] = self.MN2

        for s in sensorNeurons:
            for m in motorNeurons:  
                sim.send_synapse(source_neuron_id=sensorNeurons[s],target_neuron_id=motorNeurons[m], weight= wts[s])