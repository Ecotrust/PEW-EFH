# coding: utf-8
from madrona.features.forms import FeatureForm, SpatialFeatureForm
from django import forms
from django.forms import ModelMultipleChoiceField, CheckboxSelectMultiple
from django.forms.widgets import *
from django.forms.widgets import Input
from django.utils.safestring import mark_safe
from django.contrib.gis.geos import fromstr
from os.path import splitext, split
from madrona.analysistools.widgets import SliderWidget, DualSliderWidget
from .models import *
from widgets import AdminFileWidget, SliderWidgetWithTooltip, DualSliderWidgetWithTooltip, CheckboxSelectMultipleWithTooltip, CheckboxSelectMultipleWithObjTooltip

# http://www.neverfriday.com/sweetfriday/2008/09/-a-long-time-ago.html


class FileValidationError(forms.ValidationError):
    def __init__(self):
        super(FileValidationError, self).__init__('Document types accepted: ' + ', '.join(ValidFileField.valid_file_extensions))


class ValidFileField(forms.FileField):
    """A validating document upload field"""
    valid_file_extensions = ['odt', 'pdf', 'doc', 'xls', 'txt', 'csv', 'kml', 'kmz', 'jpeg', 'jpg', 'png', 'gif', 'zip']

    def __init__(self, *args, **kwargs):
        super(ValidFileField, self).__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        f = super(ValidFileField, self).clean(data, initial)
        if f:
            ext = splitext(f.name)[1][1:].lower()
            if ext in ValidFileField.valid_file_extensions:
                # check data['content-type'] ?
                return f
            raise FileValidationError()


class InputWithUnit(Input):
    """Modified Input class that accepts a "unit" parameter, and stores the
    value in the unit attribute.
    This is allows additional data associated with a field to be exposed to the
    template renderer. Later improvements would be to stick this value on the
    field itself rather than the widget. Also, make it a dictionary rather than
    a single value, so other arbitrary values can be brough forward.
    """
    def __init__(self, attrs=None, unit=None):
        super(InputWithUnit, self).__init__(attrs)
        self.unit = str(unit)


class TextInputWithUnit(forms.TextInput, InputWithUnit):
    pass


