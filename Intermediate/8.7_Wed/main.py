import streamlit as st

st.title('This is title')

st.header('This is Header')

st.subheader('this is Subheader')

st.text('this is text')

date ="2024-08-07"

st.write("this is write -> today is ",date)


st.markdown('markdown')
st.markdown('[naver](https://www.naver.com)')
#[] = 보여질 이름, () = 하이퍼링크

html_page = """
<div style="background-color:blue;padding:50px">
	<p style="color:yellow;font-size:5'px">Enjoy Streamlit!</p>
</div>
"""

st.markdown(html_page, unsafe_allow_html=True)

st.success('success')
st.info('info')
st.warning('warning')
st.error('error')

from PIL import Image

image = Image.open('../Bapuri/banana.png')

st.image(image, width=300, caption='Banana')

st.video('https://www.youtube.com/watch?v=T5dnEKqOaHw')


if st.button('happy birthday!'):
    st.balloons()


if st.checkbox('chekbox'):
    st.write('checked')


radio_buttons = st.radio('선호하는 색상은?', ['red', 'yellow', 'blue'])
if radio_buttons == 'red':
    st.write('Red rose')
elif radio_buttons == 'yellow':
    st.write('yellow rose')
else:
    st.write('blue rose')


city = st.selectbox('city', ['Seoul', 'Busan', 'Daegu', 'Incheon'])

job = st.multiselect('job', ['Developer', 'Designer', 'Scientist', 'Actor'])

# text_input = 한 줄 입력
name = st.text_input("What's your name?", "input your name")
if st.button('submit'):
    result = name.title()
    st.success(result)


# text_area = 여러 줄 입력 가능
message = st.text_area('Message', 'input your messages')

# 1~80 1칸씩
st.slider('How old are you', 1, 80, 1)


import pandas as pd
st.header('Pandas dataFrame')
df = pd.read_csv('./auto.csv')
st.write(df)

import time

my_bar = st.progress(0)
for v in range(100):
    my_bar.progress(v+1)
    time.sleep(0.1)