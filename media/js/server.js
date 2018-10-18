// load layers from fixture or the server
app.viewModel.loadLayers = function(data) {
	var self = app.viewModel;
	// load layers
  $.each(data.tocs, function(j, toc) {
  	$.each(toc.layers, function(i, layer) {
  		var layerViewModel = new layerModel(layer);

  		self.layerIndex[layer.id] = layerViewModel;
  		// add sublayers if they exist
  		if (layer.subLayers && layer.subLayers.length) {
  			$.each(layer.subLayers, function(i, layer_options) {
  				if (layer_options.type !== 'placeholder') {
  					var subLayer = new layerModel(layer_options, layerViewModel);
  					app.viewModel.layerIndex[subLayer.id] = subLayer;
  					layerViewModel.subLayers.push(subLayer);
  				}
  			});
  		}
  	});

  	// load themes
  	$.each(toc.themes, function(i, themeFixture) {
  		var layers = [],
  		theme = new themeModel(themeFixture);
  		$.each(themeFixture.layers, function(j, layer_id) {
  			// create a layerModel and add it to the list of layers
  			var layer = self.layerIndex[layer_id],
  				searchTerm = layer.name + ' (' + themeFixture.display_name + ')';
  			layer.themes.push(theme);
  			theme.layers.push(layer);

  			if (!layer.subLayers.length) { //if the layer does not have sublayers
                  self.layerSearchIndex[searchTerm] = {
                      layer: layer,
                      theme: theme
                  };
              } else { //if the layer has sublayers
  				$.each(layer.subLayers, function(i, subLayer) {
  					//var searchTerm = subLayer.name + ' (' + themeFixture.display_name + ')';
                      var searchTerm = subLayer.name + ' (' + themeFixture.display_name + ' / ' + subLayer.parent.name + ')';
  					if (subLayer.name !== 'Data Under Development') {
                          self.layerSearchIndex[searchTerm] = {
                              layer: subLayer,
                              theme: theme
                          };
                      }
  				});
                  layer.subLayers.sort( function(a,b) { return a.name.toUpperCase().localeCompare(b.name.toUpperCase()); } );
  			}

  		});
      //sort by name
      theme.layers.sort( function(a,b) { return a.name.toUpperCase().localeCompare(b.name.toUpperCase()); } );

  		self.themes.push(theme);
      if (!toc.hasOwnProperty('themeObjects')){
        toc.themeObjects = [];
      }
      toc.themeObjects.push(theme);
  	});
    if (!toc.hasOwnProperty('themeObjects')){
      toc.themeObjects = [];
    }
    self.tocs.push(toc);
    //fixes a problem in which the data accordion scrollbar was reinitialized before the app switched back to the data tab
    //causing the data tab to appear empty
    //the following appears to fix that problem
    $('#' + toc.tocid + '-dataTab[data-toggle="tab"]').on('shown', function(e) {
      app.viewModel.showBottomButtons(true);
      app.viewModel.updateScrollBars();
      app.viewModel.showLegend(false);
    });
    $('#' + toc.tocid + '-activeTab[data-toggle="tab"]').on('shown', function(e) {
      app.viewModel.showBottomButtons(true);
      app.viewModel.updateScrollBars();
      app.viewModel.showLegend(false);
    });
    $('#' + toc.tocid + '-designsTab[data-toggle="tab"]').on('shown', function(e) {
      app.viewModel.showBottomButtons(false);
      app.viewModel.updateAllScrollBars();
      setTimeout(function() {$('.group-members-popover').popover({html: true, trigger: 'hover', container: 'body'});}, 2000);
    });
    $('#' + toc.tocid + '-legendTab[data-toggle="tab"]').on('shown', function(e) {
      app.viewModel.showBottomButtons(true);
      app.viewModel.showLegend(true);
      app.viewModel.updateScrollBars();
    });
  });

	app.typeAheadSource = (function () {
            var keys = [];
            for (var searchTerm in app.viewModel.layerSearchIndex) {
                if (app.viewModel.layerSearchIndex.hasOwnProperty(searchTerm)) {
                    keys.push(searchTerm);
                }
            }
            return keys;
    })();

    //re-initialise the legend scrollbar
    //if ( ! app.embeddedMap ) {
    if ( $(window).width() > 767 && !app.embeddedMap ) {
        $('#legend-content').jScrollPane();
    }

};
app.viewModel.loadLayersFromFixture = function() {
	app.viewModel.loadLayers(app.fixture);
};


app.viewModel.loadLayersFromServer = function() {
    var pathname = window.location.pathname,
        slug_name = pathname.substring(1, pathname.indexOf('/planner'));
    if (slug_name === '/') {
        slug_name = pathname.substring(1, pathname.indexOf('/visualize'));
    }
	return $.getJSON('/data_manager/get_json/'+slug_name, function(data) {
		app.viewModel.loadLayers(data);
	});
};
//test comment
