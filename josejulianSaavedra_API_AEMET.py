import pandas as pd
import requests
import json

def get_codMunicipio():
    
    dtype = {
        1: str,  # Segunda columna
        2: str   # Tercera columna
    }

    archivo_excel = "20codmun.xlsx"

    df = pd.read_excel(archivo_excel, dtype=dtype)

    quinta_columna_valor = input("introduce un municipio: ")
    if quinta_columna_valor == "Murcia":
        print()
        print("Que buscas? Murcia no existe...")
        print()
        exit(0)

    datos_filtrados = df[df.iloc[:, 4] == quinta_columna_valor]

    segunda_columna = str(datos_filtrados.iloc[0, 1]).zfill(2)
    tercera_columna = str(datos_filtrados.iloc[0, 2]).zfill(3)

    codMunicipio =  segunda_columna + tercera_columna
    
    return codMunicipio

def primeraLlamada():
    
    baseUrl = "https://opendata.aemet.es/opendata"
    municipio = get_codMunicipio()
    endpoint = "/api/prediccion/especifica/municipio/horaria/"
    apikey = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJtZS5sbGFtby5qanVsaWFuQGdtYWlsLmNvbSIsImp0aSI6IjZlMjQ4ZDk2LWU1ZDYtNDg2YS1iMWJkLTlhNDU3MTc2ZGIwYSIsImlzcyI6IkFFTUVUIiwiaWF0IjoxNzA2NzkxNDM0LCJ1c2VySWQiOiI2ZTI0OGQ5Ni1lNWQ2LTQ4NmEtYjFiZC05YTQ1NzE3NmRiMGEiLCJyb2xlIjoiIn0.ZYN9g2-AVBQtfbxFph0z9n66MnuZLgAXLrC_6PTUyy0"
    
    authString = {"api_key": apikey}
   
    url =  baseUrl + endpoint + municipio
    response = requests.get(url, params=authString)

    if response.status_code != 200 :
        print("Error en la llamada")
        print(response.text)
        print(response.reason)
        return None
    else:
        try:
            jsData = response.json()
            urlToCall = jsData['datos']
            prediccion = requests.get(urlToCall)
            return prediccion
        except:
            print("Respuesta no es JSON")
            print(response.text)
            return None

def imprimirDatos():
    
    data = json.loads(primeraLlamada().text)
    
    municipio = data[0]['nombre']
    provincia = data[0]['provincia']
    prediccion_horas = data[0]['prediccion']['dia'][0]

    print("Municipio:", municipio)
    print("Provincia: ", provincia)
    
    for hora in prediccion_horas['estadoCielo'][:6]:
        print("Hora:", hora['periodo'])
        print("Estado del cielo:", hora['descripcion'])
        print()

    for hora in prediccion_horas['temperatura'][:6]:
        print("Hora:", hora['periodo'])
        print("Temperatura:", hora['value'])
        print()

    for hora in prediccion_horas['precipitacion'][:6]:
        print("Hora:", hora['periodo'])
        print("Precipitación:", hora['value'])
        print()
        
    for hora in prediccion_horas['vientoAndRachaMax'][:6]:
        print("Hora:", hora['periodo'])
        if 'direccion' in hora:
            print("Dirección del viento:", hora['direccion'][0])
        else:
            print("Dirección del viento: No disponible")
        
        if 'velocidad' in hora:
            print("Velocidad del viento:", hora['velocidad'][0])
        else:
            print("Velocidad del viento: No disponible")
        print()
        
if __name__ == "__main__":
 
  imprimirDatos()

    
            


    









