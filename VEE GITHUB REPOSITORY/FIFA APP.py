import streamlit as st
import pandas as pd
import joblib

# Load the trained model (replace 'your_model.pkl' with your actual model file)

model = joblib.load("C:\\Users\\user\\Desktop\\VEE GITHUB REPOSITORY\\best_model (2).pkl")

st.title('Player potential')

with st.form(key='player_features_form'):
    # Define input fields
    overall = st.number_input("Overall", min_value=0, max_value=100, value=50)
    potential = st.number_input("Potential", min_value=0, max_value=100, value=50)
    value_eur = st.number_input("Value (EUR)", min_value=0, max_value=1_000_000_000, value=500000)
    wage_eur = st.number_input("Wage (EUR)", min_value=0, max_value=1_000_000, value=5000)
    age = st.number_input("Age", min_value=15, max_value=45, value=25)
    international_reputation = st.number_input("International Reputation", min_value=0, max_value=5, value=3)
    shooting = st.number_input("Shooting", min_value=0, max_value=100, value=50)
    passing = st.number_input("Passing", min_value=0, max_value=100, value=50)
    dribbling = st.number_input("Dribbling", min_value=0, max_value=100, value=50)
    physic = st.number_input("Physical", min_value=0, max_value=100, value=50)
    attacking_short_passing = st.number_input("Attacking Short Passing", min_value=0, max_value=100, value=50)
    skill_curve = st.number_input("Skill Curve", min_value=0, max_value=100, value=50)
    skill_long_passing = st.number_input("Skill Long Passing", min_value=0, max_value=100, value=50)
    skill_ball_control = st.number_input("Skill Ball Control", min_value=0, max_value=100, value=50)
    movement_reactions = st.number_input("Movement Reactions", min_value=0, max_value=100, value=50)
    power_shot_power = st.number_input("Power Shot Power", min_value=0, max_value=100, value=50)
    power_long_shots = st.number_input("Power Long Shots", min_value=0, max_value=100, value=50)
    mentality_vision = st.number_input("Mentality Vision", min_value=0, max_value=100, value=50)
    mentality_composure = st.number_input("Mentality Composure", min_value=0, max_value=100, value=50)

    submit_button = st.form_submit_button(label='Submit')


    # Collect inputs into a list
    if submit_button:
        input_data = pd.DataFrame({
            'overall': [overall],
            'potential': [potential],
            'value_eur': [value_eur],
            'wage_eur': [wage_eur],
            'age': [age],
            'international_reputation': [international_reputation],
            'shooting': [shooting],
            'passing': [passing],
            'dribbling': [dribbling],
            'physic': [physic],
            'attacking_short_passing': [attacking_short_passing],
            'skill_curve': [skill_curve],
            'skill_long_passing': [skill_long_passing],
            'skill_ball_control': [skill_ball_control],
            'movement_reactions': [movement_reactions],
            'power_shot_power': [power_shot_power],
            'power_long_shots': [power_long_shots],
            'mentality_vision': [mentality_vision],
            'mentality_composure': [mentality_composure]
        })

    prediction = model.predict(input_data)

     # Display prediction
    st.subheader('Predicted Player Rating')
    
    st.write(prediction[0])






