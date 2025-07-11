import streamlit as st
import plotly.graph_objs as go
import numpy as np

st.set_page_config(page_title="결정화 시뮬레이션 (지구 vs 우주)", layout="centered")
st.title("🔬 결정화 시뮬레이션 (지구 vs 우주)")

# 🌍 환경 선택
env = st.radio("결정화 환경 선택", ["지구", "우주"], horizontal=True)

# 단계 선택
stage = st.radio("단계 선택", ["Stage 1: Particle Movement", "Stage 2: Crystal Growth"], horizontal=True)

if stage == "Stage 1: Particle Movement":
    # 입자 설정
    n_particles = 80
    steps = 30
    positions = np.random.rand(n_particles, 2) * 10
    frames = []

    # 시뮬레이션 루프
    for step_num in range(steps):
        if env == "지구":
            positions[:, 1] -= np.random.rand(n_particles) * 0.2  # 중력 침강
        else:
            positions += np.random.randn(n_particles, 2) * 0.2  # 무중력 확산

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

elif stage == "Stage 2: Crystal Growth":
    st.image("https://raw.githubusercontent.com/your_username/your_repo/main/crystal_growth_%s.gif" % ("earth" if env == "지구" else "space"),
             caption=f"Stage 2: Crystal Growth ({env})",
             use_column_width=True)

# 🧪 설명
st.markdown("---")
descriptions = {
    ("Stage 1: Particle Movement", "지구"): "지구 환경에서는 중력과 밀도 차이에 의해 입자가 침강하고, 대류 현상으로 인해 아래로 몰립니다.",
    ("Stage 1: Particle Movement", "우주"): "우주에서는 미세중력 환경으로 인해 대류와 침강이 억제되어 입자들이 자유롭게 확산됩니다.",
    ("Stage 2: Crystal Growth", "지구"): "지구에서는 빠른 결정화가 이루어지지만, 대류에 의해 구조적 결함이 많이 발생할 수 있습니다.",
    ("Stage 2: Crystal Growth", "우주"): "우주 환경에서는 결정 성장 속도가 느리지만 균일하며, 결함이 적고 구조가 정교한 결정이 형성됩니다."
}
st.markdown(f"**설명:** {descriptions[(stage, env)]}")

