#esse código é para rodar na máquina, e não no Colab

import requests #biblioteca para manipular as requisiçãoes via URL
import os       #biblioteca para lidar com o Sistema Operacional (independente de qual seja)

def baixar_arquivo (url, endereco):
  #faz requisição ao servidor
  resposta = requests.get(url)
  
  #verificar se requisição foi bem sucedida
  if resposta.status_code == requests.codes.OK:
    with open(endereco, 'wb') as novo_arquivo:
      novo_arquivo.write(resposta.content)
    print("Download finalizado. Arquivo salvo em: {}".format(endereco))
  else:
    resposta.raise_for_status()

  
if __name__ == "__main__":
  #======= baixando um arquivo de uma vez:  =========== #
  #passa a URL do arquivo que quer baixar
  BASE_URL = 'https://math.mit.edu/classes/18.745/Notes/Lecture_1_Notes.pdf'
  baixar_arquivo('https://math.mit.edu/classes/18.745/Notes/Lecture_1_Notes.pdf','test.pdf')

  #====== baixando vários arquivos de uma vez =======#
  #passa a URL do arquivo que quer baixar
  BASE_URL = 'https://math.mit.edu/classes/18.745/Notes/Lecture_{}_Notes.pdf'
  OUTPUT_DIR = 'output' #nome da pasta onde quero baixar arquivo (pode ser qualquer um)
  for i in range (1,26):
    nome_arquivo = os.path.join(OUTPUT_DIR, 'nota_de_aula_{}.pdf'.format(i))
    baixar_arquivo(BASE_URL.format(i),nome_arquivo)
