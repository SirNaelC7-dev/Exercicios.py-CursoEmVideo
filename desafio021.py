import pygame/*Módulo utilizado para jogos ex:trliha sonora*/
pygame.init()
pygame.mixer.music.load('arquivo.mp3')
pygame.mixer.music.play()
pygame.event.wait()
