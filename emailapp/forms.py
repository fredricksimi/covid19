from django import forms

class Subscribe(forms.Form):
    Email = forms.EmailField()
    phone_number =forms.TextInput()
    the_message = forms.TextInput()

    def __str__(self):
        return self.Email