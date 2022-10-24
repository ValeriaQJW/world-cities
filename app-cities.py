import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

st.title('World cities')
df = pd.read_csv('worldcities.csv')

population_filter = st.slider('Minimal Population (Millions):', 0.0, 40.0, 3.6)

capital_filter = st.sidebar.multiselect(
     'Capital Selector',
     df.capital.unique(),  # options 提取类
    df.capital.unique())  # 设置初始值


form = st.sidebar.form("country_form")
country_filter = form.text_input('Country Name (enter ALL to reset)', 'ALL')
form.form_submit_button("Apply")


df = df[df.population >= population_filter]

df = df[df.capital.isin(capital_filter)] # 选择的红框赋值

if country_filter!='ALL':
    df = df[df.country == country_filter] # 自己填国家名栏

st.map(df) # 设置图片

st.subheader('City Details:')
st.write(df[['city', 'country', 'population','admin_name']])\

st.subheader('Total Population By Country')
fig, ax = plt.subplots(figsize=(20, 5))
pop_sum = df.groupby('country')['population'].sum()
pop_sum.plot.bar(ax=ax)
st.pyplot(fig)