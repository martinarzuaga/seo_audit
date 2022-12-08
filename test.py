# import json
# import pygsheets

# # f = open('./jsonResult.json')

# # data = json.load(f)

# # def update_code_ratio(data, wks_velocidad):
# #     """Update the html, css, js and font code ratio.

# #     Args:
# #         data (list): the result from get_urls. JSON response in a list format
# #         wks_velocidad (_type_): the worksheet where will be updated.
# #     """
   
    
# #     for i in range(len(data)):
    
# #         html_bytes = int(data[i][1]['data']['median']['firstView']['breakdown']['html']['bytes'])
# #         css_bytes = int(data[i][1]['data']['median']['firstView']['breakdown']['css']['bytes'])
# #         js_bytes = int(data[i][1]['data']['median']['firstView']['breakdown']['js']['bytes'])
# #         img_bytes = int(data[i][1]['data']['median']['firstView']['breakdown']['image']['bytes'])
# #         font_bytes = int(data[i][1]['data']['median']['firstView']['breakdown']['font']['bytes'])
# #         total_bytes = html_bytes + css_bytes + js_bytes + font_bytes + img_bytes
        
    
# #         html_ratio = (html_bytes * 100) / total_bytes
# #         css_ratio = (css_bytes * 100) / total_bytes 
# #         js_ratio = (js_bytes * 100) / total_bytes
# #         img_ratio = (img_bytes * 100) / total_bytes 
# #         font_ratio = (font_bytes * 100) / total_bytes
        
# #         wks_velocidad.update_value(f'F{i+2}', html_ratio)
# #         wks_velocidad.update_value(f'G{i+2}', css_ratio)
# #         wks_velocidad.update_value(f'H{i+2}', js_ratio)
# #         wks_velocidad.update_value(f'H{i+2}', img_ratio)
# #         wks_velocidad.update_value(f'I{i+2}', font_ratio)


# # Login to Google Sheets
# gc = pygsheets.authorize(client_secret='./credentials/client_secret.json')

# # open the Google spreadsheet and save all the sheets
# sh = gc.open('Copia de Auditoria-SEO-Simplebox')

# # save all the workseets in variables
# wks_velocidad = sh.worksheet('title', 'Velocidad')

# html_ratio = round(1.161651139906327, 2)

# html_ratio = html_ratio / 100

# wks_velocidad.update_value('F2', html_ratio)

f = open('./cliente.txt', 'r')

configuration = f.readlines()

print(configuration)

print(type(configuration))

client_name = configuration[0].replace('\n', '')
location = configuration[1].replace('\n', '')

print(client_name)
print(location)
