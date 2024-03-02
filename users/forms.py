from django import forms


class AddStudentForm(forms.Form):
    """Форма добавления студента в группу"""
    surname = forms.CharField(label="Фамилия", max_length=100, required=True)
    name = forms.CharField(label="Имя", max_length=100, required=True)
    username = forms.CharField(label="Никнейм", max_length=100, required=True)
