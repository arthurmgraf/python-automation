import pyautogui
import time
from pynput import keyboard  # Biblioteca alternativa para capturar o teclado

# Variável para controle do loop
running = True

def delete_chat():
    """
    Função para apagar um bate-papo no Messenger.
    Realiza cliques nas posições especificadas ou localiza dinamicamente o botão 'Excluir bate-papo'.
    """
    try:
        # Capturar uma imagem da tela inteira (para debug)
        print("Capturando a tela para debug...")
        screenshot = pyautogui.screenshot()
        screenshot.save('tela_teste.png')
        print("Captura de tela salva como 'tela_teste.png'. Verifique a consistência com 'delete_option.png'.")

        # Passo 1: Clique no primeiro contato
        print("Clicando no primeiro contato...")
        pyautogui.click(x=234, y=506)  # Coordenadas da posição inicial
        time.sleep(0.5)

        # Passo 2: Clique nos três pontos do menu
        print("Clicando no menu...")
        pyautogui.click(x=287, y=507)  # Coordenadas dos três pontos
        time.sleep(0.3)

        # Passo 3: Localizar e clicar em "Excluir bate-papo"
        print("Tentando localizar o botão 'Excluir bate-papo'...")
        delete_position = pyautogui.locateCenterOnScreen("C:\\Users\\agraf\\Desktop\\code\\arthurmgraf\\development\\code\\python\\automation\\delete_option.png", confidence=0.6)  # Ajuste o nome do arquivo

        if delete_position:
            print(f"Botão 'Excluir bate-papo' encontrado em: {delete_position}")
            pyautogui.click(delete_position)
            time.sleep(0.3)
        else:
            print("Botão 'Excluir bate-papo' não encontrado. Verifique a imagem ou ajuste o parâmetro 'confidence'.")
            return

        # Passo 4: Clique no botão azul para confirmar a exclusão
        print("Confirmando exclusão...")
        pyautogui.click(x=1183, y=631)  # Coordenadas do botão azul
        time.sleep(0.6)

    except Exception as e:
        print(f"Erro: {e}")

def on_press(key):
    """Função que escuta a tecla ESC para encerrar o script."""
    global running
    if key == keyboard.Key.esc:
        print("\nOperação cancelada pelo usuário.")
        running = False
        return False  # Encerra o listener

def main():
    global running
    print("Iniciando o script... Posicione a janela corretamente.")
    print("Pressione ESC para encerrar o script.\n")
    time.sleep(6)  # Tempo para o usuário preparar a tela

    # Iniciar listener para ESC em uma thread separada
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    # Loop para executar as ações até que ESC seja pressionado
    while running:
        delete_chat()

    print("Script finalizado.")

if __name__ == "__main__":
    main()
