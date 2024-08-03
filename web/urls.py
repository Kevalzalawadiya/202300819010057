from django.urls import path
from django.views.generic import TemplateView
from web.views import InquiryView

urlpatterns = [
    path('pms/', TemplateView.as_view(template_name="privacy_policies/pms.html")),
    path('sales_tracker/', TemplateView.as_view(template_name="privacy_policies/sales_tracker.html")),
    path('feats_innovations/', TemplateView.as_view(template_name="privacy_policies/feats_innovations.html")),
]
