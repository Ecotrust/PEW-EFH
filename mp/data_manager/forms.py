from django import forms
from madrona.features.forms import FeatureForm, SpatialFeatureForm
from .models import ImportFeature, ImportLayer
# from .models import AOI, WindEnergySite

class ImportFeatureForm(SpatialFeatureForm):
    summary = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 30, 'rows': 3}), required=False)

    class Meta(SpatialFeatureForm.Meta):
        model = ImportFeature

# class WindEnergySiteForm(SpatialFeatureForm):
#     class Meta(SpatialFeatureForm.Meta):
#         model = WindEnergySite

class ImportLayerForm(FeatureForm):
    description = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 30, 'rows': 3}), required=False)

    import_file = forms.FileField(required=False)

    class Meta(FeatureForm.Meta):
        model = ImportLayer
