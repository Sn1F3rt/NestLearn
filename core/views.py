from django.shortcuts import render
from django.views import generic
from .models import Question, Answer
from django.contrib.auth import mixins
from django.urls import reverse_lazy

from django.http import HttpResponse

from bs4 import BeautifulSoup

# Create your views here.


class HomePage(generic.TemplateView):
    template_name = 'core/home_page.html'


class QuestionListView(generic.ListView):
    model = Question


class QuestionDetailView(generic.DetailView):
    model = Question

    def get_context_data(self, **kwargs):
        context = super(QuestionDetailView, self).get_context_data(**kwargs)
        # noinspection PyUnresolvedReferences
        context['answer_list'] = Answer.objects.all()
        return context


class QuestionCreateView(mixins.LoginRequiredMixin, generic.CreateView):
    model = Question
    fields = ['title', 'question', 'attachment', 'tag']

    def form_valid(self, form):
        # noinspection PyAttributeOutsideInit
        self.object = form.save(commit=False)
        self.object.user = self.request.user

        if self.object.user.profile.type == 'student' and \
                BeautifulSoup(str(form), features='lxml').find("input", {"id": "id_tag"})["value"] == 'exam':
            error = 'Only teachers cam create questions tagged with "exam"!'
            return HttpResponse(error, status=403)

        self.object.save()
        return super().form_valid(form)


class AnswerCreateView(mixins.LoginRequiredMixin, generic.CreateView):
    model = Answer
    fields = ['answer', 'question']

    def form_valid(self, form):
        # noinspection PyAttributeOutsideInit
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class QuestionDeleteView(mixins.LoginRequiredMixin, generic.DeleteView):
    model = Question
    success_url = reverse_lazy("core:all-questions")


class QuestionEditView(mixins.LoginRequiredMixin, generic.UpdateView):
    model = Question
    fields = ['title', 'question', 'tag']
    template_name = 'core/question_update_form.html'


class AnswerEditView(mixins.LoginRequiredMixin, generic.UpdateView):
    model = Answer
    fields = ['answer', 'question']
    template_name = 'core/answer_update_form.html'


def question_search(request):
    query = request.GET.get('q')
    # noinspection PyUnresolvedReferences
    queryset = Question.objects.all()

    if query:
        queryset = queryset.filter(tag__icontains=query)

    return render(request, 'core/question_search.html', {'results': queryset})