class ScenarioForm(FeatureForm):
    description = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 30, 'rows': 3}), required=False)

    # Step 1
    species = forms.BooleanField(
        label="Species",
        required=False,
        help_text="Species Presence",
        widget=CheckboxInput(
            attrs={
                'class': 'parameters hidden_checkbox'
            }
        )
    )
    species_choices = sorted([(x.common_name, x.common_name.title()) for x in Species.objects.all()])
    if len(species_choices) > 0 and len(species_choices[0]) > 0:
        species_input_initial = species_choices[0][0]
    else:
        species_input_initial = None
    species_input = forms.ChoiceField(
        required=False,
        widget=forms.Select(
            attrs={'class': 'parameters'}
        ),
        choices=species_choices,
        initial=species_input_initial
    )

    lifestage = forms.BooleanField(
        label="Life Stage",
        required=False,
        help_text="Species Life Stage",
        widget=CheckboxInput(
            attrs={
                'class': 'parameters hidden_checkbox'
            }
        )
    )
    lifestage_input = forms.ChoiceField(
        required=False,
        widget=forms.Select(
            attrs={'class': 'parameters'}
        ),
        choices=(
            ('adults', 'Adults'),
            ('juveniles', 'Juveniles'),
            ('eggs', 'Eggs'),
            ('larvae', 'Larvae')
        ),
        initial='Adults'
    )

    mean_fthm = forms.BooleanField(
        label="Average Depth",
        required=False,
        help_text="Mean depth of 5nmx5nm Planning Unit",
        widget=CheckboxInput(
            attrs={
                'class': 'parameters hidden_checkbox'
            }
        )
    )
    mean_fthm_min = forms.FloatField(
        required=False,
        initial=10,
        widget=forms.TextInput(
            attrs={
                'class': 'slidervalue',
                'pre_text': 'Depth'
            }
        )
    )
    mean_fthm_max = forms.FloatField(
        required=False,
        initial=50,
        widget=forms.TextInput(
            attrs={
                'class': 'slidervalue',
                'pre_text': 'to',
                'post_text': 'fathoms'
            }
        )
    )
    mean_fthm_input = forms.FloatField(
        widget=DualSliderWidget(
            'mean_fthm_min',
            'mean_fthm_max',
            min=0,
            max=3000,
            step=5
        )
    )
    hsall_m2 = forms.BooleanField(
        label="Predicted Coral Suitable Habitat",
        required=False,
        help_text="grid cells with presence of any class 1-4 suitable habitat for at least one species of coral",
        widget=CheckboxInput(
            attrs={'class': 'parameters hidden_checkbox', 'layer_id': 388, 'layer_title': 'PHS Taxa of Deep-sea Coal'}
        )
    )
    hs_classes = (("1", "Class 1"), ("2", "Class 2"), ("3", "Class 3"), ("4", "Class 4"))
    hsall_m2_checkboxes = forms.MultipleChoiceField(
        label="Classes to include",
        choices=hs_classes,
        required=False,
        help_text="include cells that include any suitable habitat meeting the selected classes",
        widget=CheckboxSelectMultiple(),
        initial=("1", "2", "3", "4")
    )
    # hsall1_m2 = forms.BooleanField(
    #     label="Predicted Class 1 Suitable Coral Habitat Area",
    #     required=False,
    #     help_text="Square kilometers of predicted class 1 habitat suitable for at least one species",
    #     widget=CheckboxInput(
    #         attrs={'class': 'parameters hidden_checkbox', 'layer_id': 388, 'layer_title': 'Coral and Sponges Predicted Habitat Suitability'}
    #     )
    # )
    # hsall1_m2_min = forms.FloatField(
    #     required=False,
    #     initial=1,
    #     widget=SliderWidget(
    #         attrs={
    #             'class': 'slidervalue',
    #             'range': 'max',
    #             'pre_text': 'Predicted Class 1 Habitat (km<sup>2</sup>)'
    #         },
    #         min=0,
    #         max=86,
    #         step=0.001
    #     )
    # )
    # hsall2_m2 = forms.BooleanField(
    #     label="Predicted Class 2 Suitable Coral Habitat Area",
    #     required=False,
    #     help_text="Square kilometers of predicted class 2 habitat suitable for at least one species",
    #     widget=CheckboxInput(
    #         attrs={'class': 'parameters hidden_checkbox', 'layer_id': 388, 'layer_title': 'Coral and Sponges Predicted Habitat Suitability'}
    #     )
    # )
    # hsall2_m2_min = forms.FloatField(
    #     required=False,
    #     initial=1,
    #     widget=SliderWidget(
    #         attrs={'class': 'slidervalue', 'range': 'max', 'pre_text': 'Predicted Class 2 Habitat (km<sup>2</sup>)'},
    #         min=0,
    #         max=86,
    #         step=0.001
    #     )
    # )
    # hsall3_m2 = forms.BooleanField(
    #     label="Predicted Class 3 Suitable Coral Habitat Area",
    #     required=False,
    #     help_text="Square kilometers of predicted class 3 habitat suitable for at least one species",
    #     widget=CheckboxInput(
    #         attrs={'class': 'parameters hidden_checkbox', 'layer_id': 388, 'layer_title': 'Coral and Sponges Predicted Habitat Suitability'}
    #     )
    # )
    # hsall3_m2_min = forms.FloatField(
    #     required=False,
    #     initial=1,
    #     widget=SliderWidget(
    #         attrs={'class': 'slidervalue', 'range': 'max', 'pre_text': 'Predicted Class 3 Habitat (km<sup>2</sup>)'},
    #         min=0,
    #         max=86,
    #         step=0.001
    #     )
    # )
    # hsall4_m2 = forms.BooleanField(
    #     label="Predicted Class 4 Suitable Coral Habitat Area",
    #     required=False,
    #     help_text="Square kilometers of predicted class 4 habitat suitable for at least one species",
    #     widget=CheckboxInput(
    #         attrs={'class': 'parameters hidden_checkbox', 'layer_id': 388, 'layer_title': 'Coral and Sponges Predicted Habitat Suitability'}
    #     )
    # )
    # hsall4_m2_min = forms.FloatField(
    #     required=False,
    #     initial=1,
    #     widget=SliderWidget(
    #         attrs={'class': 'slidervalue', 'range': 'max', 'pre_text': 'Predicted Class 4 Habitat (km<sup>2</sup>)'},
    #         min=0,
    #         max=86,
    #         step=0.001
    #     )
    # )
    hpc_est_m2 = forms.BooleanField(
        label="Estuary Habitat Area",
        required=False,
        help_text="Square miles of estuary habitat",
        widget=CheckboxInput(
            attrs={'class': 'parameters hidden_checkbox', 'layer_id': 419, 'layer_title': 'Habitat areas of particular concern - estuary'}
        )
    )
    hpc_est_m2_min = forms.FloatField(
        required=False,
        initial=1,
        widget=SliderWidget(
            attrs={'class': 'slidervalue', 'range': 'max', 'pre_text': 'Estuary Habitat (mi<sup>2</sup>)'},
            min=0,
            max=34,
            step=0.1
        )
    )
    hpc_klp_m2 = forms.BooleanField(
        label="Kelp Habitat Area",
        required=False,
        help_text="Square miles of kelp habitat",
        widget=CheckboxInput(
            attrs={'class': 'parameters hidden_checkbox', 'layer_id': 420, 'layer_title': 'Habitat areas of particular concern - canopy kelp'}
        )
    )
    hpc_klp_m2_min = forms.FloatField(
        required=False,
        initial=1,
        widget=SliderWidget(
            attrs={'class': 'slidervalue', 'range': 'max', 'pre_text': 'Kelp Habitat (mi<sup>2</sup>)'},
            min=0,
            max=5.4,
            step=0.1
        )
    )
    hpc_rck_m2 = forms.BooleanField(
        label="Rocky Reef Habitat Area",
        required=False,
        help_text="Square miles of rocky reef habitat",
        widget=CheckboxInput(
            attrs={'class': 'parameters hidden_checkbox', 'layer_id': 421, 'layer_title': 'Habitat areas of particular concern - rocky reef'}
        )
    )
    hpc_rck_m2_min = forms.FloatField(
        required=False,
        initial=1,
        widget=SliderWidget(
            attrs={'class': 'slidervalue', 'range': 'max', 'pre_text': 'Rocky Reef Habitat (mi<sup>2</sup>)'},
            min=0,
            max=34,
            step=0.1
        )
    )
    hpc_sgr_m2 = forms.BooleanField(
        label="Seagrass Habitat Area",
        required=False,
        help_text="Square miles of seagrass habitat",
        widget=CheckboxInput(
            attrs={'class': 'parameters hidden_checkbox', 'layer_id': 422, 'layer_title': 'Habitat areas of particular concern - seagrass'}
        )
    )
    hpc_sgr_m2_min = forms.FloatField(
        required=False,
        initial=1,
        widget=SliderWidget(
            attrs={
                'class': 'slidervalue',
                'range': 'max',
                'pre_text': 'Seagrass Habitat (mi<sup>2</sup>)'},
            min=0,
            max=26,
            step=0.1
        )
    )

    # Step 2
    sft_sub_m2 = forms.BooleanField(
        label="Has Soft Substrate",
        required=False,
        help_text="Planning units that contain at least some soft substrate",
        widget=CheckboxInput(
            attrs={'class': 'parameters hidden_checkbox'}
        )
    )
    sft_sub_m2_input = forms.ChoiceField(
        required=False,
        widget=forms.Select(
            attrs={'class': 'parameters'}
        ),
        choices=(
            ('Y', 'Include'),
            ('N', 'Exclude')),
        initial='Y'
    )
    mix_sub_m2 = forms.BooleanField(
        label="Has Mixed Substrate",
        required=False,
        help_text="Planning units that contain at least some mixed substrate",
        widget=CheckboxInput(
            attrs={'class': 'parameters hidden_checkbox'}
        )
    )
    mix_sub_m2_input = forms.ChoiceField(
        required=False,
        widget=forms.Select(
            attrs={'class': 'parameters'}
        ),
        choices=(
            ('Y', 'Include'),
            ('N', 'Exclude')),
        initial='Y'
    )
    hrd_sub_m2 = forms.BooleanField(
        label="Has Hard Substrate",
        required=False,
        help_text="Planning units that contain at least some hard substrate",
        widget=CheckboxInput(
            attrs={'class': 'parameters hidden_checkbox'}
        )
    )
    hrd_sub_m2_input = forms.ChoiceField(
        required=False,
        widget=forms.Select(
            attrs={'class': 'parameters'}
        ),
        choices=(
            ('Y', 'Include'),
            ('N', 'Exclude')),
        initial='Y'
    )
    rck_sub_m2 = forms.BooleanField(
        label="Has Inferred Rock Substrate (OR Only)",
        required=False,
        help_text="Planning units that contain at least some inferred rock substrate",
        widget=CheckboxInput(
            attrs={'class': 'parameters hidden_checkbox'}
        )
    )
    rck_sub_m2_input = forms.ChoiceField(
        required=False,
        widget=forms.Select(
            attrs={'class': 'parameters'}
        ),
        choices=(
            ('Y', 'Include'),
            ('N', 'Exclude')),
        initial='Y'
    )
    cnt_cs = forms.BooleanField(
        label="Has Observed Corals or Sponges",
        required=False,
        help_text="Planning units that contain observed corals or sponges",
        widget=CheckboxInput(
            attrs={'class': 'parameters hidden_checkbox'}
        )
    )
    cnt_cs_input = forms.ChoiceField(
        required=False,
        widget=forms.Select(
            attrs={'class': 'parameters'}
        ),
        choices=(
            ('Y', 'Include'),
            ('N', 'Exclude')),
        initial='Y'
    )
    cnt_penn = forms.BooleanField(
        label="Has Observed Pennatulids",
        required=False,
        help_text="Planning units that contain observed pennatulids",
        widget=CheckboxInput(
            attrs={'class': 'parameters hidden_checkbox'}
        )
    )
    cnt_penn_input = forms.ChoiceField(
        required=False,
        widget=forms.Select(
            attrs={'class': 'parameters'}
        ),
        choices=(
            ('Y', 'Include'),
            ('N', 'Exclude')),
        initial='Y'
    )

    # Depth Range (meters, avg: 0m - 212m)
    # Boolean field is the anchor, and used as the base name for rendering the form.
    # - Help_text on the boolean is included in the popup text "info" icon.
    # - Label is used as the icon label

    # depth = forms.BooleanField(label="Average Depth", required=False, help_text="Ocean depth in feet", widget=CheckboxInput(attrs={'class': 'parameters hidden_checkbox'}))
    # # depth_min = forms.FloatField(required=False, initial=10, widget=SliderWidget(attrs={'class':'slidervalue', 'pre_text': 'Distance in meters', 'post_text': 'meters'}, min=1, max=220, step=1))
    # depth_min = forms.FloatField(required=False, initial=10, widget=forms.TextInput(attrs={'class':'slidervalue', 'pre_text': 'Depth (in feet)'}))
    # depth_max = forms.FloatField(required=False, initial=50, widget=forms.TextInput(attrs={'class':'slidervalue', 'pre_text': 'to'}))
    # depth_input = forms.FloatField(widget=DualSliderWidget('depth_min', 'depth_max', min=1, max=220, step=1))

    # inlet_distance = forms.BooleanField(label="Distance from Coastal Inlet", required=False, help_text="Distance from nearest inlet in kilometers", widget=CheckboxInput(attrs={'class': 'parameters hidden_checkbox', 'layer_id': 339, 'layer_title': 'Show Inlets and Passes'}))
    # inlet_distance_min = forms.FloatField(required=False, initial=3, widget=SliderWidget(attrs={'class':'slidervalue', 'range': 'max', 'pre_text': 'Exclusion Buffer (in km)', 'post_text': 'km'}, min=0, max=16, step=.5))

    # injury_site = forms.BooleanField(label="Injury Sites", required=False, help_text="Whether a cell contains at least one recorded grounding or anchoring event in the DEP database", widget=CheckboxInput(attrs={'class': 'parameters hidden_checkbox', 'layer_id': '328', 'layer_title': 'Show Reef Injury Sites'}))
    # injury_site_input = forms.ChoiceField(required=False, widget=forms.Select(attrs={'class': 'parameters', 'layer_id': '918', 'layer_title': 'Reef Injury Site'}), choices=(('Y', 'Yes'), ('N', 'No')), initial='Y')

    # large_live_coral = forms.BooleanField(label="Large Live Corals", required=False, help_text="Whether a cell contains at least one known live coral greater than 2 meters in width", widget=CheckboxInput(attrs={'class': 'parameters hidden_checkbox'}))
    # large_live_coral_input = forms.ChoiceField(required=False, widget=forms.Select(attrs={'class': 'parameters'}), choices=(('Y', 'Yes'), ('N', 'No')), initial='Y')
    '''
    Species Habitat
    '''
    def get_step_0_fields(self):
        names = (
            ('species', None, None, 'species_input'),
            ('lifestage', None, None, 'lifestage_input')
        )

        return self._get_fields(names)


    '''
    Depth and Distances
    '''
    def get_step_1_fields(self):
        """Defines the fields that we want to show on the form in step 1, and
        the order in which they appear, and in groups of
            (parameter to test, user-min or user-selection, user-max, user-input)
        where each parameter except the first is optional.
        """
        names = [
            ('mean_fthm', 'mean_fthm_min', 'mean_fthm_max', 'mean_fthm_input')
        ]

        return self._get_fields(names)

    '''
    Some Presence/Absence Stuff
    '''
    def get_step_2_fields(self):
        names = (
            ('cnt_cs', None, None, 'cnt_cs_input'),
            ('cnt_penn', None, None, 'cnt_penn_input')
        )

        return self._get_fields(names)

    '''
    Other Habitats
    '''
    def get_step_3_fields(self):
        names = (
            ('sft_sub_m2', None, None, 'sft_sub_m2_input'),
            ('mix_sub_m2', None, None, 'mix_sub_m2_input'),
            ('hrd_sub_m2', None, None, 'hrd_sub_m2_input'),
            ('rck_sub_m2', None, None, 'rck_sub_m2_input')
        )

        return self._get_fields(names)

    '''
    More Fish and Coral
    '''
    def get_step_4_fields(self):
        names = (
            ('hsall_m2', None, None, None, 'hsall_m2_checkboxes'),
            ('hpc_est_m2', 'hpc_est_m2_min', None),
            ('hpc_klp_m2', 'hpc_klp_m2_min', None),
            ('hpc_rck_m2', 'hpc_rck_m2_min', None),
            ('hpc_sgr_m2', 'hpc_sgr_m2_min', None)
        )
        return self._get_fields(names)

    def get_steps(self):
        return self.get_step_0_fields(), self.get_step_1_fields(), self.get_step_2_fields(), self.get_step_3_fields(), self.get_step_4_fields()

    def _get_fields(self, names):

        fields = []
        for name_list in names:
            group = []
            for name in name_list:
                if name:
                    group.append(self[name])
                else:
                    group.append(None)
            fields.append(group)
        return fields

    def is_valid(self, *args, **kwargs):
        # validation fails because what the model expects, what the form expects, and how we manage these values do not match.
        if len(self.errors.keys()) == 1 and self.errors.keys()[0] == 'hsall_m2_checkboxes' and len(self.errors['hsall_m2_checkboxes']) == 1 and 'is not one of the available choices.' in self.errors['hsall_m2_checkboxes'][0]:
            del self._errors['hsall_m2_checkboxes']
        return super(FeatureForm, self).is_valid()

    def clean(self):

        super(FeatureForm, self).clean()
        try:
            if 'hsall_m2_checkboxes' not in self.cleaned_data.keys() and self.cleaned_data['hsall_m2'] == True:
                checkdata = self.data.getlist('hsall_m2_checkboxes')
                checklist = False
                for box in checkdata:
                    if not box == 'False':
                        checklist = True
                        self.cleaned_data['hsall_m2_checkboxes'] = unicode([unicode(x) for x in box.split(',')])

                if not checklist:
                    self.data.__delitem__('hsall_m2_checkboxes')
        except Exception as e:
            print(e)
            pass
        return self.cleaned_data

    def save(self, commit=True):
        inst = super(FeatureForm, self).save(commit=False)
        if self.data.get('clear_support_file'):
            inst.support_file = None
        if commit:
            inst.save()
        return inst

    class Meta(FeatureForm.Meta):
        model = Scenario
        exclude = list(FeatureForm.Meta.exclude)
        for f in model.output_fields():
            exclude.append(f.attname)

        widgets = {}
