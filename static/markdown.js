$.editor = function(url, textarea, preview, text) {
	if(url!=undefined  || text!=undefined) {
		if(textarea==undefined) {
			$.notification( 
				{
					title: "Not enough parameters were provided",
					content: "Please check the documentation for the editor.",
					error: true
				}
			);
			return false;
		}
		
		var textareaCon = $('<textarea />');
		var previewCon = $('<div class="preview">');
		
		$(textarea).html('');
		$(preview).html('');
		
		textareaCon.appendTo($(textarea));
		textarea = textareaCon;
		
		previewCon.appendTo($(preview));
		preview = previewCon;
		
		if(url!=undefined) {
			$.get(url, function(data){
				textarea.val(data);
			}).error(
					function(xhr, status, error) { 
						$.notification( 
							{
								title: "An AJAX error occured (" + error + ")",
								content: "Couldn't load the specified text file",
								error: true
							}
						);
					}
				);
		} else {
			textarea.val(text);
		}
		
		
		textarea.wysiwym(Wysiwym.Markdown, {helpEnabled: false});
		
		if(preview!=undefined) {
			var showdown = new Showdown.converter();
			var prev_text = "";
			var update_live_preview = function() {
			    var input_text = textarea.val();
			    if (input_text != prev_text) {
			        var text = $(showdown.makeHtml(input_text));
			        text.find('pre').addClass('prettyprint linenums');
			        text.find('p code').addClass('prettyprint');
			        text.find('code').each(function() {
			            $(this).html(prettyPrintOne($(this).html()));
			        });
		
		
			        preview.html(text);
			        prev_text = input_text;
			    }
			    
			    if(input_text == '') {
			    	preview.hide();
			    } else {
			    	preview.show();
			    }
			}
			clearInterval(update_live_preview);
			setInterval(update_live_preview, 200);
		}
	} else {
		$.notification( 
			{
				title: "Not enough parameters were provided",
				content: "Please check the documentation for the editor.",
				error: true
			}
		);
		return false;
	}
};
$('#preview').on('show', function () {
  $.editor(null, "#editor-textarea", "#editor-preview",$('#id_text').val());
});
$('#preview').on('hide',function(){
  var textarea = $('.editor textarea');
  $('#id_text').val(textarea.val());
});