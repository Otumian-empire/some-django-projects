from django.db import models
from django.forms import ModelForm


class employees(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    emp_id = models.IntegerField()

    def __str__(self):
        return self.firstname


class employeesModelForm(ModelForm):
    class Meta:
        model = employees
        fields = ['firstname', 'lastname', 'emp_id']
