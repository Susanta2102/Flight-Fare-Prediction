import numpy as np
import pickle
import streamlit as st
import pandas as pd
import bz2

# Setting up the page title, icons
st.set_page_config(page_title="Flight Price Predictor ✈️💰", page_icon="https://hips.hearstapps.com/hmg-prod/images/gettyimages-1677184597.jpg?crop=0.668xw:1.00xh;0.167xw,0&resize=1200:*")
st.sidebar.title('MENU BAR')
choice = st.sidebar.selectbox(' ', ('Home ✨', 'Predict 🛫', 'About Developer 👨‍💻', 'About the Projects 📊'))
st.sidebar.image('https://e0.pxfuel.com/wallpapers/209/716/desktop-wallpaper-untitled-airplane-sky-aesthetic-travel.jpg')
st.sidebar.image('https://i.pinimg.com/736x/0d/1e/96/0d1e967cde176af6f8f0568af424d07b.jpg')

if choice == 'Home ✨':
    st.title('Welcome to Flight Price Predictor')
    st.text('Hi there! Ready to predict your flight ticket price? ✈️💸')
    st.text('Click the Menu bar for further details')
    st.image('https://wallpapers.com/images/featured/airport-w6v47yjhxcohsjgf.jpg')

elif choice == 'Predict 🛫':
    st.text('Kindly fill in your flight details to view the predicted price')
    st.image('https://feeds.abplive.com/onecms/images/uploaded-images/2021/09/08/634259599cd6f60c24f9e67a5680c064_original.jpg')
    ch = st.selectbox('Airline', ('Select', 'Vistara', 'Air India', 'Indigo', 'GO FIRST', 'AirAsia', 'SpiceJet'))
    if ch == 'Vistara':
        a = 5
    elif ch == 'Air India':
        a = 1
    elif ch == 'Indigo':
        a = 3
    elif ch == 'GO FIRST':
        a = 2
    elif ch == 'AirAsia':
        a = 0
    elif ch == 'SpiceJet':
        a = 4
    
    cg = st.selectbox('From', ('Select', 'Delhi', 'Mumbai', 'Bangalore', 'Kolkata', 'Hyderabad', 'Chennai'))
    if cg == 'Delhi':
        b = 2
        cx = st.selectbox('Destination', ('Select', 'Mumbai', 'Bangalore', 'Kolkata', 'Hyderabad', 'Chennai'))
        if cx == 'Mumbai':
            f = 5
        elif cx == 'Bangalore':
            f = 0
        elif cx == 'Kolkata':
            f = 4
        elif cx == 'Hyderabad':
            f = 3
        elif cx == 'Chennai':
            f = 1
    elif cg == 'Mumbai':
        b = 5
        cx = st.selectbox('Destination', ('Select', 'Delhi', 'Bangalore', 'Kolkata', 'Hyderabad', 'Chennai'))
        if cx == 'Delhi':
            f = 2
        elif cx == 'Bangalore':
            f = 0
        elif cx == 'Kolkata':
            f = 4
        elif cx == 'Hyderabad':
            f = 3
        elif cx == 'Chennai':
            f = 1
    elif cg == 'Bangalore':
        b = 0
        cx = st.selectbox('Destination', ('Select', 'Mumbai', 'Delhi', 'Kolkata', 'Hyderabad', 'Chennai'))
        if cx == 'Mumbai':
            f = 5
        elif cx == 'Delhi':
            f = 2
        elif cx == 'Kolkata':
            f = 4
        elif cx == 'Hyderabad':
            f = 3
        elif cx == 'Chennai':
            f = 1
    elif cg == 'Kolkata':
        b = 4
        cx = st.selectbox('Destination', ('Select', 'Mumbai', 'Delhi', 'Bangalore', 'Hyderabad', 'Chennai'))
        if cx == 'Mumbai':
            f = 5
        elif cx == 'Delhi':
            f = 2
        elif cx == 'Bangalore':
            f = 0
        elif cx == 'Hyderabad':
            f = 3
        elif cx == 'Chennai':
            f = 1
    elif cg == 'Hyderabad':
        b = 3
        cx = st.selectbox('Destination', ('Select', 'Mumbai', 'Delhi', 'Bangalore', 'Kolkata', 'Chennai'))
        if cx == 'Mumbai':
            f = 5
        elif cx == 'Delhi':
            f = 2
        elif cx == 'Bangalore':
            f = 0
        elif cx == 'Kolkata':
            f = 4
        elif cx == 'Chennai':
            f = 1
    else:
        b = 1
        cx = st.selectbox('Destination', ('Select', 'Mumbai', 'Delhi', 'Bangalore', 'Kolkata', 'Hyderabad'))
        if cx == 'Mumbai':
            f = 5
        elif cx == 'Delhi':
            f = 2
        elif cx == 'Bangalore':
            f = 0
        elif cx == 'Kolkata':
            f = 4
        elif cx == 'Hyderabad':
            f = 3
                        
    cf = st.selectbox('Departure time', ('Select', 'Morning', 'Early Morning', 'Evening', 'Night', 'Afternoon', 'Late Night'))
    if cf == 'Morning':
        c = 4
    elif cf == 'Early Morning':
        c = 1
    elif cf == 'Evening':
        c = 2
    elif cf == 'Night':
        c = 5
    elif cf == 'Afternoon':
        c = 0
    elif cf == 'Late Night':
        c = 3

    ci = st.selectbox('Stops', ('Select', 'one', 'zero', 'two or more'))
    if ci == 'one':
        d = 0
    elif ci == 'zero':
        d = 2
    elif ci == 'two or more':
        d = 1

    cs = st.selectbox('Arrival time', ('Select', 'Night', 'Evening', 'Morning', 'Afternoon', 'Early Morning', 'Late Night'))
    if cs == 'Night':
        e = 5
    elif cs == 'Evening':
        e = 2
    elif cs == 'Morning':
        e = 4
    elif cs == 'Afternoon':
        e = 0
    elif cs == 'Early Morning':
        e = 1
    elif cs == 'Late Night':
        e = 3    

    cb = st.selectbox('Class', ('Select', 'Economy', 'Business'))
    if cb == 'Economy':
        g = 1
    else:
        g = 0        

    h = st.number_input('Duration')
    i = st.number_input('Days left')

    btn = st.button('Check')
    if btn:
        def decompress_pickle(file):
            data = bz2.BZ2File(file, 'rb')
            data = pickle.load(data)
            return data
        model = decompress_pickle('Flight.pbz2')
        pred = model.predict([[a, b, c, d, e, f, g, h, i]])
        st.write("The predicted price is:-", pred[0], 'Rs')
        st.header('Time to fly ✈🧳')
        st.image('https://image.cnbcfm.com/api/v1/image/106537227-1589463911434gettyimages-890234318.jpeg?v=1589463982&w=1600&h=900')

