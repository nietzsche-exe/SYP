from fastapi import FastAPI
import pandas as pd
import requests
import json
import uvicorn

app = FastAPI()

@app.get("/{municipio}")
def get_prediccion(municipio: str):
    codMunicipio = get_codMunicipio(municipio)
    prediccion = json.loads(llamadas(codMunicipio).text)
    return imprimirDatos(prediccion)

def get_codMunicipio(municipio: str):
    
    dtype = {
        1: str,  # Segunda columna
        2: str   # Tercera columna
    }

    archivo_excel = "20codmun.xlsx"

    df = pd.read_excel(archivo_excel, dtype=dtype)

    datos_filtrados = df[df.iloc[:, 4] == municipio]

    segunda_columna = str(datos_filtrados.iloc[0, 1]).zfill(2)
    tercera_columna = str(datos_filtrados.iloc[0, 2]).zfill(3)

    codMunicipio =  segunda_columna + tercera_columna
    
    return codMunicipio

def llamadas(codMunicipio: str):
    
    baseUrl = "https://opendata.aemet.es/opendata"
   
    endpoint = "/api/prediccion/especifica/municipio/horaria/"
    apikey = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJtZS5sbGFtby5qanVsaWFuQGdtYWlsLmNvbSIsImp0aSI6IjZlMjQ4ZDk2LWU1ZDYtNDg2YS1iMWJkLTlhNDU3MTc2ZGIwYSIsImlzcyI6IkFFTUVUIiwiaWF0IjoxNzA2NzkxNDM0LCJ1c2VySWQiOiI2ZTI0OGQ5Ni1lNWQ2LTQ4NmEtYjFiZC05YTQ1NzE3NmRiMGEiLCJyb2xlIjoiIn0.ZYN9g2-AVBQtfbxFph0z9n66MnuZLgAXLrC_6PTUyy0"
    
    authString = {"api_key": apikey}
   
    url =  baseUrl + endpoint + codMunicipio
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

def imprimirDatos(data):
    
    resultado = {}
    try:
        municipio = data[0]['nombre']
        provincia = data[0]['provincia']
        prediccion_horas = data[0]['prediccion']['dia'][0]

        resultado["Municipio"] = municipio
        resultado["Provincia"] = provincia
        resultado["EstadoCielo"] = [hora['descripcion'] for hora in prediccion_horas['estadoCielo'][:6]]
        resultado["Temperatura"] = [hora['value'] for hora in prediccion_horas['temperatura'][:6]]
        resultado["Precipitacion"] = [hora['value'] for hora in prediccion_horas['precipitacion'][:6]]
        resultado["VientoAndRachaMax"] = [{"periodo": hora['periodo'], "direccion": hora.get("direccion", "No disponible"), "velocidad": hora.get("velocidad", "No disponible")} for hora in prediccion_horas['vientoAndRachaMax'][:6]]

    except Exception as e:
        resultado = {"error": str(e)}

    if(municipio == "Murcia"):
        return "Murcia no exite"
    else:
        return resultado
        
@app.get("/")
async def root():
    return {"message": "Bienvenido a la API de Predicción del Tiempo"}        
        
if __name__ == "__main__":
 
  uvicorn.run(app, host="192.168.200.188", port=8000)

    
            


    









