/**
 * Created by python on 17-10-2.
 */
error_name = false;
error_password = false;
$(function(){
	$('#username').blur(function() {
		check_user_name();
	});

	$('#pwd').blur(function() {
		check_pwd();
	});

	function check_user_name(){
		var len = $('#username').val().length;
		if(len<5||len>20)
		{
			$('#username').next().html('请输入5-20个字符的用户名')
			$('#username').next().show();
			error_name = true;
		}
		else{

			$('#username').next().hide();
			error_name = false;
		}
	}

	function check_pwd(){
		var len = $('#pwd').val().length;
		if(len<8||len>20)
		{
			$('#pwd').next().html('密码最少8位，最长20位')
			$('#pwd').next().show();
			error_password = true;
		}
		else
		{
			$('#pwd').next().hide();
			error_password = false;
		}
	}

	$('#login_form').submit(function() {
		check_user_name();
		check_pwd();

		if(error_name == false && error_password == false && error_check_password == false && error_email == false && error_check == false)
		{
			return true;
		}
		else
		{
			return false;
		}

	});

})