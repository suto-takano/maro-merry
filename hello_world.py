import streamlit as st

st.title('Hello World')
st.snow()



st.title('title string `<h1>`')
st.header('大見出し`<h2>`')
st.subheader(
    body='中見出し`<h3>`',
    anchor='title',
    help='`<h3>`あるいは`###`に相当するStrealitのコマンド',
    divider=True
    )

st.caption('キャプション`<caption>`')

st.text('''
Lorem ipsum dolor sit amet, consectetur adisicing elit. Maur is vel velit leo.
Suspendisse fermentum augue metus, ac lacinia ipsum varius sit amet.
Nullam sagittis, tellus id finibus tincidunt,elit mi pellentesque sem, sed 
suscupit mi lectus non quam.''')

st.code('''
import streamlit as st
st.show()''',
    language='python',
    line_numbers=True)