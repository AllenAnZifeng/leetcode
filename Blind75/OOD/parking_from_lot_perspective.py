# enum type for Vehicle
import enum


class VehicleSize(enum.Enum):
    Motorcycle = 1
    Car = 2
    Bus = 3


class Vehicle:
    # Write your code here
    def __init__(self, size):
        self.size = size


class Motorcycle(Vehicle):
    # Write your code here
    def __init__(self):
        super().__init__(VehicleSize.Motorcycle)


class Car(Vehicle):
    # Write your code here
    def __init__(self):
        super().__init__(VehicleSize.Car)


class Bus(Vehicle):
    # Write your code here
    def __init__(self):
        super().__init__(VehicleSize.Bus)


class Columns:
    def __init__(self, k):
        self.k = k
        self.motorcycle_parking_total = k // 4 - 0
        self.car_parking_total = (k // 4 * 3) - k // 4
        self.bus_parking_total = k - (k // 4 * 3)

        self.parking = {'motorcycle_parking': {'motorcycle': []},
                        'car_parking': {'motorcycle': [], 'car': []},
                        'bus_parking': {'motorcycle': [], 'car': [], 'bus': []},
                        }
        self.debug = False
        # print(f'{self.motorcycle_parking_total=},{self.car_parking_total=},{self.bus_parking_total=}')
    def get_remaining_motorcycle_parking(self):
        return self.motorcycle_parking_total - len(self.parking['motorcycle_parking']['motorcycle'])

    def get_remaining_car_parking(self):
        occupied_car_parking = sum([len(v) for k, v in self.parking['car_parking'].items()])
        return self.car_parking_total - occupied_car_parking

    def get_remaining_bus_parking(self):
        occupied_bus_parking = 0
        for k, v in self.parking['bus_parking'].items():
            for vehicle in v:
                if isinstance(vehicle,Bus):
                    occupied_bus_parking+=5
                else:
                    occupied_bus_parking+=1

        return self.bus_parking_total - occupied_bus_parking

    def park_motorcycle(self,vehicle) -> bool:
        if self.debug:
            print(self.parking)
        if self.get_remaining_motorcycle_parking() > 0:
            self.parking['motorcycle_parking']['motorcycle'].append(vehicle)
            return True

        if self.get_remaining_car_parking() > 0:
            self.parking['car_parking']['motorcycle'].append(vehicle)
            return True

        if self.get_remaining_bus_parking() > 0:
            self.parking['bus_parking']['motorcycle'].append(vehicle)
            return True

        return False

    def unpark_motorcycle(self,vehicle) -> bool:
        if self.debug:
            print(self.parking)
        if vehicle in self.parking['bus_parking']['motorcycle']:
            self.parking['bus_parking']['motorcycle'].remove(vehicle)
            return True

        if vehicle in self.parking['car_parking']['motorcycle']:
            self.parking['car_parking']['motorcycle'].remove(vehicle)
            return True

        if vehicle in self.parking['motorcycle_parking']['motorcycle']:
            self.parking['motorcycle_parking']['motorcycle'].remove(vehicle)
            return True

        return False

    def park_car(self,vehicle) -> bool:
        if self.debug:
            print(self.parking)
        if self.get_remaining_car_parking() > 0:
            self.parking['car_parking']['car'].append(vehicle)
            return True

        if self.get_remaining_bus_parking() > 0:
            self.parking['bus_parking']['car'].append(vehicle)
            return True
        return False

    def unpark_car(self,vehicle) -> bool:
        if self.debug:
            print(self.parking)
        if vehicle in self.parking['bus_parking']['car']:
            self.parking['bus_parking']['car'].remove(vehicle)
            return True

        if vehicle in self.parking['car_parking']['car'] :
            self.parking['car_parking']['car'].remove(vehicle)
            return True

        return False

    def park_bus(self,vehicle) -> bool:
        if self.debug:
            print(self.parking)
        if self.get_remaining_bus_parking() >= 5:
            self.parking['bus_parking']['bus'].append(vehicle)
            return True

        return False

    def unpark_bus(self,vehicle) -> bool:
        if self.debug:
            print(self.parking)
        if vehicle in self.parking['bus_parking']['bus']:
            self.parking['bus_parking']['bus'].remove(vehicle)
            return True

        return False


class Level:
    # Write your code here
    def __init__(self, m, k):
        self.m = m

        self.rows: dict[int, Columns] = {}  # key: row_id, value: dict[size] = # remaining spots
        for i in range(m):
            self.rows[i] = Columns(k)

    def park_motorcycle(self,vehicle):
        for i in range(self.m):
            if self.rows[i].park_motorcycle(vehicle):
                return True
        return False

    def unpark_motorcycle(self,vehicle):
        for i in range(self.m):
            if self.rows[i].unpark_motorcycle(vehicle):
                return True
        return False

    def park_car(self,vehicle):
        for i in range(self.m):
            if self.rows[i].park_car(vehicle):
                return True
        return False

    def unpark_car(self,vehicle):
        for i in range(self.m):
            if self.rows[i].unpark_car(vehicle):
                return True
        return False

    def park_bus(self,vehicle):
        for i in range(self.m):
            if self.rows[i].park_bus(vehicle):
                return True
        return False

    def unpark_bus(self,vehicle):
        for i in range(self.m):
            if self.rows[i].unpark_bus(vehicle):
                return True
        return False


class ParkingLot:
    # @param {int} n number of leves
    # @param {int} num_rows  each level has num_rows rows of spots
    # @param {int} spots_per_row each row has spots_per_row spots
    def __init__(self, n, num_rows, spots_per_row):
        # Write your code here
        self.n = n
        self.levels: dict[int, Level] = {}
        for i in range(n):
            self.levels[i]: Level = Level(num_rows, spots_per_row)

    # Park the vehicle in a spot (or multiple spots)
    # Return false if failed
    def park_vehicle(self, vehicle: Vehicle):
        # Write your code here
        # vehicle = vehicle.split('_')
        # vehicle_type = vehicle[0]
        # if vehicle_type =='Motorcycle':
        if isinstance(vehicle, Motorcycle):
            for i in range(self.n):
                if self.levels[i].park_motorcycle(vehicle):
                    return True
            return False
        # elif vehicle_type =='Car':
        elif isinstance(vehicle, Car):
            for i in range(self.n):
                if self.levels[i].park_car(vehicle):
                    return True
            return False
        else:  # bus
            for i in range(self.n):
                if self.levels[i].park_bus(vehicle):
                    return True
            return False

    # unPark the vehicle
    def unpark_vehicle(self, vehicle):
        # Write your code here
        # vehicle = vehicle.split('_')
        # vehicle_type = vehicle[0]
        # if vehicle_type == 'Motorcycle':
        if isinstance(vehicle, Motorcycle):
            for i in range(self.n):
                if self.levels[i].unpark_motorcycle(vehicle):
                    return True
            return False
        # elif vehicle_type =='Car':
        elif isinstance(vehicle, Car):
            for i in range(self.n):
                if self.levels[i].unpark_car(vehicle):
                    return True
            return False
        else:  # bus
            for i in range(self.n):
                if self.levels[i].unpark_bus(vehicle):
                    return True
            return False



if __name__ == '__main__':


    level = 1
    num_rows = 1
    spots_per_row = 14
    parking_lot = ParkingLot(level, num_rows, spots_per_row)


    def parkVehicle(arg):
        res = parking_lot.park_vehicle(arg)
        print(res)
        return res


    unParkVehicle = parking_lot.unpark_vehicle
    parkVehicle("Motorcycle_1")
    parkVehicle("Motorcycle_2")
    parkVehicle("Motorcycle_3")
    parkVehicle("Car_1")
    parkVehicle("Car_2")
    parkVehicle("Car_3")
    parkVehicle("Motorcycle_4")
    parkVehicle("Car_4")
    parkVehicle("Car_5")
    parkVehicle("Car_6")
    parkVehicle("Car_7")
    parkVehicle("Bus_1")
    unParkVehicle("Car_1")
    unParkVehicle("Motorcycle_4")
    unParkVehicle("Car_3")
    unParkVehicle("Car_6")
    parkVehicle("Bus_1")
    unParkVehicle("Car_7")
    parkVehicle("Bus_1")
