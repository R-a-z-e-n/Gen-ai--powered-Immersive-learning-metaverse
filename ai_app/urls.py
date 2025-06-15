from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='ai_signup'),
    path('login/', views.login_view, name='ai_login'),
    path('logout/', views.logout_view, name='ai_logout'),
    path('', views.index, name='ai_index'),
    path('api/quiz/', views.quiz_api, name='ai_quiz'),
    path('api/tokenize/', views.tokenize_api, name='ai_tokenize'),
    path('api/keywords/', views.keywords_api, name='ai_keywords'),
    path('api/similar/', views.similar_api, name='ai_similar'),
    path('api/tts/', views.tts_api, name='ai_tts'),
    path('api/plot/', views.plot_api, name='ai_plot'),
    path('api/ar/', views.ar_api, name='ai_ar'),
]