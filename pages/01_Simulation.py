import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

st.set_page_config(page_title="결정화 시뮬레이션", layout="centered")
st.title("🔬 결정화 시뮬레이션 (지구 vs 우주)")

# 선택 방식: 버튼형 radio로 설정 (label 영어, 나머지 한글)
step = st.radio("단계를 선택하세요:", ["Stage 1: Particle Movement", "Stage 2: Crystal Growth"], index=0)
env = st.radio("🌍 환경 선택", ["지구", "우주"], horizontal=True)

n_particles = 80
positions = np.random.rand(n_particles, 2) * 10

# 실시간으로 움직이게 반복문 구현
fig, ax = plt.subplots(figsize=(4, 4))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_xticks([])
ax.set_yticks([])
ax.set_facecolor('#f4f4f4')

# 사각형 실험통 그리기
container = plt.Rectangle((0.5, 0.5), 9, 9, color='#d6eaf8', fill=True, alpha=0.15)
ax.add_patch(container)

stframe = st.empty()  # 반복 출력용

for frame in range(30):
    ax.cla()
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_facecolor('#f4f4f4')
    ax.add_patch(plt.Rectangle((0.5, 0.5), 9, 9, color='#d6eaf8', fill=True, alpha=0.15))

    if step == "Stage 1: Particle Movement":
        for i in range(n_particles):
            if env == "지구":
                positions[i, 1] -= np.random.rand() * 0.2  # 침강
            else:
                positions[i] += np.random.randn(2) * 0.2  # 무작위 확산

    elif step == "Stage 2: Crystal Growth":
        center = np.array([5, 5])
        for i in range(n_particles):
            direction = center - positions[i]
            if env == "지구":
                positions[i] += direction * 0.2 + np.random.randn(2) * 0.1
            else:
                positions[i] += direction * 0.05 + np.random.randn(2) * 0.02

    # 제목만 영어
    ax.set_title(f"{step} ({env})")
    ax.scatter(positions[:, 0], positions[:, 1], alpha=0.6, color="#2980b9")
    stframe.pyplot(fig)
    time.sleep(0.1)
