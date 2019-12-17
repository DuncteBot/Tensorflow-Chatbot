from django.urls import path, include

urlpatterns = [
    path('api', include("Tensorflow_Chatbot.Api.urls")),
]
