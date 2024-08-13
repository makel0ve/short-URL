from django import forms


class URLForm(forms.Form):
    input_url = forms.URLField(label='', required=True, widget=forms.TextInput(attrs={'placeholder': 'Введите ссылку',
                                                                                      'autocomplete': 'off'}))