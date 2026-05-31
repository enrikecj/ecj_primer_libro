# TEMA 1. EQUILIBRIO, AMORTIGUAMIENTO Y OSCILACIONES

## Equilibrio

En este primer tema vamos a introducir algunos conceptos que son necesarios para entender bien lo que estudiaremos a continuación. El primero de ellos es el concepto de equilibrio. A lo largo de buena parte de la asignatura vamos a estudiar oscilaciones y ondas, que son fenómenos dinámicos, pero es necesario empezar por el equilibrio. Aunque puede parecer que no tiene mucha relación con esos fenómenos, basta darse cuenta de que las oscilaciones de un sistema se producen generalmente alrededor de un punto de equilibrio. El concepto de equilibrio es esencial para el estudio de la dinámica de los sistemas porque nos proporciona el punto de referencia a partir del cual podemos analizar y comprender cómo los sistemas cambian y evolucionan en el tiempo. Por ello, es imprescindible entender bien qué es un punto de equilibrio y, más en general, a qué nos referimos (al menos en esta asignatura) cuando hablamos de equilibrio.

La primera idea cuando hablamos de equilibrio es pensar en la ausencia de movimiento, pero eso no es más que un caso muy particular de equilibrio. Ni siquiera coincide con lo que es el equilibrio mecánico, que ocurre cuando la resultante de las fuerzas que actúan sobre un sistema es igual a cero. Sin embargo, el concepto de equilibrio va más allá de la mecánica. Sin salirnos de la física, podemos hablar de otros tipos de equilibrio:

- **Equilibrio térmico**: Se refiere a la situación en la que dos o más sistemas en contacto térmico se encuentran a la misma temperatura. En este estado, no hay flujo neto de calor entre los sistemas.
- **Equilibrio termodinámico**: Un sistema se encuentra en equilibrio termodinámico cuando no experimenta cambios macroscópicos a lo largo del tiempo y todas sus partes están en equilibrio mecánico, térmico y químico. Este tipo de equilibrio implica que las variables termodinámicas del sistema, como la temperatura, la presión y el potencial químico, son uniformes.
- **Equilibrio en circuitos eléctricos**: En un circuito eléctrico, el equilibrio se alcanza cuando la corriente y el voltaje en cada punto del circuito permanecen constantes en el tiempo.

Más allá de la física, podemos hablar de equilibrio en muchas otras disciplinas:

- **Equilibrio químico**: En química, el equilibrio se refiere al estado en el cual las concentraciones de reactivos y productos en una reacción química reversible se mantienen constantes a lo largo del tiempo. En este punto, las velocidades de la reacción directa e inversa son iguales, y no hay cambios netos en la composición del sistema.
- **Equilibrio genético**: En genética de poblaciones, el equilibrio se describe como un estado en el cual las frecuencias alélicas y genotípicas en una población permanecen constantes a través de generaciones. Este estado se alcanza cuando no hay factores evolutivos que actúen sobre la población, como la mutación, la selección natural, la deriva genética, o el flujo genético.
- **Equilibrio social**: En sociología, el equilibrio social se refiere a un estado de relativa estabilidad y orden en una sociedad, donde las diferentes partes del sistema social funcionan de manera armoniosa. Este estado implica un equilibrio de poder entre los diferentes grupos sociales, así como la aceptación generalizada de las normas y valores sociales.
- **Equilibrio económico**: En economía, el equilibrio es un estado en el cual las fuerzas de la oferta y la demanda están equilibradas. En esta situación, no hay tendencia a que los precios o las cantidades cambien.
- **Equilibrio en matemáticas**: En matemáticas, un punto de equilibrio de un sistema de ecuaciones diferenciales es un punto en el que el sistema no cambia con el tiempo. En otras palabras, es un estado estacionario del sistema.

