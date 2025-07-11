import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

st.set_page_config(page_title="Crystallization Simulation", layout="centered")
st.title("🔬 Crystallization Simulation (Earth vs Space)")

# 선택 방식: 버튼형 radio로 설정 (label이 깔끔하게 보이도록 영문 처리)
step = st.radio("Choose simulation stage:", ["Stage 1: Particle Movement", "Stage 2: Crystal Growth"], index=0)
env = st.radio("🌍 Environment", ["Earth", "Space"], horizontal=True)

n_particles = 80
positions = np.random.rand(n_particles, 2) * 10  # 위치 초기화는 매 프레임마다 새로 되지 않도록 아래로 이동

# 실시간으로 움직이게 반복문으로 구현
fig, ax = plt.subplots(figsize=(4, 4))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_xticks([])
ax.set_yticks([])
ax.set_facecolor('#f4f4f4')

# 사각형 실험통 그리기
container = plt.Rectangle((0.5, 0.5), 9, 9, color='#d6eaf8', fill=True, alpha=0.15)
ax.add_patch(container)

stframe = st.empty()  # 반복 출력 위한 공간

for frame in range(30):
    ax.cla()
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_facecolor('#f4f4f4')
    ax.add_patch(plt.Rectangle((0.5, 0.5), 9, 9, color='#d6eaf8', fill=True, alpha=0.15))

    if step == "Stage 1: Particle Movement":
        st.subheader("Stage 1: Particle Movement")
        st.markdown("In a microgravity environment, particles float freely without settling.")

        for i in range(n_particles):
            if env == "Earth":
                positions[i, 1] -= np.random.rand() * 0.2  # 침강
            else:
                positions[i] += np.random.randn(2) * 0.2  # 무작위 확산

    elif step == "Stage 2: Crystal Growth":
        st.subheader("Stage 2: Crystal Growth")
        st.markdown("Particles gather slowly toward the center to form crystals.")

        center = np.array([5, 5])
        for i in range(n_particles):
            direction = center - positions[i]
            if env == "Earth":
                positions[i] += direction * 0.2 + np.random.randn(2) * 0.1
            else:
                positions[i] += direction * 0.05 + np.random.randn(2) * 0.02

    ax.scatter(positions[:, 0], positions[:, 1], alpha=0.6, color="#2980b9")
    ax.set_title(f"Simulation: {env} - {step}")
    stframe.pyplot(fig)
    time.sleep(0.1)
