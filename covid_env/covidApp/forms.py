from django import forms

from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User


def should_be_empty(value):
    if value:
        raise forms.ValidationError('Field is not empty')


class ContactForm(forms.Form):
    name = forms.CharField(label='الاسم', max_length=80)
    message = forms.CharField(label='الرسالة', widget=forms.Textarea)
    email = forms.EmailField(label='البريد الالكتروني')
    forcefield = forms.CharField(
        required=False, widget=forms.HiddenInput, label="Leave empty", validators=[should_be_empty])


# # Override the UserCreationForm
# class UserCreateForm(UserCreationForm):
#     email = forms.EmailField(required=True, label='Email', error_messages={
#                              'exists': 'This already exists!'})

#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2')

#     def save(self, commit=True):
#         user = super(UserCreateForm, self).save(commit=False)
#         user.email = self.cleaned_data['email']
#         if commit:
#             user.save()
#         return user

#     def clean_email(self):
#         if User.objects.filter(email=self.cleaned_data['email']).exists():
#             raise forms.ValidationError(
#                 self.fields['email'].error_messages['exists'])
#         return self.cleaned_data['email']

# class ContactForm(forms.Form):
#     name = forms.CharField(label='الاسم',max_length=128, required=True)
#     email = forms.EmailField(required=False)
#     title = forms.CharField(max_length=128, required=True)
#     # content = forms.TextField()
#     # img = forms.ImageField(
#     #     upload_to='contact/', null=True, blank=True)
#     # date = forms.DateTimeField(auto_now_add=True)

#     # def __str__(self):
#     #     return self.title
