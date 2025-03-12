from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Send Message', css_class='btn btn-primary'))
        self.helper.layout = Layout(
            Field('name', css_class='form-control'),
            Field('email', css_class='form-control'),
            Field('message', css_class='form-control', rows=5),
        )
