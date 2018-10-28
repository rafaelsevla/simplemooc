from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Course, Enrollment
from .forms import ContactCourse


def index(request):
    courses = Course.objects.all()
    template_name = 'courses/index.html'
    context = {
        'courses': courses
    }
    return render(request, template_name, context)

# def details(request, pk):
# 	courses = get_object_or_404(Course, pk=pk)
# 	context = {
# 		'course': courses
# 	}
# 	template_name = 'courses/details.html'
# 	return render(request, template_name, context)


def details(request, slug):
    courses = get_object_or_404(Course, slug=slug)
    context = {}
    if request.method == 'POST':
        form = ContactCourse(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            form.send_mail(courses)
            form = ContactCourse()
    else:
        form = ContactCourse()
    context ['form'] = form
    context ['course'] = courses
    template_name = 'courses/details.html'
    return render(request, template_name, context)


@login_required
def enrollment(request, slug):
    courses = get_object_or_404(Course, slug=slug)
    enrollments, created = Enrollment.objects.get_or_create(
        user=request.user, course=courses
    )
    if created:
        # enrollment.active()
        messages.success(request, 'Cadastro feito com sucesso!')
    else:
        messages.warning(request, 'Você já está cadastrado nesse curso!!', extra_tags='alert')

    return redirect('accounts:dashboard')
