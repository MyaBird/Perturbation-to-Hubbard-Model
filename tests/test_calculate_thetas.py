import perturbation_to_hubbard_model
import pytest
import numpy as np

def test_calculate_thetas():
    
    thetas = perturbation_to_hubbard_model.CalculateThetas(1,0,1,2,3,4,5)

    assert(np.isclose(thetas.theta_0, -1.047))
    assert(np.isclose(thetas.theta_2, 0.542))
    assert(np.isclose(thetas.theta_gs, 0.505))
    assert(np.isclose(thetas.theta_neg1, -2.094))
    assert(np.isclose(thetas.theta_h, 2.739))
    assert(np.isclose(thetas.theta_1, 0.368))