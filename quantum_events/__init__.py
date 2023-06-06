import sys;
import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit.providers.basicaer import QasmSimulatorPy
from qiskit.visualization import plot_histogram

# TODO: <---TEST Python basic structures and functions.
s = [1,2,3,4,5,6,7,8,9]
t = [0,0,0,0]
s.reverse()
print(s)
    
# Exit the application.
sys.exit(0); 
#############################################################
#############################################################

# Use Aer's qasm_simulator
simulator = QasmSimulatorPy()

# Create a Quantum Circuit acting on the q register
circuit = QuantumCircuit(2, 2)

# Add a H gate on qubit 0
#################
# Superposition #
#################
#circuit.h(0)

# Add a CX (CNOT) gate on control qubit 0 and target qubit 1
############################
# Controled, parametrized superposition. #
############################
circuit.cx(0, 1)

# Add a (controlled Z plane ...) gate on control qubit 0 and target qubit 1
#####################################################################
# Controlled, parametrized complexity of maximum element of system. #
#####################################################################
theta = 0    # of |0> |1> qubits - from 0 to pi
circuit.crz(theta, 0, 1)

# Add a CRY (controlled, parametrized Y plane) gate on control qubit 0 and target qubit 1
#################################################################
# Controlled complex, parametrized superposition of the system. #
#################################################################
theta = 0    # of |0> |1> qubits - from 0 to pi
circuit.cry(theta, 0, 1)

# Add a CRX (controlled, parametrized X plane) gate on control qubit 0 and target qubit 1
###########################################
# Controlled, parametrized superposition. #
###########################################
theta = 0    # of |0> |1> qubits - from 0 to pi
circuit.crx(theta, 0, 1)

# Map the quantum measurement to the classical bits
circuit.measure([0,1], [0,1])

# compile the circuit down to low-level QASM instructions
# supported by the backend (not needed for simple circuits)
compiled_circuit = transpile(circuit, simulator)

# Execute the circuit on the qasm simulator
job = simulator.run(compiled_circuit, shots=1000000)

# Grab results from the job
result = job.result()
print("\nThe result is:", result)

# Returns counts
counts = result.get_counts(compiled_circuit)
print("\nTotal count for 00 and 11 are:",counts)

# Draw the circuit
circuit.draw()