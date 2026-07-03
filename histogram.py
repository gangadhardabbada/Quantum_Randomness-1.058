from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

sim = AerSimulator()
qc = QuantumCircuit(1, 1)
qc.h(0)
qc.measure(0, 0)

job = sim.run(transpile(qc, sim), shots=1000)
counts = job.result().get_counts()

fig = plot_histogram(counts, title="Quantum Random Number Distribution")
plt.tight_layout()

output_path = Path(__file__).with_name("quantum_random_histogram.png")
fig.savefig(output_path, dpi=150)
print(f"Counts: {counts}")
print(f"Histogram saved to: {output_path}")
