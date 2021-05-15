from django import forms


class ContactForm(forms.Form):


    subject = forms.CharField(max_length=50)
    from_email = forms.EmailField(required=True)
    # phone = forms.IntegerField()
    message = forms.CharField(widget=forms.Textarea, required=True)
