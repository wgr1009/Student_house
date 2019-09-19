from django import forms
from .models import *


# class StudentForm(forms.Form):
#     name = forms.CharField(label='姓名', max_length=128)
#     sex = forms.ChoiceField(label='性别', choices=Student.SEX_ITEMS)
#     profession = forms.CharField(label='职业', max_length=128)
#     email = forms.EmailField(label='邮箱', max_length=128)
#     qq = forms.CharField(label='QQ', max_length=128)
#     phone = forms.CharField(label='手机', max_length=128)

# class StudentForm(forms.ModelForm):
#     class Meta:
#         model = Student
#         fields = [
#             'name', 'sex', 'profession', 'email', 'qq', 'phone'
#         ]


# 此处可用重新写一个form 也可以直接用models中的模型，复用代码

class StudentForm(forms.ModelForm):
    def clean_qq(self):
        cleaded_data = self.cleaned_data['qq']
        if not cleaded_data.isdigit():
            raise forms.ValidationError('必须是纯数字')
        return int(cleaded_data)

    class Meta:
        model = Student
        fields = [
            'name', 'sex', 'profession', 'email', 'qq', 'phone'
        ]