# Usage

To use Perturbation to Hubbard Model in a project:

```python
import pt_to_hubbard
```

# Define a blank quantum circuit with 8 qubits 
circuit = pt_to_hubbard.InitializeCircuit(4, 2)

# Create basic gates to construct your circuit
gates = pt_to_hubbard.ConstructionGates(4, 2, 0.1, 1, 1)

# Create multicontrolled rotation gates to construct circuit
multi_r = pt_to_hubbard.RotationGates(4, 2, 0.1, 1, 1)

# Create modules for each circuit transformation
modules = pt_to_hubbard.HubbardEstimation(4, 2, 0.1, 1, 1)