elif choice == 'About Developer 👨‍💻':
    st.title('About the Developer')
    st.text('Name: Susanta Baidya')
    st.text('Education: Master in AI & ML from Indian Institute of Information Technology 🎓')
    st.markdown('[GitHub](https://github.com/Susanta2102)')
    st.markdown('[Kaggle](https://www.kaggle.com/susanta21)')
    st.markdown('[LinkedIn](https://www.linkedin.com/in/susanta-baidya-03436628a/)')
    st.markdown('Email: msa23009@iiitl.ac.in')
    st.image('https://raw.githubusercontent.com/Susanta2102/My-photo/main/Screenshot%202024-03-29%20130556.png')

elif choice == 'About the Projects 📊':
    st.title('About the Projects')
    st.header('OVERVIEW:')
    st.text('A Streamlit app for predicting flight ticket price is deployed with the help of Machine Learning and Python programming language.')
    st.text('This app makes things easy when planning to travel.')

    st.header('DATA COLLECTION:')
    st.text('Source: https://www.kaggle.com/datasets/shubhambathwal/flight-price-prediction')
    st.text('The dataset used in this project is taken from the above mentioned Kaggle link.')
    st.text('Features such as airline names, places, duration of travel and classes (Economy and Business) are present in the dataset which helps in predicting the ticket price, where price is the target value.')
    st.text('The data used here was obtained by scraping from similar price predictor websites.')

    st.header('DATA PREPROCESSING:')
    st.text('The dataset is read using the Pandas library from a csv file and then looked for its dimensions, each columns data types.')
    st.text('Also, checked for the presence of any null values or duplicates.')

    st.header('EXPLORATORY DATA ANALYSIS:')
    st.text('With the help of Seaborn and Matplotlib, many charts and graphs were plotted.')
    st.text('This step is crucial as it helps in visualizing differnet relationships between each feature present in the dataset.')

    st.header('FEATURE ENGINEERING:')
    st.text('Outlier removal:')
    st.text('Using boxplot, outliers were found and removed, in order to obtain a clean data One hot encoding.')
    st.text('As, there are multi columns with categorical variables, label encoding was used, through which the data was ready for undergoing model buliding process.')

    st.header('MODEL BUILDING:')
    st.text('The data was separated into features and target followed by train test split.')
    st.text('As the target value is price, which is a continous variable, algorithms like Linear Regression, KNeighbors Regression and Random Forest Regression were used.')
    st.text('Grid Search CV method was employed followed by cross validation method in order to find the best model parameters.')
    st.text('From the above method, Random Forest Regression was found out to be the best fit for this prediction with around 99% accurate.')
    st.image('https://wallpapers.com/images/featured/airport-w6v47yjhxcohsjgf.jpg')
