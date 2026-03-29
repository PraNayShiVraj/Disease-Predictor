# knowledge_base.py

# Knowledge Base representing diseases and their associated attributes.
# Core symptoms have higher weight in the diagnosis process.
# Secondary symptoms help refine the diagnosis but are less critical.

KNOWLEDGE_BASE = {
    "Common Cold": {
        "Core": ["Runny Nose", "Sore Throat", "Congestion"],
        "Secondary": ["Sneezing", "Mild Cough", "Mild Fatigue"],
        "Next Steps": "Rest, stay hydrated, and take over-the-counter cold medications if needed.",
        "Precautions": ["Wash hands frequently", "Avoid close contact with sick people"]
    },
    "Influenza (Flu)": {
        "Core": ["High Fever", "Severe Muscle Aches", "Severe Fatigue"],
        "Secondary": ["Chills", "Dry Cough", "Headache"],
        "Next Steps": "Rest, drink plenty of fluids, and consult a doctor for antiviral medication if symptoms are severe.",
        "Precautions": ["Get an annual flu vaccine", "Avoid touching your face"]
    },
    "COVID-19": {
        "Core": ["Loss of Taste or Smell", "Fever", "Continuous Cough"],
        "Secondary": ["Shortness of Breath", "Extreme Fatigue", "Sore Throat", "Muscle Aches"],
        "Next Steps": "Isolate immediately to prevent spreading. Take a PCR or rapid antigen test. Contact a healthcare provider if breathing becomes difficult.",
        "Precautions": ["Wear a mask in crowded spaces", "Maintain social distancing", "Get vaccinated and boosted"]
    },
    "Strep Throat": {
        "Core": ["Severe Sore Throat", "Pain When Swallowing", "Swollen Tonsils"],
        "Secondary": ["Fever", "Swollen Lymph Nodes in Neck", "Red spots on roof of mouth"],
        "Next Steps": "See a doctor for a swab test. Antibiotics may be required.",
        "Precautions": ["Do not share utensils", "Replace toothbrush after getting well"]
    },
    "Allergic Rhinitis (Allergies)": {
        "Core": ["Itchy Eyes", "Sneezing", "Watery Eyes"],
        "Secondary": ["Runny Nose", "Postnasal Drip", "Mild Fatigue"],
        "Next Steps": "Avoid known allergens. Use antihistamines or nasal sprays.",
        "Precautions": ["Keep windows closed during high pollen seasons", "Use air purifiers"]
    }
}
