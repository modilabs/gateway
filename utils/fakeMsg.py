import uuid
from datetime import datetime
import urllib2
import urllib


def make_request(msg, phone="18182124554",
                 url="http://localhost:6543/interface/send/3"):

    data = urllib.urlencode({"message": msg,
                             "number": phone,
                             "uuid": str(uuid.uuid4())})
    return urllib2.Request(
        data=data, url=url)


def test_consumer_messages():
    account = "iwn578"
    token = 38902754073

    response = urllib2.urlopen(make_request("bal." + account))
    print("----------------------------")
    print("testing english balance")
    print(response.read())
    print("-----------------------------")

    # response = urllib2.urlopen(make_request("bal.1234"))
    # print("----------------------------")
    # print("testing english balance fail conition")
    # print(response.read())
    # print("-----------------------------")

    # response = urllib2.urlopen(make_request("solde." + account))
    # print("----------------------------")
    # print("testing french balance") 
    # print(response.read())
    # print("----------------------------") 

    # response = urllib2.urlopen(make_request("solde.12345")) 
    # print("----------------------------") 
    # print("testing french balance fail conition") 
    # print(response.read())
    # print("----------------------------") 

    # response = urllib2.urlopen(make_request("prim." + account + ".18182124554"))
    # print("----------------------------") 
    # print("set primary number english") 
    # print(response.read())
    # print("----------------------------") 

    # response = urllib2.urlopen(make_request("tel." + account +  ".18185846103")) 
    # print("----------------------------") 
    # print("set primary number fr") 
    # print(response.read())
    # print("----------------------------") 

    # response = urllib2.urlopen(
    #     make_request("add." + account + "." + str(token))) 
    # print("----------------------------") 
    # print("add credit in en") 
    # print(response.read())
    # print("----------------------------") 

    # response = urllib2.urlopen(
    #     make_request("recharge." + account  +"." + str(token))) 
    # print("----------------------------") 
    # print("add credit in fr") 
    # print(response.read())
    # print("----------------------------") 

    # response = urllib2.urlopen(make_request("on." + account)) 
    # print("----------------------------") 
    # print("turn the circuit on fr/en ") 
    # print(response.read())
    # print("----------------------------") 

    # response = urllib2.urlopen(make_request("off." + account)) 
    # print("----------------------------") 
    # print("turn the circuit off fr/en ") 
    # print(response.read())
    # print("----------------------------") 

    # response = urllib2.urlopen(make_request("use." + account)) 
    # print("----------------------------") 
    # print("testing use en") 
    # print(response.read())
    # print("----------------------------") 

    # response = urllib2.urlopen(make_request("conso." + account)) 
    # print("----------------------------") 
    # print("testing use fr") 
    # print(response.read())
    # print("----------------------------") 


    # response = urllib2.urlopen(make_request("this should fail" + account)) 
    # print("----------------------------") 
    # print("test failure with a response") 
    # print(response.read())
    # print("----------------------------") 


def test_meter_messages():
    cid = "192.168.1.201"
    meter_name = "demo001"

    response = urllib2.urlopen(
        make_request("(job=pp&cid=" + cid + "&mid=" + meter_name + "&wh=10.00&tu=12.12&ts=201101120&cr=20.10&status=1)", phone='+22365489009'))
    print("----------------------------") 
    print("testing primary log") 
    print(response.read())
    print("----------------------------") 

    # newLogs = '(l6K0AQ|0,5YI,RC,0;1,3I,1,12KM;2,5WR,4G,R94;3,0,0,Z00;4,0,0,YD3;5,0,0,M12;6,0,0,UPP;7,55L,9,PKA;8,0,0,45L;9,0,0,TV;A,23,1,KEB;B,0,0,XYS;C,9,0,JDI|)'

    # response = urllib2.urlopen(
    #     make_request(newLogs, 
    #                  phone='+22365489009'))
    # print("------------------------------")
    # print(response.read())
    # print("------------------------------")

    # response = urllib2.urlopen(
    #     make_request("(job=delete&status=1&tu=2256&ts=20110107192318&wh=9.7&cr=475.95&jobid=90&ct=CIRCUIT)",phone="13474594669"))
    # print("----------------------------") 
    # print("testing primary log") 
    # print(response.read())
    # print("----------------------------") 


    # response = urllib2.urlopen(
    #     make_request("(job=alerts&mid=" + 
    #                  meter_name + "&cid=" + cid + "&alert=md)",phone="18185846103")) 
    # print("----------------------------") 
    # print("testing alert meter down") 
    # print(response.read())
    # print("----------------------------") 
    # # test meter sd card not found 
    # response = urllib2.urlopen(
    #     make_request("(job=alerts&mid=" + 
    #                  meter_name + "&cid=" + cid + "&alert=sdc)",phone="18185846103")) 
    # print("----------------------------") 
    # print("testing alert test meter sd card not found") 
    # print(response.read())
    # print("----------------------------") 
    # # test circuit low credit
    # response = urllib2.urlopen(
    #     make_request("(job=alerts&mid=" + 
    #                  meter_name + "&cid=" + cid 
    #                  + "&alert=lcw&cr=10.00)",phone="18185846103")) 
    # print("----------------------------") 
    # print("testing alert low credit") 
    # print(response.read())
    # print("----------------------------") 

    # # test circuit no credit 
    # response = urllib2.urlopen(
    #     make_request("(job=alerts&mid=" 
    #                  + meter_name + "&cid=" 
    #                  + cid + "&alert=nocw&cr=00.00)",phone="18185846103")) 
    # print("----------------------------") 
    # print("testing alert no credit") 
    # print(response.read())
    # print("----------------------------") 
    # # test circuit compontent failure 
    # response = urllib2.urlopen(
    #     make_request("(job=alerts&mid=" 
    #                  + meter_name + "&cid=" + cid + "&alert=ce)",phone="18185846103")) 
    # print("----------------------------") 
    # print("testing alert ce") 
    # print(response.read())
    # print("----------------------------") 

def test_twilio():
    data = urllib.urlencode({"Body": '1.bzm486',
                             "From": '18182124554',
                             "SmsMessageSid": str(uuid.uuid4())})
    response = urllib2.urlopen(
        data=data,
        url='http://localhost:6543/twilio/send')
    print(response.read())


#test_consumer_messages()
#test_meter_messages()
test_twilio()
