import csv

def fuel_needed(mass):
    fuel = int(mass/3)-2
    if fuel <= 0:
        return 0
    return fuel + fuel_needed(fuel)


def test_fuel_needed():
        assert fuel_needed(4) == 0
        assert fuel_needed(6) == 0
        assert fuel_needed(12) == 2
        assert fuel_needed(14) == 2
        assert fuel_needed(1969) == 966
        assert fuel_needed(100756) == 50346



def main():
    
    with open('2019/day1_input.txt', 'rt') as f:

        reader = csv.reader(f, delimiter=' ', skipinitialspace=True)
        list_of_module_masses = list()
        for line in reader:
            list_of_module_masses.append(int(line[0]))
        
        fuel_total = int()
        for mass in list_of_module_masses:
            fuel_total = fuel_total + fuel_needed(mass)

    print(fuel_total)
    

if __name__ == "__main__":
    main()

    test_fuel_needed()
