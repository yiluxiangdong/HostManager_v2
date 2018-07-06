//添加房源
function getType(items) {
    var value='';
    var radio = document.getElementsByName(items);
    for (var i=0;i<radio.length;i++){
        if(radio[i].checked==true){
            value=radio[i].value;
            break;
        }
    }
    return value;
}

function getvalue(landermobile,rent_type,newestate,housenum,type) {
    var landermobile = $(landermobile).val();
    var rent_type = getType(rent_type);
    var newestate = $(newestate).val();
    var housenum = $(housenum).val();
    var type = type;
    var info={'landermobile':landermobile,'rent_type':rent_type,'newestate':newestate,'housenum':housenum,'type':type};
    return info;

}

$(function () {
        $("#addjz").mouseleave(function () {
            $("#infojz").html('');
            $("#landermobile1").val('');
            $("#rent_type1").val('');
            $("#newestate1").val('');
            $("#housenum1").val('');
        });
        $("#addfs").mouseleave(function () {
            $("#infofs").html('');
            $("#landermobile").val('');
            $("#rent_type").val('');
            $("#newestate").val('');
            $("#housenum").val('');
        });
    });

$(function () {
        $("#addjz").click(function () {
            var info=getvalue("#landermobile1",'rent_type1',"#newestate1","#housenum1",'jz');
            if(info['landermobile']!='' && info['rent_type']!=''&&info['housenum']!=''){
                $.ajax({
                    url:'/addhouse',
                    type:'post',
                    data:info,
                    success:function (msg) {
                        $("#infojz").html("添加信息:"+msg)
                    },
                });

            }else{
                $("#infojz").html('请填写完成信息')
            }

        });

    });

$(function () {
        $("#addfs").click(function () {
            var info=getvalue("#landermobile",'rent_type',"#newestate","#housenum",'fs');
            if(info['landermobile']!='' && info['rent_type']!=''&&info['housenum']!=''){
                $.ajax({
                    url:'/addhouse',
                    type:'post',
                    data:info,
                    success:function (msg) {
                        $("#infofs").html("添加信息:"+msg)
                    },
                });

            }else{
                $("#infofs").html('请填写完成信息')
            }

        });

    });
