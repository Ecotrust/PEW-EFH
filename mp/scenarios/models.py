# coding: utf-8

import os
import time
import json
from picklefield import PickledObjectField
from django.conf import settings
from django.contrib.gis.db import models
from django.utils.html import escape
from madrona.common.utils import asKml
from madrona.common.jsonutils import get_properties_json, get_feature_json
from madrona.features import register
from madrona.analysistools.models import Analysis
from general.utils import miles_to_meters, feet_to_meters, meters_to_feet, mph_to_mps, mps_to_mph, format_precision
from django.contrib.gis.geos import MultiPolygon
from django.contrib.gis.db.models.aggregates import Union
from django.forms.models import model_to_dict
from django.contrib.auth.models import User, Group
from django.dispatch import receiver
from django.db.models.signals import post_save

# Make sure all users are added to the public group
@receiver(post_save, sender=User, dispatch_uid='update_groups')
def userSaveCallback(sender, **kwargs):
    new_changes = False
    public_groups = Group.objects.filter(name="Share with Public")
    user = kwargs['instance']
    if len(public_groups) != 1:
        public_group = False
    else:
        public_group = public_groups[0]
    staff_groups = Group.objects.filter(name="Share with Staff")
    if len(staff_groups) != 1:
        staff_group = False
    else:
        staff_group = staff_groups[0]
    try:
        if public_group and not public_group in user.groups.all():
            user.groups.add(public_group)
            new_changes = True
        if user.is_staff and staff_group and not staff_group in user.groups.all():
            user.groups.add(staff_group)
            new_changes = True
    except ValueError:
        pass
    if new_changes:
        user.save()

