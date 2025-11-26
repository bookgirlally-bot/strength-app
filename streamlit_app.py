import streamlit as st
import openai

st.set_page_config(page_title="나의 강점 찾기", page_icon="✨")

st.title("✨ 나의 강점 찾기 프로그램 (긍정심리학 VIA 기반)")
st.write("당신의 경험을 토대로 AI가 VIA 24강점 중 상위 5개 강점을 분석해드립니다.")

# 🔑 OpenAI API Key 입력
api_key = st.text_input("🔑 OpenAI API Key를 입력하세요.", type="password")

if api_key:
    openai.api_key = api_key

    st.subheader("📘 질문에 답해주세요")

    q4 = st.text_area("1) 최근 1년 동안 ‘몰입했던 경험’을 알려주세요.")
    q5 = st.text_area("2) 주변 사람들이 자주 칭찬하는 당신의 점은 무엇인가요?")
    q6 = st.text_area("3) 힘들었지만 포기하지 않고 해낸 경험은 무엇인가요?")
    q7 = st.text_area("4) 당신이 잘한다고 느끼는 능력/태도/성격을 적어주세요.")
    q8 = st.text_area("5) 당신에게 가장 중요한 가치는 무엇인가요?")

    if st.button("🧠 강점 분석하기"):
        with st.spinner("AI가 분석 중입니다... 잠시만 기다려주세요!"):
            
            prompt = f"""
            너는 마틴 셀리그만의 긍정심리학 전문가이자 VIA 24강점 분석 코치다.
            아래 사용자의 답변을 바탕으로 상위 5개 VIA 강점을 찾아 분석하라.

            [몰입 경험] {q4}
            [칭찬 경험] {q5}
            [해낸 경험] {q6}
            [잘하는 점] {q7}
            [중요 가치] {q8}

            분석 기준:
            1) VIA 24강점에서 상위 5개 강점 선택
            2) 각 강점별 근거를 사용자의 답변에서 직접 찾아 서술
            3) 강점이 이 사람의 삶에 주는 긍정적 영향 설명
            4) 일상/관계/일·학습에서 활용 전략 2~3개씩 제안
            5) 마지막에 이 사람에게 주는 따뜻한 응원 한 문장 작성

            모든 내용은 한국어로 작성해라.
            """

            try:
                response = openai.ChatCompletion.create(
                    model="gpt-4o-mini",
                    messages=[{"role": "user", "content": prompt}]
                )

                result = response["choices"][0]["message"]["content"]
                st.success("분석이 완료되었습니다!")
                st.write(result)

            except Exception as e:
                st.error(f"오류 발생: {e}")
else:
    st.info("OpenAI API Key를 입력하면 분석 기능이 활성화됩니다.")
