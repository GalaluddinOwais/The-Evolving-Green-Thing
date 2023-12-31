# The Evolving Green Thing: A Journey of Reinforcement Learning


# About the project
This project aims to demonstrate the power of evolution using genetic algorithm by displaying 2D animations of objects while having their chromosome's genes manifested to check how fitting they are, according to which a new generation of objects develops, so it appears like the objects are undergoing trial and error evolution over the generations to learn to achieve a specific predefined goal

# Key Achievements
* Implemented a genetic algorithm with different decodings and fitness functions for different goal scenarios
* Set up various challenging goals to achieve with a customized 2D environment for each, and introduced some (local minimae) tricks, to finally have the following subprojects: 
  * Target The Ball
  * Find The Way To The Roof
  * Triple Clearance
  * Triple Goalkeeping
  * The Floor Is Lava
  * Not a Random Forest
  * Fly Me To The Ball (co-operative) - two objects cooperate to achieve each one’s goal
  * Target The Ball (neural network) - the ball can pop up from any point unpredictably
  * Smarter Not Harder
  * Hack Two-Factor Authentication
  * Count Hundred Sheep (neural network) - unpredictable height of a fence to jump over  
  * Butch and Tom and Jerry (with game version) (neural network) - an object avoids two moving balls, one of which is brought from "Target The Ball (neural network)"
* Displayed the chromosome manifestation (code decoding) process, which is a customized 2D animation played to see how a decoded chromosome acts, to allow for the calculation of the degree of goal achievement (fitness value)
* Displayed the chromosomes in each generation along with their fitness values calculated from the manifestation of each, also displayed the crossover and the mutation processes done to them, explaining the development of a new generation 
* Terminated all the running processes manually, whether for those that were seen to have achieved their goals before reaching the maximum number of generations, or those that were stuck in one generation indefinitely because a certain object's trial did not trigger the elimination criteria which was only about making an error
* Achieved all the goals set in each subproject and saved the goal-achieving (the most fitting) chromosomes



# Requirements
`Python 3.7`
`Pygame 2.0`
`Pymunk 6.5`


# Execution
For any subproject:
To run the evolution process, locate run.py and run the following command:
```
python run.py
```

To show the manifestation of the saved chromosome(s), locate physics.py and run the following command:
```
python physics.py
```

# Demonstration

