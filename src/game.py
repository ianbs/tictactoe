#import pygame
from entities.Cell import Cell
POSITIONS = [
    (0, 0, 100, 100),  # 1 celula
    (100, 0, 200, 100),  # 2 celula
    (200, 0, 300, 100),  # 3 celula
    (0, 100, 100, 200),  # 4 celula
    (100, 100, 200, 200),  # 5 celula
    (200, 100, 300, 200),  # 6 celula
    (0, 200, 100, 300),  # 7 celula
    (100, 200, 200, 300),  # 8 celula
    (200, 200, 300, 300),  # 9 celula
]

PADROES_VENCE = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [
    0, 3, 6], [1, 4, 7], [2, 6, 8], [0, 4, 8], [2, 4, 6]]


class Game:
    """Classe principal do Jogo
    """

    def __init__(self):
        self.cells = []  # Array com as celulas da matriz do jogo
        self.moves = []  # Array com as celulas que já foram
        self.moves_x = []
        self.moves_o = []
        self.screen_width = 300  # Variavel com a largura da tela
        self.screen_height = 300  # Variavel com a altura da tela

    def play(self):
        while not done:
            # drawCells() #Desenha as celulas
            # Executa os eventos de clicks e teclas pressionadas
            for event in pygame.event.get():
                game = False
                # Fecha a janela
                if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_q]:
                    done = True
                # Evento de click com o mouse em uma celula
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if which_cell_click() in moves:
                        print('x')
                    else:
                        if len(moves) % 2 == 0:
                            draw_circle()
                            moves_o.append(which_cell_click())
                        else:
                            draw_x()
                            moves_x.append(which_cell_click())
                        # Adiciona a celula ao array de movimentos feitos
                        moves.append(which_cell_click())
                    moves_o.sort()
                    moves_x.sort()
                    if padroes_vence.count(moves_o):
                        print_winner("O venceu!Pressione R para reiniciar!")
                    elif padroes_vence.count(moves_x):
                        print_winner("X venceu!Pressione R para reiniciar!")
                if pygame.key.get_pressed()[pygame.K_r]:
                    draw_cells()
                    moves = []
                    moves_o = []
                    moves_x = []
            screen.blit(game_surf, (0, 0))
            pygame.display.update()
            clock.tick(10)
