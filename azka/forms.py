from django import forms
from .models import Regisration

class signupForm(forms.ModelForm):
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label="Conform Password")
    def clean(self):
        cleaned_data=super().clean()
        p=cleaned_data['password']
        p2=cleaned_data['password2']
        if p!=p2:
            raise forms.ValidationError('Password Did Not Match')
    username = forms.RegexField(
        label="User name", max_length=30, regex=r"^[\w.@+-]+$",
        error_messages={
            'invalid': ("My message for invalid")
        }
        ,widget=forms.TextInput(attrs={'class':'form-control'})
    )
    
    class Meta:
        model=Regisration
        fields=['image','username','Full_name',"email",'Passing_Year','designation','password']
        
        # fields=['username','email','password']
        labels={'dob':'Date of Birth','phone_no':'Phone Number'}
        help_text={'username':"Enter your Full name"}
        error_messages={'username':{'required':'Plz Enter Your name'}}
        widgets={
            'Passing_Year':forms.DateTimeInput(attrs={'class':'form-control','type':'date'}),
            'Full_name':forms.TextInput(attrs={'class':'form-control','autocomplete': 'current-password'}),
            'designation':forms.TextInput(attrs={'class':'form-control',}), 
            'username':forms.TextInput(attrs={'class':'form-control','autofocus': True,}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
            'phone_no':forms.TextInput(attrs={"class":'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'father_name':forms.TextInput(attrs={'class':'form-control'}),
            'department':forms.TextInput(attrs={'class':'form-control'}),
            'is_active':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.Textarea(attrs={"rows":5, "cols":20,'class':'form-control','placeholder':'Type'}),
            'reponsibities':forms.Textarea(attrs={"rows":5, "cols":20,'class':'form-control'})
        }
    
    

class loginform(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True,'class':'form-control'}),error_messages={'required':'enter yourname'})
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'current-password','class':'form-control'}))
    
    
    




class ProfileForm(forms.ModelForm):
    class Meta:
        model=Regisration
        fields="__all__"
        exclude=('password','status','image')
        labels={'phone_no':'Phone Number','dob':'Date of Birth','Passing_Year':'Batch'}
        widgets={
            'Passing_Year':forms.TextInput(attrs={'class':'form-control','type':'date'}),
            'Full_name':forms.TextInput(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control','readonly':True}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
            'phone_no':forms.TextInput(attrs={"class":'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'father_name':forms.TextInput(attrs={'class':'form-control'}),
            'department':forms.TextInput(attrs={'class':'form-control'}),
            'is_active':forms.TextInput(attrs={'class':'form-control','readonly':True}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'reponsibities':forms.TextInput(attrs={'class':'form-control'}),
            'designation':forms.TextInput(attrs={'class':'form-control'}) 
        }

class updateForm(forms.ModelForm):
    class Meta:
        model=Regisration
        fields=['image']
        exclude=('is_active','time_stamp','status','password','username')
        # fields=['username','email','password']
        labels={'dob':'Date of Birth','phone_no':'Phone Number'}
        help_text={'username':"Enter your Full name"}
        error_messages={'username':{'required':'Plz Enter Your name'}}
        widgets={
            'Passing_Year':forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'Full_name':forms.TextInput(attrs={'class':'form-control','autocomplete': 'current-password'}),
            'designation':forms.TextInput(attrs={'class':'form-control',}), 
            'username':forms.TextInput(attrs={'class':'form-control','autofocus': True}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
            'phone_no':forms.TextInput(attrs={"class":'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'father_name':forms.TextInput(attrs={'class':'form-control'}),
            'department':forms.TextInput(attrs={'class':'form-control'}),
            'is_active':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.Textarea(attrs={"rows":5, "cols":20,'class':'form-control','placeholder':'Type'}),
            'reponsibities':forms.Textarea(attrs={"rows":5, "cols":20,'class':'form-control'})
        }
        

from .models import Testimonial
class testimonialForm(forms.ModelForm):
    class Meta:
        model=Testimonial
        fields="__all__"
        exclude=('status',)
        labels={'desc':'Description'}
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'desc': forms.TextInput(attrs={'class':'form-control'}),    
            
        }



class ContactForm(forms.Form):
	first_name = forms.CharField(widget=forms.TextInput(attrs={"class":'form-control'}),max_length = 50)
	last_name = forms.CharField(widget=forms.TextInput(attrs={"class":'form-control'}),max_length = 50)
	email_address = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control',}),max_length = 150)
	message = forms.CharField(widget = forms.Textarea(attrs={'class':'form-control'}), max_length = 2000)        