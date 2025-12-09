from django import forms
from .models import ContactSubmission


class ContactForm(forms.ModelForm):
    """
    Contact and enrollment form with validation
    """
    # Add honeypot field for spam prevention
    website = forms.CharField(required=False, widget=forms.HiddenInput())
    
    class Meta:
        model = ContactSubmission
        fields = ['name', 'email', 'phone', 'subject', 'message', 'interest_type', 'age_group']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Your Name *',
                'required': True,
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-input',
                'placeholder': 'Your Email *',
                'required': True,
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Your Phone Number *',
                'required': True,
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Subject *',
                'required': True,
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-textarea',
                'placeholder': 'Your Message *',
                'rows': 5,
                'required': True,
            }),
            'interest_type': forms.Select(attrs={
                'class': 'form-select',
            }),
            'age_group': forms.Select(attrs={
                'class': 'form-select',
            }),
        }
        labels = {
            'interest_type': 'I am interested in',
            'age_group': 'Age Group (for academy enrollment)',
        }
    
    def clean_website(self):
        """Honeypot validation"""
        website = self.cleaned_data.get('website')
        if website:
            raise forms.ValidationError('Invalid submission')
        return website
    
    def clean(self):
        cleaned_data = super().clean()
        interest_type = cleaned_data.get('interest_type')
        age_group = cleaned_data.get('age_group')
        
        # If interest is academy enrollment, age group should be provided
        if interest_type in ['academy', 'both'] and not age_group:
            self.add_error('age_group', 'Please select an age group for academy enrollment.')
        
        return cleaned_data
