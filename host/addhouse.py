<<<<<<< HEAD
#!/usr/bin/python
#-*- coding:utf-8 _*-
import  pymysql,json

class RentTest:
    def __init__(self,mobile,houseType,newestate,rentermobile):
        self.houseType = houseType
        self.mobile = mobile
        self.newestate = newestate
        self.rentermobile = rentermobile
        conn = pymysql.connect(user='root',password='111111',host='172.17.17.221',database='renting_test2')
        self.cour = conn.cursor()
#添加分散式房源并展示添加的结果
    def addhouse_fs(self):
        result = ''
        self.cour.callproc('addhouse_fs',(self.mobile,self.houseType,self.newestate,result))
        date =  self.cour.fetchone()[0]
        print  date

#添加集中式房源并展示添加的结果
    def addhouse_jz(self):
        result = ''
        self.cour.callproc('addhouse_jz',(self.mobile,self.houseType,self.newestate,result))
        date =  self.cour.fetchone()[0]
        print  date

    def allocatehouse(self):
        result = ''
        self.cour.callproc('Allocat_house', (self.mobile, result))
        date = self.cour.fetchone()[0]
        print  date

    def signcontract(self):
        result = ''
        #获取房源名称
        sql="SELECT s.`name`  FROM rms_housing s  LEFT JOIN rms_landlord t ON s.landlord_id=t.id WHERE  t.mobile='%s' AND s.`status`=0 ORDER BY  RAND() LIMIT 0,1"
        self.cour.execute(sql,self.mobile)
        housename = self.cour.fetchone()[0]

        self.cour.callproc('Sign_contract', (self.rentermobile,housename, result))
        date = self.cour.fetchone()[0]
        print  date,housename

    def payorder(self):
        payresult = ''
        self.cour.callproc('payorder_v2', (self.rentermobile, payresult))
        date = self.cour.fetchone()[0]
        print  date
    #
    def  payallorder(self,mobile):
        pass


    def __del__(self):
        self.cour.close()

if __name__ == '__main__':
    #参数需要"房东电话","整租或者合租","小区名称","租客电话"
    renttest = RentTest('16600000000','1','华天花园','18665333851')
    #添加分散式房源
    # for i in range(100):
    #     try:
    #         renttest.addhouse_fs()
    #     except Exception as e:
    #         print e
    # 添加集中式房源
    for i in range(100):
        try:
            renttest.addhouse_jz()
        except Exception as e:
            print e

    #分配房源给分店
    # renttest.allocatehouse()
    #租客登记
    # renttest.signcontract()
    #交水电费和其他费用
    # renttest.payorder()

=======
#!/usr/bin/python
#-*- coding:utf-8 _*-
import  pymysql,json

class RentTest:
    def __init__(self,mobile,houseType,newestate,rentermobile):
        self.houseType = houseType
        self.mobile = mobile
        self.newestate = newestate
        self.rentermobile = rentermobile
        conn = pymysql.connect(user='root',password='111111',host='172.17.17.221',database='renting_test2')
        self.cour = conn.cursor()
#添加分散式房源并展示添加的结果
    def addhouse_fs(self):
        result = ''
        self.cour.callproc('addhouse_fs',(self.mobile,self.houseType,self.newestate,result))
        date =  self.cour.fetchone()[0]
        print  date

#添加集中式房源并展示添加的结果
    def addhouse_jz(self,num):
        result = ''
        self.cour.callproc('addhouse_jz',(self.mobile,self.houseType,self.newestate,num,result))
        date =  self.cour.fetchone()[0]
        print  date

    def  selectlander(self,items):
        sql = "SELECT id,mobile,merchant_name,payMode  FROM  rms_landlord WHERE mobile LIKE CONCAT('%','{}','%') OR merchant_name LIKE CONCAT('%','{}','%')".format(items,items)
        self.cour.execute(sql)
        data = self.cour.fetchall()
        return data


    def allocatehouse(self):
        result = ''
        self.cour.callproc('Allocat_house', (self.mobile, result))
        date = self.cour.fetchone()[0]
        print  date

    def signcontract(self):
        result = ''
        #获取房源名称
        sql="SELECT s.`name`  FROM rms_housing s  LEFT JOIN rms_landlord t ON s.landlord_id=t.id WHERE  t.mobile='%s' AND s.`status`=0 ORDER BY  RAND() LIMIT 0,1"
        self.cour.execute(sql,self.mobile)
        housename = self.cour.fetchone()[0]

        self.cour.callproc('Sign_contract', (self.rentermobile,housename, result))
        date = self.cour.fetchone()[0]
        print  date,housename

    def payorder(self):
        payresult = ''
        self.cour.callproc('payorder_v2', (self.rentermobile, payresult))
        date = self.cour.fetchone()[0]
        print  date
    #
    def  payallorder(self,mobile):
        pass


    def __del__(self):
        self.cour.close()

class Checkdata(object):
    def __init__(self):
        self.conn = pymysql.connect(user='root', password='111111', host='172.17.17.221', database='renting_test2')
        self.cour = self.conn.cursor()

    def  selectlander(self,mobile):
        sqlbymobile="SELECT id,mobile,merchant_name,payMode  FROM  rms_landlord WHERE mobile LIKE CONCAT('%','{}','%')".format(mobile)

        self.cour.execute(sqlbymobile)
        data = self.cour.fetchall()
        return list(data)

    def __del__(self):
        self.cour.close()
        self.conn.close()




if __name__ == '__main__':
    #参数需要"房东电话","整租或者合租","小区名称","租客电话"
    renttest = RentTest('13570862000','1','华天宜居花园','18665333851')
    #添加分散式房源
    # for i in range(100):
    #     try:
    #         renttest.addhouse_fs()
    #     except Exception as e:
    #         print e
    # 添加集中式房源
    # for i in range(100):
    #     try:
    #         renttest.addhouse_jz()
    #     except Exception as e:
    #         print e
    # try:
    #     renttest.addhouse_jz(12)
    # except Exception as e:
    #     print e
    # print  renttest.selectlander('123')
    #分配房源给分店
    # renttest.allocatehouse()
    #租客登记
    # renttest.signcontract()
    #交水电费和其他费用
    # renttest.payorder()

    checkdata = Checkdata()
    print  checkdata.selectlander('136')
>>>>>>> 自动化测试脚本2018/07/06 17:38:42 更新
