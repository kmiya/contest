from collections import defaultdict


class UndergroundSystem:
    def __init__(self):
        self.dist = defaultdict(lambda: [])
        self.user = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.user[id] = {'time': t, 'station': stationName}

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        station_in = self.user[id]['station']
        self.dist[(station_in, stationName)].append(t - self.user[id]['time'])

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        times = self.dist[(startStation, endStation)]
        return sum(times) / len(times)


if __name__ == "__main__":
    undergroundSystem = UndergroundSystem()
    undergroundSystem.checkIn(45, "Leyton", 3)
    undergroundSystem.checkIn(32, "Paradise", 8)
    undergroundSystem.checkIn(27, "Leyton", 10)
    undergroundSystem.checkOut(45, "Waterloo", 15)
    undergroundSystem.checkOut(27, "Waterloo", 20)
    undergroundSystem.checkOut(32, "Cambridge", 22)
    print(14, undergroundSystem.getAverageTime("Paradise", "Cambridge"))
    print(11, undergroundSystem.getAverageTime("Leyton", "Waterloo"))
    undergroundSystem.checkIn(10, "Leyton", 24)
    print(11, undergroundSystem.getAverageTime("Leyton", "Waterloo"))
    undergroundSystem.checkOut(10, "Waterloo", 38)
    print(12, undergroundSystem.getAverageTime("Leyton", "Waterloo"))
