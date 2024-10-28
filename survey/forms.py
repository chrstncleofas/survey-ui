from django import forms

class SurveyForm(forms.Form):
    QUESTION_CHOICES = [
        (1, 'Very Inaccurate'),
        (2, 'Inaccurate'),
        (3, 'Neither Accurate nor Inaccurate'),
        (4, 'Accurate'),
        (5, 'Very Accurate'),
    ]

    question1 = forms.ChoiceField(
        label="I worry about things",
        choices=QUESTION_CHOICES,
        widget=forms.RadioSelect()
    )
    question2 = forms.ChoiceField(
        label="I make friends easily",
        choices=QUESTION_CHOICES,
        widget=forms.RadioSelect()
    )
    question3 = forms.ChoiceField(
        label="I have a vivid imagination",
        choices=QUESTION_CHOICES,
        widget=forms.RadioSelect()
    )
