from django.shortcuts import render, get_object_or_404

from .models import Subject
from teachers.models import Teacher
from .forms import Subject_create_form
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.db.models import Q

# Create your views here.

#TODO
#1. Написать класс отображения для предметов. +
#2. Написать класс и отображение, для добавления новых предметов. +
#3. Написать класс для отображения групп.
#4. Написать класс и отображение, для добавления новых групп.

class Subjects_View(ListView):
    model = Subject
    template_name = 'subjects.html'
    context_object_name = 'classes'

class Subjects_Create(CreateView):
    model = Subject
    template_name = 'subjects_create.html'
    success_url = '/subjects/'
    form_class = Subject_create_form

class Subjects_Update(UpdateView):
    model = Subject
    template_name = 'subjects_create.html'
    success_url = '/subjects/'
    form_class = Subject_create_form

class Subjects_Detail(DetailView):
    model = Subject
    template_name = 'subject_detail.html'
    context_object_name = 'current_subject'


class Subjects_Delete(DeleteView):
    model = Subject
    template_name = 'subject_delete.html'
    success_url = '/subjects/'


def subjects_view(request, pk=None) -> render:
    if pk:
        template = 'subject_detail.html'
        subject = get_object_or_404(Subject, pk=pk)
        context = {
            'subject': subject,
        }
    else:
        template = 'subjects.html'
        classes = Subject.objects.all()
        teachers = Teacher.objects.all()
        context = {
            'subjects': classes,
            'teachers': teachers,
        }

    return render(request=request, template_name=template, context=context)


def subjects_delete(request, pk) -> render:
    template = 'subjects.html'

    class_ = get_object_or_404(Subject, pk=pk)

    class_.delete()

    classes = Subject.objects.all()

    context = {
        'subjects': classes,
    }

    return render(request=request, template_name=template, context=context)

def change_teacher(request, pk, tpk) -> render:
    template = 'subjects.html'


    subject = get_object_or_404(Subject, pk=pk)
    teacher = get_object_or_404(Teacher, pk=tpk)

    subject.teacher = teacher
    subject.save()

    # class_ = Class.objects.filter(pk=pk).update(teacher=teacher)

    subjects = Subject.objects.all()
    teachers = Teacher.objects.all()

    # teachers = Teacher.objects.filter(Q(pk__lte=3))

    context = {
        'subjects': subjects,
        'teachers': teachers,
    }

    return render(request=request, template_name=template, context=context)


   # def get_context_data(self, *args, **kwargs):
   #     context = super().get_context_data(**kwargs)

  #      context['classes'] = Subject.objects.all()
 #       context['teachers'] = Teacher.objects.all()
#
 #       return context

# def show_classes_teacher(request, pk=None) -> render:
#     if pk:
#         template = 'classes_with_teachers_detail.html'
#         class_ = get_object_or_404(ClassWithTeacher, pk=pk)
#
#         teacher_first_name = []
#         q_ = Q(teacher__first_name='Кравец') | Q(teacher__first_name='Макаренко')
#
#
#         for teacher_first_name_item in ClassWithTeacher.objects.filter(teacher__first_name='Кравец').prefetch_related().values('teacher__first_name', 'teacher__last_name'):
#         # for teacher_first_name_item in ClassWithTeacher.objects.filter().prefetch_related().values('teacher__first_name', 'teacher__last_name'):
#         # for teacher_first_name_item in ClassWithTeacher.objects.filter().prefetch_related().values('teacher__first_name', 'teacher__last_name').distinct():
#             teacher_first_name.append(teacher_first_name_item)
#
#         context = {
#             'class': class_,
#             'teacher_first_name': teacher_first_name,
#         }
#     else:
#         template = 'classes_with_teachers.html'
#
#
#         # class_.teacher = teacher
#         # class_.save()
#
#         # class_ = Class.objects.filter(pk=pk).update(teacher=teacher)
#
#         subjects = ClassWithTeacher.objects.all()
#         teachers = Teacher.objects.all()
#
#
#
#         # teachers = Teacher.objects.filter(Q(pk__lte=3))
#
#         context = {
#             'subjects': subjects,
#             'teachers': teachers,
#         }
#
#     return render(request=request, template_name=template, context=context)