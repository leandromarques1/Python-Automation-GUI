#Habilitar API do Google Shhets na Conta

#passo 1: entrar no link: https://console.cloud.google.com/
#passo 2: clicar em "Selecione um Projeto" --> "Novo Projeto"
# Passo 3: escrever "Nome de Projeto" / "Organização" / (se for na conta da empresa, definir "Local")

#necessário ativar duas APIs: API do Google Drive e API do Google Sheets
#Passo 4: digitar na barra de buscas "Google Drive API" --> Clicar em "Ativar"
#Passo 5: digitar na barra de buscas "Google Sheets API" --> Clicar em "Ativar"



#Ativar Tokens de Autenticação
#passo 1: barra lateral --> "APIs e Serviços" --> "APIs e Serviços ativados"
# passo 2: Clicar em "Tela de Permissão OAuth" 
#   passo 2.1: Se for a primeira vez acessando: 
#              USER TYPE - Escolher entre uso "Interno" e "Externo"
#              (mas se você NÃO estiver usando conta de Empresa, só poderá usar Externo)

#Passo 3: preencher informações do App
#Passo 5: Escopos
#Passo 5: Usuários de Teste: (+add users) adicionar email e todos os usuarios que você quer que usem a aplicação

#Gerar credenciais
#Passo 1: barra Lateral --> clicar em "Credenciais"
#Passo 2: clicar em "+create credentials" --> "ID do cliente OAuth"
# Passo 3: na barra de opções, colocar o "Tipo do Aplicativo" --> "App para computador"
# Passo 4: "Nome"
# Passo 5: na linha "IDs do cliente OAuth 2.0" fazer download das credenciais --> "Fazer download do JSON"
# Passo 6: mudar o nome desse arquivo baixado para "credentials.json"
# Passo 7: colcoar esse arquivo "credentials.json" no mesmo local onde tem o código python que será trabalhado

#Baixando a biblioteca das APIs do Google
# passo 1: instalar biblioteca com a linha de comando
#   pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib



from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']   #assim fica com acesso global

# The ID and range of a sample spreadsheet.
#ID da planilha do Sheets (aparece logo após o "/d/" na URL)
SAMPLE_SPREADSHEET_ID = '1EpgNyLsRiRPpy84OZuO4N5aavS1PDJfGTPXp6Ithv8A'

#Intervalo de células para editar (formato: 'nome_da_aba!celula_inicial:celula_final)
SAMPLE_RANGE_NAME = 'Página1!A1:B12'


def main():
    #-------------------------------#
    #Essa parte é para fazer LOGIN
    #LOGIN na API do Google funciona por meio de Token de Autenticação 
    # (usa as credenciais que foram baixadas)
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    #-------------------------------#
    #Executar ação dentro da planilha
    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        #Ler informaçãoes do Google Sheets --> requisição GET
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME).execute()

        #adicionar/editar informações --> requisição UPDATE
        valores_adicionar = [
            ["dezembro", 'R$ 127.300,15'],
            ["Janeiro", "R$ 110.000,00"]
        ]
        result = sheet.values().update(
                                spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range="A13",  #qual célula quero acrescentar informação 
                                valueInputOption="USER_ENTERED",
                                body={'values': valores_adicionar}
                                ).execute()

#        values = result.get('values', [])
#
#        if not values:
#            print('No data found.')
#            return
#
#        print('Name, Major:')
#        for row in values:
#            # Print columns A and E, which correspond to indices 0 and 4.
#            print('%s, %s' % (row[0], row[4]))
    except HttpError as err:
        print(err)


if __name__ == '__main__':
    main()