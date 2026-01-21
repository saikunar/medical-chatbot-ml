import pickle
import pandas as pd
from nlp import extract_symptoms
from medicine import medicine_dict

model = pickle.load(open("disease_model.pkl", "rb"))

columns = ["fever", "body_pain", "headache", "nausea", "rash"]

def chatbot_response(user_input):
    symptoms = extract_symptoms(user_input)

    input_df = pd.DataFrame([symptoms], columns=columns)

    disease = model.predict(input_df)[0].lower()
    medicine = medicine_dict[disease]

    response = f"""
🩺 Possible Condition: {disease}
💊 Suggested Medicine: {medicine}

⚠️ This is an AI-based suggestion.
Please consult a qualified doctor.
"""
    return response
