# Equilibrium, damping and oscillations

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
$$ (eq:eta)

## Mechanical equilibrium

In the case of mechanical equilibrium, although sometimes we speak of "force equilibrium", the quantity that is in equilibrium is not the force but the velocity: Since the definition of mechanical equilibrium is that the net force, and not its derivative, is zero, $\vec{F} = 0$, from Newton's second law, $\vec{F} = m\vec{a}$, and taking into account that acceleration is the derivative of velocity, we have that:

$$
\vec{F} = m\frac{d\vec{v}}{dt} = 0 \implies \frac{d\vec{v}}{dt} = 0
$$ (eq:force)

so it is the velocity that is the magnitude in equilibrium.

Regarding position, it is not a property that has to be in equilibrium when we talk about mechanical equilibrium. An object that is at rest and does not move in a given reference frame is only a particular case of mechanical equilibrium.

Let us look at a few examples of equilibrium in physics:

````{admonition} Example 1. Equilibrium condition of a simple pendulum
:class: example

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

**Identify the forces:**

The forces acting on the mass of the pendulum (See {numref}`fig-pendulo-fuerzas`) are the tension $T$ of the string and the weight $\vec{F}_g = -mg \hat{e}_y$ (where the minus sign indicates that it points in the negative vertical direction).

**Project the forces onto the axes:**

The forces are decomposed into their horizontal (axis $x$) and vertical (axis $y$) components.

$$
\vec{F}_T = -T\sin\theta\,\hat{e}_x + T\cos\theta\,\hat{e}_y
$$ (eq:FT)
$$
\vec{F}_g = -mg\,\hat{e}_y
$$ (eq:Fg)

**Apply the equilibrium condition:**

For the velocity to be constant, the acceleration must be zero. According to Newton's second law, this implies that the sum of the forces on each axis must be zero.

- **Equilibrium in x**: $\quad -T \sin \theta = 0$
- **Equilibrium in y**: $\quad T \cos \theta - mg = 0$

**Solve the equations:**

The equation for the horizontal axis implies that $\sin \theta = 0$, which means that $\theta = 0$ (vertical position). Substituting this condition into the equation for axis $y$, we obtain $T = mg$, which means that the tension equals the weight at the equilibrium position.

**Conclusion:**

> The equilibrium condition in a simple pendulum is satisfied when the angle $\theta$ is zero, corresponding to the lower vertical position. At this point, the string tension equals the weight and, in addition to having no acceleration, the velocity is zero because otherwise the pendulum angle would change and it would cease to be in equilibrium.
````

````{admonition} Example 2. Equilibrium condition of a sphere in free fall with drag
:class: example

In the case of a spherical object falling through a fluid with drag, the mechanical equilibrium is also given by the balance of forces acting on the sphere. To simplify, let us assume the medium is air, whose density is much smaller than that of the sphere, so we can neglect the buoyancy force. In this case, the two forces acting on the object are the weight and the drag force (see {numref}`fig-esfera-caida`), which accounts for the effect of friction. Assuming the fall velocity is not too large, we can use Stokes' law, which states that the drag force on a sphere is proportional to the velocity $v$:

$$
F_a = -6\pi\mu r v = -bv
$$ (eq:stokes)

where $\mu$ is the dynamic viscosity and $r$ is the radius of the sphere.

```{figure} ../_static/tema1_images/esfera_caida_libre.png
---
width: 50%
name: fig-esfera-caida
align: center
---
Forces acting on a sphere in free fall with drag: the weight $F_g = -mg$ downwards and the drag force $F_a = -bv$ opposing the motion.
```

Try to find the equilibrium condition in this case. We will solve it step by step in the [Damping](sec-amortiguamiento) section.
````

## Other types of equilibrium

As mentioned before, the concept of equilibrium also exists outside mechanics. Let's look at two examples of this, one of thermal equilibrium and another in an electrical circuit.

````{admonition} Example 3. Thermal equilibrium
:class: example

As we know, two objects in contact are in thermal equilibrium if there is no net transfer of thermal energy between them. Consider the geometry shown in {numref}`fig-equilibrio-termico`. The equation governing the dynamics of the system is:

$$
\frac{dq}{dt} = -A\frac{k}{L}(T_2 - T_1)
$$ (eq:fourier)

