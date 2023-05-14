from django.urls import path
from feedback.views import FeedbackCreateAPIView

urlpatterns = [
    path('api/feedback/', FeedbackCreateAPIView.as_view(), name='feedback-create'),
]
