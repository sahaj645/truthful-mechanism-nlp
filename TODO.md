# Production Upgrade TODO - Graphs for Political Discourse User Interactions

## Phase 1: Simulation & Data (Completed)
- [x] Create `src/simulation.py`: Multi-agent political discourse sim (users submit claims, truth scoring, reputation updates, interactions).
- [x] Add sample data `data/political_claims.csv`: claims, user_ids, ground_truth.
- [x] Add `data/fact_base.txt` for fact-consensus reference.
- [x] Update `src/*`: Adapted to political context with fact-base consensus + mechanism reward.

## Phase 2: Dashboard & Graphs (Completed)
- [x] Create `dashboard.py`: Streamlit app with:
  | Graph | Description |
  |-------|-------------|
  | Reputation Trajectories | Plotly line chart: user rep over sim steps |
  | Truth Score Distribution | Histogram: truth scores per user/round |
  | Interaction Network | NetworkX/Plotly: users connected by agreement sim |
  | Claim Timeline | Scatter: claims over time colored by truth |
- [x] Controls: #users, #rounds, seed.

## Phase 3: Polish (Partially Completed)
- [ ] MLflow: Track sim params/results.
- [x] requirements.txt: Added streamlit, plotly.
- [ ] Tests: pytest for sim.
- [ ] README: Demo instructions, GIF placeholder.
- [ ] Commits: Per feature.

## Phase 4: Advanced (Optional)
- [ ] DB integration.
- [ ] FastAPI backend.
- [ ] Docker.
