import streamlit as st
import requests
import os

FASTAPI_URL = os.getenv("FASTAPI_URL", "http://backend:8000")

st.set_page_config(
    page_title="오늘 뭐 입지? 👔",
    page_icon="👔",
    layout="centered",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Noto+Sans+KR:wght@300;400;500;700&display=swap');

html, body, [class*="css"] {
  font-family: 'Noto Sans KR', sans-serif;
  background-color: #F7F3EE;
}

/* ── 히어로 배너 ── */
.hero-banner {
  background: linear-gradient(135deg, #1a0533 0%, #3d1070 40%, #c0392b 100%);
  border-radius: 24px;
  padding: 3rem 2rem 2.5rem;
  text-align: center;
  margin-bottom: 2rem;
  position: relative;
  overflow: hidden;
}
.hero-banner::before {
  content: '';
  position: absolute;
  top: -50%; left: -50%;
  width: 200%; height: 200%;
  background: radial-gradient(ellipse at center, rgba(255,255,255,0.05) 0%, transparent 60%);
  pointer-events: none;
}
.hero-eyebrow {
  font-size: 0.7rem;
  letter-spacing: 0.3em;
  color: #D4A853;
  font-weight: 700;
  text-transform: uppercase;
  margin-bottom: 0.8rem;
}
.hero-title {
  font-family: 'Playfair Display', serif;
  font-size: 3rem;
  font-weight: 900;
  color: #ffffff;
  line-height: 1.1;
  margin-bottom: 0.6rem;
}
.hero-sub {
  font-size: 0.95rem;
  color: rgba(255,255,255,0.65);
  font-weight: 300;
  letter-spacing: 0.05em;
}

/* ── 입력 섹션 ── */
.section-label {
  font-size: 0.7rem;
  font-weight: 700;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: #9B8EA0;
  margin-bottom: 0.5rem;
}

/* ── 일정 선택 pills ── */
div[data-testid="stPills"] button {
  border-radius: 100px !important;
  border: 1.5px solid #E2D9F3 !important;
  background: #fff !important;
  color: #5a4a6a !important;
  font-size: 0.88rem !important;
  font-weight: 500 !important;
  font-family: 'Noto Sans KR', sans-serif !important;
  transition: all 0.18s !important;
}
div[data-testid="stPills"] button:hover {
  border-color: #8B5CF6 !important;
  color: #8B5CF6 !important;
  background: #F5F0FF !important;
}
div[data-testid="stPills"] button[kind="pillsActive"],
div[data-testid="stPills"] button[aria-pressed="true"] {
  background: linear-gradient(135deg, #1a0533, #8B5CF6) !important;
  border-color: transparent !important;
  color: #fff !important;
}

/* ── 추천 버튼 ── */
div[data-testid="stButton"] button {
  width: 100%;
  background: linear-gradient(135deg, #1a0533, #8B5CF6);
  color: white;
  border: none;
  padding: 1rem;
  border-radius: 14px;
  font-size: 1.05rem;
  font-weight: 700;
  font-family: 'Noto Sans KR', sans-serif;
  letter-spacing: 0.05em;
  cursor: pointer;
  transition: opacity 0.2s, transform 0.1s;
  box-shadow: 0 4px 20px rgba(139,92,246,0.35);
}
div[data-testid="stButton"] button:hover {
  opacity: 0.9;
  transform: translateY(-1px);
}

/* ── 날씨 카드 ── */
.weather-card {
  background: linear-gradient(135deg, #1a0533 0%, #8B5CF6 100%);
  border-radius: 20px;
  padding: 2rem;
  color: white;
  text-align: center;
  margin: 1.5rem 0;
  box-shadow: 0 8px 32px rgba(139,92,246,0.3);
}
.weather-city {
  font-size: 0.75rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  opacity: 0.7;
  margin-bottom: 0.4rem;
}
.weather-temp {
  font-family: 'Playfair Display', serif;
  font-size: 4rem;
  font-weight: 900;
  line-height: 1;
  margin: 0.3rem 0;
}
.weather-desc {
  font-size: 0.9rem;
  opacity: 0.85;
  margin-top: 0.3rem;
}

/* ── 콘셉트 박스 ── */
.concept-card {
  background: #ffffff;
  border-radius: 20px;
  padding: 1.8rem;
  margin: 1rem 0;
  border: 1px solid #EDE8F5;
  box-shadow: 0 2px 20px rgba(139,92,246,0.08);
  position: relative;
  overflow: hidden;
}
.concept-card::before {
  content: '';
  position: absolute;
  top: 0; left: 0;
  width: 100%; height: 4px;
  background: linear-gradient(90deg, #8B5CF6, #EC4899, #D4A853);
}
.concept-eyebrow {
  font-size: 0.65rem;
  letter-spacing: 0.25em;
  text-transform: uppercase;
  color: #8B5CF6;
  font-weight: 700;
  margin-bottom: 0.5rem;
}
.concept-name {
  font-family: 'Playfair Display', serif;
  font-size: 1.7rem;
  font-weight: 700;
  color: #1a0533;
  line-height: 1.2;
  margin-bottom: 0.5rem;
}
.concept-desc {
  font-size: 0.9rem;
  color: #6B5B7B;
  line-height: 1.6;
}

/* ── 아이템 카드 공통 ── */
.item-card {
  background: #ffffff;
  border-radius: 16px;
  padding: 1.2rem 1.4rem;
  margin: 0.6rem 0;
  border: 1px solid #F0EBF8;
  box-shadow: 0 1px 8px rgba(0,0,0,0.04);
}
.item-card-header {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 0.8rem;
}
.item-icon {
  width: 28px; height: 28px;
  border-radius: 8px;
  display: flex; align-items: center; justify-content: center;
  font-size: 0.9rem;
  flex-shrink: 0;
}
.item-label {
  font-size: 0.68rem;
  font-weight: 700;
  letter-spacing: 0.18em;
  text-transform: uppercase;
}
.tags-wrap {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}
.tag {
  display: inline-block;
  padding: 5px 12px;
  border-radius: 100px;
  font-size: 0.82rem;
  font-weight: 500;
  line-height: 1.3;
}

/* 컬러 테마별 */
.top-card   .item-icon { background: #ECFDF5; }
.top-card   .item-label { color: #059669; }
.top-card   .tag { background: #ECFDF5; color: #065F46; }

.bottom-card .item-icon { background: #EFF6FF; }
.bottom-card .item-label { color: #2563EB; }
.bottom-card .tag { background: #EFF6FF; color: #1E40AF; }

.outer-card { background: #FDF4FF; border-color: #E9D5FF; }
.outer-card .item-icon { background: #F3E8FF; }
.outer-card .item-label { color: #9333EA; }
.outer-card .tag { background: #F3E8FF; color: #6B21A8; }

.acc-card   .item-icon { background: #FFF7ED; }
.acc-card   .item-label { color: #D97706; }
.acc-card   .tag { background: #FFF7ED; color: #92400E; }

/* ── 팁 박스 ── */
.tip-card {
  background: linear-gradient(135deg, #FFF8F0, #FFF1E0);
  border-radius: 16px;
  padding: 1.2rem 1.4rem;
  margin: 0.6rem 0;
  border-left: 4px solid #F59E0B;
}
.tip-title {
  font-size: 0.68rem;
  font-weight: 700;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: #D97706;
  margin-bottom: 0.5rem;
}
.tip-text {
  font-size: 0.9rem;
  color: #92400E;
  line-height: 1.6;
}

/* ── 폼 인풋 스타일 ── */
.stTextInput input {
  border-radius: 12px !important;
  border: 1.5px solid #E2D9F3 !important;
  padding: 0.7rem 1rem !important;
  font-family: 'Noto Sans KR', sans-serif !important;
  font-size: 0.95rem !important;
  background: #fff !important;
}
.stTextInput input:focus {
  border-color: #8B5CF6 !important;
  box-shadow: 0 0 0 3px rgba(139,92,246,0.12) !important;
}
.stSelectbox > div > div {
  border-radius: 12px !important;
  border: 1.5px solid #E2D9F3 !important;
  background: #fff !important;
}

/* 구분선 */
.divider {
  height: 1px;
  background: linear-gradient(90deg, transparent, #E2D9F3, transparent);
  margin: 1.5rem 0;
}

/* 섹션 헤더 */
.result-section-title {
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: #9B8EA0;
  margin: 1.5rem 0 0.8rem;
}

/* 에러/스피너 */
.stAlert { border-radius: 12px !important; }
</style>
""", unsafe_allow_html=True)


# ── 히어로 ──────────────────────────────────────────────
st.markdown("""
<div class="hero-banner">
  <div class="hero-eyebrow">✦ AI OUTFIT CURATOR ✦</div>
  <div class="hero-title">오늘 뭐 입지?</div>
  <div class="hero-sub">날씨 · 일정 · 스타일로 완성하는<br>나만의 오늘의 코디</div>
</div>
""", unsafe_allow_html=True)


# ── 입력 폼 ─────────────────────────────────────────────
with st.form("outfit_form"):

    st.markdown('<div class="section-label">📍 지금 어느 도시에 계세요?</div>', unsafe_allow_html=True)
    city = st.text_input(
        "도시명",
        value="Seoul",
        placeholder="예: Seoul · Busan · Jeju · Tokyo",
        label_visibility="collapsed",
    )

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    st.markdown('<div class="section-label">📅 오늘 일정을 선택해주세요</div>', unsafe_allow_html=True)
    schedule_raw = st.pills(
        "일정",
        options=["🌹 데이트", "👫 친구 약속", "📚 학교", "💪 운동", "🏠 재택",
                 "🎉 파티", "🎂 생일/축하", "💍 결혼식", "💘 소개팅", "💼 비즈니스", "✈️ 여행", "⛺ 캠핑"],
        default="🌹 데이트",
        label_visibility="collapsed",
    )
    schedule = (schedule_raw or "🌹 데이트").split(" ", 1)[1]

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="section-label">🎨 선호 스타일</div>', unsafe_allow_html=True)
        style = st.selectbox(
            "스타일",
            options=["캐주얼", "미니멀", "스트릿", "포멀", "Y2K", "빈티지", "아메카지"],
            label_visibility="collapsed",
        )
    with col2:
        st.markdown('<div class="section-label">🧍 성별</div>', unsafe_allow_html=True)
        gender = st.selectbox(
            "성별",
            options=["남", "여", "무관"],
            label_visibility="collapsed",
        )

    st.markdown('<div style="height:0.8rem"></div>', unsafe_allow_html=True)
    submitted = st.form_submit_button("✦ 오늘의 코디 추천받기")


# ── 결과 출력 ────────────────────────────────────────────
if submitted:
    if not city.strip():
        st.error("도시명을 입력해주세요!")
    else:
        with st.spinner("날씨를 확인하고 코디를 선별하는 중..."):
            try:
                response = requests.post(
                    f"{FASTAPI_URL}/recommend",
                    json={
                        "city": city.strip(),
                        "schedule": schedule,
                        "style": style,
                        "gender": gender,
                    },
                    timeout=15,
                )

                if response.status_code == 200:
                    d = response.json()

                    # ── 날씨 카드 ──
                    st.markdown(f"""
                    <div class="weather-card">
                      <div class="weather-city">📍 {d['city']}</div>
                      <div class="weather-temp">{d['temperature']}°</div>
                      <div class="weather-desc">
                        <img src="https://openweathermap.org/img/wn/{d['weather_icon']}@2x.png"
                             style="width:36px;vertical-align:middle;filter:brightness(0) invert(1);opacity:.9">
                        {d['weather_desc']}
                      </div>
                    </div>
                    """, unsafe_allow_html=True)

                    # ── 콘셉트 카드 ──
                    st.markdown(f"""
                    <div class="concept-card">
                      <div class="concept-eyebrow">✦ Today's Concept</div>
                      <div class="concept-name">{d['concept']}</div>
                      <div class="concept-desc">{d['concept_desc']}</div>
                    </div>
                    """, unsafe_allow_html=True)

                    st.markdown('<div class="result-section-title">✦ 코디 아이템</div>', unsafe_allow_html=True)

                    # ── 상의 ──
                    top_tags = "".join(f'<span class="tag">{i}</span>' for i in d["top"])
                    st.markdown(f"""
                    <div class="item-card top-card">
                      <div class="item-card-header">
                        <div class="item-icon">👕</div>
                        <div class="item-label">상의 TOP</div>
                      </div>
                      <div class="tags-wrap">{top_tags}</div>
                    </div>
                    """, unsafe_allow_html=True)

                    # ── 하의 ──
                    bottom_tags = "".join(f'<span class="tag">{i}</span>' for i in d["bottom"])
                    st.markdown(f"""
                    <div class="item-card bottom-card">
                      <div class="item-card-header">
                        <div class="item-icon">👖</div>
                        <div class="item-label">하의 BOTTOM</div>
                      </div>
                      <div class="tags-wrap">{bottom_tags}</div>
                    </div>
                    """, unsafe_allow_html=True)

                    # ── 아우터 (조건부) ──
                    if d["outer"]:
                        st.markdown(f"""
                        <div class="item-card outer-card">
                          <div class="item-card-header">
                            <div class="item-icon">🧥</div>
                            <div class="item-label">아우터 OUTER</div>
                          </div>
                          <div class="tags-wrap"><span class="tag">{d['outer']}</span></div>
                        </div>
                        """, unsafe_allow_html=True)

                    # ── 악세서리 ──
                    acc_tags = "".join(f'<span class="tag">{i}</span>' for i in d["accessory"])
                    st.markdown(f"""
                    <div class="item-card acc-card">
                      <div class="item-card-header">
                        <div class="item-icon">👜</div>
                        <div class="item-label">악세서리 &amp; 슈즈</div>
                      </div>
                      <div class="tags-wrap">{acc_tags}</div>
                    </div>
                    """, unsafe_allow_html=True)

                    # ── 스타일 팁 ──
                    st.markdown(f"""
                    <div class="tip-card">
                      <div class="tip-title">💡 Style Tip</div>
                      <div class="tip-text">{d['style_tip']}</div>
                    </div>
                    """, unsafe_allow_html=True)

                else:
                    detail = response.json().get("detail", "알 수 없는 오류")
                    st.error(f"❌ {detail}")

            except requests.exceptions.ConnectionError:
                st.error("❌ 백엔드 서버에 연결할 수 없어요. 서버가 실행 중인지 확인해주세요.")
            except requests.exceptions.Timeout:
                st.error("❌ 응답 시간이 초과됐어요. 잠시 후 다시 시도해주세요.")
            except Exception as e:
                st.error(f"❌ 오류: {str(e)}")
