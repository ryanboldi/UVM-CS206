import pyrosim
#start the simulation paused, run it for 1000 time steps
sim = pyrosim.Simulator( play_paused=True, eval_time=1000)

#create new cylinder and capture its ID in a variable
whiteObject = sim.send_cylinder(x=0, y=0, z=0.6,length=1.0, radius=0.1)
redObject = sim.send_cylinder(x=0, y=0.5, z=1.1, length=1.0, r=1, g=0, b=0, r1=0,r2=1,r3=0)

#adds a new joint at x,y,z with normal vec (n1,n2,n3)
joint = sim.send_hinge_joint(first_body_id=whiteObject, 
                            second_body_id=redObject,
                            x=0, y=0, z=1.1,
                            n1=1, n2=0, n3=0, #magnitude doesn't matter
                            lo=-3.14158/2, hi=3.14158/2) #rotation limits  

sim.start()
sim.wait_to_finish()