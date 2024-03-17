import os
from pydub import AudioSegment
from pydub.playback import play

# current_directory = os.getcwd()

# Print the current working directory
# print("Current Working Directory:", current_directory)

audio_directory = 'audio'

os.chdir(audio_directory)

pr_ch = AudioSegment.from_file("sound_pringles_cheese.mp3", format="mp3")
pr_sc = AudioSegment.from_file("sound_pringles_sour_cream.mp3", format="mp3")
vc = AudioSegment.from_file("sound_v_cut_cheese.mp3", format="mp3")
pc = AudioSegment.from_file("sound_piattos_cheese.mp3", format="mp3")
cc = AudioSegment.from_file("sound_clover_cheese.mp3", format="mp3")
smct = AudioSegment.from_file("sound_san_marino_corned_tuna.mp3", format="mp3")
nscn = AudioSegment.from_file("sound_nissin_seafood_cup_noodles.mp3", format="mp3")
c2a = AudioSegment.from_file("sound_c2_apple_green_tea.mp3", format="mp3")
c2c = AudioSegment.from_file("sound_c2_classic_green_tea.mp3", format="mp3")
nl = AudioSegment.from_file("sound_nestea_lemon.mp3", format="mp3")
no_obj = AudioSegment.from_file("sound_no_obj.mp3", format="mp3")

play(pr_ch)