import meraki

KEY = '75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6'

dashboard = meraki.DashboardAPI(KEY)
response = dashboard.organizations.getOrganizations()

print(response)