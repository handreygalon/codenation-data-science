import streamlit as st
import pandas as pd


def main():
    st.title('Using Streamlit with Pandas')
    file = st.file_uploader('Upload your file', type='csv')
    if file is not None:
        st.markdown('Slider')
        slider = st.slider('Values', 1, 100)
        df = pd.read_csv(file)
        st.dataframe(df.head(slider))

        st.markdown('Table')
        st.table(df.head(slider))

        st.write(df.columns)
        st.table(df.groupby('variety')['petal.width'].mean())


if __name__ == "__main__":
    main()