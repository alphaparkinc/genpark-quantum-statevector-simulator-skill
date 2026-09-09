from client import QuantumCircuit

def main():
    print("=== Quantum Statevector Simulator: Bell State Generation ===")
    qc = QuantumCircuit(2)
    # Generate Bell State |Phi+> = 1/sqrt(2) (|00> + |11>)
    qc.h(0)
    qc.cnot(0, 1)
    
    probs = qc.get_probabilities()
    print("Theoretical Probabilities:", probs)
    assert abs(probs.get("00", 0) - 0.5) < 1e-3
    assert abs(probs.get("11", 0) - 0.5) < 1e-3

    shots = qc.measure(shots=1000)
    print("Measurement Counts (1000 shots):", shots)
    print("Quantum Statevector Simulator verified successfully!")

if __name__ == "__main__":
    main()
