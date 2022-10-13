from scipy.optimize import minimize
import numpy as np
# function, pres , that we want to minimize. This function is the pressure function @x1=x2=0.5
# the values of p1_sat and p2_sat were calculated to be 17.473 and 28.824 respectively
# also, A12 will be represented as A[1] while A21 will be A[2]
pres = lambda A: ((0.5*exp(A[1]*((A[2]*0.5)/(A[1]*0.5+A[2]*0.5))**2))*17.473 +
                  (0.5*exp(A[2]*((A[1]*0.5)/(A[2]*0.5+A[1]*0.5))**2))*28.824 - 36.7) ** 2
# initial guesses for A12 and A21
A_init = [5, 5]
# constraints for the problem, it's gonna be every other combination in this list
constr = ({"type": "eq", "pres": lambda A: ((0.5*exp(A[1]*((A[2]*0.5)/(A[1]*0.5+A[2]*0.5))**2))*17.473 + (0.5*exp(A[2]*((A[1]*0.5)/(A[2]*0.5+A[1]*0.5))**2))*28.824 - 36.7) ** 2},
{"type": "eq", "pres": lambda A: ((0.5*exp(A[1]*((A[2]*0.5)/(A[1]*0.5+A[2]*0.5))**2))*17.473 + (0.5*exp(A[2]*((A[1]*0.5)/(A[2]*0.5+A[1]*0.5))**2))*28.824 - 36.7) ** 2},
{"type": "eq", "pres": lambda A: ((0.5*exp(A[1]*((A[2]*0.5)/(A[1]*0.5+A[2]*0.5))**2))*17.473 + (0.5*exp(A[2]*((A[1]*0.5)/(A[2]*0.5+A[1]*0.5))**2))*28.824 - 36.7) ** 2},
{"type": "eq", "pres": lambda A: ((0.5*exp(A[1]*((A[2]*0.5)/(A[1]*0.5+A[2]*0.5))**2))*17.473 + (0.5*exp(A[2]*((A[1]*0.5)/(A[2]*0.5+A[1]*0.5))**2))*28.824 - 36.7) ** 2},
{"type": "eq", "pres": lambda A: ((0.5*exp(A[1]*((A[2]*0.5)/(A[1]*0.5+A[2]*0.5))**2))*17.473 + (0.5*exp(A[2]*((A[1]*0.5)/(A[2]*0.5+A[1]*0.5))**2))*28.824 - 36.7) ** 2},
{"type": "eq", "pres": lambda A: ((0.5*exp(A[1]*((A[2]*0.5)/(A[1]*0.5+A[2]*0.5))**2))*17.473 + (0.5*exp(A[2]*((A[1]*0.5)/(A[2]*0.5+A[1]*0.5))**2))*28.824 - 36.7) ** 2},
{"type": "eq", "pres": lambda A: ((0.5*exp(A[1]*((A[2]*0.5)/(A[1]*0.5+A[2]*0.5))**2))*17.473 + (0.5*exp(A[2]*((A[1]*0.5)/(A[2]*0.5+A[1]*0.5))**2))*28.824 - 36.7) ** 2},
{"type": "eq", "pres": lambda A: ((0.5*exp(A[1]*((A[2]*0.5)/(A[1]*0.5+A[2]*0.5))**2))*17.473 + (0.5*exp(A[2]*((A[1]*0.5)/(A[2]*0.5+A[1]*0.5))**2))*28.824 - 36.7) ** 2},
{"type": "eq", "pres": lambda A: ((0.5*exp(A[1]*((A[2]*0.5)/(A[1]*0.5+A[2]*0.5))**2))*17.473 + (0.5*exp(A[2]*((A[1]*0.5)/(A[2]*0.5+A[1]*0.5))**2))*28.824 - 36.7) ** 2},
{"type": "eq", "pres": lambda A: ((0.5*exp(A[1]*((A[2]*0.5)/(A[1]*0.5+A[2]*0.5))**2))*17.473 + (0.5*exp(A[2]*((A[1]*0.5)/(A[2]*0.5+A[1]*0.5))**2))*28.824 - 36.7) ** 2},
          )
