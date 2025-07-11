import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

st.set_page_config(page_title="결정화 시뮬레이션", layout="centered")
st.title("🔬 결정화 시뮬레이션 (지구 vs 우주)")

# 선택 방식: 슬라이더 → 버튼형 radio로 변경
step = st.radio("결정화 단계를 선택하세요:", ["1단계: 입자 운동", "2단계: 결정 성장"], index=0)
env = st.radio("🌍 중력 환경을 선택하세요", ["지구", "우주"], horizontal=True)

n_particles = 80
positions = np.random.rand(n_particles, 2) * 10

fig, ax = plt.subplots(figsize=(4, 4))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_xticks([])
ax.set_yticks([])
ax.set_facecolor('#f4f4f4')

# 실험실 통 모양 그리기
container = plt.Circle((5, 5), 4.5, color='#d6eaf8', fill=True, alpha=0.2)
ax.add_patch(container)

if step == "1단계: 입자 운동":
    st.subheader("1단계: 무중력 상태에서의 입자 운동")
    st.markdown("입자들이 침강하지 않고 통 안에서 자유롭게 퍼지는 모습을 보여줍니다.")

    for i in range(n_particles):
        if env == "지구":
            positions[i, 1] -= np.random.rand() * 0.2  # 침강
        else:
            positions[i] += np.random.randn(2) * 0.15  # 무작위 확산

    ax.scatter(positions[:, 0], positions[:, 1], alpha=0.6, color="#2980b9")
    ax.set_title(f"입자 운동 시뮬레이션 - {env} 환경")
    st.pyplot(fig)

elif step == "2단계: 결정 성장":
    st.subheader("2단계: 결정 성장")
    st.markdown("입자들이 중심으로 모여들며 천천히 결정을 형성합니다.")

    center = np.array([5, 5])
    for i in range(n_particles):
        direction = center - positions[i]
        if env == "지구":
            positions[i] += direction * 0.25 + np.random.randn(2) * 0.1
        else:
            positions[i] += direction * 0.05 + np.random.randn(2) * 0.02

    ax.scatter(positions[:, 0], positions[:, 1], alpha=0.6, color="#27ae60")
    ax.set_title(f"결정 성장 시뮬레이션 - {env} 환경")
    st.pyplot(fig)

