"""Quantum randomness statistics using Qiskit Aer."""

import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator


SHOTS = 1000


def build_circuit() -> QuantumCircuit:
    """Create a one-qubit superposition circuit with measurement."""
    circuit = QuantumCircuit(1, 1)
    circuit.h(0)
    circuit.measure(0, 0)
    return circuit


def main() -> None:
    """Run the quantum circuit and display measurement statistics."""
    circuit = build_circuit()
    simulator = AerSimulator()

    result = simulator.run(circuit, shots=SHOTS).result()
    counts = result.get_counts(circuit)

    zero_count = counts.get("0", 0)
    one_count = counts.get("1", 0)
    total_counts = zero_count + one_count

    outcomes = np.array([0] * zero_count + [1] * one_count)
    mean = np.mean(outcomes)
    standard_deviation = np.std(outcomes)

    zero_percentage = (zero_count / SHOTS) * 100
    one_percentage = (one_count / SHOTS) * 100

    print("=" * 46)
    print("Quantum Randomness Statistics")
    print("=" * 46)
    print(f"{'0 outcomes':<24}: {zero_count:>10}")
    print(f"{'1 outcomes':<24}: {one_count:>10}")
    print(f"{'Total shots':<24}: {SHOTS:>10}")
    print("-" * 46)
    print(f"{'Mean':<24}: {mean:>10.4f}")
    print(f"{'Standard deviation':<24}: {standard_deviation:>10.4f}")
    print(f"{'Percentage of 0':<24}: {zero_percentage:>9.2f}%")
    print(f"{'Percentage of 1':<24}: {one_percentage:>9.2f}%")
    print("-" * 46)

    if total_counts == SHOTS:
        print("Validation successful: total counts match shots.")
    else:
        print(
            "Validation failed: total counts do not match shots "
            f"({total_counts} != {SHOTS})."
        )


if __name__ == "__main__":
    main()
