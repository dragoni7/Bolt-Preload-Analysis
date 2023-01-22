"""__preloadpredictor__.py: Logic layer of the application."""

__author__      = "Samuel Gibson"

# the coefficients for the equation
__coeff_dict = {}

def parseEquation(equation):
    print("parsing:" + equation)
    # TODO determine the coefficients of the equation and return them to the app
    # the app can then display the coefficients and allow the user to set values for them
    __coeff_dict.update({"example_coefficient1": 0})
    __coeff_dict.update({"example_coefficient2": 0})

def getCoefficients():
    coefficients = []
    for c in __coeff_dict:
        coefficients.append(c)
    return coefficients

def setCoefficientValue(coefficient, value):
    __coeff_dict.update({coefficient: value})
    print(__coeff_dict)

def clear():
    __coeff_dict.clear()