where $q$ is the thermal energy, $A$ is the area of the junction, $k$ is its thermal conductivity, $L$ is its length, $T_1$ is the temperature of the first body, and $T_2$ is the temperature of the second. A quick look at this equation shows that thermal equilibrium is reached when the temperatures of the two bodies are equal ($T_1 = T_2$), making the time derivative of $q$ vanish.

```{figure} ../_static/tema1_images/equilibrio_termico.png
---
width: 55%
name: fig-equilibrio-termico
align: center
---
Two objects at different temperatures with a junction of area $A$, length $L$ and thermal conductivity $k$.
```
````

````{admonition} Example 4. Equilibrium in an electrical circuit
:class: example

Consider a series RL circuit like the one in {numref}`fig-circuito-rl`, with a resistor and an inductor, in which we want to find the equilibrium condition for the current intensity.

```{figure} ../_static/tema1_images/circuito_rl.png
---
width: 55%
name: fig-circuito-rl
align: center
---
Series RL circuit.
```

How would you find the equilibrium condition in this case?
````

(sec-puntos-equilibrio)=
## Equilibrium points

In general, the equilibrium condition for a magnitude will not occur for all values of the variables it depends on, but only for some of them. For example, if the system depends on two variables, $\eta$ and $x$, and the equation of motion is:

$$
\frac{d\eta}{dt} = f(\eta, x)
$$ (eq:eq-motion-general)

then $x_0$ is an **equilibrium point** if $f(\eta, x_0) = 0$, so that at that point:

$$
\frac{d\eta}{dt} = f(\eta, x_0) = 0
$$ (eq:eq-point)

The concept of equilibrium point is not strictly geometric: the variable $x$ can be a position, but also a temperature, a chemical concentration, etc.

In the case of mechanical equilibrium, the condition is that the total force is zero. When the force is not homogeneous throughout space, equilibrium will occur at the points $\vec{r}_0$ where $\vec{F}(\vec{r}_0) = 0$.

Let us return to the simple pendulum (Example 1). We saw that equilibrium occurred when $\sin\theta = 0$. Since in our coordinate system ({numref}`fig-pendulo-fuerzas`) $x = l\sin\theta$, $y = l(1 - \cos\theta)$, the equilibrium point of the system is:

$$
(x_{eq},\, y_{eq}) = (0, 0)
$$ (eq:pendulo-eq-point)

that is, our coordinate origin.

Try to find the equilibrium points in other systems, for example a spring with a hanging mass, or an object floating partially submerged in a liquid.

(sec-estabilidad)=
## Stability of equilibrium

The equilibrium of a system can be classified into three main types: stable, unstable and indifferent (see {numref}`fig-tipos-equilibrio`). This classification is based on the system's response to small perturbations or displacements from its equilibrium position.

```{figure} ../_static/tema1_images/tipos_equilibrio.png
---
width: 85%
name: fig-tipos-equilibrio
align: center
---
Scheme of the three types of equilibrium: stable (left), unstable (centre) and indifferent (right).
```

- **Stable equilibrium**: A system is in stable equilibrium if, when slightly displaced from its equilibrium position, it experiences a force or influence that drives it back to that position. Imagine a ball at the bottom of a bowl: if displaced slightly, gravity will make it oscillate around the lowest point until, if there is friction, it stops again at the bottom. This behaviour is due to the fact that the potential energy of the system is minimum at the equilibrium position — like a valley in a topographic map — and any displacement increases the potential energy.

- **Unstable equilibrium**: A system is in unstable equilibrium if, when slightly displaced from its equilibrium position, the forces present drive it further away. The initial perturbation is amplified, causing the system to move indefinitely away from its initial state. A classic example is a ball at the top of a hill. In terms of potential energy, this corresponds to a maximum — like the summit of a mountain.

- **Indifferent or neutral equilibrium**: A system is in indifferent equilibrium if, when displaced from its equilibrium position, it remains in the new position without experiencing forces that would drive it back or further away. In terms of potential energy, this is characterised by a constant potential energy within a certain range.

There are less common situations, such as semi-stable equilibrium, which occurs when forces are attractive from one side and repulsive from the other. In addition, in systems whose dynamics occur in more than one dimension, the phenomenology can be even more complex.

It is important to note that the classification as stable, unstable or indifferent depends on the system in question and the forces acting on it. The same system can exhibit different types of equilibrium depending on its conditions.

