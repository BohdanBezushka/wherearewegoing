from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Name')
    email = forms.EmailField(required=True, label='Email')
    phone = forms.CharField(max_length=20, required=False, label='Phone')
    title = forms.CharField(max_length=100, required=True, label='Title')
    description = forms.CharField(widget=forms.Textarea, required=True, label='Description')
    contact_method = forms.ChoiceField(
        choices=[('call', 'Call'), ('message', 'Send Message')],
        widget=forms.RadioSelect,
        required=True,
        label='Preferred Contact Method'
    )