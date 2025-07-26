def predict_career(form):
    interest = form.get('interest_area')
    work_type = form.get('work_type')
    programming = form.get('programming')
    analytical = int(form.get('analytical'))
    curiosity = int(form.get('curiosity'))

    if interest == 'AI Research' and analytical >= 4 and curiosity >= 4:
        return "AI Research Scientist", "You have high curiosity and analytical skills ideal for research."
    elif interest == 'Data Science' and programming in ['Intermediate', 'Advanced']:
        return "Data Scientist", "Strong data and programming skills match data science."
    elif interest == 'NLP':
        return "NLP Engineer", "Interest in language AI suits NLP."
    elif interest == 'Prompt Engineering':
        return "Prompt Engineer", "Creative and curious minds thrive in prompt engineering."
    else:
        return "AI Analyst", "You're a great fit for analytical AI roles."
