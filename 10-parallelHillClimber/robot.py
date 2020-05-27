
class ROBOT:
    def __init__(self, sim, wts):
        #create new cylinder and capture its ID in a variable
        whiteObject = sim.send_cylinder(x=0, y=0, z=0.6,length=1.0, radius=0.1)
        redObject = sim.send_cylinder(x=0, y=0.5, z=1.1, length=1.0, r=1, g=0, b=0, r1=0,r2=1,r3=0)

        #adds a new joint at x,y,z with normal vec (n1,n2,n3)
        joint = sim.send_hinge_joint(first_body_id=redObject, 
                                second_body_id=whiteObject,
                                x=0, y=0, z=1.1,
                                n1=1, n2=0, n3=0, #magnitude doesn't matter
                                lo=-3.14158/2, hi=3.14158/2) #rotation limits  

        T0 = sim.send_touch_sensor(body_id = whiteObject)
        T1 = sim.send_touch_sensor(body_id = redObject)

        P2 = sim.send_proprioceptive_sensor(joint_id = joint)
        R3 = sim.send_ray_sensor(body_id=redObject, x=0, y=1.1, z = 1.1 , r1=0, r2=1, r3=0)

        #creates sensor neurons, each one connected to one cylinder
        SN0 = sim.send_sensor_neuron( sensor_id=T0 )
        SN1 = sim.send_sensor_neuron( sensor_id=T1 )
        
        SN2 = sim.send_sensor_neuron(sensor_id=P2)
        SN3 = sim.send_sensor_neuron(sensor_id=R3)

        #Only used for fitness computation   
        self.P4 = sim.send_position_sensor( body_id=redObject)

        #create a motor neuron on the joint
        MN2 = sim.send_motor_neuron( joint_id=joint )

        sensorNeurons = {}
        sensorNeurons[0] = SN0
        sensorNeurons[1] = SN1
        sensorNeurons[2] = SN2
        sensorNeurons[3] = SN3

        motorNeurons = {}
        motorNeurons[0] = MN2

        for s in sensorNeurons:
            for m in motorNeurons:  
                sim.send_synapse(source_neuron_id=sensorNeurons[s],target_neuron_id=motorNeurons[m], weight= wts[s])