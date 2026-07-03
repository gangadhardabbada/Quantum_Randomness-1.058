"""Compare classical and quantum random bit generation."""

import random
from collections import Counter

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator


BIT_COUNT = 20


def generate_classical_bits(bit_count: int) -> list[int]:
    """Generate random bits using Python's pseudo-random generator."""
    return [random.randint(0, 1) for _ in range(bit_count)]


def build_quantum_bit_circuit() -> QuantumCircuit:
    circuit = QuantumCircuit(1, 1)
    circuit.h(0)
    circuit.measure(0, 0)
    return circuit


def generate_quantum_bits(bit_count: int, simulator: AerSimulator) -> list[int]:
    bits = []

    for _ in range(bit_count):
        circuit = build_quantum_bit_circuit()
        result = simulator.run(circuit, shots=1).result()
        counts = result.get_counts(circuit)
        measured_bit = next(iter(counts))
        bits.append(int(measured_bit))

    return bits


def count_bits(bits: list[int]) -> Counter:
    return Counter(bits)


def percentage(count: int, total: int) -> float:
    return (count / total) * 100


def format_sequence(bits: list[int]) -> str:
    return " ".join(str(bit) for bit in bits)


def print_distribution(label: str, bits: list[int]) -> None:
    counts = count_bits(bits)
    zero_count = counts.get(0, 0)
    one_count = counts.get(1, 0)

    print(f"{label} Distribution")
    print(f"  0s: {zero_count:2d} ({percentage(zero_count, len(bits)):6.2f}%)")
    print(f"  1s: {one_count:2d} ({percentage(one_count, len(bits)):6.2f}%)")
    print()


def print_comparison_table() -> None:
    rows = [
        (
            "Classical",
            "Python random module",
            "Deterministic",
            "Simulations, games, sampling",
        ),
        (
            "Quantum",
            "Hadamard gate + measurement",
            "Probabilistic",
            "Cryptography, experiments, true randomness",
        ),
    ]

    headers = [
        "Randomness Source",
        "Generation Method",
        "Deterministic or Probabilistic",
        "Typical Use Cases",
    ]
    widths = [18, 29, 32, 39]

    print("Comparison Table")
    print("-" * sum(widths))
    print(
        f"{headers[0]:<{widths[0]}}"
        f"{headers[1]:<{widths[1]}}"
        f"{headers[2]:<{widths[2]}}"
        f"{headers[3]:<{widths[3]}}"
    )
    print("-" * sum(widths))

    for row in rows:
        print(
            f"{row[0]:<{widths[0]}}"
            f"{row[1]:<{widths[1]}}"
            f"{row[2]:<{widths[2]}}"
            f"{row[3]:<{widths[3]}}"
        )


def main() -> None:
    simulator = AerSimulator()
    classical_bits = generate_classical_bits(BIT_COUNT)
    quantum_bits = generate_quantum_bits(BIT_COUNT, simulator)

    print("=" * 44)
    print("Classical vs Quantum Randomness")
    print("=" * 44)
    print(f"Classical random sequence: {format_sequence(classical_bits)}")
    print(f"Quantum random sequence  : {format_sequence(quantum_bits)}")
    print()

    print_distribution("Classical", classical_bits)
    print_distribution("Quantum", quantum_bits)
    print_comparison_table()


if __name__ == "__main__":
    main()
