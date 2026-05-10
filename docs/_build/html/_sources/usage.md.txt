# Usage

To use Perturbation to Hubbard Model in a project:

```python
import perturbation_to_hubbard_model
```

To define a blank quantum circuit with 8 qubits:
```python
blank_circuit = perturbation_to_hubbard_model.InitializeCircuit(4, 2)
```

To create the basic gates used to construct your circuit:
```python
gates = perturbation_to_hubbard_model.ConstructionGates(4, 2, 0.1, 1, 1)
```

To create multicontrolled rotation gates to construct your circuit:
```python
multi_r = perturbation_to_hubbard_model.RotationGates(4, 2, 0.1, 1, 1)
```

To create modules for each circuit transformation:
```python
modules = perturbation_to_hubbard_model.CircuitModules(4, 2, 0.1, 1, 1, 0.785, 1, -1.56, -1, 0, 1, 2, 2.56)
```

To calculate rotation angles in U_e given the energy levels of the unperturbed Hamiltonian:
```python
thetas = perturbation_to_hubbard_model.CalculateThetas(1, -1.56, -1, 0, 1, 2, 2.56)
```

To construct the whole circuit:
```python
circuit = perturbation_to_hubbard_model.HubbardCircuit([0,0,0,0], 4, 2, 0.1, 1, 1, 0.785, 1, 1, -1.56, -1, 0, 1, 2, 2.56)
```