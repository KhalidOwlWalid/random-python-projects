import numpy as np
import matplotlib.pyplot as plt

class TSR:

    def __init__(self):
        self.rpm = None
        self.power = None

min_speed = 10
max_speed = 20

AIR_DENSITY = 1.225
DIAMETER = 0.3
RADIUS = DIAMETER/2
AREA_OF_ROTOR = np.pi*RADIUS**2

BLADE_EFF = 0.3
MECH_EFF = 0.96
ELEC_EFF = 0.64

# Cp = BLADE_EFF * MECH_EFF * ELEC_EFF
Cp = 0.42

wind_speed = np.linspace(min_speed, max_speed, 50)
tsr = np.linspace(0.1,3,20)

tsr_dict = {}
rpm_dict = {}

for i, ratio in enumerate(tsr):
    power = (1/2) * Cp * AREA_OF_ROTOR * AIR_DENSITY * wind_speed**3
    ratio = round(ratio, 3)
    rpm = (60 * ratio * wind_speed)/(np.pi * DIAMETER )
    tsr_dict[str(ratio)] = power
    rpm_dict[str(ratio)] = rpm

line_color = ['blue', 'green',  'yellow', 'cyan']
fig, ax = plt.subplots(figsize=(10,10))

for key in rpm_dict.keys():
    print(f"plotting {key}")
    ax.plot(wind_speed, rpm_dict[key], label=str(key))

# for key in tsr_dict.keys():
#     print(f"plotting {key}")
#     ax.plot(wind_speed, tsr_dict[key], label=str(key))
    
plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
plt.title('HAWT : Wind speed against rpm')
plt.xlabel('Wind speed (m/s)')
plt.ylabel('rpm of wind turbine rotor (rpm)')
plt.tight_layout()
plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')
# plt.title('HAWT : Power against wind speed')
# plt.xlabel('Wind speed (m/s)')
# plt.ylabel('Power of wind turbine (W)')
# plt.tight_layout()
plt.grid(True)
plt.show()

