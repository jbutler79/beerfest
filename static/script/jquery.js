$(document).ready(function() {
  $('select[name=brewery] option[value!=""]').remove();
  $('select[name=beer] option[value!=""]').remove();

  $('select[name=event]').change(function(){
    $('select[name=brewery] option[value!=""]').remove();
    event_id = $(this).val();
    request_url = '/event/beer/get_breweries_at_event' + event_id + '/';
    $.ajax({
      url: request_url,
      success: function(data){
        for (var key in data) {
          $('select[name=brewery]').append('<option value="' + [key] + '">' + data[key] +'</option>');
        }
      }
    });
    return false;
  });

  $('select[name=brewery]').change(function(){
    $('select[name=beer] option[value!=""]').remove();
    brewery_id = $(this).val();
    request_url = '/event/beer/get_beers_at_event_by_brewery' + brewery_id + '/';
    $.ajax({
      url: request_url,
      success: function(data){
        for (var key in data) {
          $('select[name=beer]').append('<option value="' + [key] + '">' + data[key] +'</option>');
        }
      }
    });

  if ($('#event_beer_id').val().length !== 0 && $('#event_beer_id').val() !== '') {
    //alert($('#event_beer_id').val());
    event_beer_id = $('#event_beer_id').val();
    event_name_request_url = '/event/beer/get_event_name' + event_beer_id + '/';
    brewery_name_request_url = '/event/beer/get_brewery_name' + event_beer_id + '/';
    beer_name_request_url = '/event/beer/get_beer_name' + event_beer_id + '/';

    $('select[name=event] option').remove();
    $('select[name=brewery] option').remove();
    $('select[name=beer] option').remove();
    $.ajax({
      url: event_name_request_url,
      success: function(data){
        for (var key in data) {
          $('select[name=event]').append('<option value="' + [key] + '" selected="selected">' + data[key] +'</option>');
        }
      }
    });
    $.ajax({
      url: brewery_name_request_url,
      success: function(data){
        for (var key in data) {
          $('select[name=brewery]').append('<option value="' + [key] + '" selected="selected">' + data[key] +'</option>');
          //$('select[name=brewery]').prop('disabled', true);
        }
      }
    });
    $.ajax({
      url: beer_name_request_url,
      success: function(data){
        for (var key in data) {
          $('select[name=beer]').append('<option value="' + [key] + '" selected="selected">' + data[key] +'</option>');
          //$('select[name=beer]').prop('disabled', true);
        }
      }
    });
  }

  return false;

  });



});
