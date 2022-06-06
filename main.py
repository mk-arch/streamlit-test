import streamlit as st
# import numpy as np
# import pandas as pd
# from PIL import Image
import time

st.title('streamlit')

st.write("Progress")
'Start!'

latest_itereation = st.empty()
bar = st.progress(0)

for i in range(100):
    time.sleep(0.01)
    latest_itereation.text(f'Iteration {i+1}')
    bar.progress(i+1)

'Done!'


left_column, right_column = st.columns(2)
button = left_column.button('右に文字を表示')

if button:
    right_column.write('ここは右カラム')

expander1 = st.expander('問い合わせ')
expander1.write('問い合わせ内容')
expander2 = st.expander('問い合わせ')
expander2.write('問い合わせ内容')

# text = left_column.text_input('あなたの趣味は？')
# condition = left_column.slider('あなたの今の調子',0,100,50)

# right_column.write(text)
# right_column.write(condition)

# option = st.selectbox(
#     'あなたが好きな数字',
#     list(range(1,11)) 
# )


# if st.checkbox('Show Image'):
#     img = Image.open("face_to_c.jpg")
#     st.image(img, caption='obama', use_column_width=True)


