from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

sim = AerSimulator()
qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(0, 0)

job = sim.run(transpile(qc, sim), shots=1000)
counts = job.result().get_counts()

c0 = counts.get("0", 0)
c1 = counts.get("1", 0)

print(f"\nResults: {counts}")
print(f"|0>: {c0}  ({c0 / 10:.1f}%)")
print(f"|1>: {c1}  ({c1 / 10:.1f}%)\n")
