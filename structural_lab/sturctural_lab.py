import numpy as np
import matplotlib.pyplot as plt

"""
This script is used for structural lab analysis of deflection against load angle

Plots an 5th order polynomial or below and find its maximum or minimum value
"""
fig, ax = plt.subplots()

def find_max_and_min(data, angle):
    data = list(data)
    max_val, min_val = max(data), min(data)
    max_index, min_index = data.index(max_val), data.index(min_val)

    print((max_val, min_val))
    return angle[max_index], angle[min_index]

func = lambda a,b,c,d,e,f,g,x: a* x**6 + b * x**5 + c * x**4 + d * x**3 + e*x**2 + f*x + g

x = np.linspace(0,180,100)
horizontal = func(2.57698809e-13,-1.4347601819e-10,2.592916664159e-8,-1.404465419243e-6,-2.051929282598e-5,-2.0474160792e-4,9.910534775e-2,x)
vertical = func(0,0,2.15907561277248e-9,-2.76164865780758e-7,-4.621938696407200e-5,4.694641087129800e-3,-3.22078219263197e-1 + 0.325,x)

angle1, angle2 = find_max_and_min(vertical,x)
angle3, angle4 = find_max_and_min(horizontal,x)

ax.axvline(x=angle1, linestyle='-.', color='black')
ax.axvline(x=angle2, linestyle='-.', color='black')
horizontal_plot = ax.plot(x,horizontal, label='Horizontal')
vertical_plot = ax.plot(x,vertical, label='Vertical')
ax.set_title('Deflection vs Angle')
ax.set_ylabel('Deflection (mm)')
ax.set_xlabel('Angle (degree)')
ax.legend()

textstr = f'Angle 1: {round(angle1,3)} \nAngle 2: {round(angle2,3)}'

props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

ax.text(0.5,0.95, textstr, transform=ax.transAxes, fontsize=7,
        verticalalignment='top', bbox=props)

ax.grid(True)
plt.show()