from django.urls import path
from django.views.generic import TemplateView
from cbv.views import Ex2View

app_name = 'website'

urlpatterns = [
    # extra_context Attribute from ContentMixin - keyword argument for as_view()
    # path('', TemplateView.as_view(template_name="ex1.html", extra_context={'title': 'Custom Title'})),
    path('', Ex2View.as_view(), name='ex2'),
]
