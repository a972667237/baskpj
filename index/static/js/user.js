$(function(){
  $.get("/account/getUser/", res=>{
    if(res.status == "success"){
      //delete btn
      $('.login-btn').html("注销");
      $('.login-btn').removeClass("am-btn-primary");
      $('.login-btn').addClass("am-btn-danger");
      let i = $("<b></b>").text("欢迎你，"+res.user + "    ~");
      $('.am-topbar-right').prepend(i);
      if(location.pathname == "/login/"){
        $(location).attr('href', '/');
      }
    } else {
      $('.comment').remove();
    }
  });
});
