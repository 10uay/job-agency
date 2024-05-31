from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('place-resume/', views.placeResume, name='place-resume'),
    path('place-vacancy/', views.placeVacancy, name='place-vacancy'),
    path('see-vacancies/', views.seeVacancies, name='see-offers'),
    path('see-resumes/', views.seeResumes, name='see-resumes'),
    path('see-resumes/<int:id>', views.detailResume, name='detail-resume'),
    path('delete-resume/<int:id>', views.deleteResume, name='delete-resume'),
    path('see-vacancies/<int:id>', views.detailVacancy, name='detail-vacancy'),
    path('delete-vacancy/<int:id>', views.deleteVacancy, name='delete-vacancy'),
    path('super-user/', views.superUser, name='dash')
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
