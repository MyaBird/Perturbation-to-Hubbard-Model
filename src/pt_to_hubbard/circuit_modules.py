import pennylane as qml
import numpy as np
import math

from initialize_circuit import InitializeCircuit
from construction_gates import ConstructionGates
from rotation_gates import ControlledRotations

class CircuitModules:

    '''Class to construct the major modules needed to create the circuit
    '''

    def __init__(self, N, M, pert_coeff, timestep, u_param, theta, phase, theta_gs, theta_neg1, theta_0, theta_1, theta_2, theta_h):
        '''Construction

        Parameters:
        -----------------------------
        N   : int
            Describes number of qubits representative a system of size 2^N

        M   : int
            Number of ancillary qubits required to implement the U_e gate

        pert_coeff  : float
            Defines the coefficient lambda by which to apply the perturbation

        timestep    : float
            Defines t parameter used in calculating alpha

        u_param     : float
            Defines U parameter used in calculating alpha

        theta_gs    : float
            Parameter determined by E_gs, where .. math:: \\sin(\\frac{\\theta_2 + \\theta_0 + \\theta_{gs}}{2} = 0

        theta_neg1  : float
            Parameter determined by E_-1, where .. math:: \\sin(\\frac{\\theta_{-1} + \\theta_0}{2} = \\frac{C}{E_{gs} - E_{-1}}

        theta_0     : float
            Parameter determined by E_0, where .. math:: \\sin(\\frac{theta_0}{2}) = \\frac{C}{E_{gs} - E_0}

        theta_1     : float
            Parameter determined by E_1, where .. math:: \\sin(\\frac{\\theta_1 + \\theta_0}{2} = \\frac{C}{E_{gs} - E_1}

        theta_2     : float
            Parameter determined by E_2, where .. math:: \\sin(\\frac{\\theta_2 + \\theta_0}{2}) = \\frac{C}{E_{gs} - E_2}

        theta_h     : float
            Parameter determined by E_h, where .. math:: \\sin(\\frac{\\theta_neg1 + \\theta_0 + \\theta_h}{2} = \\frac{C}{E_{gs} - E_{h}}
        
        theta   : float
            Rotation parameter used in the multicontrolled R_6_9 gate

        phase   : float
            Phase shift implemented by the single-qubit phase gate in the QFT circuit

        Notes:
        ------

        Alpha determined by U and t such that

        .. math:: \\alpha=-2\\arccos{\\frac{2t+\\sqrt{U^2/4+4t^2}}{\\sqrt{U^2/4+(2t+\\sqrt{U^2/4+4t^2})^2}}}

        '''

        self.gates = ConstructionGates(N, M, pert_coeff, timestep, u_param)
        self.rot = ControlledRotations(N, M, pert_coeff, timestep, u_param)

        #Parameters of circuit
        self.qubits = InitializeCircuit(N, M).qubits
        self.N = N
        self.M = M

        #Parameters of perturbation
        self.pert_coeff = pert_coeff
        self.t = timestep
        self.u = u_param

        #Angles of rotation
        self.theta = theta
        self.alpha = -2 * math.acos((2*timestep + math.sqrt(u_param**2/4 + 4*timestep**2))/(math.sqrt(u_param**2/4 + (2*timestep + math.sqrt(u_param**2/4 + 4*timestep**2))**2)))
        self.phase = phase
        self.theta_gs = theta_gs
        self.theta_neg1 = theta_neg1
        self.theta_0 = theta_0
        self.theta_1 = theta_1
        self.theta_2 = theta_2
        self.theta_h = theta_h

    def u_disentangle(self):
        '''Gate which transforms the system qubits from the computational basis into the energy eigenstates of the unperturbed Hamiltonian.

            .. math::
            U_{dis}^{\\dagger}H^{(0)}U_{dis}=\\sum_{n}E_n\\ket{n}\\bra{n}
            
        '''

        qml.PauliX(wires=self.qubits[0])
        qml.PauliX(wires=self.qubits[2])
        self.gates.multi_R_6_9(self.theta)
        self.gates.multi_R_5_10(self.alpha)
        self.gates.qft(self.phase)

    def perturbation(self):
        '''Applies a dipole-dipole interaction to the unperturbed Hubbard Hamiltonian
        '''
        
        self.gates.exp_perturbation()
        self.gates.perturbation_check()

    def u_inverse_energy(self):
        '''Constructs gate used to calculate inverse of 1st order energy corrections to the unperturbed Hubbard Hamiltonian
            
        '''

        self.rot.cr_0(self.theta_0)
        self.rot.cr_1(self.theta_2)
        self.rot.cr_2(self.theta_gs)
        self.rot.cr_3(self.theta_neg1)
        self.rot.cr_4(self.theta_neg1)
        self.rot.cr_5(self.theta_h)
        self.rot.cr_6(self.theta_1)
        self.rot.cr_7(self.theta_1)