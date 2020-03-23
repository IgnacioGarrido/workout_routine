import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="workout-IgnacioGarridoBotella", # Replace with your own username
    version="0.0.1",
    author="Ignacio Garrido Botella",
    author_email="ignaciogabo95@gmail.com",
    description="Proyect to create a workout routine.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/IgnacioGarrido/workout_routine.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
    )