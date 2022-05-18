import pygame
print('Jesus quer estar ao seu lado, sempre!');
pygame.mixer.init() ##iniciando o mixer
pygame.init() ##iniciando o pygame
pygame.mixer.music.load('volta.mp3') ##setando a musica a ser tocada
pygame.mixer.music.play() ##Dando play na música
pygame.event.wait() ##pedido para ele esperar até finalizar a música