Para que un sistema esté en equilibrio no basta con que una de sus propiedades esté en equilibrio, sino que todas las magnitudes que lo caracterizan deben estarlo. Eso es una condición muy exigente en sistemas que estén descritos por varias magnitudes. Por eso nosotros vamos a hablar de equilibrio de las propiedades de un sistema. Un sistema físico puede estar evolucionando en el tiempo con ciertas magnitudes, por ejemplo, las velocidades, y sin embargo tener otras magnitudes que no cambian en el tiempo, como una aceleración constante.

Pensemos por tanto en una magnitud de un sistema que vamos a denotar con la letra $\eta$. Diremos que esa propiedad está en equilibrio si no evoluciona en el tiempo. Matemáticamente podemos escribirlo con la expresión:

$$
\frac{d\eta}{dt} = 0
$$ (1.1)

## Equilibrio mecánico

En el caso del equilibrio mecánico, aunque a veces se hable de "equilibrio de fuerzas", no es la fuerza la magnitud que está en equilibrio, sino la velocidad: Dado que la definición de equilibrio mecánico es que la fuerza neta, y no su derivada, sea cero, $\vec{F} = 0$, a partir de la segunda ley de Newton, $\vec{F} = m\vec{a}$, y teniendo en cuenta que la aceleración es la derivada de la velocidad, tenemos que:

$$
\vec{F} = m\frac{d\vec{v}}{dt} = 0 \implies \frac{d\vec{v}}{dt} = 0
$$ (1.2)

por lo que es la velocidad la magnitud que está en equilibrio.

En cuanto a la posición, no es una propiedad que tenga que estar en equilibrio cuando hablamos de equilibrio mecánico. Un objeto que está en reposo y no se desplaza en un sistema de referencia dado es solo un caso particular de equilibrio mecánico.

Veamos unos cuantos ejemplos de equilibrio en física:

### Ejemplo 1. Condición de equilibrio de un péndulo simple

La condición de equilibrio en un péndulo se produce cuando la velocidad del péndulo es constante. Esto ocurre cuando el péndulo está en reposo en su posición vertical inferior (ángulo cero con respecto a la vertical).

```{figure} ../_static/tema1_images/page3_img1.jpeg
---
width: 30%
name: fig-pendulo-fuerzas
align: center
---
Esquema de las fuerzas que intervienen en el péndulo simple.
```

Veamos cómo deducirlo matemáticamente paso a paso:

#### 1. Identificar las fuerzas:

Las fuerzas que actúan sobre la masa del péndulo (Ver {numref}`fig-pendulo-fuerzas`) son la tensión $T$ de la cuerda y el peso $\vec{F}_g = -mg \hat{e}_y$ (donde el signo menos indica que apunta en sentido negativo del eje vertical).

#### 2. Proyectar las fuerzas en los ejes:

Se descomponen las fuerzas en sus componentes horizontal (eje $x$) y vertical (eje $y$).

$$
\vec{F}_T = -T\sin\theta\hat{e}_x + T\cos\theta\hat{e}_y
$$ (1.3)
$$
\vec{F}_g = -mg\hat{e}_y
$$ (1.4)

#### 3. Aplicar la condición de equilibrio:

Para que la velocidad sea constante, la aceleración debe ser cero. Según la segunda ley de Newton, esto implica que la suma de las fuerzas en cada eje debe ser igual a cero.

- **Equilibrio en x**: $-T \sin \theta = 0$
- **Equilibrio en y**: $T \cos \theta - mg = 0$

#### 4. Resolver las ecuaciones:

La ecuación para el eje horizontal implica que $\sin \theta = 0$, lo que significa que $\theta = 0$ (posición vertical). Sustituyendo esta condición en la ecuación para el eje $y$, se obtiene $T = mg$, lo que significa que la tensión es igual al peso en la posición de equilibrio.

#### Conclusión:

> La condición de equilibrio en un péndulo simple se cumple cuando el ángulo $\theta$ es cero, lo que corresponde a la posición vertical inferior. En este punto, la tensión de la cuerda es igual al peso y, además de no haber aceleración, la velocidad debe ser nula para mantener la condición de equilibrio, ya que si no lo fuera variaría el ángulo del péndulo y dejaría de estar en equilibrio.
