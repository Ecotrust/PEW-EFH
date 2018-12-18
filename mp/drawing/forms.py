from django import forms
from madrona.features.forms import FeatureForm, SpatialFeatureForm
from .models import AOI, Collection
# from .models import AOI, WindEnergySite

class AOIForm(SpatialFeatureForm):
    reg_action = forms.ChoiceField(choices=[('close','Closure'),('reopen','Re-opening')])
    description = forms.CharField(widget=forms.Textarea(attrs={'cols': 30, 'rows': 3}), required=False)

    class Meta(SpatialFeatureForm.Meta):
        model = AOI

# class WindEnergySiteForm(SpatialFeatureForm):
#     class Meta(SpatialFeatureForm.Meta):
#         model = WindEnergySite

class CollectionForm(FeatureForm):
    description = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 30, 'rows': 3}), required=False)

    import_file = forms.FileField(required=False)

    class Meta(FeatureForm.Meta):
        model = Collection
