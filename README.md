# workout_routine
This repo contains a small script to create an audio of a self defined workout routine.

# How to use:

It is very simple to use. Everything is configured in the script */workout_routine/routine.py*:

1. First set a name (and a path) of the created mp3 file.

```python
save_path = '/Users/Ignacio/Documents/Proyectos/workout_routine/workout_routine/routine_abs.mp3'
```

2. Configure the language:

```python
language = 'en'
```

3. Configure the routine. The routine is based in a list of tuples. Each tuple consists of *('Exercise to be said.', (int) Number of seconds of silence until next exercise)*. Eg:

```python
list_exercises = [
	('The routine will start in 5 seconds', 5),
	('Abs', 15),
	('Legs', 15),
	('Plank', 15),
	('Abs', 15),
	('Legs', 15),
  	('Rest for 15 seconds', 15)
	('Plank', 60),
	('Lift weight', 60),
	('Plank', 60),
	('Congratulations! End of the routine', 0)
]
```

4. Execute the script */workout_routine/routine.py*. After some seconds a mp3 audio with the specified rotine is created in the specified path ```save_path```. 

___________________________________________________________________

## #TODO:

1. The script works, but it takes the silence audio from an external mp3 file. This must be fixed.

2. It would be great to overlap the routine with some music (music instead of silence + fade in the instructions).

3. Small graphical interface (maybe flask) to ease the usage. Any help with this is welcome :).

