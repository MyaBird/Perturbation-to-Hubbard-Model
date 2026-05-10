from circuit_modules import CircuitModules
from initialize_circuit import InitializeCircuit
import numpy as np
import pennylane as qml

class HubbardCircuit:

    '''Class to construct circuit used to estimate 1st order correction to Hubbard model
    '''

    def __init__(self, config, N, M, pert_coeff, transfer, interaction, theta, phase, theta_gs, theta_neg1, theta_0, theta_1, theta_2, theta_h):
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

        '''

        self.modules = CircuitModules(N, M, pert_coeff, transfer, interaction, theta, phase, theta_gs, theta_neg1, theta_0, theta_1, theta_2, theta_h)
        self.circuit = InitializeCircuit(N, M)

        #Parameters of circuit
        self.qubits = self.modules.qubits
        self.N = N
        self.M = M

        #Parameters of perturbation
        self.pert_coeff = pert_coeff
        self.t = transfer
        self.u = interaction

        #Angles of rotation
        self.theta = theta
        self.alpha = self.modules.alpha
        self.phase = phase
        self.theta_gs = theta_gs
        self.theta_neg1 = theta_neg1
        self.theta_0 = theta_0
        self.theta_1 = theta_1
        self.theta_2 = theta_2
        self.theta_h = theta_h

        #Initial configuration
        self.config = config

    def hub_circuit(self):
        '''Construct Hubbard circuit using gates created in the circuit_modules class
        '''

        #Initialize qubits to ground state
        self.circuit.initial_state(self.config)

        #Construct circuit
        self.modules.u_disentangle()
        self.modules.perturbation()
        qml.adjoint(self.modules.u_disentangle)()
        self.modules.u_inverse_energy()

        #Check readout qubit for success
        u_e_readout = qml.expval(qml.PauliZ(wires="q2''"))

        #Measure system qubits
        state_output = []
        for idx in range(self.N):
            state_output.append(qml.expval(qml.PauliZ(wires=self.qubits[idx])))
        
        return u_e_readout, state_output