Link for the Streamlit App:- https://flight-fare-prediction-ix.streamlit.app/
App's Welcome Page:- 
![Screenshot 2024-06-11 193013](https://github.com/Susanta2102/Flight-Fare-Prediction/assets/144701829/1e2f906a-cca9-4456-ad6d-3d890623788b)

In app:-
![Screenshot 2024-06-11 193246](https://github.com/Susanta2102/Flight-Fare-Prediction/assets/144701829/de9dbfa1-3c03-42c4-bbc1-a3e574037b93)
![Screenshot 2024-06-11 193035](https://github.com/Susanta2102/Flight-Fare-Prediction/assets/144701829/4c6d80c5-740e-46de-8389-aef6fde25ff1)


OVERVIEW:-
- A Streamlit app for predicting flight ticket price is deployed with the help of Machine Learning and Python programming language
- This app makes things easy when planning to travel
  
DATA COLLECTION:-
- Source --> https://www.kaggle.com/datasets/shubhambathwal/flight-price-prediction
- The dataset used in this project is taken from the above mentioned Kaggle link.
- Features such as airline names, places, duration of travel and classes (Economy and Business) are present in the dataset which helps in predicting the ticket price, where price is the target value.
- The data used here was obtained by scraping from similar price predictor websites

DATA PREPROCESSING:-
- The dataset is read using the Pandas library from a csv file and then looked for its dimensions, each columns' data types.
- Also, checked for the presence of any null values or duplicates

EXPLORATORY DATA ANALYSIS:-
- With the help of Seaborn and Matplotlib, many charts and graphs were plotted
- This step is crucial as it helps in visualizing differnet relationships between each feature present in the dataset
  
FEATURE ENGINEERING:-
Outlier removal:
- Using boxplot, outliers were found and removed, in order to obtain a clean data
One hot encoding:
- As, there are multi columns with categorical variables, label encoding was used, through which the data was ready for undergoing model buliding process

MODEL BUILDING:-
- The data was separated into features and target followed by train test split
- As the target value is price, which is a continous variable, algorithms like Linear Regression, KNeighborsRegression and Random Forest Regression were used
- Grid Search CV method was employed followed by cross validation method in order to find the best model parameters
- From the above method, Random Forest Regression was found out to be the best fit for this prediction with around 99% accurate
- Later, it was saved by pickling method, and for a safer side, it was compressed so that deploying will be easy

APP DEPLOYMENT:-
- Since the file is compressed and saved, it is first decompressed
- Streamlit options and features were added
- Files including Python, requirements.txt were created and upload to Github profile
- Finally, on the Streamlit website the app is deployed.


# Flight-Fare-Prediction