@register
class Scenario(Analysis):

    species = models.BooleanField(default=None)
    species_input = models.CharField(max_length=255, blank=True, null=True)

    LIFESTAGE_CHOICES = (
        ('adults', 'Adults'),
        ('juveniles', 'Juveniles'),
        ('eggs', 'Eggs'),
        ('larvae', 'Larvae')
    )

    lifestage = models.BooleanField(default=None)
    lifestage_input = models.CharField(max_length=30, blank=True, null=True, choices=LIFESTAGE_CHOICES)

    min_fthm = models.BooleanField(default=None)
    # min_fthm_min = models.FloatField(null=True, blank=True)
    # min_fthm_max = models.FloatField(null=True, blank=True)
    # min_fthm_input = models.TextField(null=True, blank=True)

    mean_fthm = models.BooleanField(default=None)
    mean_fthm_min = models.FloatField(null=True, blank=True)
    mean_fthm_max = models.FloatField(null=True, blank=True)
    # mean_fthm_input = models.TextField(null=True, blank=True)

    max_fthm = models.BooleanField(default=None)
    # max_fthm_min = models.FloatField(null=True, blank=True)
    # max_fthm_max = models.FloatField(null=True, blank=True)
    # max_fthm_input = models.TextField(null=True, blank=True)

    min_meter = models.BooleanField(default=None)

    mean_meter = models.BooleanField(default=None)
    mean_meter_min = models.IntegerField(null=True, blank=True)
    mean_meter_max = models.IntegerField(null=True, blank=True)

    max_meter = models.BooleanField(default=None)

    sft_sub_m2 = models.BooleanField(default=None)
    # sft_sub_m2_min = models.FloatField(null=True, blank=True)
    # sft_sub_m2_max = models.FloatField(null=True, blank=True)
    sft_sub_m2_input = models.TextField(null=True, blank=True)

    mix_sub_m2 = models.BooleanField(default=None)
    # mix_sub_m2_min = models.FloatField(null=True, blank=True)
    # mix_sub_m2_max = models.FloatField(null=True, blank=True)
    mix_sub_m2_input = models.TextField(null=True, blank=True)

    hrd_sub_m2 = models.BooleanField(default=None)
    # hrd_sub_m2_min = models.FloatField(null=True, blank=True)
    # hrd_sub_m2_max = models.FloatField(null=True, blank=True)
    hrd_sub_m2_input = models.TextField(null=True, blank=True)

    rck_sub_m2 = models.BooleanField(default=None)
    # rck_sub_m2_min = models.FloatField(null=True, blank=True)
    # rck_sub_m2_max = models.FloatField(null=True, blank=True)
    rck_sub_m2_input = models.TextField(null=True, blank=True)

    cnt_cs = models.BooleanField(default=None)
    # cnt_cs_min = models.FloatField(null=True, blank=True)
    # cnt_cs_max = models.FloatField(null=True, blank=True)
    cnt_cs_input = models.TextField(null=True, blank=True)

    cnt_penn = models.BooleanField(default=None)
    # cnt_penn_min = models.FloatField(null=True, blank=True)
    # cnt_penn_max = models.FloatField(null=True, blank=True)
    cnt_penn_input = models.TextField(null=True, blank=True)

    ra_cs = models.BooleanField(default=None)
    # ra_cs_min = models.FloatField(null=True, blank=True)
    # ra_cs_max = models.FloatField(null=True, blank=True)
    # ra_cs_input = models.TextField(null=True, blank=True)

    cs_obs = models.BooleanField(default=None)
    cs_obs_input = models.TextField(null=True, blank=True)

    cs_spm = models.BooleanField(default=None)
    cs_spm_input = models.TextField(null=True, blank=True)

    cs3500_obs = models.BooleanField(default=None)
    cs3500_obs_input = models.TextField(null=True, blank=True)

    cs3500_spm = models.BooleanField(default=None)
    cs3500_spm_input = models.TextField(null=True, blank=True)

    ra_penn = models.BooleanField(default=None)
    # ra_penn_min = models.FloatField(null=True, blank=True)
    # ra_penn_max = models.FloatField(null=True, blank=True)
    # ra_penn_input = models.TextField(null=True, blank=True)

    hsalcy1_m2 = models.BooleanField(default=None)
    # hsalcy1_m2_min = models.FloatField(null=True, blank=True)
    # hsalcy1_m2_max = models.FloatField(null=True, blank=True)
    # hsalcy1_m2_input = models.TextField(null=True, blank=True)

    hsalcy2_m2 = models.BooleanField(default=None)
    # hsalcy2_m2_min = models.FloatField(null=True, blank=True)
    # hsalcy2_m2_max = models.FloatField(null=True, blank=True)
    # hsalcy2_m2_input = models.TextField(null=True, blank=True)

    hsalcy3_m2 = models.BooleanField(default=None)
    # hsalcy3_m2_min = models.FloatField(null=True, blank=True)
    # hsalcy3_m2_max = models.FloatField(null=True, blank=True)
    # hsalcy3_m2_input = models.TextField(null=True, blank=True)

    hsalcy4_m2 = models.BooleanField(default=None)
    # hsalcy4_m2_min = models.FloatField(null=True, blank=True)
    # hsalcy4_m2_max = models.FloatField(null=True, blank=True)
    # hsalcy4_m2_input = models.TextField(null=True, blank=True)

    hsall_m2 = models.BooleanField(default=False)
    hsall_m2_min = models.FloatField(null=True, blank=True)
    hsall_m2_checkboxes = models.TextField(null=True, blank=True, default=None)

    hsall1_m2 = models.BooleanField(default=None)
    hsall1_m2_min = models.FloatField(null=True, blank=True)
    hsall1_m2_max = models.FloatField(null=True, blank=True)
    # hsall1_m2_input = models.TextField(null=True, blank=True)

    hsall2_m2 = models.BooleanField(default=None)
    hsall2_m2_min = models.FloatField(null=True, blank=True)
    hsall2_m2_max = models.FloatField(null=True, blank=True)
    # hsall2_m2_input = models.TextField(null=True, blank=True)

    hsall3_m2 = models.BooleanField(default=None)
    hsall3_m2_min = models.FloatField(null=True, blank=True)
    hsall3_m2_max = models.FloatField(null=True, blank=True)
    # hsall3_m2_input = models.TextField(null=True, blank=True)

    hsall4_m2 = models.BooleanField(default=None)
    hsall4_m2_min = models.FloatField(null=True, blank=True)
    hsall4_m2_max = models.FloatField(null=True, blank=True)
    # hsall4_m2_input = models.TextField(null=True, blank=True)

    hsanti1_m2 = models.BooleanField(default=None)
    # hsanti1_m2_min = models.FloatField(null=True, blank=True)
    # hsanti1_m2_max = models.FloatField(null=True, blank=True)
    # hsanti1_m2_input = models.TextField(null=True, blank=True)

    hsanti2_m2 = models.BooleanField(default=None)
    # hsanti2_m2_min = models.FloatField(null=True, blank=True)
    # hsanti2_m2_max = models.FloatField(null=True, blank=True)
    # hsanti2_m2_input = models.TextField(null=True, blank=True)

    hsanti3_m2 = models.BooleanField(default=None)
    # hsanti3_m2_min = models.FloatField(null=True, blank=True)
    # hsanti3_m2_max = models.FloatField(null=True, blank=True)
    # hsanti3_m2_input = models.TextField(null=True, blank=True)

    hsanti4_m2 = models.BooleanField(default=None)

    hscalc1_m2 = models.BooleanField(default=None)
    # hscalc1_m2_min = models.FloatField(null=True, blank=True)
    # hscalc1_m2_max = models.FloatField(null=True, blank=True)
    # hscalc1_m2_input = models.TextField(null=True, blank=True)

    hscalc2_m2 = models.BooleanField(default=None)
    # hscalc2_m2_min = models.FloatField(null=True, blank=True)
    # hscalc2_m2_max = models.FloatField(null=True, blank=True)
    # hscalc2_m2_input = models.TextField(null=True, blank=True)

    hscalc3_m2 = models.BooleanField(default=None)
    # hscalc3_m2_min = models.FloatField(null=True, blank=True)
    # hscalc3_m2_max = models.FloatField(null=True, blank=True)
    # hscalc3_m2_input = models.TextField(null=True, blank=True)

    hscalc4_m2 = models.BooleanField(default=None)
    # hscalc4_m2_min = models.FloatField(null=True, blank=True)
    # hscalc4_m2_max = models.FloatField(null=True, blank=True)
    # hscalc4_m2_input = models.TextField(null=True, blank=True)

    hshola1_m2 = models.BooleanField(default=None)
    # hshola1_m2_min = models.FloatField(null=True, blank=True)
    # hshola1_m2_max = models.FloatField(null=True, blank=True)
    # hshola1_m2_input = models.TextField(null=True, blank=True)

    hshola2_m2 = models.BooleanField(default=None)
    # hshola2_m2_min = models.FloatField(null=True, blank=True)
    # hshola2_m2_max = models.FloatField(null=True, blank=True)
    # hshola2_m2_input = models.TextField(null=True, blank=True)

    hshola3_m2 = models.BooleanField(default=None)
    # hshola3_m2_min = models.FloatField(null=True, blank=True)
    # hshola3_m2_max = models.FloatField(null=True, blank=True)
    # hshola3_m2_input = models.TextField(null=True, blank=True)

    hshola4_m2 = models.BooleanField(default=None)
    # hshola4_m2_min = models.FloatField(null=True, blank=True)
    # hshola4_m2_max = models.FloatField(null=True, blank=True)
    # hshola4_m2_input = models.TextField(null=True, blank=True)

    hssclr1_m2 = models.BooleanField(default=None)
    # hssclr1_m2_min = models.FloatField(null=True, blank=True)
    # hssclr1_m2_max = models.FloatField(null=True, blank=True)
    # hssclr1_m2_input = models.TextField(null=True, blank=True)

    hssclr2_m2 = models.BooleanField(default=None)
    # hssclr2_m2_min = models.FloatField(null=True, blank=True)
    # hssclr2_m2_max = models.FloatField(null=True, blank=True)
    # hssclr2_m2_input = models.TextField(null=True, blank=True)

    hssclr3_m2 = models.BooleanField(default=None)
    # hssclr3_m2_min = models.FloatField(null=True, blank=True)
    # hssclr3_m2_max = models.FloatField(null=True, blank=True)
    # hssclr3_m2_input = models.TextField(null=True, blank=True)

    hssclr4_m2 = models.BooleanField(default=None)

    hssclx1_m2 = models.BooleanField(default=None)
    # hssclx1_m2_min = models.FloatField(null=True, blank=True)
    # hssclx1_m2_max = models.FloatField(null=True, blank=True)
    # hssclx1_m2_input = models.TextField(null=True, blank=True)

    hssclx2_m2 = models.BooleanField(default=None)
    # hssclx2_m2_min = models.FloatField(null=True, blank=True)
    # hssclx2_m2_max = models.FloatField(null=True, blank=True)
    # hssclx2_m2_input = models.TextField(null=True, blank=True)

    hssclx3_m2 = models.BooleanField(default=None)
    # hssclx3_m2_min = models.FloatField(null=True, blank=True)
    # hssclx3_m2_max = models.FloatField(null=True, blank=True)
    # hssclx3_m2_input = models.TextField(null=True, blank=True)

    hssclx4_m2 = models.BooleanField(default=None)
    # hssclx4_m2_min = models.FloatField(null=True, blank=True)
    # hssclx4_m2_max = models.FloatField(null=True, blank=True)
    # hssclx4_m2_input = models.TextField(null=True, blank=True)

    hpc_est_m2 = models.BooleanField(default=None)
    hpc_est_m2_min = models.FloatField(null=True, blank=True)
    hpc_est_m2_max = models.FloatField(null=True, blank=True)
    # hpc_est_m2_input = models.TextField(null=True, blank=True)

    hpc_klp_m2 = models.BooleanField(default=None)
    hpc_klp_m2_min = models.FloatField(null=True, blank=True)
    hpc_klp_m2_max = models.FloatField(null=True, blank=True)
    # hpc_klp_m2_input = models.TextField(null=True, blank=True)

    hpc_rck_m2 = models.BooleanField(default=None)
    hpc_rck_m2_min = models.FloatField(null=True, blank=True)
    hpc_rck_m2_max = models.FloatField(null=True, blank=True)
    # hpc_rck_m2_input = models.TextField(null=True, blank=True)

    hpc_sgr_m2 = models.BooleanField(default=None)
    hpc_sgr_m2_min = models.FloatField(null=True, blank=True)
    hpc_sgr_m2_max = models.FloatField(null=True, blank=True)
    # hpc_sgr_m2_input = models.TextField(null=True, blank=True)

    description = models.TextField(null=True, blank=True)
    satisfied = models.BooleanField(default=True, help_text="Am I satisfied?")
    active = models.BooleanField(default=True)

    grid_cells = models.TextField(verbose_name='Grid Cell IDs', null=True, blank=True)
    geometry_final_area = models.FloatField(verbose_name='Total Area', null=True, blank=True)
    geometry_dissolved = models.MultiPolygonField(srid=settings.GEOMETRY_DB_SRID, null=True, blank=True, verbose_name="Filter result dissolved")

    # format attribute JSON and handle None values
    def get_min_max_attributes(self, title, min_val, max_val, units):

        if isinstance(min_val, (int, long)):
            min_val_str = str(int(min_val))
        else:
            min_val_str = str(min_val)

        if isinstance(max_val, (int, long)):
            max_val_str = str(int(max_val))
        else:
            max_val_str = str(max_val)

        attribute = {
            'title': title,
            'data':  min_val_str + ' to ' + max_val_str + ' ' + units
        }
        return attribute

    # format attribute JSON and handle None values
    def get_min_attributes(self, title, min_val, units):

        if isinstance(min_val, (int, long)):
            min_val_str = str(int(min_val))
        else:
            min_val_str = str(min_val)

        attribute = {
            'title': title,
            'data':  'At least ' + min_val_str + ' ' + units
        }
        return attribute

    @property
    def serialize_attributes(self):
        """
        Return attributes in text format. Used to display information on click in the planner.
        """
        attributes = []

        #generic
        if self.description:
            attributes.append({
                'title': 'Description',
                'data': self.description
            })

        # Step 1
        if self.species:
            if self.lifestage:
                if self.species_input is not None and self.lifestage_input is not None:
                    title = '%s %ss present' % (self.species_input.capitalize(), self.lifestage_input.capitalize())
                    attributes.append({
                        'title': title,
                        'data':  ''
                    })
            elif self.species_input is not None:
                title = '%s present' % self.species_input.capitalize()
                attributes.append({
                    'title': title,
                    'data':  ''
                })

        if self.mean_fthm:
            attributes.append(
                self.get_min_max_attributes(
                    'Depth Range',
                    self.mean_fthm_min,
                    self.mean_fthm_max,
                    'fathoms'
                )
            )
        if self.hsall_m2 and self.hsall_m2_checkboxes:
            attributes.append({
                'title': 'Predicted Presence of Deep Sea Coral Habitat Classes',
                'data': ', '.join(eval(self.hsall_m2_checkboxes))
            })
        if self.hsall1_m2:
            attributes.append(
                self.get_min_attributes(
                    'Predicted Class 1 Deep Sea Coral Habitat',
                    float(format_precision(self.hsall1_m2_min / 2590000.0, 2)),
                    'mi<sup>2</sup>'
                )
            )
            # float(format_precision(self.hsall1_m2_min / 1000000, 2)),
            # 'km<sup>2</sup>'
        if self.hsall2_m2:
            attributes.append(
                self.get_min_attributes(
                    'Predicted Class 2 Deep Sea Coral Habitat',
                    float(format_precision(self.hsall2_m2_min / 2590000.0, 2)),
                    'mi<sup>2</sup>'
                )
            )
        if self.hsall3_m2:
            attributes.append(
                self.get_min_attributes(
                    'Predicted Class 3 Deep Sea Coral Habitat',
                    float(format_precision(self.hsall3_m2_min / 2590000.0, 2)),
                    'mi<sup>2</sup>'
                )
            )
        if self.hsall4_m2:
            attributes.append(
                self.get_min_attributes(
                    'Predicted Class 4 Deep Sea Coral Habitat',
                    float(format_precision(self.hsall4_m2_min / 2590000.0, 2)),
                    'mi<sup>2</sup>'
                )
            )

        # NOTE: The following 4 'm2' fields actually have sq miles for units,
            # not sq meters. This is just easier since it's what the user inputs
            # so we don't need to run a separate filter or convert user input
            # before the filter.

        if self.hpc_est_m2:
            attributes.append(
                self.get_min_attributes(
                    'Estuary Habitat',
                    self.hpc_est_m2_min,
                    'mi<sup>2</sup>'
                )
            )
        if self.hpc_klp_m2:
            attributes.append(
                self.get_min_attributes(
                    'Kelp Habitat',
                    self.hpc_klp_m2_min,
                    'mi<sup>2</sup>'
                )
            )
        if self.hpc_rck_m2:
            attributes.append(
                self.get_min_attributes(
                    'Rocky Reef Habitat',
                    self.hpc_rck_m2_min,
                    'mi<sup>2</sup>'
                )
            )
        if self.hpc_sgr_m2:
            attributes.append(
                self.get_min_attributes(
                    'Seagrass Habitat',
                    self.hpc_sgr_m2_min,
                    'mi<sup>2</sup>'
                )
            )

        # Step 2
        if self.sft_sub_m2:
            if self.sft_sub_m2_input == 'Y':
                title = 'Contains soft substrate'
            else:
                title = 'Does not contain any soft substrate'
            attributes.append({
                'title': title,
                'data':  ''
            })
        if self.mix_sub_m2:
            if self.mix_sub_m2_input == 'Y':
                title = 'Contains mixed substrate'
            else:
                title = 'Does not contain any mixed substrate'
            attributes.append({
                'title': title,
                'data':  ''
            })
        if self.hrd_sub_m2:
            if self.hrd_sub_m2_input == 'Y':
                title = 'Contains hard substrate'
            else:
                title = 'Does not contain any hard substrate'
            attributes.append({
                'title': title,
                'data':  ''
            })
        if self.rck_sub_m2:
            if self.rck_sub_m2_input == 'Y':
                title = 'Contains inferred rock substrate'
            else:
                title = 'Does not contain any inferred rock substrate'
            attributes.append({
                'title': title,
                'data':  ''
            })
        if self.cnt_cs:
            if self.cnt_cs_input == 'Y':
                title = 'Contains coral and/or sponges'
            else:
                title = 'Not known to contain coral or sponges'
            attributes.append({
                'title': title,
                'data':  ''
            })
        if self.cnt_penn:
            if self.cnt_penn_input == 'Y':
                title = 'Contains pennatulids (sea pen/sea whip)'
            else:
                title = 'Not known to contain pennatulids'
            attributes.append({
                'title': title,
                'data':  ''
            })
        # if self.cs_obs:
        #     if self.cs_obs_input == 'Y':
        #         title = 'Contains observed corals and/or sponges'
        #     else:
        #         title = 'No corals and/or sponges observed'
        #     attributes.append({
        #         'title': title,
        #         'data':  ''
        #     })

        attributes.append({'title': 'Number of Grid Cells',
                           'data': '{:,}'.format(self.grid_cells.count(',')+1)})
        return { 'event': 'click', 'attributes': attributes }


    def geojson(self, srid):
        props = get_properties_json(self)
        props['absolute_url'] = self.get_absolute_url()
        json_geom = self.geometry_dissolved.transform(srid, clone=True).json
        return get_feature_json(json_geom, json.dumps(props))


    def run(self):
        # placing this import here to avoid circular dependency with views.py
        from views import run_filter_query
        (query, notes) = run_filter_query(model_to_dict(self))

        if len(query) == 0:
            self.satisfied = False;
            # raise Exception("No lease blocks available with the current filters.")

        dissolved_geom = query.aggregate(Union('geometry'))
        if dissolved_geom['geometry__union']:
            dissolved_geom = dissolved_geom['geometry__union']
        else:
            raise Exception("No lease blocks available with the current filters.")

        if type(dissolved_geom) == MultiPolygon:
            self.geometry_dissolved = dissolved_geom
        else:
            self.geometry_dissolved = MultiPolygon(dissolved_geom, srid=dissolved_geom.srid)

        self.active = True # ??

        # import datetime
        # start=datetime.datetime.now()

        self.geometry_final_area = self.geometry_dissolved.area

        self.grid_cells = ','.join(str(i)
                                     for i in query.values_list('id', flat=True))

        # print("Elapsed:", datetime.datetime.now() - start)

        if self.grid_cells == '':
            self.satisfied = False
        else:
            self.satisfied = True
        return True

    def save(self, rerun=None, *args, **kwargs):
        if rerun is None and self.pk is None:
            rerun = True
        if rerun is None and self.pk is not None: #if editing a scenario and no value for rerun is given
            rerun = False
            if not rerun:
                orig = Scenario.objects.get(pk=self.pk)
                #TODO: keeping this in here til I figure out why self.grid_cells and self.geometry_final_area are emptied when run() is not called
                rerun = True
                if not rerun:
                    for f in Scenario.input_fields():
                        # Is original value different from form value?
                        if getattr(orig, f.name) != getattr(self, f.name):
                            #print 'input_field, %s, has changed' %f.name
                            rerun = True
                            break
                if not rerun:
                    '''
                        the substrates need to be grabbed, then saved, then grabbed again because
                        both getattr calls (orig and self) return the same original list until the model has been saved
                        (perhaps because form.save_m2m has to be called), after which calls to getattr will
                        return the same list (regardless of whether we use orig or self)
                    '''
                    orig_weas = set(getattr(self, 'input_wea').all())
                    orig_substrates = set(getattr(self, 'input_substrate').all())
                    orig_sediments = set(getattr(self, 'input_sediment').all())
                    super(Scenario, self).save(rerun=False, *args, **kwargs)
                    new_weas = set(getattr(self, 'input_wea').all())
                    new_substrates = set(getattr(self, 'input_substrate').all())
                    new_sediments = set(getattr(self, 'input_sediment').all())
                    if orig_substrates != new_substrates or orig_sediments != new_sediments or orig_weas != new_weas:
                        rerun = True
            super(Scenario, self).save(rerun=rerun, *args, **kwargs)
        else: #editing a scenario and rerun is provided
            super(Scenario, self).save(rerun=rerun, *args, **kwargs)

    def __unicode__(self):
        return u'%s' % self.name

    def support_filename(self):
        return os.path.basename(self.support_file.name)

    @classmethod
    def mapnik_geomfield(self):
        return "output_geom"

    @classmethod
    def mapnik_style(self):
        import mapnik
        polygon_style = mapnik.Style()

        ps = mapnik.PolygonSymbolizer(mapnik.Color('#ffffff'))
        ps.fill_opacity = 0.5

        ls = mapnik.LineSymbolizer(mapnik.Color('#555555'),0.75)
        ls.stroke_opacity = 0.5

        r = mapnik.Rule()
        r.symbols.append(ps)
        r.symbols.append(ls)
        polygon_style.rules.append(r)
        return polygon_style

    @classmethod
    def input_parameter_fields(klass):
        return [f for f in klass._meta.fields if f.attname.startswith('input_parameter_')]

    @classmethod
    def input_filter_fields(klass):
        return [f for f in klass._meta.fields if f.attname.startswith('input_filter_')]

    @property
    def grid_cells_set(self):
        if len(self.grid_cells) == 0:  #empty result
            gridcell_ids = []
        else:
            gridcell_ids = [int(id) for id in self.grid_cells.split(',')]
        gridcells = GridCell.objects.filter(pk__in=gridcell_ids)
        return gridcells

    @property
    def num_lease_blocks(self):
        if self.grid_cells == '':
            return 0
        return len(self.grid_cells.split(','))

    @property
    def geometry_is_empty(self):
        return len(self.grid_cells) == 0

    @property
    def input_wea_names(self):
        return [wea.wea_name for wea in self.input_wea.all()]

    @property
    def input_substrate_names(self):
        return [substrate.substrate_name for substrate in self.input_substrate.all()]

    @property
    def input_sediment_names(self):
        return [sediment.sediment_name for sediment in self.input_sediment.all()]

    #TODO: is this being used...?  Yes, see show.html
    @property
    def has_wind_energy_criteria(self):
        wind_parameters = Scenario.input_parameter_fields()
        for wp in wind_parameters:
            if getattr(self, wp.name):
                return True
        return False

    @property
    def has_shipping_filters(self):
        shipping_filters = Scenario.input_filter_fields()
        for sf in shipping_filters:
            if getattr(self, sf.name):
                return True
        return False

    @property
    def has_military_filters(self):
        return False

    @property
    def color(self):
        try:
            return Objective.objects.get(pk=self.input_objectives.values_list()[0][0]).color
        except:
            return '778B1A55'

    @property
    def get_id(self):
        return self.id

    class Options:
        verbose_name = 'Spatial Design for Wind Energy'
        icon_url = 'marco/img/multi.png'
        form = 'scenarios.forms.ScenarioForm'
        form_template = 'scenario/form.html'
        show_template = 'scenario/show.html'

