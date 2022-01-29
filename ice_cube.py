# -*- coding: utf-8 -*-

SPECIFIC_HEAT_CAPACITY_ICE = 2.108
SPECIFIC_HEAT_OF_FUSION_ICE = 335
SPECIFIC_HEAT_CAPACITY_WATER = 4.1819
SPECIFIC_HEAT_OF_VAPORIZATION_WATER = 2.26
SPECIFIC_HEAT_CAPACITY_STEAM = 1.996

def ice_cube_heating(energy, mass, start_temp):
     end_temp = energy/(SPECIFIC_HEAT_CAPACITY_ICE*mass) + start_temp     
     if end_temp >= 0 and (energy-max_energy_heat_ice-SPECIFIC_HEAT_OF_FUSION_ICE*mass > 0):
         final_temp = (energy - max_energy_heat_ice - SPECIFIC_HEAT_OF_FUSION_ICE*mass) / (SPECIFIC_HEAT_CAPACITY_WATER*mass)
         energy_remaining = energy - mass*SPECIFIC_HEAT_CAPACITY_WATER*(final_temp - start_temp) - max_energy_heat_ice -\
                            SPECIFIC_HEAT_OF_FUSION_ICE*mass
         melted = True
         return energy_remaining, final_temp, melted         
     else:
         final_temp = energy/(SPECIFIC_HEAT_CAPACITY_ICE*mass) + start_temp
         energy_remaining = energy - SPECIFIC_HEAT_CAPACITY_ICE*mass*(final_temp - start_temp)
         melted = False
         return energy_remaining, final_temp, melted
         
def ice_cube_melting(energy, mass):
    energy_remaining = energy - SPECIFIC_HEAT_OF_FUSION_ICE*mass - max_energy_heat_ice
    final_temp = 0.0
    if energy_remaining >= 0.0:
        melted = True
    else:
        melted = False
    return energy_remaining, final_temp, melted

def ice_cube_vaporization(energy, mass):
    energy_remaining = energy - SPECIFIC_HEAT_OF_VAPORIZATION_WATER*mass - max_energy_heat_ice - SPECIFIC_HEAT_OF_FUSION_ICE*mass -\
                       max_energy_heat_water
    final_temp = 100.0
    if energy_remaining >= 0.0:
        vaporized = True
    else:
        vaporized = False
    return energy_remaining, final_temp, vaporized

def steam_heating(energy,mass):    
     energy_remaining = 0.0
     final_temp = (energy - max_energy_heat_ice - SPECIFIC_HEAT_OF_FUSION_ICE*mass - max_energy_heat_water -\
                   SPECIFIC_HEAT_OF_VAPORIZATION_WATER*mass) / (SPECIFIC_HEAT_CAPACITY_STEAM*mass) + 100.0
     vaporized = True
     return energy_remaining, final_temp, vaporized

def print_heating_result(energy_total, mass, temp_init, temp_end, melted, vaporized):
    print("With {:.2f} kJ, an ice cube weighing {:.2f} kg heats from {:.2f} °C to {:.2f} °C."
          .format(energy_total, mass, temp_init, temp_end))
    if not melted and not vaporized:
        print("The ice cube stays solid.")
    elif melted and not vaporized:
        print("The ice cube has melted into fluid water.")
    else:
        print("The ice cube has vaporized and is now water vapor.")
 
def main():
    print("Welcome to the ice cube simulator! I will tell you stats about heating your ice cube.")
    mass = float(input("What is the mass of the ice cube (in kg)?\n"))
    while mass <= 0.0:
        print("Mass cannot be zero or negative!")
        mass = float(input("What is the mass of the ice cube?\n"))
    temp_init = float(input("What is the initial temperature of the ice cube (in °C)?\n"))
    while temp_init < -273.15 or temp_init > 0.0:
        print("The ice cube's temperature can't be under the absolute zero or above 0 degrees!")
        temp_init = float(input("What is the initial temperature of the ice cube (in °C)?\n"))
    energy_total = float(input("What is the total energy used for heating the ice cube (in kJ)?\n"))
    while energy_total < 0.0:
        print("Energy cannot be negative!")
        energy_total = float(input("What is the total energy used for heating the ice cube (in kJ)?\n"))
 
    melted = False
    vaporized = False
    global max_energy_heat_ice, max_energy_heat_water
    max_energy_heat_ice = mass*SPECIFIC_HEAT_CAPACITY_ICE*(0.0 - temp_init)
    max_energy_heat_water = mass*SPECIFIC_HEAT_CAPACITY_WATER*100.0    
    
    energy_remaining, end_temp, melted= ice_cube_heating(energy_total, mass, temp_init)
    if energy_remaining != 0.0:
        energy_remaining, end_temp, melted = ice_cube_melting(energy_total, mass)
        if energy_remaining != 0.0:
            energy_remaining, end_temp, melted = ice_cube_heating(energy_total, mass, 0.0)
            if energy_remaining != 0.0:
                energy_remaining, end_temp, vaporized = ice_cube_vaporization(energy_total, mass)
                if energy_remaining != 0.0:
                    energy_remaining, end_temp, vaporized = steam_heating(energy_total,mass)
 
    print_heating_result(energy_total, mass, temp_init, end_temp, melted, vaporized)

main()


                
                
                
                
                
