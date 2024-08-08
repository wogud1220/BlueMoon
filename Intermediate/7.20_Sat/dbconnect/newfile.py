import streamlit as st
import psycopg2

def exec_db(command):
# 데이터베이스와 통신할 수 있또록 설정을 입력
    conn = psycopg2.connect(
        # ip 주소 == 내 데베가 어디에 있느냐....
        host = 'localhost',
        # 접속하고자하는 데베 이름, 권한있는 사용자 이름, 비번
        # pgadmin-server-postgresql-properties-connection
        dbname = 'postgres',
        user='postgres',
        password = 'root',
        port = 5432
    )

    # 연결을 생성
    cursur = conn.cursor()
    # 명령어 입력
    cursur.execute(command)#select * from fbs.

    # fetchall(), rows 변수에 담음
    rows = cursur.fetchall()

    result = []
    for row in rows:
        result.append(row)
    cursur.close()
    conn.close()
    return result

st.write('DB connectro')


command = st.text_input('input sql command')

if command:
    re = exec_db(command)

    st.divider()
    st.write('db result is ..!')
    st.text(re)