#no longer needed?
# class Objective(models.Model):
#     name = models.CharField(max_length=35)
#     color = models.CharField(max_length=8, default='778B1A55')

#     def __unicode__(self):
#         return u'%s' % self.name

#no longer needed?
# class Parameter(models.Model):
#     ordering_id = models.IntegerField(null=True, blank=True)
#     name = models.CharField(max_length=35, null=True, blank=True)
#     shortname = models.CharField(max_length=35, null=True, blank=True)
#     objectives = models.ManyToManyField("Objective", null=True, blank=True)

#     def __unicode__(self):
#         return u'%s' % self.name


class GridCell(models.Model):

    min_fthm = models.IntegerField(null=True, blank=True)
    mean_fthm = models.IntegerField(null=True, blank=True)
    max_fthm = models.IntegerField(null=True, blank=True)
    min_meter = models.IntegerField(null=True, blank=True)
    mean_meter = models.IntegerField(null=True, blank=True)
    max_meter = models.IntegerField(null=True, blank=True)
    sft_sub_m2 = models.IntegerField(null=True, blank=True)
    mix_sub_m2 = models.IntegerField(null=True, blank=True)
    hrd_sub_m2 = models.IntegerField(null=True, blank=True)
    rck_sub_m2 = models.IntegerField(null=True, blank=True)
    cnt_cs = models.IntegerField(null=True, blank=True)
    cnt_penn = models.IntegerField(null=True, blank=True)
    ra_cs = models.IntegerField(null=True, blank=True)
    ra_penn = models.IntegerField(null=True, blank=True)
    hsalcy1_m2 = models.IntegerField(null=True, blank=True)
    hsalcy2_m2 = models.IntegerField(null=True, blank=True)
    hsalcy3_m2 = models.IntegerField(null=True, blank=True)
    hsalcy4_m2 = models.IntegerField(null=True, blank=True)
    hsall1_m2 = models.IntegerField(null=True, blank=True)
    hsall2_m2 = models.IntegerField(null=True, blank=True)
    hsall3_m2 = models.IntegerField(null=True, blank=True)
    hsall4_m2 = models.IntegerField(null=True, blank=True)
    hsanti1_m2 = models.IntegerField(null=True, blank=True)
    hsanti2_m2 = models.IntegerField(null=True, blank=True)
    hsanti3_m2 = models.IntegerField(null=True, blank=True)
    hsanti4_m2 = models.IntegerField(null=True, blank=True)
    hscalc1_m2 = models.IntegerField(null=True, blank=True)
    hscalc2_m2 = models.IntegerField(null=True, blank=True)
    hscalc3_m2 = models.IntegerField(null=True, blank=True)
    hscalc4_m2 = models.IntegerField(null=True, blank=True)
    hshola1_m2 = models.IntegerField(null=True, blank=True)
    hshola2_m2 = models.IntegerField(null=True, blank=True)
    hshola3_m2 = models.IntegerField(null=True, blank=True)
    hshola4_m2 = models.IntegerField(null=True, blank=True)
    hssclr1_m2 = models.IntegerField(null=True, blank=True)
    hssclr2_m2 = models.IntegerField(null=True, blank=True)
    hssclr3_m2 = models.IntegerField(null=True, blank=True)
    hssclr4_m2 = models.IntegerField(null=True, blank=True)
    hssclx1_m2 = models.IntegerField(null=True, blank=True)
    hssclx2_m2 = models.IntegerField(null=True, blank=True)
    hssclx3_m2 = models.IntegerField(null=True, blank=True)
    hssclx4_m2 = models.IntegerField(null=True, blank=True)
    hpc_est_m2 = models.IntegerField(null=True, blank=True)
    hpc_klp_m2 = models.IntegerField(null=True, blank=True)
    hpc_rck_m2 = models.IntegerField(null=True, blank=True)
    hpc_sgr_m2 = models.IntegerField(null=True, blank=True)
    cs_obs = models.IntegerField(null=True, blank=True)
    cs_spm = models.IntegerField(null=True, blank=True)
    cs3500_obs = models.IntegerField(null=True, blank=True)
    cs3500_spm = models.IntegerField(null=True, blank=True)

    unique_id = models.IntegerField(null=True, blank=True)

    centroid = models.PointField(
        srid=settings.GEOMETRY_DB_SRID,
        null=True,
        blank=True
    )

    geometry = models.MultiPolygonField(
        srid=settings.GEOMETRY_DB_SRID,
        null=True, blank=True,
        verbose_name="Grid Cell Geometry"
    )
    objects = models.GeoManager()


