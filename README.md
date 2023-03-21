# Simple Quantum Circuit for Entanglement Generation

Description: This code defines a simple quantum circuit that generates an entangled state between two qubits using a Hadamard gate and a CNOT gate. 
It then measures the qubits and stores the results in classical bits, and runs the circuit on a simulator to obtain the probabilities of measuring each possible output state.

## Prerequisites

To run the code, you will need to install the following dependencies:

* Python 3
* Qiskit
* Matplotlib.pyplot

You can install Qiskit using pip, the Python package manager: 
```python
pip install qiskit
```

## Running the Code

To run the circuit, simply execute the `Simple_QC.py` file using Python:
```python
python Simple_QC.py
```

The code will define the circuit, run it on a simulator using **1000** shots, and print the *probabilities* of measuring each output state.


## Circuit Description

* The circuit consists of two qubits and two classical bits, defined using the `QuantumRegister` and `ClassicalRegister` classes in Qiskit. 
* It applies a Hadamard gate to the first qubit, which puts it in a superposition of the |0⟩ and |1⟩ states. 
* It then applies a CNOT gate between the first and second qubits, which entangles them into a Bell state.

* The circuit then *measures* the **qubits** and *stores* the results in the **classical bits**, which are used to obtain the *probabilities* of measuring each possible output state. 
* Since the qubits are entangled, the *probabilities* are correlated and reflect the *entangled* nature of the state.

## License

This code is licensed under the `MIT` License. Feel free to use it for any purpose, commercial or non-commercial, with attribution.
