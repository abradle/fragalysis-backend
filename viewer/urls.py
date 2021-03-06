from django.conf.urls import url

from . import views

urlpatterns = [
    url(r"^react/*", views.react, name="react"),
    url(r"^img_from_smiles/$", views.img_from_smiles, name="img_from_smiles"),
    url(r"^sim_search/$", views.similarity_search, name="sim_search"),
]
