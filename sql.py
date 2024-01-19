from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import sqlite3

import google.generativeai as genai
#configure Genai key

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#FUNCTION TO LOAD GOOGLE GEMINI MODEL AND PROVIDE QUERIES as response

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text

## function to retrive query from the database 

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

## define your prompt

prompt=[
    """
    you are an expert in converting question to sql query!
    the sql database has the name STUDENT and has the following columns - NAME,CLASS,
    SECTION \n\nFor example, \nExample 1- How many entries of record are present?,the SQL command will be something like this SELECT COUNT(*) FROM STUDENT;
    \nExample 2- Tell me all the student study in data science class?,
    the SQL command will be something like this SELECT * FROM STUDENT where ClASS  = "Data Science";
    also the sql code should not have ``` in begning or end and sql word in output
"""
]

##streamlit app

st.set_page_config(page_title="I can retrive any SQL query")
st.header("Gemini app to retrive SQL DATA")

question = st.text_input("Input: ",key='input')
submit = st.button('Ask the question')

#if submit is clicked

if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    response=read_sql_query(response,"student.db")
    st.subheader("the response is")
    for row in response:
        print(row)
        st.header(row)