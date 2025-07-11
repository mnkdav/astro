import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("🔬 결정화 시뮬레이션 (지구 vs 우주)")

step = st.slider("단계 선택", 1, 2, 1, format="Step %d")
env = st.radio("🌍 중력 환경을 선택하세요", ["지구", "우주"])

n_particles = 100
positions = np.random.rand(n_particles, 2) * 10

fig, ax = plt.subplots()

if step == 1:
    st.subheader("1단계: 입자 운동")
    st.markdown("무중력 환경에서는 입자들이 침강하지 않고 자유롭게 확산합니다.")

    for i in range(n_particles):
        if env == "지구":
            positions[i, 1] -= np.random.rand() * 0.3  # 침강
        else:
            positions[i] += np.random.randn(2) * 0.1  # 무작위 확산

    ax.scatter(positions[:, 0], positions[:, 1], alpha=0.6)
    ax.set_title(f"입자 분포 - {env} 환경")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    st.pyplot(fig)

elif step == 2:
    st.subheader("2단계: 결정 성장")
    st.markdown("입자들이 서서히 모여들며 느린 속도로 정밀한 결정을 형성합니다.")

    center = np.array([5, 5])
    for i in range(n_particles):
        direction = center - positions[i]
        if env == "지구":
            positions[i] += direction * 0.2 + np.random.randn(2) * 0.1
        else:
            positions[i] += direction * 0.05 + np.random.randn(2) * 0.02

    ax.scatter(positions[:, 0], positions[:, 1], alpha=0.6, color="green")
    ax.set_title(f"결정 형성 시뮬레이션 - {env} 환경")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    st.pyplot(fig)
