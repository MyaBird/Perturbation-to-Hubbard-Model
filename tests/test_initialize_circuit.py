import pt_to_hubbard
import numpy as np
import pytest
import pennylane as qml

def test_initialize_circuit():

    circuit = pt_to_hubbard.InitializeCircuit(4,2)
    test_qubits = ["q1", "q2", "q3", "q4", "q1'", "q2'", "q1''", "q2''"]
    #Test that circuit has correct qubit configuration
    assert((circuit.qubits == test_qubits).all())

    def circuit_state():
        circuit.initial_state([0,1,0,1])
        return qml.expval(qml.PauliZ("q1"))

    def test_config():
        qml.PauliX(wires='q2')
        qml.PauliX(wires='q4')
        return qml.expval(qml.PauliZ("q1"))

    #Test initialize qubit circuit
    assert(qml.equal(circuit_state(), test_config()))