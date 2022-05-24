import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def run_eda() :

    st.subheader('데이터 분석')

    df = pd.read_csv('data/review2.csv', index_col=0)
    st.dataframe(df)


    st.write('리뷰의 길이별 히스토그램')
    fig1 = plt.figure()
    df['length'].hist()
    st.pyplot(fig1)


    st.write('리뷰의 길이가 가장 긴 데이터')
    st.dataframe(df.loc[df['length'] == df['length'].max(), ])


    st.write('리뷰의 길이가 가장 짧은 데이터')
    st.dataframe(df.loc[df['length'] == df['length'].min(), ])


    st.write('각 별점 별 리뷰의 갯수')
    my_order = df['stars'].value_counts().index

    fig2 = plt.figure()
    sns.countplot(data = df, x = 'stars', order = my_order)
    st.pyplot(fig2)


    # 리뷰의 별점을 셀렉트 박스로 만들어서 유저에게 보여준다.
    # 유저는 4를 선택하면, 별점이 4인 데이터만 가져와서
    # 별점이 4인 데이터만 가져와서 별점과 리뷰내용만 화면에 보여준다.
    
    star_menu = sorted(df['stars'].unique())
    star_choice = st.selectbox('별점 선택', star_menu)
    
    st.dataframe(df.loc[df['stars'] == star_choice , ['stars', 'text']])
    
