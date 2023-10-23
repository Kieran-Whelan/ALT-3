import csv
import math

#Rates and Constants
cars_types = {
    1: 0.02, #Hatchback
    2: 0.06, #SUV
    3: 0.04, #Sedan
    4: 0.08 #Sports
}

regions = {
    1: 0.08, #Leinster
    2: 0.06, #Munster
    3: 0.04, #Ulster
    4: 0.02  #Connacht
}

base_rates = {
    1: 200, #Third Party
    2: 300, #Third Party Fire and Theft
    3: 600  #Fully Comprehensive
}

is_garage = {
    1: False,
    2: True
}

is_provisional = {
    1: True,
    2: False
}

class Package:
    def __init__(self, value, package, region, age, garage, vehicle_type, license_type, experience, penalty_points, mileage, expected_value):
        self.value = value
        self.package = package

        if not base_rates.keys().__contains__(package):
            print("Error: Invalid package chosen. Exiting program.....")
            exit(0)

        self.base_rate = base_rates[package]
        self.region = region
        self.age = age
        self.garage = is_garage[garage]
        self.vehicle_type = cars_types[vehicle_type]
        self.license_type = is_provisional[license_type]
        self.experience = experience
        self.penalty_points = penalty_points
        self.mileage = mileage
        self.expected_value = expected_value #only for test cases
        self.rate_accumulator = []

        self.rate_accumulator.append(self.value * 0.05)
        self.rate_accumulator.append(self.base_rate * self.vehicle_type)

        #Age
        if self.age > 21 and self.age < 65:
            self.rate_accumulator.append(self.base_rate * 0.04)
        elif self.age > 65:
            self.rate_accumulator.append(self.base_rate * 0.02)
        else:
            self.rate_accumulator.append(self.base_rate * 2.5)

        #Garage
        if not self.garage:
            self.rate_accumulator.append(self.base_rate * 0.03)

        #PenaltyPoints
        self.rate_accumulator.append(self.base_rate * (0.03 * penalty_points))
        
        #License Type
        if self.license_type:
            self.rate_accumulator.append(self.base_rate * 1.5)
        
        #Mileage
        self.rate_accumulator.append(self.base_rate * (0.1 * (math.ceil(self.mileage / 1000))))
        
        #Driving Experience
        if self.experience >= 3:
            rate = 0.15 - (0.025 * (round(self.experience / 3)))
            self.rate_accumulator.append(self.base_rate * rate)  

    def get_quote(self):
        return sum(self.rate_accumulator)
    
    def get_expected_value(self):
        return self.expected_value
    
def convert_list_to_int(arr):
    for i in arr:
        try:
            arr[arr.index(i)] = int(i)
        except ValueError:
            pass
    return(arr)

def run_unit_tests():
    with open("../data/data.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        rows = list(csv_reader)
        for i in range(1, len(rows)):
            args = convert_list_to_int(rows[i])
            test_package = Package(*args)
            print(f"Test Case {i}:")
            if test_package.get_expected_value() == test_package.get_quote():
                print("Passed\n")
            else:
                print("Failed\n")
def main():
    run_unit_tests()

    #variables
    vehicle_value = float(input("Enter vehicle value:\n"))
    insurance_package = int(input("Enter insurance package: ((1) - Third Party (2) - Third Party Fire and Theft (3) - Fully comprehensive): \n"))
    region = int(input("Location: ((1) - Leinster (2) - Munster (3) - Connacht (4) - Ulster): \n"))
    age = int(input("Enter your age: \n"))
    garage = int(input("Will you store it in a garage: ((1) - No (2) - Yes) \n"))
    vehicle_type = int(input("Enter your vehicle type: ((1) - Hatchback (2) - SUV (3) - Sedan (4) - Sports) \n"))
    license_type = int(input("Enter your license type: ((1) - Provisional (2) - Full) \n"))
    experience = int(input("Enter the number of years you have been on the road: \n"))
    penalty_points = int(input("Enter the number of penalty points on your license: \n"))
    mileage = int(input("Enter your intended milage (yearly): \n"))

    package = Package(vehicle_value, insurance_package, region, age, garage, vehicle_type, license_type, experience, penalty_points, mileage, 0)
    print("----------------")
    print(f"Your premium is: \n€{package.get_quote()}!")
    
if __name__ == "__main__":
    main()