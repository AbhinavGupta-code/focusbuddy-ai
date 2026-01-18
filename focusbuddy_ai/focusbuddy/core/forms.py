from django import forms

class StudyForm(forms.Form):
    subject = forms.CharField(label="Subject")
    time_available = forms.IntegerField(label="Time (minutes)")
    energy_level = forms.ChoiceField(
        choices=[
            ('Low', 'Low'),
            ('Medium', 'Medium'),
            ('High', 'High')
        ]
    )
