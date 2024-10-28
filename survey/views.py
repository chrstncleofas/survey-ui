import json
from survey.forms import SurveyForm
from survey.models import SurveyResponse
from django.shortcuts import render, redirect

def survey_view(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            answers = {
                "Q1": form.cleaned_data['question1'],
                "Q2": form.cleaned_data['question2'],
                "Q3": form.cleaned_data['question3']
            }
            SurveyResponse.objects.create(answers=json.dumps(answers))
            return redirect('thank_you')
    else:
        form = SurveyForm()
    return render(request, 'survey/survey.html', {'form': form})

def thank_you(request):
    return render(request, 'survey/thank_you.html')
