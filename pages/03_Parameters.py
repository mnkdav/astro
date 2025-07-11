import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

st.set_page_config(page_title="Interactive Parameters", layout="centered")

st.title("🧪직접 결정화 조건을 설정해보세요")

st.markdown("""
여기서는 여러분이 직접 결정 성장 조건을 조절해보며 시각적 결과에 어떤 영향을 주는지 체험해볼 수 있습니다. 직접 체험해보세용^^ """)

# 시각화 먼저 생성 후 슬라이더 노출 순서 변경
n_particles = 80
positions = np.random.rand(n_particles, 2) * 10
center = np.array([5, 5])

fig, ax = plt.subplots(figsize=(4, 4))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_xticks([])
ax.set_yticks([])
ax.set_facecolor('#f9f9f9')
container = plt.Rectangle((0.5, 0.5), 9, 9, color='#e0f7fa', fill=True, alpha=0.2)
ax.add_patch(container)

stframe = st.empty()

# 시뮬레이션 조건 슬라이더 (밑에 배치)
st.markdown("### 🔧 Set Your Parameters")
growth = st.slider("Crystal Growth Rate", 0.1, 1.0, 0.5)
viscosity = st.slider("Solvent Viscosity", 0.1, 1.0, 0.3)
time_steps = st.slider("Simulation Duration (steps)", 10, 50, 30)

# 실시간 시뮬레이션 반복
for frame in range(time_steps):
    ax.cla()
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_facecolor('#f9f9f9')
    ax.add_patch(plt.Rectangle((0.5, 0.5), 9, 9, color='#e0f7fa', fill=True, alpha=0.2))

    for i in range(n_particles):
        direction = center - positions[i]
        drift_strength = (1.0 - growth) * 0.3
        noise_strength = viscosity * 0.2
        positions[i] += direction * drift_strength + np.random.randn(2) * noise_strength

    ax.scatter(positions[:, 0], positions[:, 1], alpha=0.6, color="#6c5ce7")
    ax.set_title("Crystal Growth in Virtual Chamber")
    stframe.pyplot(fig)
    time.sleep(0.08)

st.markdown("""
🧠 **해설 가이드**
- 성장 속도가 **너무 빠르면** 결함이 많이 생길 수 있어요.
- 점도가 **높을수록** 입자의 이동이 어려워져 결정이 비대칭이 되기 쉬워요.
- 결정화 시간이 **너무 짧으면** 구조가 덜 자랄 수 있어요.

👉 여러분이 생각하는 이상적인 결정화 조건은 무엇인가요?
""")
