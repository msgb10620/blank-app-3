import streamlit as st

# 1. 앱 제목 및 기본 데이터 설정
st.title("🍕 나만의 피자 만들기 대작전!")
st.subheader("원하는 토핑을 골라 나만의 피자를 디자인해 보세요.")

# 제공하는 토핑 리스트 (출력용 문자열 정리)
available_toppings = ['페퍼로니', '올리브', '파인애플', '소고기', '소세지']

# 세션 상태(Session State) 초기화: 선택한 토핑을 저장할 리스트
if 'my_toppings' not in st.session_state:
    st.session_state.my_toppings = []

# --- 사이드바: 메뉴판 제공 ---
st.sidebar.header("📜 토핑 메뉴판")
st.sidebar.write(available_toppings)

# --- 메인 화면 ---

# 2. 토핑 개수 입력 받기
count = st.number_input(
    '넣고 싶은 피자 토핑의 총 개수를 입력하세요 (최대 5개):', 
    min_value=1, 
    max_value=5, 
    value=1, 
    step=1
)

st.info(f"선택하신 토핑 개수는 총 **{count}개**입니다.")

# 3. 토핑 선택 (다중 선택 위젯 활용으로 기존 input 창 여러 번 뜨는 문제 해결)
# 사용자가 직관적으로 고를 수 있게 멀티셀렉트(multiselect)를 활용했습니다.
choices = st.multiselect(
    '메뉴에서 원하는 토핑을 골라주세요:', 
    options=available_toppings,
    max_selections=count  # 위에서 입력한 개수만큼만 선택 가능하도록 제한
)

# 현재 선택한 토핑 보여주기
if choices:
    st.write("### 🛒 현재 선택한 토핑")
    st.success(f"당신이 선택한 토핑은: **{', '.join(choices)}** 입니다.")



# 4. 주문 완료 및 추가 토핑 섹션
st.divider() # 구분선
st.write("### 🏁 주문을 완료하시겠습니까?")

# 라디오 버튼을 이용해 주문 완료 여부 확인
order_status = st.radio("주문 상태를 선택하세요:", ("아직 고르는 중 (추가 토핑 필요)", "주문 완료"))

if order_status == "주문 완료":
    if len(choices) == 0:
        st.warning("🚨 토핑을 최소 1개 이상 선택해야 주문이 가능합니다!")
    else:
        st.success("🎉 주문이 완료되었습니다! 맛있는 피자를 만들어 드릴게요!")
        
        # 최종 주문서 시각화 (데이터프레임 활용)
        st.balloons() # 축하 효과
        st.write("#### 📋 최종 주문서")
        st.dataframe({"선택한 토핑 내역": choices}, use_container_width=True)

else:
    st.info("💡 추가하고 싶은 토핑이 있다면 위 메뉴에서 더 골라주세요!")
    # 추가 토핑을 주관식으로 입력받고 싶을 때를 위한 텍스트 입력창
    extra_topping = st.text_input("추가로 요청할 토핑이 있다면 적어주세요:")
    if extra_topping:
        st.success(f"✍️ 추가 요청 토핑: **{extra_topping}** (주문 시 함께 반영됩니다.)")