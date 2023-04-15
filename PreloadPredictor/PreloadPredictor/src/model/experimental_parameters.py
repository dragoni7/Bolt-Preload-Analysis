'''Stores the experimental parameters that have an effect on the exp2 models'''
'''Currently serves as example'''

SEALANT = "Sealant"
PLATE_MATERIAL = "Plate Material"
BOLT_DIAMETER = "Bolt Diameter"
FASTENER_MATERIAL = "Fastener Material"
FASTENER_THREAD_SIZE = "Fastener Thread Size"

values = {
    SEALANT: {
        "BMS 5-45": float(2.0),
        "v2": float(4.0),
        "none": float(0.1)
    },
    PLATE_MATERIAL: {
        "aluminum": float(5.0),
        "CFRP": float(6.2)
    },
    BOLT_DIAMETER: {
        "v1": float(1.0),
        "v2": float(2.0),
        "v3": float(2.5)
    },
    FASTENER_MATERIAL: {
        "steel": float(1.5),
        "titanium": float(4.0)
    },
    FASTENER_THREAD_SIZE: {
        "1/4in": float(1.1),
        "3/8in": float(1.2),
        "1/2in": float(1.3)
    }
}

'''Returns a list of values for the given parameter'''
def get_values(name):
    return list(values[name].keys())
        