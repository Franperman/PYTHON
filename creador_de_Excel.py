import pandas as pd

# Datos de ejemplo
datos = {
    'Empresa': ['PUERTAS ROPER', 'CAPWAY SYSTEMS', 'Baker Perkins', 'Fluinox Procesos S.L.', "ARM Robotics Group", "Element Logic", 
                "INGENERSUN", "Aritex", "EDS Robotics", "CYO Ingenieria", "Sadako Technologies", "Lely"],
    'Email': ['roper@roper.es', 'parts@capwayautomation.com', 'bpinc@bakerperkins.com', 'fluinox@fluinox.com', "comercial@armroboticsgroup.com", 
            "info@elementlogic.es", "ingenersun@ingenersun.com", "comercial@loxin2002.com", "rrhh@edsrobotics.com", "info@ingenieriacyo.com", 
            "info@sadako.es", "elelij@lely.com"],
    "Ubicación": ["Revilla de Camargo, Cantabria", "YORK, Pennsylvania, EEUU", "Peterborough, Cambs, United Kingdom", 
                "Valencia", "Barakaldo, Pais Vasco", "Barcelona, Cataluña. Sede: Noruega", "Zamudio, Bizkaia, Pais Vasco", 
                "Barcelona, Cataluña. Sede: Turquía", "Aspe, Alicante", "Zaragoza, Aragón", "L'Hospitalet de LLobregat, Barcelona", 
                "Avila. sede: Paises bajos"],
    "Enlace a LinkedIn": ["https://www.linkedin.com/company/puertas-roper/", "https://www.linkedin.com/company/capway-systems-inc./about/", 
                        "https://www.linkedin.com/company/baker-perkins/", "https://www.linkedin.com/company/fluinox-procesos-sl/about/", 
                        "https://www.linkedin.com/company/arm-robotics-group/about/", "https://www.linkedin.com/company/element-logic/", 
                        "https://www.linkedin.com/company/ingenersun-s-l-/", "https://www.linkedin.com/company/aritex/", None, 
                        "https://www.linkedin.com/company/cyo-ingenieria/", "https://www.linkedin.com/company/sadako-technologies/", 
                        "https://www.linkedin.com/company/lely-industries-nv/"],
    "Sitio web": ["https://www.puertasroper.com", "http://capwayusa.com", "http://www.bakerperkins.com", "http://fluinox.com", 
                "Teléfono 944180035", "https://www.elementlogic.net", "https://www.ingenersun.com", "http://www.aritex-es.com", 
                "https://www.edsrobotics.com/", "http://www.ingenieriacyo.com/", "http://www.sadako.es", "https://www.lely.com/"]}

# Crear un DataFrame a partir de los datos
df = pd.DataFrame(datos)

# Especifica la ruta completa donde deseas que se cree el archivo
ruta_archivo = 'C:/Nueva carpeta/empresas_email.xlsx'

# Escribir el DataFrame en un archivo XLS
df.to_excel(ruta_archivo, index=False)

print('Se ha creado el archivo con éxito.')
