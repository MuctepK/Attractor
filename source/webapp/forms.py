from django import forms
from django.forms import widgets
STATUS_CHOICES = [
    ('new', 'Новая'),
    ('in_progress', 'В процессе'),
    ('done', 'Сделано')]

YEARS_CHOICES = range(2015, 2026)


class TaskForm(forms.Form):
    description = forms.CharField(max_length=50,label='Описание', required=True)
    full_description = forms.CharField(max_length=3000, label='Полное описание', required=False,widget=forms.Textarea(
        attrs={'rows':4, 'cols':15}))
    status = forms.ChoiceField(label = 'Статус', required=True,choices=STATUS_CHOICES)
    execution_date = forms.DateField(label = 'Дата выполнения', required=False,widget=widgets.SelectDateWidget(years=YEARS_CHOICES, empty_label=("Выберите год", "Выберите месяц", "Выберите день")))