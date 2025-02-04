import joblib
import streamlit as st
import numpy as np

# 유저에게 예측에 필요한 데이터를 입력받는다.
#성별, 나이, 연봉, 신용카드 부채, 순자산
def run_ml():
    gender=st.radio('성별 선택', ['남자','여자'])
    if gender == '남자':
        gender=1
    elif gender == '여자':
        gender=0
    age=st.number_input('나이 입력', min_value=18, max_value=100, value=20)
    annual_salary=st.number_input('연봉 입력', min_value=0, value=50000,step=1000)
    credit_card_debt=st.number_input('신용카드 부채 입력', min_value=0, value=10000,step=1000)
    net_worth=st.number_input('순자산 입력', min_value=0, value=60000,step=1000)
    #new_data=np.array([0,40,50000,10000,60000])
    new_data=np.array([gender,age,annual_salary,credit_card_debt,net_worth]).reshape(1,-1)
    print(new_data)

    #모델 불러오기
    regressor=joblib.load('model/regressor.pkl')
    #예측
    if st.button('예측하기'):
        result=regressor.predict(new_data)
        print(result[0])
        if result[0] < 0:
            st.error('가격이 0보다 작습니다. 다시 입력하세요.')
        else:
            result=round(result[0],2)
            result=format(result,',')
            print(type(result))
            st.success(f'예측 결과는 {result} 달러 입니다.')

            #round(result[0]) : 소수점 이하 반올림
            # 숫자에 ,넣어주기. format(result,',')

    