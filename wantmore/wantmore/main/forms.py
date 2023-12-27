from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import User
from django import forms


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите имя пользователя'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите пароль'}))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistationForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите имя пользователя'}))
    email = forms.CharField(label='Email', widget=forms.EmailInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите Email'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
         'class': 'form-control py-4', 'placeholder': 'Подтвердите пароль'}))
    #steam_id = forms.CharField(widget=forms.TextInput(attrs={
        #'class': 'form-control py-4', 'placeholder': 'Введите Steam ID'}))
    #steam_api = forms.CharField(widget=forms.TextInput(attrs={
        #'class': 'form-control py-4', 'placeholder': 'Введите Api Key'}))

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')