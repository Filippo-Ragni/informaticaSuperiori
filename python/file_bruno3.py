import os
from random import randint

class Entity: 
  def __init__(self, x, y, field):
    self.x = x
    self.y = y
    self.field = field
    self.field.entities.append(self)

  def move(self, direction):
    futureX = self.x
    futureY = self.y

    if direction == "up" and self.y > 0:
      futureY -= 1
    elif direction == "down" and self.y < self.field.h - 1:
      futureY += 1
    elif direction == "left" and self.x > 0:
      futureX -= 1
    elif direction == "right" and self.x < self.field.w - 1:
      futureX += 1

    e = self.field.get_entity_at_coords(futureX, futureY)

    if e == None:
      self.x = futureX
      self.y = futureY
    elif e != self:
      self.collide(e)

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
        self.field.entities.remove(enemy)
      else:
        enemy.hp -= self.damage
  
  def collide(self, entity):
    self.attack(entity)

class Field:
  def __init__(self):
    self.w = 5
    self.h = 5
    self.entities = []

  def get_entity_at_coords(self, x, y):
    for e in self.entities:
      if e.x == x and e.y == y:
        return e

    return None
    
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
p = Monster(0, 0, "Player", 4, field)

def clear_screen():
  if os.name == "nt":
    os.system("cls")
  else:
    os.system("clear")
    
clear_screen()
while True: 
  if p.hp <= 0:
    print("hai perso")
    break

  m = randint(0, 4)

  casual_m = field.entities[randint(0, len(field.entities) - 1)]
  while casual_m == p:
    casual_m = field.entities[randint(0, len(field.entities) - 1)]
  if m == 0:
    casual_m.move("up")
  elif m == 1:
    casual_m.move("right")
  elif m == 2:
    casual_m.move("down")
  elif m == 3:
    casual_m.move("left")

  for e in field.entities:
    if e.hp <= 0:
      field.entities.remove(e)
  field.draw()

  command = input("input: ").lower()
  clear_screen()

  if command == "q": break
  elif command == "w": p.move("up")
  elif command == "a": p.move("left")
  elif command == "s": p.move("down")
  elif command == "d": p.move("right")
