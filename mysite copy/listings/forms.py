from django import forms


class SignupForm(forms.Form):
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(),
        required=True,
    )
    display_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)


class SigninForm(forms.Form):
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(),
        required=True,
    )
    email = forms.EmailField()