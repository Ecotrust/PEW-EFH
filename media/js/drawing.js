
function drawingModel(options) {
    var self = this;

    var ret = scenarioModel.apply(this, arguments);

    //self.isSelectionModel = true;

    //self.pointControl = new OpenLayers.Control.DrawFeature(pointLayer, OpenLayers.Handler.Point);
    //self.lineControl = new OpenLayers.Control.DrawFeature(lineLayer, OpenLayers.Handler.Path);

    //will need to distinguish between drawing types...
    self.editDrawing = function() {
        self.drawing = this;
        if ( ! self.drawing.active() ) {
            self.drawing.activateLayer();
        }
        //app.viewModel.scenarios.drawingFormModel.polygonLayer.addFeatures([new OpenLayers.Feature.Vector(new OpenLayers.Geometry.fromWKT($('#id_geometry_orig')[0].value))]);
        //app.viewModel.scenarios.drawingFormModel.polygonLayer.addFeatures([new OpenLayers.Format.WKT().read($('#id_geometry_orig')[0].value)]);

        //app.setLayerVisibility(drawing, false);
        return $.ajax({
            url: '/features/aoi/' + self.drawing.uid + '/form/',
            success: function(data) {
                app.viewModel.scenarios.drawingForm(true);
                app.viewModel.scenarios.drawingFormModel = new polygonFormModel();
                //app.viewModel.scenarios.drawingFormModel.replacePolygonLayer(self.drawing.layer);
                var oldLayer = app.viewModel.scenarios.drawingFormModel.polygonLayer;

                app.viewModel.scenarios.drawingFormModel.originalDrawing = self.drawing;
                app.viewModel.scenarios.drawingFormModel.polygonLayer = self.drawing.layer;

                if (self.geometry_orig) {
                    app.viewModel.scenarios.drawingFormModel.polygonLayer.removeAllFeatures();
                    app.viewModel.scenarios.drawingFormModel.polygonLayer.addFeatures(self.geometry_orig);
                }

                app.map.zoomToExtent(self.drawing.layer.getDataExtent());
                app.map.zoomOut();

                $('#'+app.viewModel.currentTocId()+'-drawing-form > .drawing-form').html(data);
                ko.applyBindings(app.viewModel.scenarios.drawingFormModel, document.getElementById(app.viewModel.currentTocId()+'-drawing-form').children[0]);

                app.viewModel.scenarios.drawingFormModel.showEdit(true);
                app.viewModel.scenarios.drawingFormModel.hasShape(true);
                app.viewModel.scenarios.drawingFormModel.startEdit();
                app.onResize();
            },
            error: function (result) {
                console.log('error in drawing.js: editDrawing');
            }
        });
    };

    self.createCopyDrawing = function() {
        var drawing = this;

        //create a copy of this shape to be owned by the user
        $.ajax({
            url: '/scenario/copy_design/' + drawing.uid + '/',
            type: 'POST',
            dataType: 'json',
            success: function(data) {
                //app.viewModel.scenarios.loadSelectionsFromServer();
                app.viewModel.scenarios.addScenarioToMap(null, {uid: data[0].uid});
            },
            error: function (result) {
                console.log('error in drawing.js: createCopyDrawing');
            }
        });
    };

    self.selectScenarioForAdd = function () {
      var drawing = this;
      //TODO: Trigger scenario selection modal

    }

    self.addToScenario = function() {
      var drawing = this;
      //TODO: Trigger this after a scenario is selected from the modal opened by selectScenarioForAdd
      // * post drawing and collection to server to copy and associate.
    }

    self.deleteDrawing = function() {
        var drawing = this;

        //remove from activeLayers
        app.viewModel.activeLayers.remove(drawing);
        //remove from app.map
        if (drawing.layer) {
            app.map.removeLayer(drawing.layer);
        }
        //remove from selectionList
        app.viewModel.scenarios.drawingList.remove(drawing);
        //update scrollbar
        app.viewModel.scenarios.updateDesignsScrollBar();

        //remove from server-side db (this should provide error message to the user on fail)
        $.ajax({
            url: '/drawing/delete_design/' + drawing.uid + '/',
            type: 'POST',
            success: function (result) {
                app.viewModel.scenarios.loadScenariosFromServer();
                app.viewModel.scenarios.loadCollectionsFromServer();
            },
            error: function (result) {
                console.log('error in drawing.js: deleteDrawing');
            }
        });
    };

}

