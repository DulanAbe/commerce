from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new", views.new, name="new"),
    path("test", views.test, name="test"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("listings/<str:listing_id>", views.listing, name="listing")
]