(sec-grados-libertad)=
## Degrees of freedom and constraints

The **degrees of freedom** of a physical system refer to the minimum number of independent coordinates needed to fully describe the state or configuration of the system in space. To better understand this concept, consider the following examples:

- **A spring moving only vertically**: We only need one coordinate, the height, to describe its position. It has a single degree of freedom.

- **A simple pendulum**: Although the pendulum moves in a two-dimensional plane (coordinates $x$ and $y$), it actually has only one degree of freedom because both coordinates are not independent: the length of the pendulum is constant, imposing a restriction on the motion. The pendulum's position can be fully determined by knowing the angle $\theta$ it makes with the vertical. These restrictions are called **constraints**.

- **An insect floating on water**: It can move freely on the water's surface, a two-dimensional plane. It has two degrees of freedom.

In general, the number of degrees of freedom equals the number of system variables minus the number of constraints between them.

Identifying degrees of freedom is crucial for simplifying the analysis. Using independent coordinates that respect the system's constraints makes the equations of motion more manageable.

```{admonition} Derivation of the pendulum equation
:class: example

Let us return to example 2 and analyse the motion of the simple pendulum (see {numref}`fig-pendulo-fuerzas`). In this case, it is much easier to work with a single equation for the angle $\theta$ than with two coupled equations for $x$ and $y$. Let us see how:

**Equations of motion in $x$ and $y$**

From the forces involved in the problem ({eq}`eq:FT` and {eq}`eq:Fg`) we can write the equations of motion:

$$
m\frac{d^2x}{dt^2} = -T\sin\theta
$$ (eq:pendulo-x)

$$
m\frac{d^2y}{dt^2} = -mg + T\cos\theta
$$ (eq:pendulo-y)

**Change to polar coordinates $(l,\, \theta)$**

Since the relationship between the two coordinate systems is $x = l\sin\theta$, $y = l(1 - \cos\theta)$, differentiating we get:

$$
\frac{dx}{dt} = l\cos\theta\,\frac{d\theta}{dt}
$$

$$
\frac{d^2x}{dt^2} = -l\sin\theta\left(\frac{d\theta}{dt}\right)^2 + l\cos\theta\,\frac{d^2\theta}{dt^2}
$$ (eq:d2x)

$$
\frac{dy}{dt} = l\sin\theta\,\frac{d\theta}{dt}
$$

$$
\frac{d^2y}{dt^2} = l\cos\theta\left(\frac{d\theta}{dt}\right)^2 + l\sin\theta\,\frac{d^2\theta}{dt^2}
$$ (eq:d2y)

**Pendulum equation in the coordinate $\theta$**

Substituting {eq}`eq:d2x` and {eq}`eq:d2y` into {eq}`eq:pendulo-x` and {eq}`eq:pendulo-y`, multiplying the first by $\cos\theta$ and the second by $\sin\theta$, and adding them, the tension $T$ is eliminated. After simplification:

$$
\frac{d^2\theta}{dt^2} = -\frac{g}{l}\sin\theta
$$ (eq:pendulo-nolineal)

This second-order differential equation describes the evolution of angle $\theta$ for a simple pendulum. Note that it is **non-linear** due to the $\sin\theta$ term.

The well-known linear pendulum equation is obtained by applying the **small-angle approximation**: for $\theta \ll 1\,\text{rad}$, $\sin\theta \approx \theta$. This gives the linear pendulum equation, valid for small oscillations:

$$
\frac{d^2\theta}{dt^2} = -\frac{g}{l}\,\theta
$$ (eq:pendulo-lineal)

This linear second-order differential equation is much simpler to solve analytically.
```

In multidimensional systems with several degrees of freedom, the concept of equilibrium point generalises and we can obtain not only equilibrium points, but also equilibrium curves, equilibrium surfaces, etc. An example is the water surface when a ship is floating: the ship is in equilibrium at any point on that surface, regardless of its horizontal position. This is a **plane of equilibrium**, a two-dimensional equilibrium condition.

(sec-dinamica-equilibrio)=
## Dynamics around equilibrium

In a physical system, there are two main dynamic behaviours when a system is displaced from its stable equilibrium position: **damping** and **oscillations**. Damping refers to the loss of energy over time, which causes the system to gradually approach the equilibrium condition, typically caused by forces opposing motion such as friction. Oscillation is the repetitive variation in time of one or more physical properties of a system around an equilibrium point.

