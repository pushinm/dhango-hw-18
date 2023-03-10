from django.shortcuts import render, get_object_or_404
from .models import Student, Group

from django.db.models import Q, F, Count
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView
from django.views.generic.base import TemplateView

from .forms import StudentAddForm, Group_Create_Form


class StudentsTemplateView(TemplateView):
    template_name = "students_all.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        groups = Group.objects.all()
        students = Student.objects.select_related("group").all()

        max_cols = 0

        for group_item in groups:
            students_len = len(
                Student.objects.select_related("group").filter(Q(group=group_item.pk))
            )

            if max_cols < students_len:
                max_cols = students_len

        context = {
            "students": students,
            "groups": groups,
            "max_cols": max_cols,
        }

        context["students"] = students
        context["groups"] = groups
        context["max_cols"] = max_cols

        return context


class StudentTempateView(TemplateView):
    template_name = "student_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {"student": get_object_or_404(Student, pk=self.kwargs["pk"])}
        return context


class StudentAddView(CreateView):
    model = Student
    template_name = "student_add.html"
    success_url = "/students/"
    form_class = StudentAddForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            form.save(commit=True)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class StudentListView(ListView):
    model = Student
    template_name = "students_all.html"
    context_object_name = "students"

    def get_queryset(self):
        qs = {
            "students": Student.objects.select_related("group").all(),
            "groups": Group.objects.all(),
        }
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["students"] = self.get_queryset()["students"]
        context["groups"] = self.get_queryset()["groups"]

        max_cols = 0

        for group_item in context["groups"]:
            students_len = len(context["students"].\
                filter(Q(group=group_item.pk)))
            if max_cols < students_len:
                max_cols = students_len

        context["max_cols"] = max_cols

        return context


class StudentUpdateView(UpdateView):
    model = Student
    template_name = "student_add.html"
    form_class = StudentAddForm
    success_url = "/students/"


class StudentDeleteView(DeleteView):
    model = Student
    template_name = "student_delete.html"
    success_url = "/students/"


#TODO
#1. ???????????????? ?????????? ?????????????????????? ?????? ??????????????????. +
#2. ???????????????? ?????????? ?? ??????????????????????, ?????? ???????????????????? ?????????? ??????????????????. +
#3. ???????????????? ?????????? ?????? ?????????????????????? ??????????. +
#4. ???????????????? ?????????? ?? ??????????????????????, ?????? ???????????????????? ?????????? ??????????. +

class Group_View(ListView):
    template_name = 'groups_all.html'
    model = Group
    context_object_name = 'groups'

class Group_Create_View(CreateView):
    model = Group
    template_name = 'create_group.html'
    success_url = '/students/groups/'
    form_class = Group_Create_Form


class Group_Update(UpdateView):
    model = Group
    template_name = 'create_group.html'
    success_url = '/students/groups/'
    form_class = Group_Create_Form

class Group_Detail(DetailView):
    model = Group
    template_name = 'group_deteail.html'
    context_object_name = 'group'


class Group_Delete(DeleteView):
    model = Group
    template_name = 'delete_group.html'
    success_url = '/students/groups/'