[Google drive link](https://drive.google.com/file/d/1oK4afoIg-lpiYwr-77rcmSVbHn5sSxIC/view?usp=share_link)

### Target The Ball

The goal is to get the free ball as close as possible to the pinned ball, before a specific time period elapses

<img src="https://github.com/GalaluddinOwais/The-Evolving-Green-Thing-A-REINFORCEMENT-LEARNING-JOURNEY/assets/111979327/13d87c21-5339-4754-9cd4-97aab05f6ff6" width="40%" height="40%">

### Triple Clearance

The goal is to get the three balls as close as possible to the side without a boundary and beyond, before a specific time period elapses

![clearamce](https://github.com/GalaluddinOwais/The-Evolving-Green-Thing-A-REINFORCEMENT-LEARNING-JOURNEY/assets/111979327/bad4354b-2b18-4e53-9fcd-e958d949d220)

### Triple Goalkeeping

The goal is to keep the three balls within the frame, preventing each from going beyond the side without a boundary, until a specific time period elapses

![goalkeeping](https://github.com/GalaluddinOwais/The-Evolving-Green-Thing-A-REINFORCEMENT-LEARNING-JOURNEY/assets/111979327/e0496d35-9b8a-4586-98a3-0d8714f1bba1)

### The Floor Is Lava

The goal is to avoid contact with the lower boundary for as long as possible, before a specific time period elapses

(Note that the amount of movement is limited for that type of "thing")

![lava](https://github.com/GalaluddinOwais/The-Evolving-Green-Thing-A-REINFORCEMENT-LEARNING-JOURNEY/assets/111979327/137060dc-7c4d-46d3-8be2-714f5455bd0b)

### Find The Way To The Roof

The goal is to get as high as possible, before a specific time period elapses

<img src="https://github.com/GalaluddinOwais/The-Evolving-Green-Thing-A-REINFORCEMENT-LEARNING-JOURNEY/assets/111979327/4055f8d5-1c6e-4c96-9e82-7cc131c32726" width="40%" height="40%">
<img src="https://github.com/GalaluddinOwais/The-Evolving-Green-Thing-A-REINFORCEMENT-LEARNING-JOURNEY/assets/111979327/a312356f-f5a0-4d64-8348-e182772f80d8" width="40%" height="40%">

<img src="https://github.com/GalaluddinOwais/The-Evolving-Green-Thing-A-REINFORCEMENT-LEARNING-JOURNEY/assets/111979327/c1e24f1d-acfa-48c2-ad02-dffb3ed58731" width="40%" height="40%">
<img src="https://github.com/GalaluddinOwais/The-Evolving-Green-Thing-A-REINFORCEMENT-LEARNING-JOURNEY/assets/111979327/60581a47-acc8-4783-92a4-f163af41852a" width="40%" height="40%">

### Fly Me To The Ball

The goal for the two "things" is to get as close as possible to each one's ball, before a specific time period elapses

<img src="https://github.com/GalaluddinOwais/The-Evolving-Green-Thing-A-REINFORCEMENT-LEARNING-JOURNEY/assets/111979327/a117075d-14d2-4866-a26f-bd364a7270e1" width="60%" height="60%">

### Count Hundred Sheep (Neural Network)

The goal is to get as close as possible to the opening and beyond, whatever the location of the opening is

<img src="https://github.com/GalaluddinOwais/The-Evolving-Green-Thing-A-REINFORCEMENT-LEARNING-JOURNEY/assets/111979327/2db49fa8-2ef6-4330-9138-2342f67529c1" width="38%" height="38%">

### Hack Two-Factor Authentication

The goal is to get the free ball as close as possible to the openings and beyond, before a specific time period elapses

(The learning process was executed for each openings situation at a time) 

![hack](https://github.com/GalaluddinOwais/The-Evolving-Green-Thing-A-REINFORCEMENT-LEARNING-JOURNEY/assets/111979327/10e55487-2e58-4324-b597-63fe0eefea29)

### Target The Ball (Neural Network)

The goal is to get as close as possible to the pinned ball, wherever the pinned ball pops up from

<img src="https://github.com/GalaluddinOwais/The-Evolving-Green-Thing-A-REINFORCEMENT-LEARNING-JOURNEY/assets/111979327/33bf0734-0d9b-4eba-8975-67bef6239f1e" width="40%" height="40%">

### Not a Random Forest

The goal for the green "things" is to extend their length as possible while still allowing the gray "thing" to drop out from the frame, before a specific time period elapses

<img src="https://github.com/GalaluddinOwais/The-Evolving-Green-Thing-A-REINFORCEMENT-LEARNING-JOURNEY/assets/111979327/67e190dc-3ade-4e40-b4e7-dcc4eb988eb7" width="40%" height="40%">

### Smarter Not Harder

The goal is to get as high as possible while exerting as low force as possible, before a specific time period elapses

In other words, the goal is to maximize the sum of the highest height reached and the force preserved

(The paler color of the "thing" indicates less force applied)

<img src="https://github.com/GalaluddinOwais/The-Evolving-Green-Thing-A-REINFORCEMENT-LEARNING-JOURNEY/assets/111979327/86b50b00-9b41-4520-b539-23fe05800599" height="20%" width="20%">

### Butch and Tom and Jerry (Neural Network)

The goal is to avoid the two moving balls for as long as possible


<img src="https://github.com/GalaluddinOwais/The-Evolving-Green-Thing-A-REINFORCEMENT-LEARNING-JOURNEY/assets/111979327/a071a8eb-70cd-4f2a-b952-3441f541fdb5" width="40%" height="40%">
<img src="https://github.com/GalaluddinOwais/The-Evolving-Green-Thing-A-REINFORCEMENT-LEARNING-JOURNEY/assets/111979327/fc3a5bc8-c1f8-4f49-875f-6b5093e230e1" width="40%" height="40%">

<img src="https://github.com/GalaluddinOwais/The-Evolving-Green-Thing-A-REINFORCEMENT-LEARNING-JOURNEY/assets/111979327/1b28880b-4cb0-49db-b852-04fa4dcc4fb2" width="40%" height="40%">
<img src="https://github.com/GalaluddinOwais/The-Evolving-Green-Thing-A-REINFORCEMENT-LEARNING-JOURNEY/assets/111979327/e14fbdd4-ea9c-478d-9ca2-0e6940538385" width="40%" height="40%">




# Additional Notes

* In the footsteps of the genetic algorithm in the project, the neural networks in the project were also implemented from scratch as mathematical equations, which may be seen as a pro or a con.
* One drawback of the project is that it doesn't follow a best practice in the training process, as it doesn't run the manifestation of all chromosomes in a generation in parallel. While this is time-consuming, it is suitable for less powerful processors.
* One other drawback of the project is that it contains some code repetition that could be better modularized.
* It all started from here: [4-Queens Solver](https://github.com/GalaluddinOwais/4-Queens-Solver).
