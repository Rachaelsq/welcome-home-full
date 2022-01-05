
''' 
========================
JOURNAL VIEWS
========================
'''

from django.shortcuts import render
from django.urls.base import reverse
#CRUD imports
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

#redirect
from django.urls import reverse_lazy

#User auth imports
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

#model imports
from .models import Journal



# =============================
# LOGIN CLASSES
#============================== 

#typically, the login would be in a separate app
class CustomLoginView(LoginView):
    template_name = 'journalapp/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('journals')

#USER REGISTRATION
class RegisterPage(FormView):
    template_name = 'journalapp/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('journals')

# if user is succesfully created, go ahead and log in the user
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

#if user is logged in, do not show register page
"""     def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPage, self).get(*args, **kwargs) """




class JournalList(ListView):
    template_name = 'index.html'
    queryset = Journal.objects.order_by('-completed')

# =============================
#CRUD CLASSES
#============================== 

class JournalList(LoginRequiredMixin, ListView):
    model = Journal
    context_object_name = 'journals'
    
#restrict pages - getcontextdata
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['journals'] = context['journals'].filter(user=self.request.user)
        context['count'] = context['journals'].filter(complete=False).count()
        
        #search
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['journals'] = context['journals'].filter(
                title__contains=search_input)

        context['search_input'] = search_input

        return context
        

class JournalDetail(LoginRequiredMixin, DetailView):
    model = Journal
    context_object_name = 'journal'
    template_name = 'journal.html'

""" the 'fields' mixin gets submitted by the POST in the journal_form """

class JournalCreate(LoginRequiredMixin, CreateView):
    model = Journal
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('journals')
    #sends user back to url name which is 'journals'
    
    #newlyy created journal show up for appropriate user
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(JournalCreate, self).form_valid(form)

class JournalUpdate(LoginRequiredMixin, UpdateView):
    model = Journal
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('journals')
    
class DeleteView(LoginRequiredMixin, DeleteView):
    model = Journal
    context_object_name = 'journal'
    success_url = reverse_lazy('journals')