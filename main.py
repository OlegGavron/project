class Human:
  def __init__(self, name):
    self.name = name

class Auto:
  def __init__(self, brand):
    self.brand = brand
    self.passengers = []
  def add_passenger(self, human):
    self.passengers.append(human)

  def print_passengers(self):
    if self.passengers != []:
      print(f"В машині {self.brand} такі пасажири:")
      for passenger in self.passengers:
        print(passenger.name)
    else:
      print(f"В машині {self.brand} немає пасажирів. Всі втікли!")

car = Auto('Nissan GTR')
car.add_passenger(Human("Oleg"))
car.add_passenger(Human("Igor"))
car.add_passenger(Human("Vlad"))
car.add_passenger(Human("Valentyn"))
car.print_passengers()

input("How many passangers you going to place in car?:")
passangers = 5
print("If you wrote 5:I Not much place in car")
passengers = 4
print("If you wrote 4:Car is full now")
passengers = 3
print("If you wrote 3:Cool")
passengers = 2
print("If you wrote 2:Only passanger and driver")
passengers = 1
print("If you wrote 1:Only driver")