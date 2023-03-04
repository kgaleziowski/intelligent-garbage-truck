# Intelligent Garbage Truck

**Implementation of intelligent autonomous garbage truck that travels by path with the lowest cost (TSP problem solved with genetic algorithms) from garbage to garbage, collects garbage if circumstances allows to do so (decision trees classification) and recogonizes type of garbage that is in trash (neural network object recognition). Agent uses BFS and A(*) algorithms implementation for state space searching, agent environment is highly configurable.**

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

---

### Autonomous garbage truck in action:

---

### Agent environment:

![s1](https://user-images.githubusercontent.com/72214275/222919705-3ac36d0c-9cae-4c56-bcc7-dd6826db0220.png)

![s2](https://user-images.githubusercontent.com/72214275/222919713-7d319a08-0bc4-4d2c-9474-101292a40d0c.png)

![s3](https://user-images.githubusercontent.com/72214275/222919718-2733e477-43f3-4b2f-980b-0d1b397f16bc.png)

---

### Dataset samples (examples of glass/paper/plastic/mix):

![glass (20)](https://user-images.githubusercontent.com/72214275/222919732-5634a553-3c5d-45f4-a2a8-44e28a2da4c4.jpg)

![paper (131)](https://user-images.githubusercontent.com/72214275/222919747-37f00c92-3865-48d5-b3c2-aa651ce65d8b.jpg)

![plastic (13)](https://user-images.githubusercontent.com/72214275/222919756-050717de-f3a3-43b2-bd34-7e42a2eb0cb0.jpg)

![mix (648)](https://user-images.githubusercontent.com/72214275/222919821-394071a6-e4dd-4f71-b3df-b84e7d497626.jpg)

---

### Genetic algorithms plot visualization of cost optimisation (different parameters):

![PLOT-003](https://user-images.githubusercontent.com/72214275/222919869-9d3a4795-4859-4a9f-afba-1f0a29cd2b46.png)

![PLOT-002](https://user-images.githubusercontent.com/72214275/222919930-bf8a2b69-3c03-4d37-948c-e59903499328.png)

![PLOT-004](https://user-images.githubusercontent.com/72214275/222919878-68ab2209-3a17-4f8d-aebb-b5228fca2676.png)

![PLOT-008](https://user-images.githubusercontent.com/72214275/222919899-ee819059-86c8-4f59-8ff7-d6fdaaf4d9cd.png)

---

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

---

### Additional features:

:heavy_check_mark: **User can load multiple configurations in settings.py file and also create his own configurations according to instructions in file "GA-How to use.txt".**

:heavy_check_mark: **User can easily change used algorithm for state space searching by pressing A key (A(*)/BFS).**

:heavy_check_mark: **User can analyse optimise obtained by genetic algorithms by checking plots generated in configurations folder 001, 002, etc.**

:heavy_check_mark: **All important information are logged in real time to the console and can be verified.**
