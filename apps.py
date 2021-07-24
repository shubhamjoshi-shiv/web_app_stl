# from PIL import Image
# import re
# import string
import pickle
# import newspaper
import copy
import streamlit as st
# import pandas 
# import numpy
# import pickle


@st.cache(persist=True, allow_output_mutation=True)
def load_trained_model():
    trained_model = pickle.load(open('finalized_model.sav', 'rb'))
    return trained_model


def predict(text, trained_model):
    prediction = trained_model.predict([text])[0]
    if prediction == 0:
        result = False
    else:
        result = True
    return {'result': result}


def main():
    tm = copy.deepcopy(load_trained_model())
    st.title("fake news detector v-2")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
    </div>
    """
    news_text = st.text_area('give the text of news here')
    if st.button("Predict"):
        result = predict(news_text, tm)
        st.write(result)


if __name__ == '__main__':
    main()


# def wordopt(text):#puntuation aur link hata dega thoda cleen karega
#     text = text.lower()
#     text = re.sub('\[.*?\]', '', text)
#     text = re.sub("\\W"," ",text)
#     text = re.sub('https?://\S+|www\.\S+', '', text)
#     text = re.sub('<.*?>+', '', text)
#     text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
#     text = re.sub('\n', '', text)
#     text = re.sub('\w*\d\w*', '', text)
#     return text
