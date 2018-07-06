$(function () {
   $("#checkland").click(function () {
       var landcontent = $("#landcontent").val();
       $.ajax({
           url:'/checkland',
           type:'post',
           data:{'landcontent':landcontent},
           success:function (msg) {
               var  items;
               var  landresults = JSON.parse(msg)['result'];
               var  status = JSON.parse(msg)['status'];
               var  len = JSON.parse(msg)['len'];
               if(status==1){
                    $.each(landresults,function(i, item) {
                    switch (item[3]) {
                    case 0:item[3]='对私';break;
                    case 1:item[3]='对公';break;
                    default:item[3]='默认对公';
                }
                if(i%2==0){
                        items+="<tr  style='background-color: #269abc'><td>"+item[0]+"</td><td>"+item[1]+"</td><td>"+item[2]+"</td><td>"+item[3]+"</td></tr>"
                }else {
                    items+="<tr><td>"+item[0]+"</td><td>"+item[1]+"</td><td>"+item[2]+"</td><td>"+item[3]+"</td></tr>"
                }
                   });

                $("#landresult").html(items)
                   $("#datacount").html("<label>共计"+len+"条</label>")
               }else{
                   $("#landresult").html("<tr style='background-color: burlywood'><td colspan='4' style='text-align: center'>"+landresults+"</td></tr></tr>")
               }
           },
       });
   });

   $("#checkland").mouseleave(function () {
       $("#landinfo").html('')
   });
});

$(function(){
    $("#start").click(function () {

        var showTime = setInterval(function () {
            var count=1;
            $("#startTime").val(count);
            count+=1;
            if(count>10){
                alert('时间到！！！！');
                clearInterval(showTime);

            }
        },1000)

});
});