function polygonFormModel(options) {
    var self = this;

    self.newPolygonLayerName = "New Polygon Design 23";

    self.isDrawing = ko.observable(false);
    self.showEdit = ko.observable(false);
    self.isEditing = ko.observable(false);
    self.hasShape = ko.observable(false);
    self.clipAttemptFailed = ko.observable(false);

    self.polygonLayer = new OpenLayers.Layer.Vector(self.newPolygonLayerName);
    app.map.addLayer(self.polygonLayer);

    self.polygonControl = new OpenLayers.Control.DrawFeature(self.polygonLayer, OpenLayers.Handler.Polygon);
    app.map.addControl(self.polygonControl);

    self.editControl = new OpenLayers.Control.ModifyFeature(self.polygonLayer);
    app.map.addControl(self.editControl);

    self.planningGridLayer = app.viewModel.getLayerById(434);
    if (self.planningGridLayer.active()) {
        self.planningGridLayerWasActive = true;
        if ( !self.planningGridLayer.visible() ) {
            self.planningGridLayer.setVisible();
        }
    } else {
        self.planningGridLayer.activateLayer();
    }

    //self.selectFeature = new OpenLayers.Control.SelectFeature(self.polygonLayer);
    //app.map.addControl(self.selectFeature);

    self.polygonControl.events.register(
        'featureadded',
        self.polygonLayer,
        function(e) {
            self.completeSketch();
            self.showEdit(true);
            // TODO - toggle clipping drawings to grid in settings
            // self.clipToGrid();
            self.finishDrawing();
        }
    );

    self.finishDrawing = function() {
      var format = new OpenLayers.Format.WKT();
      var wkt = format.write(self.polygonLayer.features[0]);
      feature = format.read(wkt);

      self.completeEdit();
      self.clipAttemptFailed(false);

      $('#step-1-instructions').effect("highlight", {}, 1000);
    };

    self.clipToGrid = function() {
        var format = new OpenLayers.Format.WKT();
        var wkt = format.write(self.polygonLayer.features[0]);
        $.ajax({
            url: '/drawing/clip_to_grid',
            type: 'POST',
            // data: {'target_shape': self.polygonLayer},
            data: { target_shape: wkt },
            // dataType: json
            success: function(data) {
                var data_obj = JSON.parse(data),
                    format = new OpenLayers.Format.WKT(),
                    wkt = data_obj.clipped_wkt,
                    feature = format.read(wkt);

                self.completeEdit();

                self.clipAttemptFailed(false);
                self.polygonLayer.setVisibility(false);
                if (!self.clippedDrawing) {
                    self.clippedDrawing = new OpenLayers.Layer.Vector("Clipped Drawing");
                }
                self.clippedDrawing.removeAllFeatures();
                self.clippedDrawing.addFeatures(feature);
                app.map.addLayer(self.clippedDrawing);
                $('#step-1-instructions').effect("highlight", {}, 1000);
            },
            error: function (result) {
                // clip was unsuccessful (e.g. no overlap with planning grid)
                self.clipAttemptFailed(true);
                self.startEdit();
                $('#clip-failed-alert').effect("highlight", {}, 1000);
            }
        });
    };

    self.startEdit = function() {
        self.isEditing(true);
        //activate the modify feature control
        self.editControl.activate();
        //disable feature attribution
        app.viewModel.disableFeatureAttribution();

        if (self.clippedDrawing && app.map.getLayer(self.clippedDrawing.id)) {
            app.map.removeLayer(self.clippedDrawing);
        }

        self.polygonLayer.setVisibility(true);
        //select polygon
        self.editControl.selectFeature(self.polygonLayer.features[0]);

        $('#editing-instructions').effect("highlight", {}, 1000);
    };

    self.completeEdit = function() {
        self.isEditing(false);
        //deactivate the modify feature control
        self.editControl.deactivate();
        //re-enable feature attribution
        app.viewModel.enableFeatureAttribution();

        $('#editing-instructions').effect("highlight", {}, 1000);

        // self.clipToGrid();
        //advance form (in case this was called clicking Done Editing button
        // $('#button_next').click();
    };

    self.completeSketch = function() {
        self.hasShape(true);
        self.isDrawing(false);
        //deactivate the draw feature control
        self.polygonControl.deactivate();
        //re-enable feature attribution
        app.viewModel.enableFeatureAttribution();
    };

    self.startSketch = function() {
        self.isDrawing(true);
        //activate the draw feature control
        self.polygonControl.activate();
        //disable feature attribution
        app.viewModel.disableFeatureAttribution();

        $('#drawing-instructions').effect("highlight", {}, 1000);
    };
    /*
    self.replacePolygonLayer = function(newLayer) {
        app.map.removeLayer(self.polygonLayer);
        self.polygonLayer = newLayer;
        //maybe remove layer from app.map and then re-add layer?
        app.map.removeLayer(newLayer);
        app.map.addLayer(newLayer);
    };
    */
    self.cleanUp = function() {
        //app.map.removeLayer(self.polygonLayer);
        self.polygonControl.deactivate();
        app.map.removeControl(self.polygonControl);
        self.editControl.deactivate();
        app.map.removeControl(self.editControl);
        //BETTER YET -- just remove all app.map.layer items that match the name New Polygon Layer
        //might make the name slightly more cryptic for this...
        app.map.removeLayerByName(self.newPolygonLayerName);
        // app.map.removeLayer(self.polygonLayer);
        if (self.clippedDrawing) {
            app.map.removeLayerByName("Clipped Drawing");
        }

        if ( ! self.planningGridLayerWasActive ) {
            if ( self.planningGridLayer.active() ) {
                self.planningGridLayer.deactivateLayer();
            }
        }

    };

    self.togglePlanningGridLayer = function(formModel, event) {
        if ( event.target.type === "checkbox" ) {
            if ($('#planning-grid-layer-toggle input').is(":checked")) {
                self.planningGridLayer.activateLayer();
            } else {
                self.planningGridLayer.deactivateLayer();
            }
        }
        return true;
    };

    return self;
} // end polygonFormModel