class SpeciesHabitatOccurence(models.Model):
    LIFESTAGE_CHOICES = (
        ('adults', 'Adults'),
        ('juveniles', 'Juveniles'),
        ('eggs', 'Eggs'),
        ('larvae', 'Larvae')
    )
    SEX_CHOICES = (
        ('Both', 'Both'),
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Unknown', 'Unknown')
    )
    ASSOCIATION_CHOICES = (
        ('Strong', 'Strong'),
        ('Medium', 'Medium'),
        ('Weak', 'Weak'),
        ('Unknown', 'Unknown'),
        ('null', None)
    )
    SEASON_CHOICES = (
        ('Unknown', 'Unknown'),
        ('All Year', 'All Year'),
        ('Winter', 'Winter'),
        ('Spring', 'Spring'),
        ('Summer', 'Summer'),
        ('Autumn', 'Autumn')
    )
    LEVEL_1_HABITAT_CHOICES = (
        ('Estuarine', 'Estuarine'),
        ('Nearshore', 'Nearshore'),
        ('Shelf', 'Shelf'),
        ('Slope/Rise', 'Slope/Rise')
    )
    LEVEL_2_HABITAT_CHOICES = (
        ('Benthos', 'Benthos'),
        ('Unknown', 'Unknown'),
        ('Submarine Canyon', 'Submarine Canyon'),
        ('Intertidal Benthos', 'Intertidal Benthos'),
        ('Basin', 'Basin')
    )
    LEVEL_3_HABITAT_CHOICES = (
        ('Hard Bottom', 'Hard Bottom'),
        ('Unconsolidated', 'Unconsolidated'),
        ('Mixed Bottom', 'Mixed Bottom'),
        ('Unknown', 'Unknown'),
        ('Vegetated Bottom', 'Vegetated Bottom')
    )
    LEVEL_4_HABITAT_CHOICES = (
        ('Algal Beds/Macro', 'Algal Beds/Macro'),
        ('Bedrock', 'Bedrock'),
        ('Cobble', 'Cobble'),
        ('Gravel', 'Gravel'),
        ('Gravel/Cobble', 'Gravel/Cobble'),
        ('Mixed mud/sand', 'Mixed mud/sand'),
        ('Mud', 'Mud'),
        ('Mud/Boulders', 'Mud/Boulders'),
        ('Mud/Cobble', 'Mud/Cobble'),
        ('Mud/gravel', 'Mud/gravel'),
        ('Mud/Rock', 'Mud/Rock'),
        ('Rooted Vascular', 'Rooted Vascular'),
        ('Sand', 'Sand'),
        ('Sand/Boulders', 'Sand/Boulders'),
        ('Sand/Rock', 'Sand/Rock'),
        ('Silt', 'Silt'),
        ('Soft Bottom/Boulder', 'Soft Bottom/Boulder'),
        ('Soft Bottom/rock', 'Soft Bottom/rock'),
        ('Unknown', 'Unknown')
    )
    ACTIVITY_CHOICES = (
        ('All', 'All'),
        ('Feeding', 'Feeding'),
        ('Growth to Maturity', 'Growth to Maturity'),
        ('Unknown', 'Unknown')
    )
    object_id = models.IntegerField(primary_key=True)
    species_common = models.CharField(max_length=255, blank=False, null=False)
    species_sci = models.CharField(max_length=255, blank=False, null=False)
    lifestage = models.CharField(max_length=30, blank=False, null=False, choices=LIFESTAGE_CHOICES)
    sex = models.CharField(max_length=50, blank=False, null=False, choices=SEX_CHOICES)
    habitat_association = models.CharField(max_length=30, null=True, choices=ASSOCIATION_CHOICES)
    season = models.CharField(max_length=20, blank=False, null=False, choices=SEASON_CHOICES)
    level_1_habitat = models.CharField(max_length=30, blank=False, null=False, choices=LEVEL_1_HABITAT_CHOICES)
    level_2_habitat = models.CharField(max_length=30, blank=False, null=False, choices=LEVEL_2_HABITAT_CHOICES)
    level_3_habitat = models.CharField(max_length=30, blank=False, null=False, choices=LEVEL_3_HABITAT_CHOICES)
    level_4_habitat = models.CharField(max_length=30, blank=False, null=False, choices=LEVEL_4_HABITAT_CHOICES)
    xwalk_sgh = models.CharField(max_length=10, blank=False, null=False)
    sgh_lookup_code = models.CharField(max_length=30, blank=False, null=False)
    activity = models.CharField(max_length=30, blank=False, null=False, choices=ACTIVITY_CHOICES)
    activity_association = models.CharField(max_length=30, null=True, choices=ASSOCIATION_CHOICES)
    preferred_min_depth = models.IntegerField(blank=True, null=True, default=None)
    preferred_max_depth = models.IntegerField(blank=True, null=True, default=None)
    absolute_min_depth = models.IntegerField(blank=True, null=True, default=None)
    absolute_max_depth = models.IntegerField(blank=True, null=True, default=None)


class PlanningUnitHabitatLookup(models.Model):
    sgh_lookup_code = models.CharField(primary_key=True, max_length=30, blank=False, null=False)
    pug_ids = models.TextField(blank=False, null=False, default="[]", help_text="string list of Planning Unit Grid IDs")


class Species(models.Model):
    common_name = models.CharField(max_length=255, blank=False, null=False)
    scientific_name = models.CharField(max_length=255, blank=False, null=False)
