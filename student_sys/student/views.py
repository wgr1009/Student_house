from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import *
from .forms import StudentForm


def index(request):
    # students = Student.objects.all()
    students = Student.get_all()  # 因为后期可能会对学员的数据 进行过滤，比如需要调整为展示所有审核通过的学员， 此时就需要调整 view 函数中的代码者对结果进行缓存，也需要调整代码
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            # cleaned_data = form.cleaned_data   手动构建 Studnet 对象 保存 Student数据
            # student = Student()
            # student.name = cleaned_data['name']
            # student.sex = cleaned_data['sex']
            # student.email = cleaned_data['email']
            # student.profession = cleaned_data['profession']
            # student.qq = cleaned_data['qq']
            # student.phone = cleaned_data['phone']
            # student.save()

            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = StudentForm()

    context = {
        'students': students,
        'form': form
    }
    # 如果是 get 请求 返回空  post填充
    return render(request, 'index.html', context=context)

