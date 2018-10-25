initImport = function(data, e) {
  e.stopPropagation();
  e.preventDefault();
  $('#import-layer-modal').modal('show');
  // TODO: Set on-change events on fields to check is submit is to be enabled
  $('#import-layer-form-name').on('input', validateImportForm);
  $('#import-layer-form-file').on('change', validateImportForm);
};

submitImport = function(data, e) {
  console.log('submit imported layer!');
};

validateImportForm = function() {
  console.log('validate import form!');
  if ($('#import-layer-form-name').val() != null && $('#import-layer-form-name').val() != "" && $('#import-layer-form-file').val() != "") {
    $('#import-layer-form-submit').removeAttr("disabled");
    $('#import-layer-form-submit').on("click", submitImport);
  } else {
    $('#import-layer-form-submit').attr("disabled", true);
    $('#import-layer-form-submit').unbind("click");
  }
};
