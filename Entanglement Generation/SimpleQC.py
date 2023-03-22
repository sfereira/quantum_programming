"""
Description: This code defines a simple quantum circuit that generates an entangled state between 
two qubits using a Hadamard gate and a CNOT gate.
It then measures the qubits and stores the results in classical bits, and runs the circuit on a 
simulator to obtain the probabilities of measuring each possible output state."""

# Required Libraries
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import Aer, execute
import matplotlib.pyplot as plt

# Define a quantum circuit with 2 qubits and 2 classical bits
q = QuantumRegister(2)
c = ClassicalRegister(2)
qc = QuantumCircuit(q, c)

# Apply a Hadamard gate to the first qubit
qc.h(q[0])

# Apply a CNOT gate between the first and second qubits
qc.cx(q[0], q[1])

# Measure the qubits and store the results in the classical bits
qc.measure(q, c)

# Draw the circuit diagram using matplotlib
qc.draw(output='mpl')

# Run the circuit on a simulator
backend = Aer.get_backend('qasm_simulator')
job = execute(qc, backend, shots=1000)
result = job.result()

# Print the results
counts = result.get_counts(qc)
print(counts)
