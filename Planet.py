class Planet:
  def __init__(self,name,radius):
    self.name = name
    self.planets = []

  def add_planets(self,_planets):
    self.planets.append(_planets)

  def show_planets(self):
    for x in self.planets:
      print(x)

  '''
    self.radius = radius


  def get_name(self):
    return self.name

  def get_radius(self):
    return self.radius
  
  def set_name(self,newname):
    self.name = newname
  
  def __str__(self):
    msg = ''
    msg += f'hi, Im {self.name}'
    return msg
    '''

Planet1 = Planet('X25',10)
Planet2 = Planet('Z37',9)

print(Planet1.get_name())
print(Planet1.get_radius())