It is important to note that these two behaviours are **not mutually exclusive**. A system can exhibit damping and oscillations simultaneously. For example, a pendulum oscillates around its equilibrium point, but the amplitude of the oscillations decreases over time due to air friction.

(sec-amortiguamiento)=
## Damping

Damping in a dynamical system occurs when the rate of change of a system variable has the opposite sign to the deviation of that variable from its equilibrium value, as shown in {numref}`fig-amortiguamiento-signo`. Mathematically, if the evolution of that variable is given by:

$$
\frac{d\eta}{dt} = f(\eta)
$$ (eq:amort-general)

for the system to exhibit damping, the function $f(\eta)$ must satisfy the following conditions:

- $f(\eta) < 0$ if $\eta > \eta_{eq}$: the force must act to decrease the variable and bring it closer to equilibrium.
- $f(\eta) = 0$ if $\eta = \eta_{eq}$: the force is zero at equilibrium.
- $f(\eta) > 0$ if $\eta < \eta_{eq}$: the force must act to increase the variable and bring it closer to equilibrium.

```{figure} ../_static/tema1_images/amortiguamiento_signo.png
---
width: 70%
name: fig-amortiguamiento-signo
align: center
---
Scheme of the sign of $f(\eta)$ for damping to occur: always opposite to the deviation from equilibrium $\eta_{eq}$.
```

A special case is **linear damping**, in which $f(\eta)$ is proportional to the displacement from equilibrium:

$$
f(\eta) = -C\left(\eta - \eta_{eq}\right)
$$ (eq:amort-lineal)

where $C$ is a positive constant. The general solution of this type of differential equation is a decreasing exponential, meaning the variable approaches the equilibrium value asymptotically over time.

```{admonition} Analysis of damping in fluids
:class: example

To better understand damping, we will study Example 2 step by step: the free fall of a sphere in a fluid (see {numref}`fig-esfera-caida`).

**Problem definition**

An object falls through a fluid without causing turbulence. The forces acting on it are gravity and the fluid drag force. We neglect buoyancy.

**Equation of motion**

The two forces are gravity, $F_g = -mg$, and drag, $F_a = -bv$. The equation of motion is:

$$
m\frac{dv}{dt} = F_g + F_a = -mg - bv
$$ (eq:caida-libre)

**Equilibrium condition**

The equilibrium velocity $v_{eq}$ is reached when the acceleration is zero, $dv/dt = 0$. Solving:

$$
v_{eq} = -\frac{mg}{b}
$$ (eq:vel-eq)

This means that after a certain time, the object will fall at a constant velocity $v_{eq}$, determined by the balance between gravity and drag.

**Solution of the equation of motion**

We solve {eq}`eq:caida-libre` by separation of variables:

$$
\frac{dv}{bv + mg} = -\frac{1}{m}\,dt
$$

Integrating both sides and solving for the velocity:

$$
v(t) = \left(v_0 + \frac{mg}{b}\right)e^{-bt/m} - \frac{mg}{b}
$$ (eq:vel-tiempo)

where $v_0 = v(0)$ is the initial velocity.

**Analysis of the solution**

The solution {eq}`eq:vel-tiempo` describes the behaviour of a damped system: the velocity of the object approaches the equilibrium velocity {eq}`eq:vel-eq` exponentially. The **time constant** $\tau = m/b$ determines the rate of that process. The larger the object's mass or the smaller the damping constant, the larger $\tau$ and the more slowly the object reaches equilibrium.
```

(sec-oscilaciones)=
## Oscillations

Oscillations in a dynamical system are characterised by the presence of a **restoring force** that opposes the displacement of a variable from its equilibrium point. This force always acts in the direction opposite to the displacement, pushing the system back towards equilibrium. However, due to the inertia of the system, it overshoots the equilibrium point, creating a back-and-forth motion around it.

Mathematically, oscillation can be described by a second-order differential equation:

$$
m\frac{d^2\eta}{dt^2} = f(\eta - \eta_{eq})
$$ (eq:oscilacion-general)

where $f(\eta - \eta_{eq})$ describes the restoring force. For oscillations to occur:

