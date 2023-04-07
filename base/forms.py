"""
from django import forms
from  . models import Users, Tasks, Categories, Reminders

class Users(forms.Form):
    class Meta:
        model = Users
        fields = "__all__"

class Tasks(forms.Form):
    class Meta:
        model = Tasks
        fields = "__all__"

class Reminders(forms.Form):
    class Meta:
        model = Reminders
        fields = "__all__"

class Categories(forms.Form):
    class Meta:
        model = Categories
        fields = "__all__"

"""