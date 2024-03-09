from typing import List


class Direction:
    UP = 'UP'
    DOWN = 'DOWN'


class Status:
    UP = 'UP'
    DOWN = 'DOWN'
    IDLE = 'IDLE'


class Request:
    def __init__(self, l=0):
        self.level = l

    def getLevel(self):
        return self.level


class ElevatorButton:
    def __init__(self, level, e):
        self.level = level
        self.elevator = e

    def pressButton(self):
        request = InternalRequest(self.level)
        self.elevator.handleInternalRequest(request)


class ExternalRequest(Request):
    def __init__(self, l=0, d=None):
        Request.__init__(self, l)
        self.direction = d

    def getDirection(self):
        return self.direction


class InternalRequest(Request):
    def __init__(self, l=None):
        Request.__init__(self, l)


class Elevator:
    def __init__(self, n):
        # Keep them, don't modify.
        self.n = n
        self.upStops = []
        self.downStops = []
        for i in range(n):
            self.upStops.append(False)
            self.downStops.append(False)
        self.currLevel = 0
        self.status = Status.IDLE

    def insertButton(self, eb):
        return

    def handleExternalRequest(self, r: ExternalRequest):
        if self.status == Status.IDLE:
            if r.direction == 'DOWN':
                self.status = Status.DOWN
            else:
                self.status = Status.UP

        if r.direction == 'DOWN':
            self.downStops[r.level - 1] = True
        else:
            self.upStops[r.level - 1] = True

        print(f'handleExternalRequest {r.direction=} {r.level=}')
        self.elevatorStatusDescription()

    # Write your code here

    def handleInternalRequest(self, r):
        if self.status == Status.DOWN:
            self.downStops[r.level - 1] = True
        else:
            self.upStops[r.level - 1] = True

        # Write your code here
        self.elevatorStatusDescription()

    def find_highest_floor(self, arr: List[bool]) -> int:
        floor = -1
        for i in range(len(arr)):
            if arr[i]:
                floor = i
        return floor

    def find_lowest_floor(self, arr: List[bool]) -> int:
        floor = -1
        for i in range(len(arr) - 1, -1, -1):
            if arr[i]:
                floor = i
        return floor

    def openGate(self):

        if self.status == Status.DOWN:  # must have true in down
            if self.currLevel == 0:  # go to highest floor
                self.currLevel = self.find_highest_floor(self.downStops)
                self.downStops[self.currLevel] = False
            else:  # go down from cur level
                floor = self.find_highest_floor(
                    self.downStops[:self.currLevel + 1] + [False] * (self.n - self.currLevel - 1))
                if floor == -1:
                    self.currLevel = self.find_highest_floor(self.downStops)
                else:
                    self.currLevel = floor

                self.downStops[self.currLevel] = False
        elif self.status == Status.UP:  # up
            if self.currLevel == self.n - 1:  # go to lowest floor
                self.currLevel = self.find_lowest_floor(self.upStops)
                self.upStops[self.currLevel] = False
            else:  # go up from cur level
                floor = self.find_lowest_floor([False] * self.currLevel + self.upStops[self.currLevel:])
                if floor == -1:
                    self.currLevel = self.find_lowest_floor(self.upStops)
                else:
                    self.currLevel = floor
                self.upStops[self.currLevel] = False
        else:  # idle
            pass
        print('openGate')
        self.elevatorStatusDescription()

    # Write your code here

    def closeGate(self):

        if self.noRequests(self.upStops + self.downStops):
            self.status = Status.IDLE
            return

        if self.status == Status.DOWN:
            if self.find_highest_floor(self.downStops[:self.currLevel + 1]) == -1:
                if True in self.upStops:
                    self.status = Status.UP

        else:
            if self.find_lowest_floor(self.upStops[self.currLevel:]) == -1:
                if True in self.downStops:
                    self.status = Status.DOWN
        print('closeGate')
        self.elevatorStatusDescription()

    # Write your code here

    def noRequests(self, stops):
        for stop in stops:
            if stop:
                return False
        return True

    def elevatorStatusDescription(self):
        description = "Currently elevator status is : " + self.status + \
                      ".\nCurrent level is at: " + str(self.currLevel + 1) + \
                      ".\nup stop list looks like: " + self.toString(self.upStops) + \
                      ".\ndown stop list looks like:  " + self.toString(self.downStops) + \
                      ".\n*****************************************\n"
        print(description)

    @classmethod
    def toString(cls, stops):
        return str(stops).replace("False", "false").replace("True", "true")


if __name__ == '__main__':
    ele = Elevator(10)
    ele.handleExternalRequest(ExternalRequest(1, "UP"))
    ele.handleExternalRequest(ExternalRequest(5, "UP"))
    ele.handleExternalRequest(ExternalRequest(4, "DOWN"))
    ele.handleExternalRequest(ExternalRequest(7, "DOWN"))
    ele.handleExternalRequest(ExternalRequest(4, "DOWN"))
    ele.handleExternalRequest(ExternalRequest(7, "DOWN"))
    ele.handleExternalRequest(ExternalRequest(4, "DOWN"))
    ele.handleExternalRequest(ExternalRequest(7, "DOWN"))

    ele.openGate()
    ele.closeGate()
    ele.openGate()
    ele.closeGate()
    ele.openGate()
    ele.closeGate()
    ele.openGate()
    ele.closeGate()
    ele.openGate()
    ele.closeGate()
    ele.openGate()
    ele.closeGate()
    ele.openGate()
    ele.closeGate()
    ele.openGate()
    ele.closeGate()
