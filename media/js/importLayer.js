initImport = function(data, e) {
  e.stopPropagation();
  e.preventDefault();
  $('#import-layer-form-info').css("display", "none");
  $('#import-layer-form-success').css("display", "none");
  $('#import-layer-form-error').css("display", "none");
  $('#import-layer-form-other').css("display", "none");
  $('#import-layer-progress-bar').css('width', "1px");
  $('#import-layer-modal').modal('show');
  $('#import-layer-form-name').unbind('input');
  $('#import-layer-form-name').on('input', validateImportForm);
  $('#import-layer-form-file').unbind('change');
  $('#import-layer-form-file').on('change', validateImportForm);
};

submitImport = function(e) {
  e.preventDefault();
  var name = $('#import-layer-form-name').val();
  $('#import-layer-form-info').css("display", "");
  $('#import-layer-form-success').css("display", "none");
  $('#import-layer-form-error').css("display", "none");
  $('#import-layer-form-other').css("display", "none");
  var $form = $('#import-layer-form');
  var url = $form.attr('action'),
      $bar = $('#import-layer-progress-bar'),
      data = new FormData(),
      barTimer;

  //progress bar
  barTimer = setInterval(function () {
      var width = parseInt($bar.css('width').replace('px', ''), 10) + 5,
          barWidth = parseInt($bar.parent().css('width').replace('px',''), 10);

      if (width < barWidth) {
          $bar.css('width', width + "px");
      } else {
          clearInterval(barTimer);
      }
  }, 500);

  $form.find('input,select,textarea').each( function(index, input) {
      var $input = $(input);

      if ($input.attr('type') == 'file') {
          $.each($input[0].files, function(i, file) {
              data.append('file-'+i, file);
          });
      } else {
          data.append($input.attr('name'), $input.val());
      }

  });


  $.ajax( {
      url: url,
      data: data,
      cache: false,
      contentType: false,
      processData: false,
      type: 'POST',
      traditional: true,
      dataType: 'json',
      success: function(result) {
        $('#import-layer-form-info').css("display", "none");
        if (result.success) {
          $('#import-layer-form-success').css("display", "");
        } else {
          $('#import-layer-form-error').css("display", "");
          $('#import-modal-error-text').text(result.message);
        }
      },
      error: function(result) {
        $('#import-layer-form-info').css("display", "none");
        if (result.status == 504) {
          $('#import-layer-form-other').css("display", "");
          var response_text = "Your request is taking longer than normal to process. \
          If your file was over 50MB, please give the server some more time to \
          import your data (about 1 minute for every 2 MB) and refresh. If you \
          do not see your data under the \"Imported\" category after waiting the\
          appropriate amount of time and then refreshing your browser, you may\
          try again, or edit your shapefile to be simpler or of smaller scope."
          $('#import-modal-other-text').text(response_text);
        } else {
          $('#import-layer-form-error').css("display", "");
          $('#import-modal-error-text').text(result.responseText);
        }
      }
  });
};

validateImportForm = function() {
  var name = $('#import-layer-form-name').val();
  if ($.trim(name) === "") {
    $('#import-invalid-name-message').show();
  } else {
    $('#import-invalid-name-message').hide();
  }
  if (name != null && $.trim(name) != "" && $('#import-layer-form-file').val() != "") {
    $('#import-layer-form-submit').removeAttr("disabled");
    $('#import-layer-form-submit').on("click", submitImport);
  } else {
    $('#import-layer-form-submit').attr("disabled", true);
    $('#import-layer-form-submit').unbind("click");
  }
};

