import csv
import math

Cars = {
    "COMPACT": 0.02,
    "SUV": 0.06,
    "SEDAN": 0.04,
    "SPORTS": 0.08
}

Regions = {
    "LEINSTER": 0.08,
    "MUNSTER": 0.06,
    "ULSTER": 0.04,
    "CONNACHT": 0.02
}

BaseRates = {
    "TP": 200,
    "TPFT": 300,
    "CI": 600
}

def calculateInsurance(Age, Model, Region, Package, Garage, PenaltyPoints, Mileage, DrivingExperience):
    Rates = []
    Rates.append(BaseRates[Package] * Cars[Model])
    Rates.append(BaseRates[Package] * Regions[Region])
    
    
    #Age
    if Age > 25 and Age < 65:
        Rates.append(BaseRates[Package] * 0.04)
    elif Age > 65:
        Rates.append(BaseRates[Package] * 0.02)
    else:
        Rates.append(BaseRates[Package] * 0.08)
    
    #Garage
    if Garage == "N":
        Rates.append(BaseRates[Package] * 0.03)
    
    #PenaltyPoints
    Rates.append(BaseRates[Package] * (0.03 * PenaltyPoints))
    
    #Mileage
    Rates.append(BaseRates[Package] * (0.1 * (math.ceil(Mileage / 1000))))
    
    #Driving Experience
    if DrivingExperience >= 3:
        x = round(DrivingExperience / 3)
        rate = 0.15 - (0.025 * x)
        Rates.append(BaseRates[Package] * rate)

    return(f"€{sum(Rates) + BaseRates[Package]}")

def ConvertListToInt(arr):
    for i in arr:
        try:
            arr[arr.index(i)] = int(i)
        except ValueError:
            pass
    return(arr)

def UnitTest():
    with open("data/data.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        rows = list(csv_reader)
        for i in range(1, len(rows)):
            args = ConvertListToInt(rows[i])
            print(f"\nRow {i}:")
            print(calculateInsurance(*args))
            
select = int(input("Main (1) | Unit Testing (2): "))
if select == 1:
    Age = int(input("Age: "))
    Model = input("Car Model (Compact, SUV, Sedan, Sports): ").upper()
    Region = input("Region (Leinster, Munster, Ulster, Connacht): ").upper()
    Package = input("Insurance Package (TP/TPFT/CI): ").upper()
    Garage = input("Garage? (Y/N): ").upper()
    PenaltyPoints = int(input("Penalty Points: "))
    Mileage = int(input("Mileage (KM): "))
    DrivingExperience = int(input("Driving Experience (Years): "))

    print(calculateInsurance(Age, Model, Region, Package, Garage, PenaltyPoints, Mileage, DrivingExperience))
elif select == 2:
    UnitTest()
else:
    print("Select a valid option!")
    exit(0)