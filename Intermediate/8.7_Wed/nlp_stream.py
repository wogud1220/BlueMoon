#스트림릿 사용
import streamlit as st
#자연어 처리와 관련된 패키지 
import spacy 
#텍스트 전처리 패키지
import neattext as nt 
# 정규표현식 가-힣
import re
#텍스트 처리, 감정분석 패키지
from textblob import TextBlob
#시각화 및 번역 패키지
import matplotlib.pyplot as plt
import matplotlib 
from wordcloud import WordCloud
from deep_translator import GoogleTranslator
#카운팅용 함수
from collections import Counter

def text_anlysis(text):
    #자연어처리 spacy -> en_core_web_sm(영어 처리) 모델 로드
    nlp = spacy.load("en_core_web_sm")
    #입력한 text를, nlp 전처리기를 활용해서 doc 변수에 저장
    doc = nlp(text)
    #doc에 저장된 토큰화된 데이터를
    #Token, Lemma 라는 라벨을 붙여 all_data에 저장
    #이 함수가 실행된 후 최종적으로 결과를 전달
    all_Data = [('"Token" : {}, \n "Lemma: : {} '.format(token.text, token.lemma_)) for token in doc]
    return all_Data

# 입력한 텍스트를 저장히는 함수
def summarize_text(text, num_sentence = 3):


    # 입력한 텍스트를 정리
    # text 데이터 중에서 알파벳이 아닌 것을 공백으로 치환하고 lower 처리해라
    cleaned_text = re.sub(r'[^a-zA-Z]', ' ', text).lower()

    words = cleaned_text.split()
    
    # words의 각 단어의 빈도수를 계산
    words_freq = Counter(words)


    # 얼마나 빈번하게 나타났는가 정렬
    sorted_words_freq = sorted(words_freq, key=words_freq.get, reverse=True)

    #top의 3개의빈번하게 나타나는 단어 추출
    top_words = sorted_words_freq[:num_sentence]

    
    summary = ' '.join(top_words)

    return summary


def main():
    subheader = """
    <div style="background-color:white; padding:8px;">
    <h3 style="color:black">텍스트 분석 및 감성분석</h1>
    </div>
    """

    title = '자연어 처리 프로젝트'
    st.title(title)
    st.markdown(subheader, unsafe_allow_html=True)
    st.sidebar.title('NLP project')
    menu = st.sidebar.selectbox('Menu', ['Text Analyse', 'Emotion Analyse', '번역', '이 프로젝트에 대하여'])



    if menu == 'Text Analyse':
        raw_text = st.text_area("Text Input", "여기에 영어 텍스트를 입력하세요", height =  300)

        # 버튼을 누르면 분석을 실행하도록 함
        if st.button('Start'):
            if len(raw_text) == 0:
                st.warning('텍스트가 입력되지 않음.')
            else:
                col1, col2 = st.columns(2)
                with col1:
                # 내가 입력한 자연어에 대한 기본적인 분석 정보
                # 누르면 나오는
                    with st.expander('Basic Info for NLP'):
                        word_desc = nt.TextFrame(raw_text).word_stats()
                        result_desc = {'len of text :', word_desc['Length of Text'],
                                    "Num of Vowels :", word_desc['Num of Vowels'],
                                    "Num of Stopwords :", word_desc['Num of Stopwords']}
                        st.write(result_desc)

                with col2:
                    with st.expander('preprocessedtext'):
                        # 불용어 제거
                        processed_text = str(nt.TextFrame(raw_text).remove_stopwords())
                        # 정제된 텍스트를 표기
                        st.write(processed_text)


    elif menu == 'Emotion Analyse':
        st.subheader('감성분석')
        raw_text = st.text_area("Text Input", "여기에 영어 텍스트를 입력하세요", height =  300)

        # 버튼을 누르면 분석을 실행하도록 함
        if st.button('Start'):
            if len(raw_text) == 0:
                st.warning('텍스트가 입력되지 않음.')

            else:
                blob = TextBlob(raw_text)
                result = blob.sentiment
                st.success(result)
    
    
    elif menu == '번역':
        raw_text = st.text_area('Text INput', '여기에 텍스트를 입력', height=300)

        if len(raw_text) < 3:
            st.warning('텍스트가 너무 짧습니다.')

        else:
            target_language = st.selectbox('번역할 언어를 선택', ['German', 'Spanish', 'French', 'Italian'])
            if target_language == 'German':
                target_lang = 'de'
            elif target_language == 'Spanish':
                target_lang = 'es'
            elif target_language == 'French':
                target_lang = 'fr'
            else :
                target_lang = 'it'
        

            if st.button('번역 시작'):
                translator = GoogleTranslator(source =
                'auto', target = target_lang)
                translated_text = translator.translate(raw_text)
                st.write(translated_text)



        return


if __name__ == "__main__":
    main()