from django import forms


class EditPostForm(forms.Form):
    id = forms.IntegerField(required=True)
    content = forms.CharField(label="Content", widget=forms.Textarea, required=True)
    title = forms.CharField(label="Title", required=False)
    tags = forms.CharField(label="Tags", required=False)
    location = forms.CharField(label="Location", required=False)
    price = forms.IntegerField(label="Price", required=False)
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