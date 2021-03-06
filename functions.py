import xlrd
import requests
import json

#formatar o esquema de datas para ser aceito pela API
def formatarData(t, wb):
  if len(str(t)) != 0:
    r = xlrd.xldate_as_tuple(t, wb.datemode)
    return str(r[0])+"-"+str(r[1])+"-"+str(r[2])+"T03:00:00Z"
  else:
    return ""

#preenchendo os valores 
def setDados(data, workbook, name, type_, registration, driverTeam_id, rg, cpf, status, hiringType, riskDriver, integrationId, licenseCategory, licenseExpedition, licenseExpiration, licenseRegister, registrationCode):
    data['name'] = name
    data['type'] = type_
    data['registration'] = str(int(registration))
    data['driverTeam']['id'] = driverTeam_id
    data['rg'] = str(int(rg))
    data['cpf'] = str(int(cpf))
    data['status'] = status
    data['hiringType'] = hiringType
    data['riskDriver'] = int(riskDriver)
    data['integrationId'] = str(int(integrationId))
    data['licenseCategory'] = licenseCategory
    data['licenseExpedition'] = formatarData(licenseExpedition, workbook)
    data['licenseExpiration'] = formatarData(licenseExpiration, workbook)
    data['licenseRegister'] = licenseRegister
    data['registrationCode'] = registrationCode
    if data['licenseExpedition'] == '':
        data.pop('licenseExpedition')
    if data['licenseExpiration'] == '':
        data.pop('licenseExpiration')
    if data['registrationCode'] == '':
        data.pop('registrationCode')
    if data['licenseRegister'] == '':
        data.pop('licenseRegister')
    return data

#faz request para cadastrar o condutor
def cadastrarDriver(data):
  base_url = "http://demo.trixlog.com/trix/"
  auth = ('carloseduardo@teste', 'carloseduardo@teste')

  x = requests.post(base_url+'driver', headers={'Content-Type': 'application/json'}, json=data, auth=auth)
  return x

# def salvarCadastrado(condutor):
#   print(condutor)
#   f = open('condutor.txt', 'w')
#   f.write(condutor+"\n")
#   f.close()

def deletarCadastrado(c):
  base_url = "http://demo.trixlog.com/trix/"
  auth = ('carloseduardo@teste', 'carloseduardo@teste')
  print(base_url+'driver/'+str(c))
  x = requests.delete(base_url+'driver/'+str(c), auth=auth)
  return x