import pyautogui  #Ferramenta de automação (Python assume controle do seu teclado por exemplo);
import time       #Facilita no desenvolvimento de códigos que envolvem tempo, tempo de espera etc...
import pyperclip  #Permite copiar e colar via Python

#biblioteca "pyautogui" nos permite criar um código que simula que estamo
# s usando o computador
#"autogui" --> Automatização da GUI (interface gráfica de usuário)
pyautogui.PAUSE = 1
pyautogui.press("winleft")
pyautogui.write("chrome")
pyautogui.press("enter")
#pyautogui.alert("Vai começar, aperte OK e não mexa em nada") #cria um alerta na tela do computador
pyautogui.hotkey('ctrl','t')  #executa um atalho

#===== Abrir Drive =====#
#ensinar aqui o "write"
link = "https://drive.google.com/drive/folders/1mhXZ3JPAnekXP_4vX7Z_sJj35VWqayaR?usp=sharing"
pyperclip.copy(link)    #equivalente ao "CTRL+C"
pyautogui.hotkey("ctrl","v")    #executa um atalho
pyautogui.press("enter")    #apertar "ENTER"
time.sleep(5)  #tempo em SEGUNDOS necessário para esperar antes de ir para a próxima linha do código

#===== Baixar Base de Dados atualizada =====#
#isso é um problema pois depende da posição do Mouse
# a posição do Mouse depende de computador pra computador
pyautogui.click(430,508, clicks=2)
pyautogui.click(421,311,clicks=1)
pyautogui.click(1737,210)
pyautogui.click(1455,789)
time.sleep(5)


#===== Fim do Código =====#
pyautogui.alert("Fim do Código!")