# =============================
#.JOURNAL APP URLS
#==============================
from django.urls import path
from .views import JournalList, JournalDetail, JournalCreate, JournalUpdate, DeleteView, CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    #logout. there is no class/ custom view for logout
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('Register/', RegisterPage.as_view(), name='register'),
    path('', JournalList.as_view(), name='journals'),
    path('create-journal/', JournalCreate.as_view(), name='journal-create'),
    path('journal/<int:pk>/', JournalDetail.as_view(), name='journal'),
    path('journal-update/<int:pk>/', JournalUpdate.as_view(), name='journal-update'),
    path('journal-delete/<int:pk>/', DeleteView.as_view(), name='journal-delete'),
] 