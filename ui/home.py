import streamlit as st

def run_home():
    st.subheader('자동차 가격을 예측하는 앱')
    st.write('데이터는 케글의 Car_purchasing_data.csv를 사용합니다.')
    st.write('EDA 탭에서는 데이터를 탐색하고, ML 탭에서는 데이터를 학습하여 예측합니다.')
    st.write('왼쪽의 사이드바에서 EDA 및 ML 메뉴를 선택하세요.')

    st.image('image/car.jpg', width=500)