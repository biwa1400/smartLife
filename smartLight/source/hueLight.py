import requests
import json
class Light():
	#define control_method_url command
	LIGHT_STATE_GET='/lights/LIGHT_NUM'
	LIGHT_STATE_CONFIG = '/lights/LIGHT_NUM/state'
	
	def __init__(self,ip_addr,light_num,username):
		self.ip_addr = ip_addr
		self.username = username
		self.light_num = light_num
	
	# replace LIGHT_NUM in control_method_url
	def method_URL(self,definedString):
		return definedString.replace('LIGHT_NUM',str(self.light_num))
	
	# request to Hue Bridge 
	# request_method: PUT,GET
	# control_method_url: method_URL(define control_method_url command)
	# json_send: jsonDict
	def commmunication (self,request_method,control_method_url='',json_send=None):
		url = 'http://'+self.ip_addr+'/api/'+self.username+control_method_url 
		if request_method == "PUT":
			if json_send != None:
				jsonString = json.dumps(json_send)
				r = requests.put(url,data = jsonString)
			else:
				r = requests.put(url)
			return r
		elif request_method == "GET":
			r = requests.get(url)
			return r

# public method			
	def state(self):
		return self.commmunication ('GET',self.method_URL(Light.LIGHT_STATE_GET))
	
	def turnOn(self):
		json_send= {"on" :True}
		return self.commmunication ('PUT',self.method_URL(Light.LIGHT_STATE_CONFIG),json_send)
		
	def turnOff(self):
		json_send= {"on" : False}
		return self.commmunication ('PUT',self.method_URL(Light.LIGHT_STATE_CONFIG),json_send)
		
	def sat(self,value):
		json_send= {"sat" : value}
		return self.commmunication ('PUT',self.method_URL(Light.LIGHT_STATE_CONFIG),json_send)
	
	def bri(self,value):
		json_send= {"bri" : value}
		return self.commmunication ('PUT',self.method_URL(Light.LIGHT_STATE_CONFIG),json_send)
		
	def hue(self,value):
		json_send= {"hue" : value}
		return self.commmunication ('PUT',self.method_URL(Light.LIGHT_STATE_CONFIG),json_send)
		
	def color(self,hue,sat,bri):
		json_send= {"hue" : hue,"sat" : sat,"bri" : bri}
		return self.commmunication ('PUT',self.method_URL(Light.LIGHT_STATE_CONFIG),json_send)
		
			
if __name__ == "__main__":
	import sys
	light_test = Light('192.168.0.100',1,'N-ooTd-KQ6oRls3zAF9S2jG4DLJsonrgaccR4eqQ')
	method = getattr(light_test,sys.argv[1][1:])
	if len(sys.argv) == 3:
		parameter = int(sys.argv[2])
		print(method(parameter).text)
	elif len(sys.argv) == 5:
		para1=int(sys.argv[2])
		para2=int(sys.argv[3])
		para3=int(sys.argv[4])
		print(method(para1,para2,para3).text)
	else:
		print(method().text)
		
		