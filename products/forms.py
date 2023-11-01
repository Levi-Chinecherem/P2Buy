from django import forms
from .models import Product
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class ProductForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    
    class Meta:
        model = Product
        fields = ['name', 'short_description', 'product_cover_image', 'content', 'amount', 'category']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'short_description': forms.Textarea(attrs={'class': 'form-control'}),
            'product_cover_image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'content': forms.Textarea(attrs={'class': 'form-control ckeditor'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
