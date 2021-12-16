# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 11:37:55 2020

https://towardsdatascience.com/optimization-with-constraints-using-lagrange-multiplier-in-python-82769c9a43fe

@author: emc1977
"""

import matplotlib.pyplot as plt
import numpy as np

cost_social = 25
cost_tv = 250
budget = 2500

#lets get the minimum and maximum number of campaigns:
social_min = 0
social_max = budget / cost_social

tv_min = 0
tv_max = budget / cost_tv

# if we fix the number of tv campaings, we know the number of social campaigns left to buy by inverting the formula
def n_social(n_tv, budget):
    return (budget - 250 * n_tv) / 25

# if we fix the number of social campaings, we know the number of tv campaigns left to buy by inverting the formula
def n_tv(n_social, budget):
    return (budget - 25 * n_social) / 250

social_x = np.linspace(social_min, social_max, 100)
tv_y = n_tv(social_x, budget)

plt.figure(figsize=(10,5))
plt.plot(social_x, tv_y)
plt.xlabel('Number of social campaigns')
plt.ylabel('Number of tv campaigns')
plt.title('Possible ways of spending the budget')
plt.show()

def revenues(social, tv):
    return social**(3/4) * tv**(1/4) * 7

from mpl_toolkits.mplot3d import Axes3D
social_axis = np.linspace(social_min, social_max, 100)
tv_axis = np.linspace(tv_min, tv_max, 100)
social_grid, tv_grid = np.meshgrid(social_axis, tv_axis)

fig = plt.figure()
ax = fig.gca(projection='3d')

ax.plot_surface(tv_grid, social_grid, revenues(social_grid, tv_grid))

ax.plot(tv_y, social_x, linewidth = 5, color = 'r')

ax.set_xlabel('Number of hours bought')
ax.set_ylabel('Number of materials bought')
ax.set_title('Possible ways of spending the budget')
plt.show()

fig, (ax_l, ax_r) = plt.subplots(1, 2, figsize = (15, 5))


social_axis = np.linspace(social_min, social_max, 100)
tv_axis = np.linspace(tv_min, tv_max, 100)
social_grid, tv_grid = np.meshgrid(social_axis, tv_axis)
    
im = ax_l.imshow(revenues(social_grid, tv_grid), aspect = 'auto', extent=[social_min, social_max, tv_min, tv_max])
ax_l.plot(social_axis, n_tv(social_axis, 2500), 'r')
ax_l.set_xlabel('Number of social campaigns bought')
ax_l.set_ylabel('Number of tv campaigns bought')
ax_l.set_title('Possible ways of spending the budget')


# The contours are showing how the intersection looks like

social_axis = np.linspace(social_min, social_max)
tv_axis = np.linspace(tv_min, tv_max)
social_grid, tv_grid = np.meshgrid(social_axis, tv_axis)

im2 = ax_r.contour(revenues(social_grid,tv_grid), extent=[social_min, social_max, tv_min, tv_max])
ax_r.plot(social_axis, n_tv(social_axis, 2500), 'r')
ax_r.set_xlabel('Number of social campaings bought')
ax_r.set_ylabel('Number of tv campaigns bought')
ax_r.set_title('Possible ways of spending the budget')

plt.colorbar(im,ax=ax_l)
plt.colorbar(im2,ax=ax_r)

plt.show()

from sympy import *

s, t, l = symbols('s t l')

solve([Eq((21/4)*((t**(1/4))/s**(1/4)) - 25*l, 0),
   Eq((7/4)*(s**(3/4)/t**(3/4)) - 250*l, 0),
   Eq(25*s+250*t - 2500, 0)], [s,t,l], simplify=False)

revenues(75, 2.5)
