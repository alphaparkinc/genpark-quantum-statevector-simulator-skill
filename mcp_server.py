import sys
import json
from client import QuantumCircuit

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    if method == "bell_state":
        qc = QuantumCircuit(2).h(0).cnot(0, 1)
        return {"probabilities": qc.get_probabilities(), "measurement": qc.measure(shots=params.get("shots", 100))}
    return {"error": "Unknown method"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        req = json.loads(line)
        res = handle_request(req)
        print(json.dumps(res))
        sys.stdout.flush()

if __name__ == "__main__":
    main()
