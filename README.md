## Stochastic Local Search sloving Traveling Salesman Probelm
### Simulating-Annealing Algorithm

#### Algorithm Design:
The order of visiting nodes would be shown in a list. For example, if the list = [0,1,2,3,4] means the path for traveling would be from 0 to 1, then to 2, all the way to 4.
The algorithm randomly changes the order of two elements in the list in every iteration. If the change is a good move then take it. To avoid being stuck in a local minimum, the algorithm has a probability of taking bad moves.
In this case, the algorithm would have both greedy moves and random moves. In normal conditions, where the next move is better, the algorithm takes the greedy move. However when the next move is a bad move, the random part starts.
There’s a probability that the algorithm would take the bad move. Temperature is a parameter for developers to tune. Temperature decreases exponentially in the algorithm by adding cooling rate.
When temperature decreases, the probability also decreases. Therefore, the algorithm acts more randomly at first, as the temperature drops the algorithm would take its next step more carefully.
Iteration is also a parameter that the developers can tune. A larger number of iterations can increase the chances of finding a better solution but may also increase the computational time.

#### Explanation of Algorithm:
The inputs of the function are a list of nodes with initial order, the initial temperature, and the cooling rate. We set the initial list (tour) as a list of integers from 0 to n-1, where n is the total number of the nodes.
In the function, we let current_tour, current_distance = tour, total_distance(current_tour) to initialize. Then in the for loop, we randomly swap two nodes’ order to be our potential next move.
If the new total distance is less than the current total distance then we'll take the move. However, when the new total distance is greater than the current one, we only take this move with a probability of e^(ΔE/T).
ΔE = current distance - new distance and T is the temperature. Else, just don’t take the bad move. At the end of the loop we’ll decrease the temperature by timing the cooling rate. This is how the simulating annealing algorithm works.
As the for loop runs, temperature would get lower and lower in exponential rate. Making the probability of taking a worse result less possible as the loop runs. After the loop finishes, we return the final solution. 

#### Algorithm Analysis:
##### Time Complexity:
The time complexity of simulated annealing is typically expressed in terms of the number of iterations. The number of iterations (or moves) is determined by parameters such as the initial temperature, cooling rate, and the stopping criterion. In general, the time complexity can be represented as O(m*n), where m is the iteration and n is the number of nodes, which is the number of cities.
##### Space Complexity:
The space complexity of simulated annealing is mainly determined by the storage of the current and new solutions during the algorithm's execution. It involves keeping track of the current solution, the new solution being evaluated, and potentially additional data structures. In our design, the representation of the solution is a one dimensional list, which requires O(n) space, where n is the number of nodes or cities. 
