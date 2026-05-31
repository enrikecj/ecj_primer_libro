# Chapter 1. EQUILIBRIUM, DAMPING AND OSCILLATIONS

## Equilibrium

In this first chapter we will introduce some concepts that are necessary to properly understand what we will study next. The first of them is the concept of equilibrium. Throughout a large part of the course we will study oscillations and waves, which are dynamic phenomena, but it is necessary to start with equilibrium. Although it may seem to have little relation to those phenomena, it is enough to realize that the oscillations of a system are generally produced around an equilibrium point. The concept of equilibrium is essential for the study of system dynamics because it provides the reference point from which we can analyse and understand how systems change and evolve over time. Therefore, it is indispensable to fully understand what a point of equilibrium is and, more generally, what we mean (at least in this course) when we talk about equilibrium.

The first idea when speaking of equilibrium is to think of the absence of motion, but that is only a very particular case of equilibrium. It does not even coincide with what is mechanical equilibrium, which occurs when the resultant of the forces acting on a system is zero. However, the concept of equilibrium goes beyond mechanics. Without leaving physics, we can talk about other types of equilibrium:

- **Thermal equilibrium**: It refers to the situation in which two or more systems in thermal contact are at the same temperature. In this state, there is no net heat flow between the systems.
- **Thermodynamic equilibrium**: A system is in thermodynamic equilibrium when it does not experience macroscopic changes over time and all its parts are in mechanical, thermal and chemical equilibrium. This type of equilibrium implies that the thermodynamic variables of the system, such as temperature, pressure and chemical potential, are uniform.
- **Electrical circuit equilibrium**: In an electrical circuit, equilibrium is reached when the current and voltage at each point of the circuit remain constant over time.

Beyond physics, equilibrium can be discussed in many other disciplines:

- **Chemical equilibrium**: In chemistry, equilibrium refers to the state in which the concentrations of reactants and products in a reversible reaction remain constant over time. At this point, the rates of the forward and reverse reactions are equal and there are no net changes in the composition of the system.
- **Genetic equilibrium**: In population genetics, equilibrium describes a state in which allele and genotype frequencies in a population remain constant across generations. This state is reached when there are no evolutionary forces acting on the population, such as mutation, natural selection, genetic drift, or gene flow.
- **Social equilibrium**: In sociology, social equilibrium refers to a state of relative stability and order in a society, where the different parts of the social system function harmoniously. This state implies a balance of power among the various social groups, as well as the widespread acceptance of norms and values.
- **Economic equilibrium**: In economics, equilibrium is a state in which the forces of supply and demand are balanced. In this situation, there is no tendency for prices or quantities to change.
- **Mathematical equilibrium**: In mathematics, an equilibrium point of a system of differential equations is a point where the system does not change over time. In other words, it is a stationary state of the system.

For a system to be in equilibrium it is not enough that one of its properties is in equilibrium; all the magnitudes that characterise it must be as well. This is a very demanding condition for systems described by several magnitudes. Therefore we will talk about equilibrium of the properties of a system. A physical system may evolve in time with certain magnitudes, for example, velocities, and yet have other magnitudes that do not change in time, such as a constant acceleration.

Let us therefore consider a magnitude of a system that we will denote with the letter $\eta$. We will say that this property is in equilibrium if it does not evolve in time. Mathematically we can write it with the expression:

$$
\frac{d\eta}{dt} = 0
$$ (1.1)

## Mechanical equilibrium

In the case of mechanical equilibrium, although sometimes we speak of "force equilibrium", the quantity that is in equilibrium is not the force but the velocity: Since the definition of mechanical equilibrium is that the net force, and not its derivative, is zero, $\vec{F} = 0$, from Newton's second law, $\vec{F} = m\vec{a}$, and taking into account that acceleration is the derivative of velocity, we have that:

$$
\vec{F} = m\frac{d\vec{v}}{dt} = 0 \implies \frac{d\vec{v}}{dt} = 0
$$ (1.2)

so it is the velocity that is the magnitude in equilibrium.

Regarding position, it is not a property that has to be in equilibrium when we talk about mechanical equilibrium. An object that is at rest and does not move in a given reference frame is only a particular case of mechanical equilibrium.

Let us look at a few examples of equilibrium in physics:

### Example 1. Equilibrium condition of a simple pendulum

The equilibrium condition in a pendulum occurs when the pendulum's velocity is constant. This happens when the pendulum is at rest in its lower vertical position (zero angle with respect to the vertical).

```{figure} ../_static/tema1_images/page3_img1.jpeg
---
width: 30%
name: fig-pendulo-fuerzas
align: center
---
Scheme of the forces acting on a simple pendulum.
```

We will see how to deduce it mathematically step by step:

#### 1. Identify the forces:

The forces acting on the mass of the pendulum (See {numref}`fig-pendulo-fuerzas`) are the tension $T$ of the string and the weight $\vec{F}_g = -mg \hat{e}_y$ (where the minus sign indicates that it points in the negative vertical direction).

#### 2. Project the forces onto the axes:

The forces are decomposed into their horizontal (axis $x$) and vertical (axis $y$) components.

$$
\vec{F}_T = -T\sin\theta\hat{e}_x + T\cos\theta\hat{e}_y
$$ (1.3)
$$
\vec{F}_g = -mg\hat{e}_y
$$ (1.4)

#### 3. Apply the equilibrium condition:

For the velocity to be constant, the acceleration must be zero. According to Newton's second law, this implies that the sum of the forces on each axis must be zero.

- **Equilibrium in x**: $-T \sin \theta = 0$
- **Equilibrium in y**: $T \cos \theta - mg = 0$

#### 4. Solve the equations:

The equation for the horizontal axis implies that $\sin \theta = 0$, which means that $\theta = 0$ (vertical position). Substituting this condition into the equation for axis $y$, we obtain $T = mg$, which means that the tension equals the weight at the equilibrium position.

#### Conclusion:

> The equilibrium condition in a simple pendulum is satisfied when the angle $\theta$ is zero, corresponding to the lower vertical position. At this point, the string tension equals the weight and, in addition to having no acceleration, the velocity is zero because otherwise the pendulum angle would change and it would cease to be in equilibrium.