editImportLayerInit = function(data, e) {
  e.stopPropagation();
  e.preventDefault();
  app.currentLayerModel(data);
  $.ajax( {
    url: '/features/importlayer/' + data.uid + '/form/',
    type: 'GET',
    success: function(result) {
      $('#import-layer-edit-form').empty();
      $('#import-layer-edit-form').append(result);
      // Remove file import field
      $('#id_import_file').parent().remove();
      // Remove default submit button
      $('#import-layer-edit-form div #featureform').find("[type='submit']").parent().remove();
      $('.wizard_nav').next().remove();
      $('.wizard_nav').remove();
      // $('.wizard_control').remove();
      $('#import-layer-edit-form-submit').unbind("click");
      $('#import-layer-edit-form-submit').on("click", submitEditImportLayer);
      var $form = $('#import-layer-edit-form div #featureform');
      $form.keydown(function (e) {
        if(e.which == 13){
          e.stopPropagation();
          e.preventDefault();
          submitEditImportLayer($form);
        }
      });


      $('#import-layer-edit-modal').modal('show');
    },
    error: function(result) {
      window.alert("Unable to retrieve edit form for this layer.")
    }
  });
};

submitEditImportLayer = function(data) {
  var $form = $('#import-layer-edit-form div #featureform');
  var url = $form.attr('action'),
      $bar = $('#import-layer-edit-progress-bar'),
      data = new FormData(),
      barTimer;

  //progress bar
  barTimer = setInterval(function () {
      var width = parseInt($bar.css('width').replace('px', ''), 10) + 5,
          barWidth = parseInt($bar.parent().css('width').replace('px',''), 10);

      if (width < barWidth) {
          $bar.css('width', width + "px");
      } else {
          clearInterval(barTimer);
      }
  }, 500);

  $form.find('input,select,textarea').each( function(index, input) {
      var $input = $(input);

      if ($input.attr('type') == 'file') {
          $.each($input[0].files, function(i, file) {
              data.append('file-'+i, file);
          });
      } else {
          data.append($input.attr('name'), $input.val());
      }

  });

  $.ajax( {
      url: url,
      data: data,
      cache: false,
      contentType: false,
      processData: false,
      type: 'POST',
      traditional: true,
      dataType: 'json',
      success: function(result) {
        var $form = $('#import-layer-edit-form div #featureform');
        new_name = $form.find('#id_name').val();
        new_description = $form.find('#id_description').val();
        updateImportLayer(new_name, new_description);
        $('#import-layer-edit-modal').modal('hide');
      },
      error: function(result) {
        $('#import-layer-edit-form-info').css("display", "none");
        $('#import-layer-edit-form-error').css("display", "");
        $('#import-modal-edit-error-text').text(result.responseText);
      }
  });

};

updateImportLayer = function(new_name, new_description) {
  var layer_button = $('.layer_' + app.currentLayerModel().id + "_name");
  layer_button.html(new_name);
  app.currentLayerModel().name = new_name;
  app.currentLayerModel().overview = new_description;
};

cancelEditImportLayer = function(data, e) {

};

removeDeletedLayer = function(layer) {
  setTimeout(function(){
    $('#layer_' + layer.id).empty();
    $('#layer_' + layer.id).remove();
    $('#layer_' + layer.id).hide();
    $('#import-layer-delete-modal').modal('hide');
  }, 200);
};

deleteImportLayer = function(e) {
  e.stopPropagation();
  e.preventDefault();
  $.ajax( {
      url: "/data_manager/import_layer/" + app.deleteLayerId + "/delete/",
      type: 'POST',
      success: function(result) {
        removeDeletedLayer(app.deleteLayer);
        $('#import-layer-delete').modal('hide');
      },
      error: function(result) {
        window.alert("Unable to complete request. Error deleting imported layer.")
      }
  });
};

deleteImportInit = function(layer, e) {
  e.stopPropagation();
  e.preventDefault();
  app.deleteLayer = layer;
  app.deleteLayerId = parseInt(layer.id.split('il')[1]);
  $('#import-layer-delete-button').unbind('click');
  $('#import-layer-delete-button').on('click', deleteImportLayer);
  $('#import-layer-delete-modal').modal('show');
};

shareImportInit = function(layer, e) {
  e.stopPropagation();
  e.preventDefault();
  layer.showSharingModal(layer);
}
