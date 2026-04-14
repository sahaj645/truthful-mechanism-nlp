# truthful-mechanism-nlp

Simulation framework for **incentive-compatible truthful political discourse** using NLP-based claim scoring, mechanism design, and dynamic reputation updates.

## Table of Contents
- [Overview](#overview)
- [Core Features](#core-features)
- [Architecture](#architecture)
- [Repository Structure](#repository-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Project](#running-the-project)
- [Experiment Workflows](#experiment-workflows)
- [Dashboard](#dashboard)
- [Development & Quality](#development--quality)
- [Troubleshooting](#troubleshooting)
- [Roadmap](#roadmap)
- [License](#license)

---

## Overview

This repository implements a simulation-first framework for studying how platform incentives can encourage truthful behavior in political discourse. Instead of only detecting misinformation after publication, it models a feedback loop where users are rewarded for factual consistency and penalized for manipulative behavior.

The system combines:

1. **NLP-driven truth/consistency signals**
2. **Mechanism-based reward shaping**
3. **Reputation dynamics across repeated interactions**

---

## Core Features

- Claim processing pipeline with semantic scoring primitives
- Truth score and agreement score integration
- Reward and reputation update mechanism for each interaction round
- Multi-round, multi-user simulation engine
- Parameter sweep and robustness experiment scripts
- Streamlit dashboard for interactive analysis and visualization
- Production-oriented project metadata and dependency management via Poetry

---

## Architecture

High-level interaction loop:

`User Claim -> Embedding/Similarity -> Truth Score -> Mechanism Reward -> Reputation Update -> Next Round`

Key module responsibilities:

- `src/data_loader.py`  
  Handles dataset/fact base ingestion.

- `src/embedding.py`  
  Embedding generation and vector-level operations.

- `src/truth_score.py`  
  Computes credibility/truth-oriented metrics from claim context.

- `src/mechanism.py`  
  Converts truth and agreement signals into reward/reputation updates.

- `src/simulation.py`  
  Orchestrates users, rounds, state transitions, and output records.

---

## Repository Structure

```text
truthful-mechanism-nlp/
├─ data/
│  ├─ political_claims.csv
│  └─ fact_base.txt
├─ experiments/
│  ├─ noise_robustness.py
│  └─ parameter_sweep.py
├─ notebooks/
│  └─ testscript.py
├─ scripts/
│  └─ download_fakenewsnet.py
├─ src/
│  ├─ data_loader.py
│  ├─ embedding.py
│  ├─ mechanism.py
│  ├─ simulation.py
│  └─ truth_score.py
├─ config.yaml
├─ dashboard.py
├─ pyproject.toml
├─ requirements.txt
└─ README.md
```

---

## Prerequisites

- Python **3.10+**
- pip (or Poetry)
- Git

Optional:
- Virtual environment tooling (`venv`, `virtualenv`, or Poetry-managed env)

---

## Installation

### Option A: pip + requirements.txt

```bash
git clone https://github.com/sahaj645/truthful-mechanism-nlp.git
cd truthful-mechanism-nlp
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
# source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### Option B: Poetry (recommended for production/development parity)

```bash
git clone https://github.com/sahaj645/truthful-mechanism-nlp.git
cd truthful-mechanism-nlp
poetry install
poetry shell
```

---

## Configuration

Primary config is defined in `config.yaml`.

Key fields:

- `paths.data_dir`, `paths.claims_file`, `paths.fact_base_file`
- `simulation.n_users_default`, `simulation.n_rounds_default`, `simulation.seed`
- `simulation.embedding_model` (default: `all-MiniLM-L6-v2`)
- `logging.level`, `logging.format`, `logging.log_dir`

If you change data file locations or model configuration, update `config.yaml` accordingly before running experiments.

---

## Running the Project

### Run experiments

```bash
python experiments/parameter_sweep.py
python experiments/noise_robustness.py
```

### Run Streamlit dashboard

```bash
streamlit run dashboard.py
```

Dashboard provides:
- Reputation trajectories
- Truth score distributions
- Interaction/agreement heatmap
- Claim timeline across rounds

---

## Experiment Workflows

### 1) Parameter sweep
Use `experiments/parameter_sweep.py` to evaluate mechanism sensitivity under varying settings (e.g., users/rounds/noise assumptions).

### 2) Noise robustness
Use `experiments/noise_robustness.py` to test stability under imperfect truth signal conditions.

Recommended outputs to track:
- Average reward by user type
- Reputation convergence/divergence
- Truth-score drift over rounds
- Mechanism stability under perturbations

---

## Dashboard

`dashboard.py` offers an interview-ready UI to run and inspect simulations interactively.

Typical flow:
1. Select number of users and rounds
2. Set random seed
3. Run simulation
4. Inspect generated charts and table snapshots

---

## Development & Quality

If using Poetry, dev dependencies are already declared in `pyproject.toml`:
- `pytest`, `pytest-cov`
- `ruff`, `black`, `mypy`
- `pre-commit`, `coverage`

Suggested checks:

```bash
# Formatting
black .

# Linting
ruff check .

# Type checking
mypy src

# Tests
pytest -q
```

---

## Troubleshooting

- **Model download delays / network issues**  
  First run may download transformer assets; ensure internet access and retry.

- **Out-of-memory with larger settings**  
  Reduce number of users/rounds and rerun.

- **Streamlit not found**  
  Install dependencies in the active environment:
  `pip install -r requirements.txt` or `poetry install`.

- **Config/data path errors**  
  Verify `config.yaml` paths and data files exist under `data/`.

---

## Roadmap

- Add explicit CLI entrypoints for simulation orchestration
- Add persisted experiment tracking (e.g., MLflow integration path)
- Add stronger unit/integration test coverage per module
- Add containerized runtime profile for reproducible deployments

---

## License

MIT License.
