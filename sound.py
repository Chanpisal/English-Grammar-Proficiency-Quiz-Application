import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Load sound files
try:
    correct_sound = pygame.mixer.Sound('531508__cogfirestudios__soft-dreamy-beep.wav')
    incorrect_sound = pygame.mixer.Sound('700641__producing_raylite__incorrect-buzzer.wav')
    button_click_sound = pygame.mixer.Sound('256116__kwahmah_02__click.wav')
    congratulations_sound = pygame.mixer.Sound('666280__logatron__oldtada.wav')
    background_music = '384934__ispeakwaves__soft-piano-loop-1.mp3'
except pygame.error as e:
    print(f"Error loading sound files: {e}")
    correct_sound = incorrect_sound = button_click_sound = congratulations_sound = None
    background_music = None


def toggle_music(is_muted):
    """Mute or unmute sounds and music."""
    if is_muted:
        pygame.mixer.music.set_volume(0)
        if correct_sound: correct_sound.set_volume(0)
        if incorrect_sound: incorrect_sound.set_volume(0)
        if button_click_sound: button_click_sound.set_volume(0)
        if congratulations_sound: congratulations_sound.set_volume(0)
    else:
        pygame.mixer.music.set_volume(1)
        if correct_sound: correct_sound.set_volume(1)
        if incorrect_sound: incorrect_sound.set_volume(1)
        if button_click_sound: button_click_sound.set_volume(1)
        if congratulations_sound: congratulations_sound.set_volume(1)


def play_sound(sound):
    """Play a sound if it's loaded and not muted."""
    if sound:
        sound.play()