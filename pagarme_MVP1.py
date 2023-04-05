import pyautogui  #Ferramenta de automação (Python assume controle do seu teclado por exemplo);
import time       #Facilita no desenvolvimento de códigos que envolvem tempo, tempo de espera etc...
import pyperclip  #Permite copiar e colar via Python

#Tempo de pausa entre a execução de certas partes do codigo
tempo_pausa = 5     #medido em Segundos

#biblioteca "pyautogui" nos permite criar um código que simula que estamos usando o computador
#"autogui" --> Automatização da GUI (interface gráfica de usuário)
pyautogui.PAUSE = 1
pyautogui.press("winleft")
pyautogui.write("chrome")
pyautogui.press("enter")
#pyautogui.alert("Vai começar, aperte OK e não mexa em nada") #cria um alerta na tela do computador
pyautogui.hotkey('ctrl','t')  #executa um atalho

#===== Abrir Site =====#
#ensinar aqui o "write"
link = "https://beta.dashboard.pagar.me/#/account/login"
pyperclip.copy(link)    #equivalente ao "CTRL+C"
pyautogui.hotkey("ctrl","v")    #executa um atalho
pyautogui.press("enter")    #apertar "ENTER"
time.sleep(tempo_pausa)  #tempo em SEGUNDOS necessário para esperar antes de ir para a próxima linha do código

#===== Colocar dados de Acesso (Email e Senha)=====#
#Colocar email
pyautogui.click(955,471, clicks=1)

email = "anderson.leandro@agendaedu.com"
pyperclip.copy(email)
pyautogui.hotkey("ctrl","v")    #executa um atalho
pyautogui.press("enter")    #apertar "ENTER"
time.sleep(tempo_pausa)

#colocar senha
pyautogui.click(955,531, clicks=1)

senha = "Nick2@@9"
pyperclip.copy(senha)
pyautogui.hotkey("ctrl","v")    #executa um atalho
pyautogui.press("enter")    #apertar "ENTER"
time.sleep(tempo_pausa)

#Ir em RECEBEDORES
pyautogui.click(82,404, clicks=1)

#Digitar “fm securitizadora” na caixa de busca
pyautogui.click(905,230, clicks=1)
pyperclip.copy("fm securitizadora")
pyautogui.hotkey("ctrl","v")    #executa um atalho
pyautogui.press("enter")

#Clicar em Filtro
pyautogui.click(1831,494, clicks=1)
#Clicar em VER DETALHES
pyautogui.click(1764,576, clicks=1)

#esperar carregar (aguardar 15 seg)
time.sleep(10)

#ir em Periodo
pyautogui.click(979,921, clicks=1)
pyautogui.hotkey("ctrl","a") 
periodo = "01/01/2022"
pyperclip.copy(periodo)
pyautogui.hotkey("ctrl","v") 
pyautogui.click(1194,917, clicks=1)
time.sleep(3)

#abaixar tela
time.sleep(2)
for i in range(0,10,1):
    pyautogui.hotkey("down")

#Clicar em EXPORTAR TABELA 
pyautogui.click(1251,701, clicks=1)

#Clicar em "Formato Excel – xlsx"
pyautogui.click(1258,861, clicks=1)

#Aguardar 60 seg antes de ir para a próxima etapa
time.sleep(60)
#fechar tela do site Pagar.me




#===== Sair do Site =====#
#pyautogui.hotkey("ctrl","w")

#===== Fim do Código =====#
pyautogui.alert("Fim do Código!")
