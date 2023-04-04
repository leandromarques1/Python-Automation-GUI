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
link = "https://analytics.agendaedu.com/question/2025-lista-mg-atualizacao-pagamentos-sec"
pyperclip.copy(link)    #equivalente ao "CTRL+C"
pyautogui.hotkey("ctrl","v")    #executa um atalho
pyautogui.press("enter")    #apertar "ENTER"
time.sleep(tempo_pausa)  #tempo em SEGUNDOS necessário para esperar antes de ir para a próxima linha do código

#===== Colocar dados de Acesso (Email e Senha)=====#
#Acessar conta
pyautogui.click(943,601, clicks=1)

#Conta do Google para Acessar
pyautogui.click(967,508, clicks=1)

#Aguardar tempo 30 segundos
time.sleep(30)

#Fazer download
pyautogui.click(1851,999, clicks=1)

#Baixar em Formato Excel (xlsx)
pyautogui.click(1655,871, clicks=1)
time.sleep(60)

#===== Sair do Site =====#
#pyautogui.hotkey("ctrl","w")

#===== Fim do Código =====#
pyautogui.alert("Fim do Código!")