function collectionModel(options) {
    var self = this;

    //TODO - get drawing attrs from collection to apply to info box.
    var ret = scenarioModel.apply(this, arguments);

    self.editCollection = function() {
      self.collection = this;
      if (! self.collection.active()) {
        self.collection.activateLayer;
      }

      return $.ajax({
        url: '/features/collection/' + self.collection.uid + '/form/',
        success: function(data) {
          app.viewModel.scenarios.collectionForm(true);
          $('#'+app.viewModel.currentTocId()+'-scenario-collection-form > div').html(data);
          app.viewModel.scenarios.collectionFormModel = new collectionFormModel();
          var model = app.viewModel.scenarios.collectionFormModel;

          ko.applyBindings(model, document.getElementById(app.viewModel.currentTocId()+'-scenario-collection-form').children[0]);

          // var parameters = [
          //     'species',
          //     'lifestage',
          //     'mean_fthm',
          //     'hsall_m2',
          //     'cnt_cs',
          //     'cnt_penn'
          // ];
          //
          // for (var i = 0; i < parameters.length; i++) {
          //     var id = '#id_' + parameters[i];
          //
          //     if ($(id).is(':checked')) {
          //         model.toggleParameter(parameters[i]);
          //     }
          // }

        },
        error: function (result) {
          console.log('error in drawing.js: editCollection');
        }
      });
    };

    self.deleteCollection = function() {
      var collection = this;

      //remove from activeLayers
      app.viewModel.activeLayers.remove(collection);
      //remove from app.map
      if (collection.layer) {
          app.map.removeLayer(collection.layer);
      }
      //remove from selectionList
      app.viewModel.scenarios.collectionList.remove(collection);
      //update scrollbar
      app.viewModel.scenarios.updateDesignsScrollBar();

      //remove from server-side db (this should provide error message to the user on fail)
      $.ajax({
          url: '/drawing/delete_collection/' + collection.uid + '/',
          type: 'POST',
          success: function (result) {
            app.viewModel.scenarios.loadDrawingsFromServer();
            app.viewModel.scenarios.loadScenariosFromServer();
          },
          error: function (result) {
              console.log('error in drawing.js: deleteCollection');
          }
      });

    };

    self.zoomToScenario = function(collection) {
        if (!collection.active()) {
            collection.activateLayer();
        }
        // ActivateLayer needs some time to load (50-100ms locally).
        // This next function checks every 20th of a second for up to 1/2 second
        //   to see if the layer has loaded and then zooms if appropriate.
        countdown = 10;
        zoomToLoadedCollection = function(countdown, collection) {
          setTimeout( function(){
              if (collection.layer) {
                  var layer = collection.layer;
                  if (layer.features.length > 0) {
                    app.map.zoomToExtent(layer.getDataExtent());
                    app.map.zoomOut(); //Sometimes close is too close
                  } else {
                      window.alert('No drawings associated with this scenario.');
                  }
              } else {
                  if (countdown > 0) {
                    zoomToLoadedCollection(countdown-1, collection);
                  } else {
                      window.alert('Could not determine the extent of this scenario.');
                  }
              }
            }, 50
          );
        };
        zoomToLoadedCollection(countdown, collection);
    };

    self.addDrawing = function() {

    };

    self.removeDrawing = function() {

    };

    self.calculateScore = function() {

    };

    self.createCopyCollection = function(collection) {
      $.ajax({
          url: '/drawing/copy_collection/' + collection.uid + '/',
          type: 'POST',
          dataType: 'json',
          success: function(data) {
              app.viewModel.scenarios.loadCollectionsFromServer();
              app.viewModel.scenarios.addScenarioToMap(null, {uid: data.copy_uid});
          },
          error: function (result) {
              console.log('error in drawing.js: createCopyCollection');
          }
      });
      // TODO: Open 'edit' view of new collection.
      // features = collection.layer.features;
    };


}

function collectionFormModel(options) {
  var self = this;

  return self;
}
