from django import forms


class EditPostForm(forms.Form):
    content = forms.CharField(label="Content", widget=forms.Textarea, required=True)
    title = forms.CharField(label="Title", required=False)
    picture = forms.FileField(label="Picture", required=False)


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