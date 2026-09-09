# genpark-quantum-statevector-simulator-skill

[![Agentic Skill](https://img.shields.io/badge/GenPark-Agentic__Skill-blue.svg)](https://github.com/alphaparkinc/genpark-quantum-statevector-simulator-skill)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-brightgreen.svg)](https://python.org)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-0%20Pip-orange.svg)](#)
[![Dual Org Verified](https://img.shields.io/badge/GitHub-Dual__Org-purple.svg)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> Universal n-qubit quantum statevector circuit simulator supporting arbitrary unitary gates, Hadamard, CNOT entanglement, Pauli Pauli-X/Y/Z, and multi-qubit measurement with 0-pip pure Python.

## Architecture Overview

```mermaid
flowchart TD
    A[Agentic AI / LLM Orchestrator] -->|JSON-RPC / Method Call| B[MCP Server / Client]
    B --> C[genpark-quantum-statevector-simulator-skill Core Engine]
    C --> D[Quantum State / Gate Matrix Operations]
    D --> E[Exact Algorithmic Solution & Measurement]
    E -->|Structured Output| A
```

## Features
- **0 External Pip Dependencies**: Pure Python standard library implementation.
- **MCP Protocol Ready**: Includes Model Context Protocol server script (`mcp_server.py`).
- **Production Standard**: Comprehensive state validation, unit test coverage, and benchmark speed.

## Quick Start
```bash
python example_usage.py
```
