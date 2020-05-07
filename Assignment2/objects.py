import pyrosim
#start the simulation paused, run it for 1000 time steps
sim = pyrosim.Simulator( play_paused=True, eval_time=1000)

#create new cylinder and capture its ID in a variable
whiteObject = sim.send_cylinder(x=0, y=0, z=0.6 ,length=1.0, radius=0.1)
redObject = sim.send_cylinder(x=-0.2, y=0, z=0.6)
print(redObject)

sim.start()
sim.wait_to_finish()