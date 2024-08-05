import plotly.express as px
import streamlit as st
import sqlite3

connection = sqlite3.connect("../data.db")


def get_values():
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM temperatures')
    rows = cursor.fetchall()
    times = [row[0] for row in rows]
    temperatures = [row[1] for row in rows]
    return times, temperatures


if __name__ == '__main__':
    times, temperatures = get_values()

    fig = px.line(x=times, y=temperatures,
                  labels={'x': 'Date', 'y': 'Temperature'})


    st.header('Makapaka')
    st.plotly_chart(fig)