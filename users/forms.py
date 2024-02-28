from django import forms


class AddStudentForm(forms.Form):
    surname = forms.CharField(label="Фамилия", max_length=100, required=True)
    name = forms.CharField(label="Имя", max_length=100, required=True)
    username = forms.CharField(label="Никнейм", max_length=100, required=True)
    product_name = forms.CharField(label="Название продукта", max_length=100, required=True)

