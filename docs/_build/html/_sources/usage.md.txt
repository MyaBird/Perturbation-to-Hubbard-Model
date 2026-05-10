# Usage

To use Perturbation to Hubbard Model in a project:

```python
import pt_to_hubbard
```

# Define a blank quantum circuit with 8 qubits 
blank_circuit = pt_to_hubbard.InitializeCircuit(4, 2)

# Create basic gates to construct your circuit
gates = pt_to_hubbard.ConstructionGates(4, 2, 0.1, 1, 1)

# Create multicontrolled rotation gates to construct circuit
multi_r = pt_to_hubbard.RotationGates(4, 2, 0.1, 1, 1)

# Create modules for each circuit transformation
modules = pt_to_hubbard.CircuitModules(4, 2, 0.1, 1, 1, 0.785, 1, -1.56, -1, 0, 1, 2, 2.56)

# Calculate rotation angles in U_e given the energy levels of the unperturbed Hamiltonian
thetas = pt_to_hubbard.CalculateThetas(1, -1.56, -1, 0, 1, 2, 2.56)

# Construct circuit
circuit = pt_to_hubbard.HubbardCircuit([0,0,0,0], 4, 2, 0.1, 1, 1, 0.785, 1, 1, -1.56, -1, 0, 1, 2, 2.56)