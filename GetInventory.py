import requests
import csv

url = "https://api.meraki.com/api/v1/organizations/1215707/devices"

headers = {
    "Authorization": "Bearer 75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6",
    "Accept": "application/json"
}

# dashboard = meraki.DashboardAPI(KEY)
# id = '1215707'
# devices = dashboard.organizations.getOrganizationDevices(id, total_pages='all')

response = requests.request('GET', url, headers=headers)
devices = response.json()
excepcion = response.raise_for_status() #En caso de error, genera una excepción

print('¿Ocurrió un error?', excepcion)

#print(devices)

with open('inventario.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    
    #Encabezado
    writer.writerow(['model' , 'name' , 'mac' , 'serial', 'productType', 'publicIp', 'lanIp', 'status', 'productType' ])

    #Dispositivos
    for device in devices:
        if device.get('productType') == 'appliance' or device.get('productType') == 'wireless':
            writer.writerow([
                device.get('model', ''),
                device.get('name', ''),
                device.get('mac', ''),
                device.get('serial', ''),
                device.get('publicIp', ''),
                device.get('lanIp', ''),
                device.get('status', ''),
                device.get('productType', ''),
            ])
        
print('Done')