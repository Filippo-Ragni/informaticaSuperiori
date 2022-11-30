class Entity: 
  def __init__(self, x, y, field):
    self.x = x
    self.y = y
    self.field = field
    self.field.entities.append(self)
    self.collision = False

  def move(self, direction):
    p_x = self.x
    p_y = self.y
    
    if direction == "up" and self.y > 0:
      self.y -= 1
    elif direction == "down" and self.y < self.field.h - 1:
      self.y += 1
    elif direction == "left" and self.x > 0:
      self.x -= 1
    elif direction == "right" and self.x < self.field.w - 1:
      self.x += 1

    self.check_collision()
    
    if self.x == p_x and self.y == p_y:
      print("l'entità non può uscire dal campo")
    elif self.collision == True:
      self.x = p_x
      self.y = p_y
      print("l'entità non può essere sovrapposta ad un'altra")


  def check_collision(self):
    self.collision = False
    for e in self.field.entities:
      if self.x == e.x and self.y == e.y and self.name != e.name:
        self.collision = True


class Monster(Entity):
  def __init__(self, x, y, name, damage, field):
    super().__init__(x, y, field)
    self.name = name
    self.hp = 10
    self.damage = damage


  def info(self):
    print("sono", self.name, "hp:", self.hp, "/10", "e mi trovo a", self.x, ",", self.y)


  def attack(self, enemy):
    if self.hp <= 0:
      print(self.name, "prova ad attaccare da morto con scarsi risultati")
    else: 
      print(self.name, "attacca", enemy.name)

      if (enemy.hp <= 0):
        print(enemy.name, "e' morto")
      else:
        enemy.hp -= self.damage


class Field:
  def __init__(self):
    self.w = 5
    self.h = 5
    self.entities = []


  def draw(self):
    for y in range(self.h):
      for x in range(self.w):
        for e in self.entities:
          if x == e.x and y == e.y:
            print("[x]", end = "")
            break    
        else:
          print("[ ]", end = "")
      print()


field = Field()
m1 = Monster(2, 2, "Pino", 10, field)
m2 = Monster(1, 1, "Gino", 10, field)

field.draw()
print()

for i in range(2):
  m1.move("right")
  field.draw()
  print()

for i in range(1):
  m1.move("up")
  field.draw()
  print()

for i in range(4):
  m1.move("left")
  field.draw()
  print()

for i in range(5):
  m1.move("down")
  field.draw()
  print()
