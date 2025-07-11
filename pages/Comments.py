import streamlit as st

st.set_page_config(page_title="💬 댓글창", layout="centered")
st.title("💬 의견 남기기")

st.markdown("""
이 페이지에서는 이 앱에 대한 **건의사항, 아이디어, 버그 신고** 등을 남길 수 있습니다.
아래에 자유롭게 댓글을 남겨주세요. 👇
""")

# 간단한 세션 상태로 댓글 저장
def init_comments():
    if "comments" not in st.session_state:
        st.session_state.comments = []

init_comments()

# 입력창
name = st.text_input("이름 (선택)")
comment = st.text_area("댓글을 입력하세요")

if st.button("댓글 남기기"):
    if comment.strip():
        st.session_state.comments.append({"name": name if name else "익명", "text": comment})
        st.success("댓글이 등록되었습니다!")
    else:
        st.warning("댓글을 입력해주세요.")

st.divider()

# 기존 댓글 표시
st.subheader("📌 남겨진 댓글")
if st.session_state.comments:
    for idx, c in enumerate(reversed(st.session_state.comments), 1):
        with st.expander(f"{c['name']}님의 댓글 #{idx}"):
            st.markdown(c['text'])
else:
    st.info("아직 등록된 댓글이 없습니다.")

