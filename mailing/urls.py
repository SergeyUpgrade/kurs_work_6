from django.urls import path
from django.views.decorators.cache import cache_page

from mailing.apps import MailingConfig
from mailing.views import (
    ClientCreateView,
    ClientDeleteView,
    ClientUpdateView,
    ClientListView,
    ClientDetailView,
    MailingCreateView,
    MailingDeleteView,
    MailingDetailView,
    MailingUpdateView,
    MailingListView,
    MessageCreateView,
    MessageDeleteView,
    MessageDetailView,
    MessageUpdateView,
    MessageListView, MainPage, MailingAttemptListView,
)

app_name = MailingConfig.name

urlpatterns = [
    path('', cache_page(5)(MainPage.as_view()), name='main_page'),
    path("client/", ClientListView.as_view(), name="client_list"),
    path("client/create", ClientCreateView.as_view(), name="client_create"),
    path("client/<int:pk>/update/", ClientUpdateView.as_view(), name="client_update"),
    path("client/<int:pk>/delete/", ClientDeleteView.as_view(), name="client_delete"),
    path("client/<int:pk>/", ClientDetailView.as_view(), name="client_detail"),
    path("mailing/", MailingListView.as_view(), name="mailing_list"),
    path("mailing/create", MailingCreateView.as_view(), name="mailing_create"),
    path("mailing/<int:pk>/update/", MailingUpdateView.as_view(), name="mailing_update"),
    path("mailing/<int:pk>/delete/", MailingDeleteView.as_view(), name="mailing_delete"),
    path('mailings/<int:mailing_id>/attempts/', MailingAttemptListView.as_view(), name="mailing_attempt_list"),
    path("mailing/<int:pk>/", MailingDetailView.as_view(), name="mailing_detail"),
    path("message/", MessageListView.as_view(), name="message_list"),
    path("message/create", MessageCreateView.as_view(), name="message_create"),
    path("message/<int:pk>/update/", MessageUpdateView.as_view(), name="message_update"),
    path("message/<int:pk>/delete/", MessageDeleteView.as_view(), name="message_delete"),
    path("message/<int:pk>/", MessageDetailView.as_view(), name="message_detail"),
]