- $f(\eta - \eta_{eq}) > 0$ if $\eta < \eta_{eq}$: the force pushes the variable upward (towards equilibrium).
- $f(\eta - \eta_{eq}) = 0$ if $\eta = \eta_{eq}$: the restoring force is zero at equilibrium.
- $f(\eta - \eta_{eq}) < 0$ if $\eta > \eta_{eq}$: the force pushes the variable downward (towards equilibrium).

````{admonition} Example 5: Mass-spring system
:class: example

A classic example of oscillation is the dynamics of a mass-spring system:

**System definition**

The mass-spring system ({numref}`fig-masa-muelle`) consists of a mass $m$ connected to a spring with elastic constant $\kappa$. Consider a vertical spring with one end fixed and the mass $m$ suspended from its free end.

```{figure} ../_static/tema1_images/masa_muelle.png
---
width: 35%
name: fig-masa-muelle
align: center
---
Mass-spring system at equilibrium with the two forces involved. The $y$ axis points downward (positive direction).
```

We define $y(t)$ as the position of the mass, with origin $y = 0$ where the unstretched spring rests and positive direction downwards. $l_0$ is the elongation of the spring at equilibrium.

**Identification of forces**

The forces acting on the mass are gravity, $F_g = mg$, and the spring restoring force, $F_k = -\kappa y$.

**Equation of motion**

Applying Newton's second law:

$$
m\frac{d^2y}{dt^2} = F_g + F_k = mg - \kappa y
$$ (eq:muelle-newton)

**Simplification and solution**

At the equilibrium position ($y = l_0$), acceleration is zero, so $mg = \kappa l_0$. Substituting into the equation of motion:

$$
m\frac{d^2y}{dt^2} = -\kappa\left(y - l_0\right)
$$ (eq:muelle-eq)

This differential equation is that of a linear oscillator. As we will see in the next chapter, the general solution is:

$$
y(t) = l_0 + A\cos\left(\omega_0 t + \varphi\right)
$$ (eq:muelle-sol)

where:
- $A$ is the **amplitude**: the maximum displacement from the equilibrium position.
- $\omega_0$ is the **natural angular frequency**, given by:

$$
\omega_0 = \sqrt{\frac{\kappa}{m}}
$$ (eq:omega0)

- $\varphi$ is the **initial phase**, which defines the position of the mass at $t = 0$.

The constants $A$ and $\varphi$ are determined from the initial conditions of the problem (initial position and velocity of the mass).
````

```{admonition} Summary: two routes to equilibrium
:class: tip

- A system is **damped** in one of its variables if the rate of change of the variable has the opposite sign to the deviation of that variable from its equilibrium value.
- A system **oscillates** in one of its variables if the force acts in the opposite direction to the displacement from the equilibrium point.
```

(sec-mapas-energia)=
## Energy maps and gravitational analogy

The last part of this chapter focuses on the concepts of potential energy, potential energy maps and the gravitational analogy. These concepts are essential for understanding the behaviour of physical systems, especially those that exhibit oscillatory motion, without having to solve complex equations of motion.

### Potential energy

**Potential energy** is defined as the energy possessed by an object due to its position or configuration in a force field. It is the energy stored in a system as a result of work done against a conservative force. A **conservative force** is one in which the work done to move an object from one point to another does not depend on the path taken, but only on the initial and final points.

In a one-dimensional system, potential energy can be calculated using:

$$
U(b) - U(a) = -\int_a^b F(x)\,dx
$$ (eq:energia-potencial)

where $U$ is the potential energy, $F(x)$ is the conservative force acting on the object and $x$ is the position.

A key aspect is that the force can be obtained as the negative derivative of the potential energy with respect to position:

$$
F(x) = -\frac{dU(x)}{dx}
$$ (eq:fuerza-potencial)

In systems with more dimensions, the derivative with respect to the coordinate is replaced by the gradient.

### Potential energy maps

**Potential energy maps** (or potential energy diagrams) are graphical representations of $U$ as a function of position. Since the equilibrium condition occurs when the force is zero (and therefore when $dU/dx = 0$), the equilibrium points coincide with the extrema of the potential energy map:

- **Minima** of $U$ (valleys) correspond to **stable equilibrium** points.
- **Maxima** of $U$ (peaks) correspond to **unstable equilibrium** points.

{numref}`fig-mapa-energia` shows an example of a potential energy map.

