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
print ("Na lista abaixo, pode encontrar as networks disponíveis para sua Organização: ")

#Requesting the Network list
responseNet = requests.get(url=netIdUrl, headers=headers)
responseNetJson = json.loads(responseNet.content)

#Parsing the Network Name
for listNetwork in responseNetJson:
    print(listNetwork['name'])

#Information
storeName = input("Qual loja deseja fazer a migração? ")

#Parsing desirable fields and saving to file.
for network in responseNetJson:
     if storeName == network['name']:
        netId = network['id']
        netName = network['name']
        print ("Será gerado o arquivo para a loja: " + netName)
        if network['type'] in ('combined') or ('appliance'):
            try:
                vlanUrl = mainUrl + "/networks/{}/vlans".format(netId)
                responseVlans = requests.get(url=vlanUrl, headers=headers)
                responseVlansJson = json.loads(responseVlans.content)
                tofile = []
                with open(netName + ".json", "a") as f:
                    for vlans in responseVlansJson:
                        vlanId = str(vlans['id'])
                        tofile.append({
                                        "id": vlanId,
                                        "name": vlans['name'],
                                        "subnet": vlans['subnet'],
                                        "applianceIp": vlans['applianceIp']
                        })
                    json.dump(tofile, f, indent=4, ensure_ascii=False)
                f.close()
                print("Arquivo salvo com sucesso!")          
            except:
                print("Não temos VLANs habilitadas na loja: " + netName)
        else:
            print ("Primeiro habilite as VLANs para essa loja.")
     
        