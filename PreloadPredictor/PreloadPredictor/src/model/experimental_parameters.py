'''Stores the experimental parameters that have an effect on the exp2 models'''
'''These parameters are determined through our bolt testing experiments'''
'''Hard coded for now'''

SEALANT = "Sealant"
PLATE_MATERIAL = "Plate Material"
BOLT_ID = "Bolt ID"
FASTENER_MATERIAL = "Fastener Material"
FASTENER_THREAD_SIZE = "Fastener Thread Size"

values = {
    SEALANT: {
        "BMS 5-45": float(0.5),
        "v2": float(0.4),
        "none": float(1.0)
    },
    PLATE_MATERIAL: {
        "aluminum": float(1.0),
        "CFRP": float(0.7),
        "NA": float(1.0)
    },
    BOLT_ID: {
        "AN4-28": float(1.0),
        "NA": float(1.0)
    },
    FASTENER_MATERIAL: {
        "steel": float(0.76),
        "stainless steel": float(0.7),
        "titanium": float(0.6),
        "aluminum": float(0.76),
        "A286 alloy": float(0.4),
        "NA": float(1.0)
    },
    FASTENER_THREAD_SIZE: {
        "1/4in": float(1.2),
        "3/8in": float(1.5),
        "1/2in": float(2.3),
        "NA": float(1.0)
    }
}

def get_values(name):
    '''Returns a list of values for the given parameter name'''
    return list(values[name].keys())
        