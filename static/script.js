$(document).ready(function() {

	$('form').on('submit', function(event) {

		$.ajax({
			data : {
				a : $('#home').val(),
				b : $('#away').val()
			},
			type : 'POST',
			url : '/process'
		})
		.done(function(data) {
      console.log(data);
      $('#para').text(data);
      $('#home_pc').text(Math.round(data[0]*100));
      $('#draw_pc').text(Math.round(data[1]*100));
      $('#away_pc').text(Math.round(data[2]*100));
      $(".results-container").toggle();

		});

		event.preventDefault();

	});

});