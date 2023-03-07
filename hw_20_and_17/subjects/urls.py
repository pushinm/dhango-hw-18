from django.urls import path

from teachers.urls import app_name

from .views import (Subjects_View,
                    Subjects_Create,
                    Subjects_Update,
                    Subjects_Detail,
                    Subjects_Delete)
# from classboard.views import filter_students_group

app_name = 'subjects'

urlpatterns = [
    path('', Subjects_View.as_view(), name='subjects_view'),
    path('create/', Subjects_Create.as_view(), name='create_subject'),
    path('<int:pk>/', Subjects_Detail.as_view(), name='subjects_detail'),
    path('delete/<int:pk>/', Subjects_Delete.as_view(), name='subjects_delete'),
    path('update/<int:pk>/', Subjects_Update.as_view(), name='subject_update')
    # path('with_teacher/', show_classes_teacher, name='show_classes_teacher'),
    # path('with_teacher/<int:pk>', show_classes_teacher, name='show_classes_teacher'),
    # path('with_teacher', class_view, name='class_view'),
   # path('change_teacher/<int:pk>/<int:tpk>', change_teacher, name='change_teacher'),
    # path('filter_group/', filter_students_group, name='filter_students_group'),
]
