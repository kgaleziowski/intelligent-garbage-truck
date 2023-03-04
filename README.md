# Intelligent Garbage Truck

---

### Project contains:

:heavy_check_mark: **Agent environment in the form of a tile map generated from a .tmx configuration files**

:heavy_check_mark: **Agent movement within environment, state space traversal.**

:heavy_check_mark: **Implementation of state space searching with BFS (Breadth-first search) algorithm**

:heavy_check_mark: **Implementation of state space searching with heuristic algorithm A(*) and Manhattan distance.**

:heavy_check_mark: **Implementation of decision trees for making decision about picking up garbage under current circumstances based on 8 parameters (even/odd day of the week, size of garbage, weight of garbage, paid bill, can/cannot close bin, free space, type of garbage, time of a day), model training, learning set, extracted trainer for model**

:heavy_check_mark: **Implementation of neural networks for recognizing four different types of garbage (plastic, paper, glass, mixed) based on given picture. Model training with keras using multiple layers and saving it to file.**

:heavy_check_mark: **Implementation of genetic algorithms for solving traveling salesman problem: cost matrix generation, chromosome adjustment to environment, mutations, elitism, crossover, ranking, mating pool, all parameters can be easily changed (population size, elite size, mutation rate, number of generations), generation of plot for cost optimision obtained by genetic algorithms.**

:heavy_check_mark: **Clear HUD that shows what is happening in the agent's environment at the moment (including picture of garbage).**

:heavy_check_mark: **Dataset containing nearly 1000 pictures of each type of garbage (plastic, paper, glass, mixed)**

:heavy_check_mark: **Access to configuration files which allows to play with generated environment**

### Agent environment:

### Dataset samples:

### Genetic algorithms plot visualization of cost optimisation:

### Technology stack:

*  **Python Programming Language**

* **PyGame library**

* **Keras library**

* **PyTorch library**

* **Sklearn library**

### Requirements:

**1. Install Python 3.x (version 3.9 is recommended)**

**2. Install pygame library**

**3. Install numpy library**

**4. Install torch library**

**5. Install tensorflow (version 2.8.0) library**

**6. Install torchvision library**

**7. Install pytmx library**

**8. Install scikit-learn library**

**9. Open project ("intelligent-garbage-truck-main" folder) under PyCharm IDE**

**10. Run main.py**

**11. Press space when after everything is loaded**

:bangbang: **If any library is missing, just install it according to the information returned by ModuleNotFoundError.** :bangbang:

### Additional features:

* **User can load multiple configurations in settings.py file and also create his own configurations according to instructions in file "GA-How to use.txt".**

* **User can easily change used algorithm for state space searching by pressing A key (A(*)/BFS).**

* **User can analyse optimise obtained by genetic algorithms by checking plots generated in configurations folder 001, 002, etc.**

* **All important information are logged in real time to the console and can be verified.**
