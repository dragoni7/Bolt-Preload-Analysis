'''Stores the experimental parameters that have an effect on the exp2 models'''
'''These parameters are determined through our bolt testing experiments'''
'''Hard coded for now'''

# TODO: Increase flexibility, encapsulate parameters as their own objects, finish extrapolating parameter scales through testing
SEALANT = "Sealant"
PLATE_MATERIAL = "Plate Material"
BOLT_ID = "Bolt ID"
FASTENER_MATERIAL = "Fastener Material"
FASTENER_THREAD_SIZE = "Fastener Thread Size"

values = {
    SEALANT: {
        # Parameter we were able to investigate. The values in the list represent the scale to apply to the corresponding coefficients in order: a, b, c, d
        # a and c coefficients should be multipliers, and b and d should be additive.
        # all other values are placeholders.
        #               a          b         c           d
        "BMS 5-45": [float(0.4658), float(-0.0510), float(1.0612), float(-9.1570e-7)],
        "v2": [float(1.0), float(0.0), float(1.0), float(0.0)],
        "none": [float(1.0), float(0.0), float(1.0), float(0.0)]
    },
    PLATE_MATERIAL: {
        "aluminum": [float(1.0), float(0.0), float(1.0), float(0.0)],
        "CFRP": [float(1.0), float(0.0), float(1.0), float(0.0)],
        "NA": [float(1.0), float(0.0), float(1.0), float(0.0)]
    },
    BOLT_ID: {
        "AN4-28": [float(1.0), float(0.0), float(1.0), float(0.0)],
        "NA": [float(1.0), float(0.0), float(1.0), float(0.0)]
    },
    FASTENER_MATERIAL: {
        "steel": [float(1.0), float(0.0), float(1.0), float(0.0)],
        "stainless steel": [float(1.0), float(0.0), float(1.0), float(0.0)],
        "titanium": [float(1.0), float(0.0), float(1.0), float(0.0)],
        "aluminum": [float(1.0), float(0.0), float(1.0), float(0.0)],
        "A286 alloy": [float(1.0), float(0.0), float(1.0), float(0.0)],
        "NA": [float(1.0), float(0.0), float(1.0), float(0.0)]
    },
    FASTENER_THREAD_SIZE: {
        "1/4in": [float(1.0), float(0.0), float(1.0), float(0.0)],
        "3/8in": [float(1.0), float(0.0), float(1.0), float(0.0)],
        "1/2in": [float(1.0), float(0.0), float(1.0), float(0.0)],
        "NA": [float(1.0), float(0.0), float(1.0), float(0.0)]
    }
}

def get_values(name):
    '''Returns a list of values for the given parameter name'''
    return list(values[name].keys())
        