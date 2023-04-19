from django import forms

class feedbackForm(forms.Form):
    title = forms.CharField(label='Title',min_length=1,widget=forms.TextInput(attrs={'class':'form-control'}))
    subject = forms.CharField(label='Subject Description',max_length=200,widget=forms.Textarea(attrs={'class':'form-control'}))
    email = forms.CharField(label='Email',min_length=1,widget=forms.TextInput(attrs={'class':'form-control'}))