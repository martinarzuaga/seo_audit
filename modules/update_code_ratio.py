
def update_code_ratio(data, wks_velocidad):
    """Update the html, css, js and font code ratio.

    Args:
        data (list): the result from get_urls. JSON response in a list format
        wks_velocidad (_type_): the worksheet where will be updated.
    """
   
    
    for i in range(len(data)):
    
        html_bytes = int(data[i][1]['data']['median']['firstView']['breakdown']['html']['bytes'])
        css_bytes = int(data[i][1]['data']['median']['firstView']['breakdown']['css']['bytes'])
        js_bytes = int(data[i][1]['data']['median']['firstView']['breakdown']['js']['bytes'])
        img_bytes = int(data[i][1]['data']['median']['firstView']['breakdown']['image']['bytes'])
        font_bytes = int(data[i][1]['data']['median']['firstView']['breakdown']['font']['bytes'])
        total_bytes = html_bytes + css_bytes + js_bytes + font_bytes + img_bytes
        
    
        html_ratio = round((html_bytes * 100) / total_bytes, 2) / 100
        css_ratio = round((css_bytes * 100) / total_bytes, 2) / 100
        js_ratio = round((js_bytes * 100) / total_bytes, 2) / 100
        img_ratio = round((img_bytes * 100) / total_bytes, 2) / 100
        font_ratio = round((font_bytes * 100) / total_bytes, 2) / 100
        
        wks_velocidad.update_value(f'F{i+2}', html_ratio)
        wks_velocidad.update_value(f'G{i+2}', css_ratio)
        wks_velocidad.update_value(f'H{i+2}', js_ratio)
        wks_velocidad.update_value(f'I{i+2}', img_ratio)
        wks_velocidad.update_value(f'J{i+2}', font_ratio)
    
    print('Code Ratio Updated')

