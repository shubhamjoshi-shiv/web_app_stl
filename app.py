# # -*- coding: utf-8 -*-
# """
# Created on Sat Jun 13 02:20:31 2020
# #
# @author: Krish Naik
# """

# # -*- coding: utf-8 -*-
# """
# Created on Fri May 15 12:50:04 2020

# @author: krish.naik
# """


import copy
# import numpy as np
import pickle
# import pandas as pd
# #from flasgger import Swagger
import streamlit as st

# from PIL import Image

# app=Flask(__name__)
# Swagger(app)

# pickle_in = open("classifier.pkl", "rb")
# classifier = pickle.load(pickle_in)

# # @app.route('/')


# def welcome():
#     return "Welcome All"

# # @app.route('/predict',methods=["Get"])


# # def predict_note_authentication(variance, skewness, curtosis, entropy):
# #     """Let's Authenticate the Banks Note 
# #     This is using docstrings for specifications.
# #     ---
# #     parameters:  
# #       - name: variance
# #         in: query
# #         type: number
# #         required: true
# #       - name: skewness
# #         in: query
# #         type: number
# #         required: true
# #       - name: curtosis
# #         in: query
# #         type: number
# #         required: true
# #       - name: entropy
# #         in: query
# #         type: number
# #         required: true
# #     responses:
# #         200:
# #             description: The output values

# #     """

#     # prediction = classifier.predict([[variance, skewness, curtosis, entropy]])
#     # print(prediction)
#     # return prediction


# def main():
#     st.title("fake news detector")
#     html_temp = """
#     <div style="background-color:tomato;padding:10px">
#     <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
#     </div>
#     """
#     news_text=st.text_area('give the text of news here')
#     if st.button("Predict"):
#             result = news_text
#             st.write(result)

#     # st.markdown(html_temp, unsafe_allow_html=True)
#     # variance = st.text_input("Variance", "Type Here")
#     # skewness = st.text_input("skewness", "Type Here")
#     # curtosis = st.text_input("curtosis", "Type Here")
#     # entropy = st.text_input("entropy", "Type Here")
#     # result = ""
#     # if st.button("Predict"):
#     #     result = predict_note_authentication(
#     #         variance, skewness, curtosis, entropy)
#     # st.success('The output is {}'.format(result))
#     # if st.button("About"):
#     #     st.text("Lets LEarn")
#     #     st.text("Built with Streamlit")




# if __name__ == '__main__':
#     main()


# from PIL import Image
# import re
# import string
# import newspaper
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
