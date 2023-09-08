# About the project
#### This project aims to showcase the power of evolution using genetic algorithm by displaying a 2D animation of objects while having their chromosome's genes manifested to check how fitting they are in order to develop the next generation of objects, so it looks like the objects are undergoing trial and error evolution over the generations to learn to achieve a specific predefined goal

# Key Achievements
* Implemented a genetic algorithm with different decoding and fitness functions for different goal scenarios
* Set up various challenging goals to achieve with a customized 2D environment for each, and introduced some global minimae tricks, to finally have the following subprojects: 
 * Target the ball
 * Find the way to the roof
 * Triple Clearance
 * Triple Goalkeeping
 * The floor is lava
 * Not a random forest
 * Fly me to the ball (co-operative) - two objects cooperates to achieve each one’s goal
 * Target the ball (neural network) - the ball can pop up from unpredictable places
 * Smarter not harder
 * Hack Two-Factor Authentication
 * Count Hundred Sheep (neural network) - unpredictable height of a fence to jump over  
 * Butch and Tom and Jerry (with game version) (neural network) - an object avoids two moving balls, one of which is brought from "Target the ball (neural network)"
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


