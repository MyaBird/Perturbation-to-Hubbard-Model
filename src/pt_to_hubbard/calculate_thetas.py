import numpy as np
import math

class CalculateThetas:

    '''Class to calculate angles of rotation for multicontrolled rotation gates constructing U_e
    '''

    def __init__(self, c, e_gs, e_neg1, e_0, e_1, e_2, e_h):
        '''Constructor

        Parameters:
        -----------

        c : float
            Normalization parameter
        
        e_gs : float
            Ground state energy

        e_neg1 : float
            Energy of excited state e_neg1

        e_0 : float
            Energy of excited state e_0

        e_1 : float
            Energy of excited state e_1

        e_2 : float
            Energy of excited state e_2

        e_h : float
            Highest excited state energy

        '''

        self.theta_0 = 2 * math.asin(c / (e_gs - e_0))
        self.theta_2 = 2 * math.asin(c / (e_gs - e_2)) - self.theta_0
        self.theta_gs = - self.theta_0 - self.theta_2
        self.theta_neg1 = 2 * math.asin(c / (e_gs - e_neg1)) - self.theta_0
        self.theta_h = 2 * math.asin(c / (e_gs - e_h)) - self.theta_0 - self.theta_neg1
        self.theta_1 = 2 * math.asin(c / (e_gs - e_1)) - self.theta_0