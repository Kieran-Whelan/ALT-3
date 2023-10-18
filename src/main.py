class Package:
    def __init__(self, value, package, region, age, l_type, experience, pen_points):
        base_rate = 400
        self.value = value
        self.package = package
        self.base_rate = base_rate
        self.region = region
        self.age = age
        self.l_type = l_type
        self.experience = experience
        self.pen_points = pen_points

        if self.package == 1:
            pass
        elif self.package == 2:
            base_rate += 200
        elif self.package == 3:
            base_rate += 400
        else:
            print("Invalid option chosen for package. Quiting....")
            exit(0)

    def get_quote(self):
        return self.base_rate


def main():
    #variables
    vehicle_value = float(input("Enter vehicle value: \n"))
    insurance_package = int(input("Enter insurance package: ((1) - Third Party (2) - Third Party Fire and Theft (3) - Fully comprehensive): \n"))
    region = int(input("Enter insurance package: ((1) - Leinster (2) - Munster (3) - Connacht (4) - Ulster): \n"))
    age = int(input("Enter your age: \n"))
    license_type = int(input("Enter your license type: ((1) - Provisional (2) - Full) \n"))
    experience = int(input("Enter the number of years you have been on the road: \n"))
    penalty_points = int(input("Enter the number of penalty points on your license: \n"))

    package = Package(vehicle_value, insurance_package, region, age, license_type, experience, penalty_points)
    print(package.get_quote())
    

    
if __name__ == "__main__":
    main()