```{figure} ../_static/tema1_images/mapa_energia_potencial.png
---
width: 60%
name: fig-mapa-energia
align: center
---
Potential energy map showing stable equilibrium points (B and D, minima) and unstable equilibrium points (A and C, maxima).
```

By analysing the shape of the potential energy map we can predict the motion of the system. For example, in a potential well, an object will oscillate around the stable equilibrium point.

### Gravitational analogy

The **gravitational analogy** is a conceptual tool that uses our intuitive experience with gravity to understand systems with different types of forces. The key idea is that if two systems — even if physically different — have potential energy maps with the same shape, their motions will be qualitatively similar.

In the case of gravitational potential energy, energy is proportional to height $h$, so the topographic landscape itself acts as a potential energy map (a roller coaster is a good example).

The motion of a mass attached to a spring, experiencing an elastic restoring force, can be visualised as the motion of an object in an equivalent gravitational field. The potential energy of a spring is proportional to the square of its deformation from the equilibrium position (you can prove this from {eq}`eq:energia-potencial`):

$$
U(x) = \frac{1}{2}\kappa x^2 \quad \Rightarrow \quad h(x) = \frac{\kappa}{2mg}x^2 = Ax^2
$$ (eq:potencial-muelle)

This generates a **parabolic** potential energy map ({numref}`fig-analogia-gravitatoria`), which predicts simple harmonic oscillatory motion around the equilibrium point.

```{figure} ../_static/tema1_images/analogia_gravitatoria.png
---
width: 55%
name: fig-analogia-gravitatoria
align: center
---
Gravitational analogy for the spring: the parabolic potential energy $U(x) = \frac{1}{2}\kappa x^2$ is equivalent to a hill with profile $h(x) = Ax^2$, predicting simple harmonic oscillations.
```

It is important to bear in mind the **limitations** of the gravitational analogy:

- It does not account for non-conservative forces, such as friction, which can dissipate energy and modify the motion of the system.
- In non-inertial reference frames, where fictitious forces such as the Coriolis force act, the analogy is not directly applicable without modifications.

In summary, potential energy, potential energy maps and the gravitational analogy are powerful conceptual tools for understanding the behaviour of a wide range of physical systems. However, it is crucial to be aware of their limitations and to consider the influence of other factors, such as non-conservative forces and non-inertial reference frames.

<!--
```{admonition} Chapter 1 Summary

**Synthesis of Concepts**

In this first chapter of the course, we have explored the concept of equilibrium as the indispensable reference point for analysing any dynamic system. We have seen that, beyond the intuitive idea of "absence of movement", equilibrium is a stationary state where a property ceases to evolve in time. By grounding this idea in mechanics, we have understood that the magnitude that is actually in equilibrium is velocity, since when the net force is zero, it remains constant. This has allowed us to see that an object at rest is only a particular case of this broader phenomenon.

Throughout the chapter, we have learned to classify equilibrium according to its stability, analysing how a system responds to small perturbations. Through visual analogies, such as a ball in a bowl or on top of a hill, we have differentiated between stable equilibrium (where the system tends to return to its initial state), unstable equilibrium (where the perturbation is amplified) and neutral equilibrium. This distinction has been fundamental to connect the geometry of potential energy maps with dynamics: energy minima act as valleys of stability, while maxima act as unstable peaks.

To simplify the study of complex systems, we have introduced degrees of freedom, learning to identify the minimum number of independent coordinates necessary to fully describe a system. We have seen how constraints, such as the constant length of the string in a pendulum, allow us to reduce the number of variables and handle much simpler equations of motion.

From there, we have studied the two main routes a system follows when displaced from its stable equilibrium: damping and oscillation. Through the example of a sphere falling in a fluid, we have seen how dissipative forces cause the system to lose energy and gradually seek its equilibrium condition. On the other hand, we have analysed how restoring forces, like those of a spring, create a repetitive back-and-forth movement. Finally, thanks to the gravitational analogy, we have discovered that any potential with a parabolic shape will always generate a simple harmonic oscillatory motion.

**Connection Map**

This last finding serves as our bridge to the rest of the course. Chapter 2 will allow us to delve exclusively into the simple harmonic oscillator. We will study this universal model as the basis for understanding different physical systems before launching into the study of more complex phenomena.
```
-->
