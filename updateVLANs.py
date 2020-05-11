#Importing required modules
import requests
import json
from config import *

#Main Meraki URL API
mainUrl = "https://api.meraki.com/api/v0"

#URL to get the Network ID
netIdUrl = mainUrl + "/organizations/{}/networks".format(orgId)

#Creating Headers
headers = {
  'Content-Type': 'application/json',
  'X-Cisco-Meraki-API-Key': apiKey
}

#Information
storeName = input("Qual loja deseja fazer a migração? ")

#Check if the file exists
try:
  with open(storeName + ".json", "r") as openfile:
      vlansFromfile = json.loads(openfile.read())
except:
  print ("Nenhum arquivo encontrado com o nome: " + storeName + ". Execute o script getVLANs primeiro.")
  exit()

#Requesting the Network list
responseNet = requests.get(url=netIdUrl, headers=headers)
responseNetJson = json.loads(responseNet.content)

#Translating the Network Name to Network ID
for storeId in responseNetJson:
  if storeId['name'] == storeName:
    #print (storeId['id'])
    trUrl = mainUrl + "/networks/{}/vlans/".format(storeId['id'])

#Updating the VLANs
for vlansToUpdate in vlansFromfile:
    body = { "id": vlansToUpdate ['id'],
      "name": vlansToUpdate ['name'],
      "subnet": vlansToUpdate ['subnet'],
      "applianceIp": vlansToUpdate ['applianceIp']
    }
    bodyJson = json.dumps(body)
    #print (bodyJson)
    updateUrl = trUrl + vlansToUpdate['id']
    #print (updateUrl)
    responseUpdate = requests.put(url=updateUrl, headers=headers, data=bodyJson)
    if responseUpdate.status_code == 200:
      print ("VLAN " + vlansToUpdate['name'] + " atualizada com sucesso!")
    else:
      print ("Falha ao atualizar a VLAN: " + vlansToUpdate['name'])
    #print (responseUpdate.status_code)
  


