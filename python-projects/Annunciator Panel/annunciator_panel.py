from re import A
import numpy as np
import matplotlib.pyplot as plt
import time

def read_data_file(file):

    time, voltage = [], []
    f = open(file, "r")
    lines = f.readlines()

    for line in lines:
        line = line.split()
        time.append(float(line[0]))
        voltage.append(float(line[1]))

    return time, voltage

def moving_average(voltage_list):
    average = (voltage_list[0] + voltage_list[1] + voltage_list[2])/len(voltage_list)
    return average


sim_time, voltage = read_data_file('coursework_data.txt')
voltage_list = []
avg_time = 0
avg_volt = []

for i in range(len(voltage)):

    voltage_list.append(voltage[i])

    if len(voltage_list) == 3:
        avg_voltage = moving_average(voltage_list)
        print(avg_voltage)

        del voltage_list[0]

        avg_volt.append((avg_time, avg_voltage))
        avg_time += 1

    else:
        pass
    
    try:
        if avg_voltage > 4.27:
            print("HIGH")
        if avg_voltage < -2.56:
            print("LOW")
        else:
            print(f"OK {i}")
    except:
        print("Not enough data")

    time.sleep(1)

plt.plot(sim_time, voltage)
plt.plot(*zip(*avg_volt))
plt.show()


