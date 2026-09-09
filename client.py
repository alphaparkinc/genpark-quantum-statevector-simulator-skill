import math
import cmath
import random

class QuantumCircuit:
    """Universal n-qubit quantum statevector circuit simulator in pure Python."""
    def __init__(self, num_qubits: int):
        self.num_qubits = num_qubits
        self.num_states = 1 << num_qubits
        # Initialize statevector to |00...0>
        self.state = [0.0 + 0.0j] * self.num_states
        self.state[0] = 1.0 + 0.0j

    def _apply_single_qubit_gate(self, target: int, matrix: list[list[complex]]):
        new_state = [0.0 + 0.0j] * self.num_states
        for i in range(self.num_states):
            bit = (i >> target) & 1
            i0 = i & ~(1 << target)
            i1 = i | (1 << target)
            if bit == 0:
                new_state[i] += matrix[0][0] * self.state[i0] + matrix[0][1] * self.state[i1]
            else:
                new_state[i] += matrix[1][0] * self.state[i0] + matrix[1][1] * self.state[i1]
        self.state = new_state

    def h(self, target: int):
        inv_sqrt2 = 1.0 / math.sqrt(2.0)
        gate = [[inv_sqrt2, inv_sqrt2], [inv_sqrt2, -inv_sqrt2]]
        self._apply_single_qubit_gate(target, gate)
        return self

    def x(self, target: int):
        gate = [[0.0, 1.0], [1.0, 0.0]]
        self._apply_single_qubit_gate(target, gate)
        return self

    def z(self, target: int):
        gate = [[1.0, 0.0], [0.0, -1.0]]
        self._apply_single_qubit_gate(target, gate)
        return self

    def cnot(self, control: int, target: int):
        new_state = list(self.state)
        for i in range(self.num_states):
            ctrl_val = (i >> control) & 1
            if ctrl_val == 1:
                toggled = i ^ (1 << target)
                if toggled > i:
                    new_state[i], new_state[toggled] = self.state[toggled], self.state[i]
        self.state = new_state
        return self

    def get_probabilities(self) -> dict[str, float]:
        probs = {}
        for i, amp in enumerate(self.state):
            prob = abs(amp) ** 2
            if prob > 1e-9:
                bitstr = format(i, f'0{self.num_qubits}b')
                probs[bitstr] = round(prob, 4)
        return probs

    def measure(self, shots: int = 1000) -> dict[str, int]:
        probs = [abs(amp) ** 2 for amp in self.state]
        counts = {}
        for _ in range(shots):
            r = random.random()
            cum = 0.0
            chosen = 0
            for idx, p in enumerate(probs):
                cum += p
                if r <= cum:
                    chosen = idx
                    break
            bitstr = format(chosen, f'0{self.num_qubits}b')
            counts[bitstr] = counts.get(bitstr, 0) + 1
        return counts
