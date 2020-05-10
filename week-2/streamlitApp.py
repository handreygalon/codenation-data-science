import streamlit as st
import pandas as pd
import base64

def get_table_download_link(df):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a href="data:file/csv;base64,{b64}">Download csv file</a>'
    return href

def main():
    st.image('codenation.png', width= 200)
    st.title('AceleraDev Data Science')
    st.subheader('Week 2 - Pre data processing using Python')
    st.image('https://media.giphy.com/media/KyBX9ektgXWve/giphy.gif', width=200)
    
    file  = st.file_uploader('Chose the database you want to analyze (.csv)', type = 'csv')
    
    if file is not None:
        st.subheader('Analyzing the data')
        df = pd.read_csv(file)
        
        st.markdown('**Number of lines:**')
        st.markdown(df.shape[0])
        
        st.markdown('**Number of columns:**')
        st.markdown(df.shape[1])
        
        st.markdown('**Visualizing the dataframe**')
        number = st.slider('Chose the number of columns you want to see', min_value=1, max_value=20)
        st.dataframe(df.head(number))  # st.table
        
        st.markdown('**Column names:**')
        st.markdown(list(df.columns))

        # Create another dataframe to make it easier to create filters
        exploration = pd.DataFrame({'names' : df.columns, 'types' : df.dtypes, 'NA #': df.isna().sum(), 'NA %' : (df.isna().sum() / df.shape[0]) * 100})
        
        st.markdown('**Count of data types:**')
        st.write(exploration.types.value_counts())
        
        st.markdown('**Column names of type int64:**')
        st.markdown(list(exploration[exploration['types'] == 'int64']['names']))
        
        st.markdown('**Column names of type float64:**')
        st.markdown(list(exploration[exploration['types'] == 'float64']['names']))
        
        st.markdown('**Column names of type object:**')
        st.markdown(list(exploration[exploration['types'] == 'object']['names']))
        
        st.markdown('**Table with column and percentage of missing data :**')
        st.table(exploration[exploration['NA #'] != 0][['types', 'NA %']])
        
        st.subheader('Entering numerical data :')
        percentual = st.slider('Chose the missing percentage limit for the columns you want to input data', min_value=0, max_value=100)
        lista_colunas = list(exploration[exploration['NA %']  < percentual]['names'])
        select_method = st.radio('Chose a method below :', ('Average', 'Median'))
        st.markdown('You selected : ' +str(select_method))
        if select_method == 'Average':
            df_introduced = df[lista_colunas].fillna(df[lista_colunas].mean())
            exploration_introduced = pd.DataFrame({'names': df_introduced.columns, 'types': df_introduced.dtypes, 'NA #': df_introduced.isna().sum(),
                                       'NA %': (df_introduced.isna().sum() / df_introduced.shape[0]) * 100})
            st.table(exploration_introduced[exploration_introduced['types'] != 'object']['NA %'])
            st.subheader('Data entered download below : ')
            st.markdown(get_table_download_link(df_introduced), unsafe_allow_html=True)
        if select_method == 'Median':
            df_introduced = df[lista_colunas].fillna(df[lista_colunas].mean())
            exploration_introduced = pd.DataFrame({'names': df_introduced.columns, 'types': df_introduced.dtypes, 'NA #': df_introduced.isna().sum(),
                                       'NA %': (df_introduced.isna().sum() / df_introduced.shape[0]) * 100})
            st.table(exploration_introduced[exploration_introduced['types'] != 'object']['NA %'])
            st.subheader('Data entered download below : ')
            st.markdown(get_table_download_link(df_introduced), unsafe_allow_html=True)


if __name__ == '__main__':
	main()