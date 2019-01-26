#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Classe da Celula
class Cell:
  #Variaveis de cada objeto Celula
  def __init__(self, screen, positions, color, n, body=None, cliked=False, center=None):
    self.screen = screen
    self.positions = positions
    self.color = color
    self.n = n
    self.clicked = False

  #Função para desenhar o retangulo da celula
  def draw(self, pygame):
    self.body = pygame.draw.rect(self.screen, self.color, [self.positions[0], self.positions[1], self.positions[2], self.positions[3]])
    return self.body

  #Função que verifica se a celula foi clicada
  def click(self, pygame):
    if pygame.mouse.get_pressed()[0] and self.body.collidepoint(pygame.mouse.get_pos()):
      self.clicked = True
      return True
   
  def get_center(self):
    x = self.body.centerx
    y = self.body.centery
    if x == 200:
      x = 150
    if y == 200:
      y = 150
    return [x, y]