
# Car class를 상속받아서 Truck class를 정의하라.
# 적재량을 관리하는 loadage 변수를 정의하라.
# ‘load’를 화면에 인쇄하는 load 메쏘드를 정의하라.
# ‘unload’를 화면에 인쇄하는 unload 메쏘드를 정의하라.

class Vehicle:
    def __init__(self, speed):
        self.speed = speed
    def speed_up(self):
        self.speed += 10
    def speed_dn(self):
        self.speed -= 10

class Car(Vehicle):
    def __init__(self, speed, wheels, seats):
        Vehicle.__init__(self, speed)
        self.wheels = wheels
        self.seats = seats
    def info(self):
        print(self.speed, self.wheels, self.seats)

class Truck(Car):
    def __init__(self, speed, wheels, seats, loadage):
        Car.__init__(self, speed, wheels, seats)
        self.loadage = loadage
    def load(self):
        print('load')
    def unload(self):
        print('unload')
    def info(self):
        print(self.speed, self.wheels, self.seats, self.loadage)

truck = Truck(100, 6, 2, 30)
truck.load()
truck.unload()
truck.info()

truck.speed_dn()
truck.info()
truck.speed_up()
truck.info()
