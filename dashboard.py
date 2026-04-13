import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from src.simulation import PoliticalDiscourseSimulation


st.set_page_config(page_title="Political Discourse Interaction Graphs", layout="wide")
st.title("Political Discourse: User Interaction Graphs")
st.caption("Interview-ready simulation dashboard for truth/reputation dynamics.")

with st.sidebar:
    st.header("Simulation Controls")
    n_users = st.slider("Number of users", min_value=3, max_value=20, value=8, step=1)
    n_rounds = st.slider("Number of rounds", min_value=5, max_value=50, value=15, step=1)
    seed = st.number_input("Random seed", value=42, step=1)

run_button = st.button("Run Simulation", type="primary")

if run_button:
    sim = PoliticalDiscourseSimulation(n_users=n_users, n_rounds=n_rounds, seed=int(seed))
    df = sim.run()

    st.subheader("Simulation Data")
    st.dataframe(df.head(20), use_container_width=True)

    c1, c2 = st.columns(2)

    with c1:
        st.markdown("### 1) Reputation Trajectories")
        rep_df = df[["round", "user_id", "reputation"]].copy()
        fig_rep = px.line(rep_df, x="round", y="reputation", color="user_id", markers=True)
        st.plotly_chart(fig_rep, use_container_width=True)

    with c2:
        st.markdown("### 2) Truth Score Distribution")
        fig_truth = px.histogram(df, x="truth_score", color="user_id", nbins=20, barmode="overlay")
        st.plotly_chart(fig_truth, use_container_width=True)

    c3, c4 = st.columns(2)

    with c3:
        st.markdown("### 3) Interaction Heatmap (Avg Agreement)")
        heat = df.pivot_table(index="user_id", values="agreement_score", aggfunc="mean").sort_index()
        heat_matrix = pd.DataFrame(index=heat.index, columns=heat.index, data=0.0)
        for i in heat.index:
            for j in heat.index:
                heat_matrix.loc[i, j] = float((heat.loc[i, "agreement_score"] + heat.loc[j, "agreement_score"]) / 2)
        fig_heat = px.imshow(heat_matrix, labels=dict(x="User", y="User", color="Agreement"))
        st.plotly_chart(fig_heat, use_container_width=True)

    with c4:
        st.markdown("### 4) Claims Timeline (Truth vs Round)")
        timeline = df.copy()
        timeline["claim_short"] = timeline["claim_text"].str.slice(0, 40) + "..."
        fig_timeline = px.scatter(
            timeline,
            x="round",
            y="truth_score",
            color="user_id",
            size="reward",
            hover_data=["claim_short", "ground_truth", "reputation"],
        )
        st.plotly_chart(fig_timeline, use_container_width=True)

    st.success("Graphs generated successfully.")
else:
    st.info("Set parameters and click 'Run Simulation' to generate interaction graphs.")
