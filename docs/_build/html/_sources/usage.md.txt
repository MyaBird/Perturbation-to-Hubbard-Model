# Usage

To use Perturbation to Hubbard Model in a project:

```python
import pt_to_hubbard
```

To define a blank quantum circuit with 8 qubits:
```python
blank_circuit = pt_to_hubbard.InitializeCircuit(4, 2)
```

To create the basic gates used to construct your circuit:
```python
gates = pt_to_hubbard.ConstructionGates(4, 2, 0.1, 1, 1)
```

To create multicontrolled rotation gates to construct your circuit:
```python
multi_r = pt_to_hubbard.RotationGates(4, 2, 0.1, 1, 1)
```

To create modules for each circuit transformation:
```python
modules = pt_to_hubbard.CircuitModules(4, 2, 0.1, 1, 1, 0.785, 1, -1.56, -1, 0, 1, 2, 2.56)
```

To calculate rotation angles in U_e given the energy levels of the unperturbed Hamiltonian:
```python
thetas = pt_to_hubbard.CalculateThetas(1, -1.56, -1, 0, 1, 2, 2.56)
```

To construct the whole circuit:
```python
circuit = pt_to_hubbard.HubbardCircuit([0,0,0,0], 4, 2, 0.1, 1, 1, 0.785, 1, 1, -1.56, -1, 0, 1, 2, 2.56)
```