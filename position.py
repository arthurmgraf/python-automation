import pyautogui
from pynput import mouse, keyboard
import threading

# Variável global para controlar o loop
running = True

# Função para capturar cliques do mouse
def on_click(x, y, button, pressed):
    if pressed and button == mouse.Button.left:  # Clique esquerdo
        print(f"\nClique do mouse registrado em: X={x}, Y={y}")

# Função para capturar eventos do teclado
def listen_keyboard():
    global running
    def on_press(key):
        try:
            if key.char == 'p':  # Tecla 'P' foi pressionada
                x, y = pyautogui.position()
                print(f"\nTecla 'P' pressionada. Posição do mouse: X={x}, Y={y}")
        except AttributeError:
            if key == keyboard.Key.esc:  # Tecla 'Esc' para encerrar
                print("\nEncerrando o programa.")
                running = False
                return False  # Para encerrar o listener do teclado

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

# Listener do mouse em uma thread separada
def listen_mouse():
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()

# Função principal
def main():
    global running
    print("Pressione 'P' para capturar a posição do mouse.")
    print("Clique com o botão esquerdo para registrar o clique.")
    print("Pressione 'Esc' para encerrar o programa.\n")

    # Executa o listener do mouse em uma thread
    mouse_thread = threading.Thread(target=listen_mouse, daemon=True)
    mouse_thread.start()

    # Executa o listener do teclado (bloqueia o programa até 'Esc')
    listen_keyboard()

if __name__ == "__main__":
    main()
