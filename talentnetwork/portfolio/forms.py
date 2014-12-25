from django import forms


class UploadPhotosForm(forms.Form):
    photos = forms.FileField(label="Upload Photos", required=False)


class EditProfileForm(forms.Form):
    aboutme = forms.CharField(label="Intro", widget=forms.Textarea, required=False)
    website_url = forms.CharField(label="URL", required=False)
    website_name = forms.CharField(label="Name", required=False)
    picture = forms.FileField(label="Photo", required=False)


class EditPhotoForm(forms.Form):
    title = forms.CharField(label="Title", required=False)


class RegisterForm(forms.Form):
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(),
        required=True,
    )
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)


class LoginForm(forms.Form):
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(),
        required=True,
    )
    email = forms.EmailField()


class PortfolioForm(forms.Form):
    photo = forms.ImageField(label="Upload a photo")