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

    def park(self,lid,cid,col:'Columns',cache)->bool:
        pass

    def unpark(self,col:'Columns'):
        pass

class Motorcycle(Vehicle):
    # Write your code here
    def __init__(self):
        super().__init__(VehicleSize.Motorcycle)

    def park(self,lid,cid,col:'Columns', cache):
        if col.get_remaining_motorcycle_parking() > 0:
            cache[self] = [lid,cid]
            col.parking['motorcycle_parking']['motorcycle'].append(self)
            return True
        if col.get_remaining_car_parking() >0:
            cache[self] = [lid, cid]
            col.parking['car_parking']['motorcycle'].append(self)
            return True
        if col.get_remaining_bus_parking()>0:
            cache[self] = [lid, cid]
            col.parking['bus_parking']['motorcycle'].append(self)
            return True
        return False

    def unpark(self,col:'Columns'):
        if self in col.parking['bus_parking']['motorcycle']:
            col.parking['bus_parking']['motorcycle'].remove(self)
            return True

        if self in col.parking['car_parking']['motorcycle']:
            col.parking['car_parking']['motorcycle'].remove(self)
            return True

        if self in col.parking['motorcycle_parking']['motorcycle']:
            col.parking['motorcycle_parking']['motorcycle'].remove(self)
            return True

        return False

class Car(Vehicle):
    # Write your code here
    def __init__(self):
        super().__init__(VehicleSize.Car)

    def park(self,lid,cid,col:'Columns',cache):
        if col.get_remaining_car_parking() > 0:
            cache[self] = [lid, cid]
            col.parking['car_parking']['car'].append(self)
            return True
        if col.get_remaining_bus_parking() > 0:
            cache[self] = [lid, cid]
            col.parking['bus_parking']['car'].append(self)
            return True
        return False

    def unpark(self, col: 'Columns'):
        if self in col.parking['bus_parking']['car']:
            col.parking['bus_parking']['car'].remove(self)
            return True

        if self in col.parking['car_parking']['car']:
            col.parking['car_parking']['car'].remove(self)
            return True

        return False

class Bus(Vehicle):
    # Write your code here
    def __init__(self):
        super().__init__(VehicleSize.Bus)

    def park(self,lid,cid, col: 'Columns',cache):
        if col.get_remaining_bus_parking() >= 5:
            cache[self] = [lid, cid]
            col.parking['bus_parking']['bus'].append(self)
            return True
        return False

    def unpark(self, col: 'Columns'):
        if self in col.parking['bus_parking']['bus']:
            col.parking['bus_parking']['bus'].remove(self)
            return True

        return False

class Columns:
    def __init__(self,cid, lid,k):
        self.cid = cid
        self.lid = lid
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



class Level:
    # Write your code here
    def __init__(self,lid, m, k):
        self.lid = lid
        self.m = m

        self.rows: dict[int, Columns] = {}  # key: row_id, value: dict[size] = # remaining spots
        for cid in range(m):
            self.rows[cid] = Columns(cid,lid,k)

    def park_vehicle(self, lid, vehicle: Vehicle, cache):
        for i in range(self.m):
            if vehicle.park(lid, i,self.rows[i],cache):
                return True
        return False

    def unpark_vehicle(self, vehicle: Vehicle, cid):
        return vehicle.unpark(self.rows[cid])

class ParkingLot:
    # @param {int} n number of leves
    # @param {int} num_rows  each level has num_rows rows of spots
    # @param {int} spots_per_row each row has spots_per_row spots
    def __init__(self, n, num_rows, spots_per_row):
        # Write your code here
        self.n = n
        self.levels: dict[int, Level] = {}
        for lid in range(n):
            self.levels[lid]: Level = Level(lid,num_rows, spots_per_row)

        self.cache = {}


    def park_vehicle(self, vehicle: Vehicle):
        for i in range(self.n):
            if self.levels[i].park_vehicle(i,vehicle,self.cache):
                return True
        return False


    # unPark the vehicle
    def unpark_vehicle(self, vehicle):

        lid,cid = self.cache[vehicle]
        return self.levels[lid].unpark_vehicle(vehicle,cid)





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
