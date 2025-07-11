import streamlit as st
import plotly.graph_objs as go
import numpy as np

st.set_page_config(page_title="결정화 시뮬레이션 (Plotly)", layout="centered")
st.title("🔬 결정화 시뮬레이션 (지구 vs 우주)")

# 환경 선택 버튼
env = st.radio("🌍 환경 선택", ["지구", "우주"], horizontal=True)

# 입자 설정
n_particles = 80
steps = 30
positions = np.random.rand(n_particles, 2) * 10
frames = []

# 입자 움직임 시뮬레이션
for step in range(steps):
    if env == "지구":
        positions[:, 1] -= np.random.rand(n_particles) * 0.2  # 침강
    else:
        positions += np.random.randn(n_particles, 2) * 0.2  # 무작위 확산 (우주)

    frames.append(go.Frame(data=[
        go.Scatter(
            x=positions[:, 0],
            y=positions[:, 1],
            mode='markers',
            marker=dict(size=6, color='royalblue', opacity=0.7)
        )
    ], name=str(step)))

# 기본 프레임
scatter = go.Scatter(
    x=positions[:, 0],
    y=positions[:, 1],
    mode='markers',
    marker=dict(size=6, color='royalblue', opacity=0.7)
)

# 레이아웃
layout = go.Layout(
    title=f"Stage 1: Particle Movement ({env})",
    xaxis=dict(range=[0, 10], showgrid=False, zeroline=False),
    yaxis=dict(range=[0, 10], showgrid=False, zeroline=False),
    width=500,
    height=500,
    updatemenus=[dict(
        type='buttons',
        showactive=False,
        buttons=[dict(label='▶ Play', method='animate', args=[None, {
            "frame": {"duration": 100, "redraw": True},
            "fromcurrent": True
        }])]
    )]
)

fig = go.Figure(data=[scatter], layout=layout, frames=frames)
st.plotly_chart(fig)

