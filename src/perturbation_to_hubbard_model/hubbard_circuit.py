from .circuit_modules import CircuitModules
from .initialize_circuit import InitializeCircuit
from .calculate_thetas import CalculateThetas
import numpy as np
import pennylane as qml

class HubbardCircuit:

    '''Class to construct circuit used to estimate 1st order correction to Hubbard model
    '''

    def __init__(self, config, N, M, pert_coeff, transfer, interaction, theta, phase, c, e_gs, e_neg1, e_0, e_1, e_2, e_h):
        '''Construction

        Parameters:
        -----------------------------
        N   : int
            Describes number of qubits representative a system of size 2^N

        M   : int
            Number of ancillary qubits required to implement the U_e gate

        pert_coeff  : float
            Defines the coefficient lambda by which to apply the perturbation

        transfer    : float
            Defines coefficient of transfer integral used in calculating alpha

        interaction     : float
            Defines U parameter used in calculating alpha
        
        theta   : float
            Rotation parameter used in the multicontrolled R_6_9 gate

        phase   : float
            Phase shift implemented by the single-qubit phase gate in the QFT circuit

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

        self.circuit = InitializeCircuit(N, M)
        
        thetas = CalculateThetas(c, e_gs, e_neg1, e_0, e_1, e_2, e_h)

        #Parameters of perturbation
        self.pert_coeff = pert_coeff
        self.t = transfer
        self.u = interaction

        #Angles of rotation
        thetas = CalculateThetas(c, e_gs, e_neg1, e_0, e_1, e_2, e_h)
        self.theta = theta
        self.phase = phase
        self.theta_gs = thetas.theta_gs
        self.theta_neg1 = thetas.theta_neg1
        self.theta_0 = thetas.theta_0
        self.theta_1 = thetas.theta_1
        self.theta_2 = thetas.theta_2
        self.theta_h = thetas.theta_h

        #Initial configuration
        self.config = config

        #Modules for circuit
        self.modules = CircuitModules(N, M, pert_coeff, transfer, interaction, theta, phase, self.theta_gs, self.theta_neg1, self.theta_0, self.theta_1, self.theta_2, self.theta_h)
        
        #Parameters of circuit
        self.qubits = self.modules.qubits
        self.N = N
        self.M = M

        #Rotation angle for disentangling circuit
        self.alpha = self.modules.alpha

    def build_circuit(self):
        '''Construct Hubbard circuit using gates created in the circuit_modules class
        '''

        #Initialize qubits to ground state
        self.circuit.initial_state(self.config)

        #Construct circuit
        self.modules.u_disentangle()
        self.modules.perturbation()
        qml.adjoint(self.modules.u_disentangle)()
        self.modules.u_inverse_energy()

        return qml.expval(qml.PauliZ(wires="q1''"))
    
    def read_circuit():
        '''
        #Check readout qubit for success
        u_e_readout = qml.expval(qml.PauliZ(wires="q2''"))

        #Measure system qubits
        state_output = []
        for idx in range(self.N):
            state_output.append(qml.expval(qml.PauliZ(wires=self.qubits[idx])))
        
        return u_e_readout, state_output

        '''