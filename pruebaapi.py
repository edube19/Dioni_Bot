import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

SPREADSHEET_ID ="10E8p8wXZl85mzL5q2yb62m4TAjJq1iXSTa3l9PC1zqw"

def main():
    credenciales =None
    if os.path.exists("token.json"):
        credenciales = Credentials.from_authorized_user_file("token.json",SCOPES)
    if not credenciales or not credenciales.valid:
        if credenciales and credenciales.expired and credenciales.refresh_token:
            credenciales.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credenciales.json",SCOPES)
            credenciales = flow.run_local_server(port=0)
        with open("token.json","w") as token:
            token.write(credenciales.to_json())
    try:
        service = build("sheets","v4", credentials=credenciales)
        sheets = service.spreadsheets()
        #leer datos de la hoja

        '''result = sheets.values().get(spreadsheetId =SPREADSHEET_ID, range = "hoja1!A1:D4").execute()

        values = result.get("values",[])
        
        for row in values:
            print(row)'''
        
        #escribir datos en la hoja
        nombres = ['eduardo','cecilia','Isabel']
        edad = [26,50,11]
        oficio = ['egresado','ama de casa','escolar']
        lista_combinada = []

        for i in range(len(nombres)):
            elemento_combinado = [nombres[i], edad[i], oficio[i]]
            lista_combinada.append(elemento_combinado)
        

        for row in range(1,6):
            num1 = int(sheets.values().get(spreadsheetId =SPREADSHEET_ID, range = f"pruebas!A{row}").execute().get("values")[0][0])
            num2 = int(sheets.values().get(spreadsheetId =SPREADSHEET_ID, range = f"pruebas!B{row}").execute().get("values")[0][0])
            resultado = num1+num2
            print(f'Procesando {num1} + {num2}')

            sheets.values().update(spreadsheetId =SPREADSHEET_ID, range = f"pruebas!C{row}",
                                   valueInputOption = "USER_ENTERED",
                                   body ={"values":[[f'{resultado}']]}).execute()
            
            sheets.values().update(spreadsheetId =SPREADSHEET_ID, range = f"pruebas!D{row}",
                                   valueInputOption = "USER_ENTERED",
                                   body ={"values":[["REALIZADO"]]}).execute()
            
            #########
        j=0
        for row in range(7,10):
            
            valor_nombre = str(lista_combinada[j][0])
            valor_edad = int(lista_combinada[j][1])
            valor_oficio = str(lista_combinada[j][2])
            sheets.values().update(spreadsheetId =SPREADSHEET_ID, range = f"pruebas!A{row}",
                                   valueInputOption = "USER_ENTERED",
                                   body ={"values":[[f'{valor_nombre}']]}).execute()
            
            sheets.values().update(spreadsheetId =SPREADSHEET_ID, range = f"pruebas!B{row}",
                                   valueInputOption = "USER_ENTERED",
                                   body ={"values":[[f'{valor_edad}']]}).execute()
            
            sheets.values().update(spreadsheetId =SPREADSHEET_ID, range = f"pruebas!C{row}",
                                   valueInputOption = "USER_ENTERED",
                                   body ={"values":[[f'{valor_oficio}']]}).execute()
            j=j+1

    except HttpError as e:
        print("error: ",e)

if __name__ == "__main__":
    main()