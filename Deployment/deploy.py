import streamlit as st
import joblib
import pandas as pd
import numpy as np
import requests


# Load the trained model
model = joblib.load('player_pred.joblib')

# Function to make predictions and return position names
def predict_player_position(Overall, Age, Height, Weight, Weak_Foot_Rating,
                            Skill_Moves, Pace_Total, Shooting_Total, Passing_Total,
                            Dribbling_Total, Defending_Total, Physicality_Total,
                            Crossing, Finishing, Heading_Accuracy, Short_Passing,
                            Curve, Acceleration, Agility, Reactions, Balance,
                            Shot_Power, Jumping, Stamina, Strength, Aggression,
                            Vision, Penalties, Composure, GoalkeeperKicking,
                            Nationality, Preferred_Foot):
    
    # Prepare input data as a DataFrame
    input_data = pd.DataFrame({
        'Overall': [Overall],
        'Age': [Age],
        'Height(in cm)': [Height],
        'Weight(in kg)': [Weight],
        'Weak Foot Rating': [Weak_Foot_Rating],
        'Skill Moves': [Skill_Moves],
        'Pace Total': [Pace_Total],
        'Shooting Total': [Shooting_Total],
        'Passing Total': [Passing_Total],
        'Dribbling Total': [Dribbling_Total],
        'Defending Total': [Defending_Total],
        'Physicality Total': [Physicality_Total],
        'Crossing': [Crossing],
        'Finishing': [Finishing],
        'Heading Accuracy': [Heading_Accuracy],
        'Short Passing': [Short_Passing],
        'Curve': [Curve],
        'Acceleration': [Acceleration],
        'Agility': [Agility],
        'Reactions': [Reactions],
        'Balance': [Balance],
        'Shot Power': [Shot_Power],
        'Jumping': [Jumping],
        'Stamina': [Stamina],
        'Strength': [Strength],
        'Aggression': [Aggression],
        'Vision': [Vision],
        'Penalties': [Penalties],
        'Composure': [Composure],
        ' GoalkeeperKicking': [GoalkeeperKicking],
        'Nationality': [Nationality],
        'Preferred Foot': [Preferred_Foot]
    })

    # Make predictions
    prediction = model.predict(input_data)

    # Map numeric positions to their names
    position_names = {
        0: 'Midfielder',
        1: 'Defender',
        2: 'Forward',
        3: 'Goalkeeper'
    }

    predicted_position = position_names.get(prediction[0], 'Unknown')
    return predicted_position

# Set a background image
page_bg_img = """
    <style>
    [data-testid = "stAppViewContainer"]{
        background-color: #002147;
        color: #f95959; 
    }
       [data-testid = "stHeader"]{
        background-color: #002147;
        color: #f95959; 
    }

    [data-testid = "stSidebar"] {
        background-color: #455d7a;
        color: #C0C0C0
    }
     [data-testid = "collapsedControl"] {
        color: #f95959;
    }
      [data-testid = "stVerticalBlock"] {
        color: #f95959;
    }
     [data-testid = "baseButton-secondary"]{
        background-color: #f95959; 
    }
    p{
        color: #e3e3e3;
    }
    [data-testid = "StyledLinkIconContainer"]{
        color: #e3e3e3;
    }
    h1{
        color: #002147;
    }
   
    </style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Create a Streamlit app with tabs
st.title("Player Position Prediction App")

# Add a sidebar for information
st.sidebar.title("About This App")
st.sidebar.write("This app predicts the best player position based on input features.")
st.sidebar.write("It uses a machine learning model trained on football player data.")
st.sidebar.write("Adjust the sliders and input fields on the left to make predictions.")
st.sidebar.write("Developed by Dipeolu Ayomide")

# Input features for prediction
Overall = st.slider("Overall", min_value=1, max_value=100)
Age = st.slider("Age", min_value=16, max_value=40)
Height = st.slider("Height (in cm)", min_value=150, max_value=220)
Weight = st.slider("Weight (in kg)", min_value=50, max_value=150)
Weak_Foot_Rating = st.slider("Weak Foot Rating", min_value=1, max_value=5)
Skill_Moves = st.slider("Skill Moves", min_value=1, max_value=5)
Pace_Total = st.slider("Pace Total", min_value=1, max_value=100)
Shooting_Total = st.slider("Shooting Total", min_value=1, max_value=100)
Passing_Total = st.slider("Passing Total", min_value=1, max_value=100)
Dribbling_Total = st.slider("Dribbling Total", min_value=1, max_value=100)
Defending_Total = st.slider("Defending Total", min_value=1, max_value=100)
Physicality_Total = st.slider("Physicality Total", min_value=1, max_value=100)
Crossing = st.slider("Crossing", min_value=1, max_value=100)
Finishing = st.slider("Finishing", min_value=1, max_value=100)
Heading_Accuracy = st.slider("Heading Accuracy", min_value=1, max_value=100)
Short_Passing = st.slider("Short Passing", min_value=1, max_value=100)
Curve = st.slider("Curve", min_value=1, max_value=100)
Acceleration = st.slider("Acceleration", min_value=1, max_value=100)
Agility = st.slider("Agility", min_value=1, max_value=100)
Reactions = st.slider("Reactions", min_value=1, max_value=100)
Balance = st.slider("Balance", min_value=1, max_value=100)
Shot_Power = st.slider("Shot Power", min_value=1, max_value=100)
Jumping = st.slider("Jumping", min_value=1, max_value=100)
Stamina = st.slider("Stamina", min_value=1, max_value=100)
Strength = st.slider("Strength", min_value=1, max_value=100)
Aggression = st.slider("Aggression", min_value=1, max_value=100)
Vision = st.slider("Vision", min_value=1, max_value=100)
Penalties = st.slider("Penalties", min_value=1, max_value=100)
Composure = st.slider("Composure", min_value=1, max_value=100)
GoalkeeperKicking = st.slider("GoalkeeperKicking", min_value=1, max_value=100)
Nationality = st.text_input("Nationality")
Preferred_Foot = st.selectbox("Preferred Foot", ["Left", "Right"])

# Make predictions when the Predict button is clicked
if st.button("Predict"):
    predicted_position = predict_player_position(Overall, Age, Height, Weight, Weak_Foot_Rating,
                                                Skill_Moves, Pace_Total, Shooting_Total, Passing_Total,
                                                Dribbling_Total, Defending_Total, Physicality_Total,
                                                Crossing, Finishing, Heading_Accuracy, Short_Passing,
                                                Curve, Acceleration, Agility, Reactions, Balance,
                                                Shot_Power, Jumping, Stamina, Strength, Aggression,
                                                Vision, Penalties, Composure, GoalkeeperKicking,
                                                Nationality, Preferred_Foot)

# Run the Streamlit app

    st.success(f"Predicted Player Position: {predicted_position}")

