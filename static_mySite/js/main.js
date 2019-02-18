$(document).ready(function() {
		function displaySubmit(submitBtn,defaultText,doSubmit){
			if (doSubmit){
			submitBtn.addClass('disabled')
			submitBtn.html('<i class="fa fa-spin fa-spinner"></i> Sending.....')
		}
		else{
			submitBtn.removeClass('disabled')
			submitBtn.html(defaultText)
			
		}
	}

	var registerFormButton=  $('#registerForm').find('[type="submit"]')
	var registerFormButtonText = registerFormButton.text()

	$('#registerForm').submit(function(event){
		event.preventDefault();
		displaySubmit(registerFormButton,registerFormButtonText,true)
		$.ajax({
			data:$(this).serialize(),
			method:$(this).attr('method'),
			url:'',
			success: function(response){
				if (response['success']){
					$('#formmessage').html('<h3>SuccessFully Registered, Thanks</h3>')
				}


				if(response['error']){
					console.log(response['error'])
					var error=response['error']

				var msg=''

				$.each(error,function(key,value){
					msg +='<li>'+value+'</li>'
				})
				$('#formmessage').html('<ul class="errormsg">'+msg+'</ul>')
				}

			setTimeout(function(){
						displaySubmit(registerFormButton,registerFormButtonText,false)
					},500)
			},
			error:function(request, status, error){
				console.log(request.responseText)
			}
		})
	});
});