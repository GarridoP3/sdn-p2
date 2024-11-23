import requests
import csv

url = "https://api.meraki.com/api/v1/organizations/{organizationId}/devices"

headers = {
    "Authorization": "Bearer 75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6",
    "Accept": "application/json"
}

# dashboard = meraki.DashboardAPI(KEY)
# id = '1215707'
# devices = dashboard.organizations.getOrganizationDevices(id, total_pages='all')

device = requests.request('GET', url, headers=headers,)

print(devices)

with open('inventario.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    
    #Encabezado
    writer.writerow(['model' , 'name' , 'mac' , 'serial', 'productType', 'publicIp', 'lanIp', 'status' ])

    for device in devices:
        if device.get('productType') == 'appliance' or device.get('productType') == 'wireless':
            writer.writerow([
                device.get('model', ''),
                device.get('name', ''),
                device.get('mac', ''),
                device.get('serial', ''),
                device.get('publicIp', ''),
                device.get('lanIp', ''),
                device.get('status', '')
            ])
        
print('Done')