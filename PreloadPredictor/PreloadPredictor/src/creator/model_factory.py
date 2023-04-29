from model.preload_decay_model import PreloadDecayModel

class ModelFactory():
    '''Creates a new PreloadDecayModel object'''
    def create_model(self, typ, name, c_A, c_B, c_C, c_D) -> PreloadDecayModel:
        if (typ == "exp2"):
            return PreloadDecayModel(label= name, c_A=c_A, c_B=c_B, c_C=c_C, c_D=c_D)