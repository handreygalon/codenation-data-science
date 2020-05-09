import streamlit as st


def main():
    st.title('Hello World')

    st.markdown('Button')
    button = st.button('Button')
    if button:
        st.markdown('Click')

    st.markdown('Checkbox')
    check = st.checkbox('Checkbox')
    if check:
        st.markdown('Checked')

    st.markdown('Radio Button')
    radio = st.radio('Choose an option', ('Option 1', 'Option 2'))
    if radio == 'Option 1':
        st.markdown('Option 1 was choosen')
    if radio == 'Option 2':
        st.markdown('Option 2 was choosen')
    
    st.markdown('Selectbox')
    selectbox = st.selectbox('Choose an option', ('Option 1', 'Option 2'))
    if selectbox == 'Option 1':
        st.markdown('Option 1 was choosen')
    if selectbox == 'Option 2':
        st.markdown('Option 2 was choosen')
    
    st.markdown('Multi')
    multi = st.multiselect('Choose some options', ('Option 1', 'Option 2'))
    if multi == 'Option 1':
        st.markdown('Option 1 was choosen')
    if multi == 'Option 2':
        st.markdown('Option 2 was choosen')

    st.markdown('File Update')
    file = st.file_uploader('Choose a file', type='csv')
    if file is not None:
        st.markdown('File is not empty')


if __name__ == "__main__":
    main()