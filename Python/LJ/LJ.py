class particle: # Generates particle for simulation
    def __init__(self,name,initial_position,initial_velocity,epsilon=10,sigma=0.1,mass=1):
        self.name=name
        self.positions=[tuple(initial_position)]
        self.velocities=[tuple(initial_velocity)]
        self.epsilon=epsilon  # dispersion energy
        self.sigma=sigma      # particle size
        self.mass=mass
    def other_particles(self,others):
        self.others = list(others)
        self.others.remove(self)
    def update(self,time_step): 
        self.forces = []
        for p in self.others:
            self.r = tuple(self.positions[-1][_]-p.positions[-1][_]
                            for _ in range(3))
            self.r_magnitude = (self.r[0]**2+self.r[1]**2+self.r[2]**2)**0.5
            if self.r_magnitude/self.epsilon<2.5:
                  self.r_unit = tuple(_/self.r_magnitude for _ in self.r)
            else: self.r_unit = (0,0,0) # ignoring negligible long range effects 
            self.forces.append(tuple(_*(24*self.epsilon/self.r_magnitude)
                                          *((self.sigma/self.r_magnitude)**6
                                         -2*(self.sigma/self.r_magnitude)**12)
                                             for _ in self.r_unit)) # force = gradient(potential)
        self.acceleration = tuple(sum(_)/self.mass for _ in  zip(*self.forces))
        self.velocities.append(tuple(self.acceleration[_]*time_step+self.velocities[-1][_] 
                                     for _ in range(3)))
        self.positions.append(tuple(0.5*self.acceleration[_]*time_step**2+self.velocities[-1][_]*time_step+self.positions[-1][_] 
                                    for _ in range(3)))
    def __str__(self):
        return f'{self.name}({self.positions[-1]},{self.velocities[-1]})'

def simulation(particles,time_step,duration): # updates particle properties
    for p in particles: p.other_particles(particles)
    while(duration>0):
        for p in particles: p.update(time_step)
        duration-=time_step