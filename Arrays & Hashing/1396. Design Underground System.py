# An underground railway system is keeping track of customer travel times between different stations. They are using this data to calculate the average time it takes to travel from one station to another.

# Implement the UndergroundSystem class:

# void checkIn(int id, string stationName, int t)
# A customer with a card ID equal to id, checks in at the station stationName at time t.
# A customer can only be checked into one place at a time.
# void checkOut(int id, string stationName, int t)
# A customer with a card ID equal to id, checks out from the station stationName at time t.
# double getAverageTime(string startStation, string endStation)
# Returns the average time it takes to travel from startStation to endStation.
# The average time is computed from all the previous traveling times from startStation to endStation
# that happened directly, meaning a check in at startStation followed by a check out from endStation.
# The time it takes to travel from startStation to endStation may be different from the time it takes to 
# travel from endStation to startStation. There will be at least one customer that has traveled from 
# startStation to endStation before getAverageTime is called. You may assume all calls to the checkIn 
# and checkOut methods are consistent. If a customer checks in at time t1 then checks out at time t2, then t1 < t2. All events happen in chronological order.

 

# Example 1:

# Input
# ["UndergroundSystem","checkIn","checkIn","checkIn","checkOut","checkOut","checkOut",
#  "getAverageTime","getAverageTime","checkIn","getAverageTime","checkOut","getAverageTime"]
# [[],[45,"Leyton",3],[32,"Paradise",8],[27,"Leyton",10],[45,"Waterloo",15],[27,"Waterloo",20],
#  [32,"Cambridge",22],["Paradise","Cambridge"],["Leyton","Waterloo"],[10,"Leyton",24],["Leyton","Waterloo"],
#  [10,"Waterloo",38],["Leyton","Waterloo"]]

# Output
# [null,null,null,null,null,null,null,14.00000,11.00000,null,11.00000,null,12.00000]

class UndergroundSystem:

    def __init__(self):
        self.cin = {}  
        self.trips = {}  

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.cin[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.cin.pop(id)  
        route = (startStation, stationName)
        travelTime = t - startTime

        if route not in self.trips:
            self.trips[route] = [0, 0] 
        self.trips[route][0] += travelTime
        self.trips[route][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time, count = self.trips[(startStation, endStation)]
        return total_time / count
    
undergroundSystem = UndergroundSystem()
undergroundSystem.checkIn(10, "Leyton", 3)
undergroundSystem.checkOut(10, "Paradise", 8)
print(undergroundSystem.getAverageTime("Leyton", "Paradise"))
undergroundSystem.checkIn(5, "Leyton", 10)
undergroundSystem.checkOut(5, "Paradise", 16)
print(undergroundSystem.getAverageTime("Leyton", "Paradise"))
undergroundSystem.checkIn(2, "Leyton", 21)
undergroundSystem.checkOut(2, "Paradise", 30)
print(undergroundSystem.getAverageTime("Leyton", "Paradise"))