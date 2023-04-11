from django.shortcuts import render, HttpResponse, get_object_or_404
from .forms import DepartmentForm, StudentInfoForm
from .models import Department, StudentInfo
from .filters import FilterStudentInfo


# Create your views here.



def searchStudentInfo(request):

	students = StudentInfo.objects.all()
	filters = FilterStudentInfo(request.GET, queryset=students)

	context = {'filters': filters}

	return render(request, 'student/searchStudent.html', context)






