import pygame
import pygame_gui
import sys
import time

# Inicializa Pygame
pygame.init()

# Configura el tamaño de la ventana
window_size = (800, 600)
window = pygame.display.set_mode(window_size)

# Crea un administrador de interfaz de usuario
ui_manager = pygame_gui.UIManager(window_size)

# Crea un deslizador
slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((350, 50), (100, 20)),
                                                start_value=3,
                                                value_range=(1, 7),
                                                manager=ui_manager)

# Configura los colores
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # Rojo, verde, azul

def draw_towers():
    # Limpia la ventana
    window.fill((255, 255, 255))  # Blanco

    # Dibuja los discos
    for i, tower in enumerate([A, B, C]):
        for j, disk in enumerate(tower):
            pygame.draw.circle(window, colors[disk-1], (200*(i+1), 500-50*j), 20*disk)

    # Actualiza la ventana
    pygame.display.flip()

def hanoi(n, source, target, auxiliary):
    if n > 0:
        hanoi(n - 1, source, auxiliary, target)
        if source:
            target.append(source.pop())
            draw_towers()
            time.sleep(0.5)  # Agrega un retraso para la animación
        hanoi(n - 1, auxiliary, target, source)

# Configura las torres
n = 3
A = list(range(n, 0, -1))
B = []
C = []

# Ejecuta el algoritmo
draw_towers()
hanoi(n, A, B, C)

# Mantiene la ventana abierta hasta que el usuario la cierre
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
                if event.ui_element == slider:
                    n = int(slider.get_current_value())
                    A = list(range(n, 0, -1))
                    B = []
                    C = []
                    draw_towers()
                    hanoi(n, A, B, C)
        ui_manager.process_events(event)

    ui_manager.update(time.delta)
    ui_manager.draw_ui(window)

    pygame.display.update()
