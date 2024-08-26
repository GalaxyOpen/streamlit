import streamlit as st 
import pandas as pd 

print("page reload") # session_state를 확인하기 위함. 
st.set_page_config(
    page_title = "포켓몬 도감", # 윈도우에 띄워진 크롬창의 이름 설정 
    page_icon="./images/monsterball.jpg" # 윈도우에 띄워진 크롬창의 아이콘 설정
)


st.title("streamlit 포켓몬 도감") # 제목 
st.text("포켓몬을 하나씩 추가해서 도감을 채워보세요!") # 일반 텍스트 

# st.subheader("포켓몬을 하나씩 추가해서 도감을 채워보세요!") # 부제목 
# st.markdown("포켓몬 **포켓몬**") # 마크다운 문법의 언어를 넣을 수 있음. 

type_emoji_dict = {
    "노말": "⚪",
    "격투": "✊",
    "비행": "🕊",
    "독": "☠️",
    "땅": "🌋",
    "바위": "🪨",
    "벌레": "🐛",
    "고스트": "👻",
    "강철": "🤖",
    "불꽃": "🔥",
    "물": "💧",
    "풀": "🍃",
    "전기": "⚡",
    "에스퍼": "🔮",
    "얼음": "❄️",
    "드래곤": "🐲",
    "악": "😈",
    "페어리": "🧚"
}

initial_pokemons = [
    {
        "name": "피카츄",
        "types": ["전기"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/pikachu.webp"
    },
    {
        "name": "누오",
        "types": ["물", "땅"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/nuo.webp",
    },
    {
        "name": "갸라도스",
        "types": ["물", "비행"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/garados.webp",
    },
    {
        "name": "개굴닌자",
        "types": ["물", "악"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/frogninja.webp"
    },
    {
        "name": "루카리오",
        "types": ["격투", "강철"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/lukario.webp"
    },
    {
        "name": "에이스번",
        "types": ["불꽃"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/acebun.webp"
    },
]


if "pokemons" not in st.session_state: # 세션 스테이트는 일종의 딕셔너리처럼 쓸 수 있음. 
    st.session_state.pokemons = initial_pokemons


with st.form(key="form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input(label="포켓몬 이름")
    with col2:
        types = st.multiselect(label="포켓몬 속성", 
                           options=list(type_emoji_dict.keys()),
                           max_selections = 2
                           )
    image_url = st.text_input(label="포켓몬 이미지 URL")            
    submit = st.form_submit_button(label="Submit")
    if submit:
        if not name:
            st.error("포켓몬의 이름을 입력해주세요")
        elif len(types) == 0:
            st.error("포켓몬의 속성을 적어도 한 개 선택해주세요.")
        else:
            st.success("포켓몬을 도감에 추가하였습니다.")
            st.session_state.pokemons.append({
                "name": name,
                "types":types,
                "image_url": image_url if image_url else "./images/monsterball.jpg"
            })        



for i in range(0, len(st.session_state.pokemons), 3):
    row_pokemons = st.session_state.pokemons [i:i+3] # 한줄에 표현할 포켓몬의 수 
    cols = st.columns(3)
    for j in range(len(row_pokemons)):
        with cols[j]:
            pokemon = row_pokemons[j]
            with st.expander(label =f"**{i+j+1}, {pokemon["name"]}**", expanded=True):
                st.image(pokemon["image_url"])
                emoji_types = [f"{type_emoji_dict[x]} {x}" for x in pokemon["types"]]
                st.subheader("/".join(emoji_types))
                delete_button = st.button(label="삭제", key=i+j, use_container_width=True)
                if delete_button:
                    print("delete button clicked!") # button 을 한 번 누르면 맨 위의 page reload로 올라가서 다시 내려온다. 
                    del st.session_state.pokemons[i+j] # 이 코드만 있을 경우, 정상적으로 동작하지 않는다. 
                    st.rerun() # 이 코드를 




























#적기 
# st.write("""
# # My first app Hello *world!*
# """)

# 파일 불러오기
# df = pd.read_csv("C:\streamlit\simple_chart_data.csv")
# st.line_chart(df)

# 슬라이더
# number = st.slider("Pick a number", 0, 100)

