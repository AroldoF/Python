import pygame

print("Sente o song")
pygame.init()
pygame.mixer.music.load("Questões/Ex021.mp3")
pygame.mixer.music.play(loops=0, start=0.0)
pygame.event.wait()
input("Que vibes")
