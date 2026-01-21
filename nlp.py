symptom_keywords = {
    "fever": ["fever", "temperature"],
    "cold": ["cold", "cough", "sneezing", "muscle pain"],
    "headache": ["headache", "head pain", "migraine"],
    "nausea": ["nausea", "vomiting"],
    "rash": ["rash", "red spots"]
}

def extract_symptoms(text):
    text = text.lower()
    symptoms = []

    for symptom, keywords in symptom_keywords.items():
        found = any(word in text for word in keywords)
        symptoms.append(1 if found else 0)

    return symptoms
