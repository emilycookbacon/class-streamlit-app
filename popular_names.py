import pandas as pd
import plotly.express as px
import streamlit as st

# create a title
st.title('Popular Name Trends')


# read in the data
url = 'https://github.com/esnt/Data/raw/main/Names/popular_names.csv'
df = pd.read_csv(url)

# create the mini dataframe
# this asks for an input, where I set the default value as 'John'
name = st.text_input('Enter a name', value = 'John') 
name_df = df[df['name']==name]

st.header(f'{name} over time')

tab1, tab2 = st.tabs(["Female", "Male"])

with tab1:
    plot_df = name_df[name_df['sex']== 'F']
    fig_f = px.line(data_frame = plot_df, x = 'year', y = 'n')
    st.plotly_chart(fig_f)

with tab2:
    plot_df = name_df[name_df['sex']== 'M']
    fig_m = px.line(data_frame = plot_df, x = 'year', y = 'n')
    st.plotly_chart(fig_m)


with st.sidebar:
    year = st.slider("Choose a year", 1910, 2021)
    st.header(f'Top names by {year}')
    year_df = df[df['year']== year]
    # st.dataframe(year_df)

    girls_names = year_df[year_df.sex=='F'].sort_values('n', ascending=False).head(5)['name']
    boys_names = year_df[year_df.sex=='M'].sort_values('n', ascending=False).head(5)['name']

    top_names = pd.concat([girls_names.reset_index(drop=True), boys_names.reset_index(drop=True)], 
          ignore_index=True, axis=1)
    top_names.columns = ['Girls','Boys'] 
    top_names.index = [1,2,3,4,5]
    st.dataframe(top_names)   



# commented out for the time being
# name_df = name_df.groupby('year')['n'].sum().reset_index()

# create figure
# fig = px.line(data_frame = name_df, x = 'year', y = 'n')

# use plotly figure 
# update header to use the variable
# st.header(f'{name} over time')
# st.plotly_chart(fig)

