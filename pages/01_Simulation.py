import streamlit as st
import plotly.graph_objs as go
import numpy as np

st.set_page_config(page_title="결정화 시뮬레이션 (Plotly)", layout="centered")
st.title("🔬 결정화 시뮬레이션 (지구 vs 우주)")

# 🌍 환경 선택
env = st.radio("결정화 환경 선택", ["지구", "우주"], horizontal=True)

# 단계 선택
stage = st.radio("단계 선택", ["Stage 1: Particle Movement", "Stage 2: Crystal Growth"], horizontal=True)

# 입자 설정
n_particles = 80
steps = 30
positions = np.random.rand(n_particles, 2) * 10
frames = []

# 🌌 시뮬레이션 루프
for step_num in range(steps):
    if stage == "Stage 1: Particle Movement":
        if env == "지구":
            positions[:, 1] -= np.random.rand(n_particles) * 0.2  # 중력 영향에 의한 침강
        else:
            positions += np.random.randn(n_particles, 2) * 0.2  # 무중력 확산 (대류·침강 억제)

    elif stage == "Stage 2: Crystal Growth":
        center = np.array([5, 5])
        for i in range(n_particles):
            direction = center - positions[i]
            if env == "지구":
                positions[i] += direction * 0.2 + np.random.randn(2) * 0.1  # 빠르고 불균일하게 응집
            else:
                positions[i] += direction * 0.05 + np.random.randn(2) * 0.02  # 느리지만 균일하게 성장

    frames.append(go.Frame(data=[
        go.Scatter(
            x=positions[:, 0],
            y=positions[:, 1],
            mode='markers',
            marker=dict(size=6, color='royalblue', opacity=0.7)
        )
    ], name=str(step_num)))

# 초기 프레임
scatter = go.Scatter(
    x=positions[:, 0],
    y=positions[:, 1],
    mode='markers',
    marker=dict(size=6, color='royalblue', opacity=0.7)
)

layout = go.Layout(
    title=f"{stage} ({env})",
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

# 🧪 설명 추가
descriptions = {
    ("Stage 1: Particle Movement", "지구"): "지구 환경에서는 중력과 밀도 차이에 의해 침강 및 대류 현상이 발생하여 입자들이 아래로 가라앉습니다.",
    ("Stage 1: Particle Movement", "우주"): "우주에서는 미세중력 환경으로 인해 침강이 억제되고, 입자들이 무작위로 확산되어 공간을 떠다니게 됩니다.",
    ("Stage 2: Crystal Growth", "지구"): "지구에서는 빠른 결정화가 이루어지나, 대류로 인해 결정 사이에 결함이 많이 생깁니다.",
    ("Stage 2: Crystal Growth", "우주"): "우주에서는 느리지만 균일한 결정 성장이 가능하여, 더 완벽하고 고품질의 결정 구조가 형성됩니다."
}

st.markdown(f"**설명:** {descriptions[(stage, env)]}")

