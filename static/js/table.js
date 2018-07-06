function getorder() {
    var value='';
    var radio = document.getElementsByName('radio');
    for (var i=0;i<radio.length;i++){
        if(radio[i].checked==true){
            value=radio[i].value;
            break;
        }
    }
    return value;
}

function tableList(status,data) {
    var items;

    if (status) {
        $.each(data,function(i, item) {

            if (i % 2 == 0) {
            items += "<tr style='background-color: #269abc'><td>" + item['id'] + "</td><td>" + item['name'] + "</td><td>" + item['mobile'] + "</td><td>" + item['idcard'] + "</td><td>" + "<a href='/updateuser/" + item['id'] + "'>修改</a>/<a href='/delteuser/" + item['id'] + "'>删除</a>" + "</td></tr>"
            } else {
            items += "<tr><td>" + item['id'] + "</td><td>" + item['name'] + "</td><td>" + item['mobile'] + "</td><td>" + item['idcard'] + "</td><td>" + "<a href='/updateuser/" + item['id'] + "'>修改</a>/<a href='/delteuser/" + item['id'] + "'>删除</a>" + "</td></tr>"
            }
            });
        }
        else {items = "<tr><td colspan='5'  style='text-align: center'>查询结果为空</td></tr>";}
    $("#resultuser").html(items);
    $("#usersnow").append('999999999999999999');


}

$(function() {$("#selectbtn").click(function() {
      var names = $('#name').val();
      var datacount = $('#datacount').val();
      var orders = getorder();
      $.ajax({
        type: 'post',
        url: '/selectuser',
        data: {'name': names,'pagecount': datacount,'page':1,'order':orders},
        success: function(msg) {
          var data = JSON.parse(msg)['data'];
          var len = JSON.parse(msg)['len'];
          var status = JSON.parse(msg)['status'];
          var options = {
            bootstrapMajorVersion: 3,
            currentPage: 1,
            totalPages: Math.ceil(len/datacount),
            itemTexts: function(type, page, current) {
              switch (type) {
                  case "first": return "首页";
                  case "prev": return "上一页";
                  case "next":  return "下一页";
                  case "last": return "末页";
                  case "page":  return page;
              }
            },
            onPageClicked: function(event, originalEvent, type, page) {
              var names = $('#name').val();
              var datacount = $('#datacount').val();
              var orders = getorder();
                $.ajax({
                type: 'post',
                url: "/selectuser",
                data: { 'page': page, 'name': names,'pagecount': datacount,'order':orders },
                success: function(msg) {
                  var data = JSON.parse(msg)['data'];
                  var status = JSON.parse(msg)['status'];
                  var len = JSON.parse(msg)['len'];
                  tableList(status,data);

                },

              });
            },

          };
          tableList(status,data);
          $("#page").bootstrapPaginator(options)

        },
        error: function() {}
      });
    })});

$(function() {
    $("#houseselectbtn").click(function() {
          var housename = $('#housename').val();
          $.ajax({
            type: 'post',
            url: '/selecthouse',
            data: {'name': housename},
            success: function(msg) {
            var datas = JSON.parse(msg)['data'];
            var status = JSON.parse(msg)['status'];
            var len = JSON.parse(msg)['len'];
            var items;
            if (status){
                $.each(datas,function (i,item) {
                switch (item[5])
                {
                    case 0:item[5]='待出租';break;
                    case 1:item[5]='已出租';break;
                    case 2:item[5]='待签约';break;
                    case 3:item[5]='已预订';break;
                }
                items+="<tr><td>"+item[0]+"</td><td>"+item[1]+"</td><td>"+item[2]+"</td><td>"+item[3]+"</td><td>"+item[4].substr(0,25)+"</td><td>"+item[5]+"</td><td>"+"<a href=' / updatehouse / "+item[0]+"'>修改</a>/<a href=' / deltehouse / "+item[0]+"'>删除</a>"+"</td></tr>"
            });
            }else {
                items="<tr><td colspan='7 '  style='text - align: center '>查询结果为空</td></tr>";
            }
            $("#resulthouse").html(items);



        },
        error:function (){
    }
   });
   });
});

$(function () {
        $("#fileload").click(function () {
            var form_data = new FormData();
            var file_info =$('#file_upload')[0].files[0];
            form_data.append('file',file_info);

            $.ajax({
                url:'/fileload',
                type:'post',
                data: form_data,
                processData: false,
                contentType: false,
                 success: function(msg) {
                     var results = JSON.parse(msg)['status'];
                     if(results){
                         $("#result").html("<label style='color: green'>上传成功</label>")
                     }else{
                         $("#result").html("<label style='color: red'>上传失败</label>")
                     }
                }
            });
        })
    });

$(function () {
$("#code").click(function () {
    var content=$("#content").val();
    $.ajax({
        type:'post',
        url:'/code',
        data:{'content':content},
        success:function (msg){
            var status = JSON.parse(msg)['status'];
            if(status=="1"){
                var image = JSON.parse(msg)['images'];
                $("#imagecode").html("<img  src="+image+"/>")
            }else {$("#imagecode").html('二维码生成失败')}

        }
        });
    });
});

$(function () {
   $("#createcode").click(function () {
       if($("#createcode").hasClass('active')){


       }else{
           $("#createcode").addClasse('active')
       }

   });
});

// #显示查询数量


