from django import forms

class HeartPredictionForm(forms.Form):
    GENDER_CHOICES = [(1, 'Male'), (0, 'Female')]
    YES_NO_CHOICES = [(1, 'Yes'), (0, 'No')]
    threechoices=[(0, 'Low'), (1,'Average', ),(2, 'High')]
    male = forms.ChoiceField(choices=GENDER_CHOICES, label='Please specify your Gender')  # ✅ Dropdown
    currentSmoker = forms.ChoiceField(choices=YES_NO_CHOICES, label='Are you current Smoker?')  # ✅ Dropdown
    BPMeds = forms.ChoiceField(choices=YES_NO_CHOICES, label=' Are you on BP Medication?')  # ✅ Dropdown
    prevalentStroke = forms.ChoiceField(choices=YES_NO_CHOICES, label='Do you have history of Stroke?')  # ✅ Dropdown
    prevalentHyp = forms.ChoiceField(choices=YES_NO_CHOICES, label='Do you have hypertension?')  # ✅ Dropdown
    diabetes = forms.ChoiceField(choices=YES_NO_CHOICES, label='Do you have Diabetes?')  # ✅ Dropdown
    obesity = forms.ChoiceField(choices=YES_NO_CHOICES, label='Do you have obesity?')  # ✅ Dropdown
    chestPain_1 = forms.ChoiceField(choices=YES_NO_CHOICES, label='Do you suffer from chest pain')  # ✅ Dropdown
    shortnessOfBreath_yes = forms.ChoiceField(choices=YES_NO_CHOICES, label='Do you suffer from shortness of breath')  # ✅ Dropdown
    dizziness_yes = forms.ChoiceField(choices=YES_NO_CHOICES, label='Do you feek dizzy sometimes')  # ✅ Dropdown
    hereditaryDisease_yes = forms.ChoiceField(choices=YES_NO_CHOICES, label='Do you have hereditary disease realted to heart in you r family?')  # ✅ Dropdown
    heartRateLevel = forms.ChoiceField(choices=threechoices, label="what is your Heart Rate Level?")
    cholesterolLevel = forms.ChoiceField(choices = threechoices, label='What is Cholesterol Level')
    diabetesLevel=forms.ChoiceField(choices=threechoices, label= "Whats your diabetes level?")
    bloodPressureLevel = forms.ChoiceField(choices=YES_NO_CHOICES, label= "Do you have high blood pressure?")
    # Numeric input fields (textboxes)
    age = forms.IntegerField(label='Whats you Age?')
    cigsPerDay = forms.FloatField(label='How many cigarettes do you have per day?')
    totChol = forms.FloatField(label='What is your Total Cholesterol?')
    sysBP = forms.FloatField(label='What is your upper Blood Pressure level?')
    diaBP = forms.FloatField(label='What is your lower Blood Pressure level?')
    BMI = forms.FloatField(label=' What is your BMI?')
    heartRate = forms.FloatField(label='What is your exact heart rate?')
    glucose = forms.FloatField(label=' What is your exact glucose reading?')
   
  

GENDER_CHOICES = [(1, 'Male'), (0, 'Female')]
YES_NO_CHOICES = [(1, 'Yes'), (0, 'No')]
THREE_CHOICES = [(0, 'Low'), (1, 'Average'), (2, 'High')]

class SymptomForm(forms.Form):
    male = forms.ChoiceField(choices=GENDER_CHOICES, label='Please specify your Gender')
    currentSmoker = forms.ChoiceField(choices=YES_NO_CHOICES, label='Are you current Smoker?')
    BPMeds = forms.ChoiceField(choices=YES_NO_CHOICES, label='Are you on BP Medication?')
    prevalentStroke = forms.ChoiceField(choices=YES_NO_CHOICES, label='Do you have history of Stroke?')
    prevalentHyp = forms.ChoiceField(choices=YES_NO_CHOICES, label='Do you have hypertension?')
    diabetes = forms.ChoiceField(choices=YES_NO_CHOICES, label='Do you have Diabetes?')
    obesity = forms.ChoiceField(choices=YES_NO_CHOICES, label='Do you have obesity?')
    chestPain_1 = forms.ChoiceField(choices=YES_NO_CHOICES, label='Do you suffer from chest pain')
    shortnessOfBreath_yes = forms.ChoiceField(choices=YES_NO_CHOICES, label='Do you suffer from shortness of breath')
    dizziness_yes = forms.ChoiceField(choices=YES_NO_CHOICES, label='Do you feel dizzy sometimes')
    hereditaryDisease_yes = forms.ChoiceField(choices=YES_NO_CHOICES, label='Do you have hereditary disease related to heart in your family?')
    heartRateLevel = forms.ChoiceField(choices=THREE_CHOICES, label='What is your Heart Rate Level?')
    cholesterolLevel = forms.ChoiceField(choices=THREE_CHOICES, label='What is your Cholesterol Level?')
    diabetesLevel = forms.ChoiceField(choices=THREE_CHOICES, label='What is your diabetes level?')
    bloodPressureLevel = forms.ChoiceField(choices=YES_NO_CHOICES, label='Do you have high blood pressure?')
    age = forms.IntegerField(label='What is your Age?')
    cigsPerDay = forms.FloatField(label='How many cigarettes do you have per day?')
    totChol = forms.FloatField(label='What is your Total Cholesterol?')
    sysBP = forms.FloatField(label='What is your upper Blood Pressure level?')
    diaBP = forms.FloatField(label='What is your lower Blood Pressure level?')
    BMI = forms.FloatField(label='What is your BMI?')
    heartRate = forms.FloatField(label='What is your exact heart rate?')
    glucose = forms.FloatField(label='What is your exact glucose reading?')