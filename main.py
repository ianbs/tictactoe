#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Importação das bibliotecas
import pygame
import os

#Importação das Classes
from cell import Cell

#VARIAVEIS GLOBAIS
cells = [] #Array com as celulas da matriz do jogo
moves = [] #Array com as celulas que já foram 
moves_x = []
moves_o = []
screen_width = 300 #Variavel com a largura da tela
screen_height = 300 #Variavel com a altura da tela

#Variavel com as posições das celulas na tela 
positions = [
  (0, 0, 100, 100), # 1 celula
  (100, 0, 200, 100), # 2 celula
  (200, 0, 300, 100), # 3 celula
  (0, 100, 100, 200), # 4 celula
  (100, 100, 200, 200), # 5 celula
  (200, 100, 300, 200), # 6 celula
  (0, 200, 100, 300), # 7 celula
  (100, 200, 200, 300), # 8 celula
  (200, 200, 300, 300), # 9 celula
]

grid = [[0,0,0],
        [0,0,0],
        [0,0,0]]

padroes_vence = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,6,8],[0,4,8],[2,4,6]]

#Configurações iniciais do jogo
os.environ["SDL_VIDEO_CENTERED"] = "1" #Inicializa a janela no centro
pygame.init() #Inicia o PyGame
screen = pygame.display.set_mode((screen_width,screen_height)) #Define as configurações da janela
pygame.display.set_caption("Jogo da Velha") #Define o titulo da janela
game_surf = pygame.Surface((300,300))
done = False #Variavel para o programa rodar em loop infinito
clock = pygame.time.Clock()

#Função que desenha as celulas e as linhas que as dividem
def draw_cells():
  for c in cells:
    c.draw(pygame)
  #Desenha as linhas que dividem as celulas
  pygame.draw.line(game_surf,(0,0,0), [100,0],[100,300],5)
  pygame.draw.line(game_surf,(0,0,0), [200,0],[200,300],5)
  pygame.draw.line(game_surf,(0,0,0), [0,100],[300,100],5)
  pygame.draw.line(game_surf,(0,0,0), [0,200],[300,200],5)

#Função que checa qual celula foi clicada 
def which_cell_click():
  n = 0
  for c in cells:
    if c.click(pygame):
      n = c.n
  return n

def draw_circle():
  pygame.draw.circle(game_surf, (0,0,0), cells[which_cell_click()].get_center(), 40, 3)
  screen.blit(game_surf, (0,0))

def draw_x():
  pygame.draw.line(game_surf,(0,0,0), [cells[which_cell_click()].positions[0],cells[which_cell_click()].positions[1]],[cells[which_cell_click()].positions[2],cells[which_cell_click()].positions[3]],5)
  pygame.draw.line(game_surf,(0,0,0), [cells[which_cell_click()].positions[0]+100,cells[which_cell_click()].positions[1]],[cells[which_cell_click()].positions[2]-100,cells[which_cell_click()].positions[3]],5)
  screen.blit(game_surf, (0,0))

def print_winner(frase):
  game_surf.fill([255,255,255])
  pygame.font.init()
  myfont = pygame.font.SysFont('Liberation Serif', 18)
  textsurface = myfont.render(frase, False, (0, 0, 0))
  game_surf.blit(textsurface,(15,130))

#For loop para gerar o Array com todas as celulas
for i in range(9):
  cells.append(Cell(game_surf, positions[i], (255,255,255), i))

draw_cells() #Desenha as celulas

#Main do programa
if __name__ == "__main__":
  while not done:
    # drawCells() #Desenha as celulas
    #Executa os eventos de clicks e teclas pressionadas
    for event in pygame.event.get():
      game = False
      #Fecha a janela
      if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_q]:
        done = True
      #Evento de click com o mouse em uma celula
      if event.type == pygame.MOUSEBUTTONDOWN:
        if which_cell_click() in moves:
          print('x')        
        else:
          if len(moves)%2 == 0:
            draw_circle()
            moves_o.append(which_cell_click())
          else:
            draw_x()
            moves_x.append(which_cell_click())
          moves.append(which_cell_click()) #Adiciona a celula ao array de movimentos feitos
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


