'''Stores the experimental parameters that have an effect on the exp2 models'''
'''Currently serves as example'''

SEALANT = "sealant"
PLATE_MATERIAL = "plate material"
PARAMETER3 = "parameter3"
PARAMETER4 = "parameter4"

values = {
    SEALANT: {
        "v1": float(2.0),
        "v2": float(3.0),
        "v3": float(5.0)
    },
    PLATE_MATERIAL: {
        "aluminum": float(5.0),
        "carbon fiber": float(6.2),
        "v3": float(10.0)
    },
    PARAMETER3: {
        "v1": float(1.1),
        "v2": float(1.2),
        "v3": float(1.3)
    },
    PARAMETER4: {
        "v1": float(1.0),
        "v2": float(2.0),
        "v3": float(3.0)
    }
}

'''Returns a list of values for the given parameter'''
def get_values(name):
    return list(values[name].keys())
        