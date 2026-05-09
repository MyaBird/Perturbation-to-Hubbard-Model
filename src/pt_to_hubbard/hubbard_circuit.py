from circuit_modules import CircuitModules
from initialize_circuit import InitializeCircuit
import numpy as np
import pennylane as qml

class HubbardCircuit:

    def __init__(self, config, N, M, pert_coeff, transfer, interaction, theta, phase, theta_gs, theta_neg1, theta_0, theta_1, theta_2, theta_h):

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