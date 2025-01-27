from django import forms
from user.models import *

class RegistroForm(forms.Form):
    numero_documento = forms.CharField(max_length=11, widget=forms.TextInput(attrs={
        'class': 'form-control form-control-user',
        'placeholder': 'Número de documento'
    }))
    nombre_usuario = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control form-control-user',
        'placeholder': 'Nombre completo'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control form-control-user',
        'placeholder': 'Correo electrónico'
    }))
    contrasena = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control form-control-user',
        'placeholder': 'Contraseña'
    }))
    confirmar_contrasena = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control form-control-user',
        'placeholder': 'Confirmar contraseña'
    }))
    perfil = forms.FileField(widget=forms.FileInput(attrs={
        'class': 'form-control form-file'
    }))

class UsuarioEditForm(forms.Form):
    rol = forms.ChoiceField(
        choices=[(1, 'Administrador'), (2, 'Usuario')],
        widget=forms.Select(attrs={
            'class': 'form-control form-control-rol',
        }),
    )
    img = forms.FileField(widget=forms.FileInput(attrs={
        'class': 'form-control form-control-img',
    }), required=False )
    nombre = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
        'class': 'form-control form-control-user',
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control form-control-user',
    }))
    habilitacion = forms.ChoiceField(
        choices=[(1, 'Sí'), (0, 'No')],
        widget=forms.Select(attrs={
            'class': 'form-control form-control-habilitacion',
        }),
        required=False
    )