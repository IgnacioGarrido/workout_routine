# workout_routine
This repo contains a small script to create an audio of a self defined workout routine.

# How to use:

It is very simple to use:

1. First set a name (and a path) of the created mp3 file.

```python
save_path = '/Users/Ignacio/Documents/Proyectos/Workout/routine_abs.mp3'
```

2. Configure the language:

```python
language = 'en'
```

3. Configure the routine. The routine is based in a list of tuples. Each tuple consists of *('Exercise to be said.', (int) Number of seconds of silence until next exercise)*. Eg:

´´´python
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
]
´´´

