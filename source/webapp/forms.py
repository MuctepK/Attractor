from django import forms
from django.forms import widgets
STATUS_CHOICES = [
    ('new', 'Новая'),
    ('in_progress', 'В процессе'),
    ('done', 'Сделано')]

class TaskForm(forms.Form):
    description = forms.CharField(max_length=50,label='Описание', required=True)
    full_description = forms.CharField(max_length=3000, label='Полное описание', required=False)
    status = forms.ChoiceField(label = 'Статус', required=True,choices=STATUS_CHOICES)
    execution_date = forms.DateField(label = 'Дата выполнения', required=False)