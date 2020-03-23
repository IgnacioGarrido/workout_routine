""" EXECUTION:
	python3 /Users/Ignacio/Documents/Proyectos/workout_routine/workout_routine/routine.py
"""
from gtts import gTTS
from time import sleep
import os
from pydub import AudioSegment

# *******************
# CONFIGURATION:
save_path = '/Users/Ignacio/Documents/Proyectos/workout_routine/workout_routine/routine_abs.mp3' #Path in which the audio of the workout routine is saved.

#Language
language = 'es'

#Routine ---> (Message, seconds)
list_exercises = [
	('La rutina comenzará en 5 segundos', 5),
	('Uve', 15),
	('Piernas', 15),
	('Plancha', 15),
	('Tijera', 15),
	('Uve', 15),
	('Rodillas', 15),
	('Plancha', 15),
	('Pesa', 45),
	('Fondos', 30),
	('Rodillas alternadas', 15),
	('Plancha', 45),
	('Fin de la rutina', 0)
]

# END OF CONFIGURATION
# *******************

# Working directory:
dirname = os.path.dirname(os.path.realpath(__file__))

# Load silence files
silence10 = AudioSegment.from_mp3(os.path.join(dirname, "aux_files/10_seconds_silence.mp3"))
silence5 = silence10[:len(silence10)/2]
silence1 = silence10[:len(silence10)/10]


def get_silence_files(seconds):
	""" This function returns an audio of silence of the specified number of seconds in the format of pydub.

	:param :seconds: (int) Seconds of silence.
	:return:
		* :output: Audio of silence in the format of pydub.
	"""
	output = silence1
	num_sec_to_cover = seconds - 1
	while num_sec_to_cover > 0:
		if num_sec_to_cover >= 10:
			output += silence10
			num_sec_to_cover -= 10
		elif num_sec_to_cover >= 5:
			output += silence5
			num_sec_to_cover -= 5
		else: 
			output += silence1
			num_sec_to_cover -= 1
	return output

if not os.path.exists(os.path.join(dirname, 'aux_files/temp_files')):
	os.mkdir(os.path.join(dirname, 'aux_files/temp_files'))

audio = silence10[:1]
for exercise in list_exercises:
	temp_audio = gTTS(text=exercise[0], lang='es-es',slow=False)
	temp_audio.save(os.path.join(dirname, 'aux_files/temp_files/temp_audio.mp3'))
	tts = AudioSegment.from_mp3(dirname, 'aux_files/temp_files/temp_audio.mp3'))
	audio += tts
	audio += get_silence_files(exercise[1])
	os.remove(os.path.join(dirname, 'aux_files/temp_files/temp_audio.mp3'))

os.rmdir(os.path.join(dirname, 'aux_files/temp_files'))

# Write mp3 file
audio.export(save_path, format="mp3")

