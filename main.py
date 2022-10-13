from scipy.optimize import minimize
from scipy.optimize import NonlinearConstraint
import numpy as np
import math

# function, pres , that we want to minimize. This function is the pressure function @x1=x2=0.5
# the values of p1_sat and p2_sat were calculated to be 17.473 and 28.824 respectively
# also, A12 will be represented as a[0] while A21 will be a[1]
pres = lambda a: ((0.5*math.exp(a[0]*((a[1]*0.5)/(a[0]*0.5+a[1]*0.5))**2))*17.473+(0.5*math.exp(a[1]*((a[0]*0.5)/(a[1]*0.5+a[0]*0.5))**2))*28.824-36.7)**2
# initial guesses for A12 and A21
A_init = [100, 1]
# constraints for the problem, it's gonna be every other combination in this list
constr = ({"type": "eq", "fun": lambda a: ((0.1*math.exp(a[0]*((a[1]*0.9)/(a[0]*0.1+a[1]*0.9))**2))*17.473+(0.9*math.exp(a[1]*((a[0]*0.1)/(a[1]*0.1+a[0]*0.9))**2))*28.824-34.4)**2},
          {"type": "eq", "fun": lambda a: ((0.2*math.exp(a[0]*((a[1]*0.8)/(a[0]*0.2+a[1]*0.8))**2))*17.473+(0.8*math.exp(a[1]*((a[0]*0.2)/(a[1]*0.2+a[0]*0.8))**2))*28.824-36.7)**2},
          {"type": "eq", "fun": lambda a: ((0.3*math.exp(a[0]*((a[1]*0.7)/(a[0]*0.3+a[1]*0.7))**2))*17.473+(0.7*math.exp(a[1]*((a[0]*0.3)/(a[1]*0.3+a[0]*0.7))**2))*28.824-36.9)**2},
          {"type": "eq", "fun": lambda a: ((0.4*math.exp(a[0]*((a[1]*0.6)/(a[0]*0.4+a[1]*0.6))**2))*17.473+(0.6*math.exp(a[1]*((a[0]*0.4)/(a[1]*0.6+a[0]*0.4))**2))*28.824-36.8)**2},
          {"type": "eq", "fun": lambda a: ((0.6*math.exp(a[0]*((a[1]*0.4)/(a[0]*0.6+a[1]*0.4))**2))*17.473+(0.4*math.exp(a[1]*((a[0]*0.6)/(a[1]*0.4+a[0]*0.6))**2))*28.824-36.5)**2},
          {"type": "eq", "fun": lambda a: ((0.7*math.exp(a[0]*((a[1]*0.3)/(a[0]*0.7+a[1]*0.3))**2))*17.473+(0.3*math.exp(a[1]*((a[0]*0.7)/(a[1]*0.3+a[0]*0.7))**2))*28.824-35.4)**2},
          {"type": "eq", "fun": lambda a: ((0.8*math.exp(a[0]*((a[1]*0.2)/(a[0]*0.8+a[1]*0.2))**2))*17.473+(0.2*math.exp(a[1]*((a[0]*0.8)/(a[1]*0.2+a[0]*0.8))**2))*28.824-32.9)**2},
          {"type": "eq", "fun": lambda a: ((0.9*math.exp(a[0]*((a[1]*0.1)/(a[0]*0.9+a[1]*0.1))**2))*17.473+(0.1*math.exp(a[1]*((a[0]*0.9)/(a[1]*0.1+a[0]*0.9))**2))*28.824-27.7)**2})

bnds = ((0, 1000), (0, 1000))

res = minimize(pres, A_init, method='SLSQP', bounds=bnds, constraints=constr)

print(res.x)

# so the error I get on my computer is apparently something about access which, I don't know man I've looked up some
# stuff and most of it is about C++ which I've been reading up on but I really don't like coding. Which sucks since
# the field which I've enjoyed most in college requires coding to do anything of substance in it. Anyway, whatever you
# input for the initial conditions is what it thinks A12 and A21 are which is obviously wrong. As a chemical engineer
# I've seen problems like this before but coding them is another matter.

# For part 3, all I have to say is no because my model kind of sucks. It was hardcoded with bad intentions. I want to
# see if a simpler version of this would run but I'm not holding my breath. It would be nice to see what the code should
# look like but I understand the risks with academic dishonesty if the code were to be published. Anyway, my model
# doesn't match the data for obvious reasons. See ya next time.