# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
class Vehicle():
    pass

class FlightVehicle(Vehicle):
    pass
#base is Vehicle

class Starship(FlightVehicle):
    pass
#base is FlightVehicle -> Vehicle

class Airplane(FlightVehicle):
    pass
#base is FlightVehicle -> Vehicle

class GroundVehicle(Vehicle):
    pass
#base is Vehicle

class Car(GroundVehicle):
    pass
#base is GroundVehicle -> Vehicle

class Motorcycle(GroundVehicle):
    pass
#base is GroundVehicle -> Vehicle
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class
