from django.urls import path
from . import views as v

from django.conf import settings
from django.conf.urls.static import static

app_name = 'core'

urlpatterns = [
    path('', v.HomePage.as_view(), name='home'),
    path('question/all', v.QuestionListView.as_view(), name='all-questions'),
    path('question/in/<int:pk>/', v.QuestionDetailView.as_view(), name='single-question'),
    path('question/new/', v.QuestionCreateView.as_view(), name='create-question'),
    path('question/delete/<int:pk>/', v.QuestionDeleteView.as_view(), name='delete-question'),
    path('question/update/<int:pk>/', v.QuestionEditView.as_view(), name='edit-question'),
    path('answer/new/', v.AnswerCreateView.as_view(), name='new-answer'),
    path('answer/update/<int:pk>/', v.AnswerEditView.as_view(), name='edit-answer'),
    path('question/search/', v.question_search, name='q-search'),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
