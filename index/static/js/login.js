$(function(){
  $('.login-btn').on('click', function(){
    let email = $("#login_email").val();
    let password = $("#login_password").val();
    let param = {
      email: email,
      password: password
    };
    $.ajax({
      type: 'POST',
      url: "/account/login/",
      data: param,
      async: true,
      success: res => {
        console.log(res);
        if(res.status == "success"){
          $('.md-title').html("login success");
          $('.md-content').html("hello " + res.user);
          $('#your-modal').modal();
          setTimeout(function(){
            $(location).attr('href', '/');
          }, 2000);
        } else {
          $('.md-title').html("login fail");
          $('.md-content').html("检查一下你的密码啥的");
          $('#your-modal').modal();
        }
      },
      error: res => {
        $('.md-title').html("login fail");
        $('.md-content').html("邮箱填错了");
        $('#your-modal').modal();
      }
    });
  });
  $('.register-btn').on('click', function(){
    let nick = $('#register_nick').val();
    let password = $('#register_password').val();
    let email = $('#register_email').val();
    let param = {
      nick: nick,
      email: email,
      password: password
    };
    console.log(param);
    $.ajax({
      type: 'POST',
      url: "/account/sign/",
      data: param,
      async: true,
      success: res => {
        $('.md-title').html("register success");
        $('.md-content').html("呆火再登录一下就行了");
        $('#your-modal').modal();
        setTimeout(function(){
          $(location).attr('href', '/login');
        }, 2000);
      },
      error: res=>{
        $('.md-title').html("register fail");
        $('.md-content').html("可能邮箱存在或者不符合规范");
        $('#your-modal').modal();
      }
    });
  })
});
