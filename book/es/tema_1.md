# Tema 1. Equilibrio, amortiguamiento y oscilaciones

## Introducción al equilibrio

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
$$ (eq:eta)

## Equilibrio mecánico

En el caso del equilibrio mecánico, aunque a veces se hable de "equilibrio de fuerzas", no es la fuerza la magnitud que está en equilibrio, sino la velocidad: Dado que la definición de equilibrio mecánico es que la fuerza neta, y no su derivada, sea cero, $\vec{F} = 0$, a partir de la segunda ley de Newton, $\vec{F} = m\vec{a}$, y teniendo en cuenta que la aceleración es la derivada de la velocidad, tenemos que:

$$
\vec{F} = m\frac{d\vec{v}}{dt} = 0 \implies \frac{d\vec{v}}{dt} = 0
$$ (eq:force)

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

**Identificar las fuerzas:**

Las fuerzas que actúan sobre la masa del péndulo (Ver {numref}`fig-pendulo-fuerzas`) son la tensión $T$ de la cuerda y el peso $\vec{F}_g = -mg \hat{e}_y$ (donde el signo menos indica que apunta en sentido negativo del eje vertical).

**Proyectar las fuerzas en los ejes:**

Se descomponen las fuerzas en sus componentes horizontal (eje $x$) y vertical (eje $y$).

$$
\vec{F}_T = -T\sin\theta\,\hat{e}_x + T\cos\theta\,\hat{e}_y
$$ (eq:FT)
$$
\vec{F}_g = -mg\,\hat{e}_y
$$ (eq:Fg)

**Aplicar la condición de equilibrio:**

Para que la velocidad sea constante, la aceleración debe ser cero. Según la segunda ley de Newton, esto implica que la suma de las fuerzas en cada eje debe ser igual a cero.

- **Equilibrio en x**: $\quad -T \sin \theta = 0$
- **Equilibrio en y**: $\quad T \cos \theta - mg = 0$

**Resolver las ecuaciones:**

La ecuación para el eje horizontal implica que $\sin \theta = 0$, lo que significa que $\theta = 0$ (posición vertical). Sustituyendo esta condición en la ecuación para el eje $y$, se obtiene $T = mg$, lo que significa que la tensión es igual al peso en la posición de equilibrio.

**Conclusión:**

> La condición de equilibrio en un péndulo simple se cumple cuando el ángulo $\theta$ es cero, lo que corresponde a la posición vertical inferior. En este punto, la tensión de la cuerda es igual al peso y, además de no haber aceleración, la velocidad debe ser nula para mantener la condición de equilibrio, ya que si no lo fuera variaría el ángulo del péndulo y dejaría de estar en equilibrio.

### Ejemplo 2. Condición de equilibrio de una esfera en caída libre con rozamiento

En el caso de un objeto esférico que cae en un fluido con rozamiento, el equilibrio mecánico también viene dado por la compensación de las fuerzas que actúan sobre la esfera. Para simplificar las cosas, pensemos que el medio en el que se produce la caída es el aire y que, al ser su densidad mucho menor que la de la esfera, podemos despreciar el empuje. En ese caso, las dos fuerzas que actúan sobre el objeto son el peso y la fuerza de arrastre (Ver {numref}`fig-esfera-caida`), que da cuenta del efecto del rozamiento. Dependiendo de las características del fluido y si la velocidad de caída no es muy grande, podemos asumir que la fuerza de arrastre es proporcional a la velocidad $v$ (ley de Stokes). Concretamente, para una esfera la fuerza de arrastre es:

$$
F_a = -6\pi\mu r v = -bv
$$ (eq:stokes)

siendo $\mu$ la viscosidad dinámica y $r$ el radio de la esfera.

```{figure} ../_static/tema1_images/esfera_caida_libre.png
---
width: 50%
name: fig-esfera-caida
align: center
---
Fuerzas que actúan sobre una esfera en caída libre con rozamiento: el peso $F_g = -mg$ hacia abajo y la fuerza de arrastre $F_a = -bv$ que se opone al movimiento.
```

Puedes intentar encontrar la condición de equilibrio en este caso. En la sección de [Amortiguamiento](sec-amortiguamiento) lo resolveremos paso a paso.

## Otros tipos de equilibrio

### Ejemplo 3. Equilibrio térmico

Como sabemos, dos objetos en contacto están en equilibrio térmico si no hay transferencia de energía térmica entre ellos. Supongamos una geometría como la que se muestra en la {numref}`fig-equilibrio-termico`. La ecuación que rige la dinámica del sistema es:

$$
\frac{dq}{dt} = -A\frac{k}{L}(T_2 - T_1)
$$ (eq:fourier)

donde $q$ es la energía calórica, $A$ es el área de la zona de la unión, $k$ es su conductividad térmica, $L$ es su longitud, $T_1$ es la temperatura del primer cuerpo y $T_2$ es la temperatura del segundo. Una simple ojeada a esta ecuación nos indica que el equilibrio térmico se produce cuando las temperaturas de los dos cuerpos son iguales ($T_1 = T_2$), haciendo que la derivada temporal de $q$ se anule.

```{figure} ../_static/tema1_images/equilibrio_termico.png
---
width: 55%
name: fig-equilibrio-termico
align: center
---
Dos objetos a diferente temperatura con una zona de unión de área $A$, longitud $L$ y conductividad térmica $k$.
```

### Ejemplo 4. Equilibrio en un circuito eléctrico

Pensemos por ejemplo en un circuito RL en serie como el de la {numref}`fig-circuito-rl`, con una resistencia y una bobina, en el que queremos encontrar la condición de equilibrio de la intensidad de corriente.

```{figure} ../_static/tema1_images/circuito_rl.png
---
width: 55%
name: fig-circuito-rl
align: center
---
Circuito RL en serie.
```

¿Cómo hallarías esa condición de equilibrio?

(sec-puntos-equilibrio)=
## Puntos de equilibrio

En general, la condición de equilibrio para una magnitud no se va a dar para todos los valores de las variables de las que depende, sino solamente para algunos. Por ejemplo, si el sistema que consideramos depende de dos variables, $\eta$ e $x$, y la ecuación de movimiento es:

$$
\frac{d\eta}{dt} = f(\eta, x)
$$ (eq:eq-motion-general)

entonces $x_0$ es un **punto de equilibrio** si $f(\eta, x_0) = 0$, de forma que en ese punto se cumple que:

$$
\frac{d\eta}{dt} = f(\eta, x_0) = 0
$$ (eq:eq-point)

El concepto de punto de equilibrio no es estrictamente geométrico: la variable $x$ puede ser una posición, pero también una temperatura, una concentración química, etc.

En el caso del equilibrio mecánico, sabemos que la condición que lo define es que la fuerza total sea nula. Cuando la fuerza no es homogénea en todo el espacio, tendremos que el equilibrio se producirá en los puntos $\vec{r}_0$ en los que $\vec{F}(\vec{r}_0) = 0$.

Retomemos el caso del péndulo simple (Ejemplo 1). Habíamos visto que el equilibrio se producía cuando $\sin\theta = 0$. Como en nuestro sistema de coordenadas ({numref}`fig-pendulo-fuerzas`) $x = l\sin\theta$, $y = l(1 - \cos\theta)$, el punto de equilibrio del sistema será:

$$
(x_{eq},\, y_{eq}) = (0, 0)
$$ (eq:pendulo-eq-point)

es decir, nuestro origen de coordenadas.

Puedes intentar hallar los puntos de equilibrio en otros sistemas, por ejemplo un muelle del que cuelga una masa, o un objeto que flota parcialmente sumergido en un líquido.

(sec-estabilidad)=
## Estabilidad del equilibrio

El equilibrio de un sistema puede ser clasificado en tres tipos principales: estable, inestable e indiferente (Ver {numref}`fig-tipos-equilibrio`). Esta clasificación se basa en la respuesta del sistema ante pequeñas perturbaciones o desplazamientos desde su posición de equilibrio.

```{figure} ../_static/tema1_images/tipos_equilibrio.png
---
width: 85%
name: fig-tipos-equilibrio
align: center
---
Esquema con los tres tipos de equilibrio: estable (izquierda), inestable (centro) e indiferente (derecha).
```

- **Equilibrio estable**: Un sistema se encuentra en equilibrio estable si, al ser desplazado ligeramente de su posición de equilibrio, experimenta una fuerza o influencia que lo impulsa a regresar a dicha posición. En otras palabras, se caracteriza por la tendencia del sistema a restaurar su estado inicial después de una perturbación. Imaginemos una pelota en el fondo de un cuenco: si la desplazamos un poco de su posición de reposo, la gravedad la hará oscilar alrededor del punto más bajo hasta que, si hay rozamiento, finalmente se detenga de nuevo en el fondo. Este comportamiento se debe a que la energía potencial del sistema es mínima en la posición de equilibrio —como un valle en un mapa topográfico— y cualquier desplazamiento desde esta posición implica un aumento de la energía potencial.

- **Equilibrio inestable**: Un sistema está en equilibrio inestable si, al ser desplazado levemente de su posición de equilibrio, las fuerzas presentes lo alejan aún más de dicha posición. La perturbación inicial se amplifica, provocando que el sistema se aleje indefinidamente de su estado inicial. Un ejemplo clásico es una pelota en la cima de una colina. Desde el punto de vista de la energía potencial, corresponde a un máximo —como la cima de una montaña.

- **Equilibrio indiferente o neutro**: Un sistema se encuentra en equilibrio indiferente si, al ser desplazado de su posición de equilibrio, permanece en la nueva posición sin experimentar fuerzas que lo impulsen a regresar o a alejarse. En términos de energía potencial, se caracteriza por una energía potencial constante dentro de un cierto rango.

Hay situaciones menos habituales, como el equilibrio semiestable, que ocurre cuando las fuerzas son atractivas desde uno de los lados y repulsivas desde el otro. Además, en sistemas cuya dinámica ocurre en más de una dimensión, la fenomenología puede ser todavía más complicada.

Es importante destacar que la clasificación como estable, inestable o indiferente depende del sistema en cuestión y de las fuerzas que actúan sobre él. Un mismo sistema puede presentar diferentes tipos de equilibrio dependiendo de las condiciones en las que se encuentre.

(sec-grados-libertad)=
## Grados de libertad y ligaduras

Los **grados de libertad** en un sistema físico se refieren al número mínimo de coordenadas independientes necesarias para describir completamente el estado o la configuración de un sistema en el espacio. Para comprender mejor este concepto, consideremos los siguientes ejemplos:

- **Un muelle que solo se mueve verticalmente**: Solo necesitamos una coordenada, la altura, para describir su posición. Tiene un único grado de libertad.

- **Un péndulo simple**: Aunque el péndulo se mueve en un plano bidimensional (coordenadas $x$ e $y$), en realidad solo tiene un grado de libertad porque ambas coordenadas no son independientes entre sí: la longitud del péndulo es constante, lo que impone una restricción al movimiento. La posición del péndulo se puede determinar completamente conociendo el ángulo $\theta$ que forma con la vertical. Este tipo de restricciones se denominan **ligaduras**.

- **Un insecto flotando en agua**: Puede moverse libremente en la superficie del agua, un plano bidimensional. Tiene dos grados de libertad.

En general, el número de grados de libertad será igual al número de variables del sistema menos el número de ligaduras entre ellas.

La identificación de los grados de libertad es crucial para simplificar el análisis. Al utilizar las coordenadas independientes que respetan las restricciones del sistema, las ecuaciones de movimiento se vuelven más manejables.

Retomemos el ejemplo 2 y analicemos el movimiento del péndulo simple (ver {numref}`fig-pendulo-fuerzas`). En este caso es mucho más fácil trabajar con una sola ecuación para el ángulo $\theta$ que con dos ecuaciones acopladas para $x$ e $y$. Veámoslo:

**Ecuaciones de movimiento en $x$ e $y$**

A partir de las fuerzas que intervienen en el problema ({eq}`eq:FT` y {eq}`eq:Fg`) podemos escribir las ecuaciones de movimiento:

$$
m\frac{d^2x}{dt^2} = -T\sin\theta
$$ (eq:pendulo-x)

$$
m\frac{d^2y}{dt^2} = -mg + T\cos\theta
$$ (eq:pendulo-y)

**Cambio a coordenadas polares $(l,\, \theta)$**

Como la relación entre los dos sistemas de coordenadas es $x = l\sin\theta$, $y = l(1 - \cos\theta)$, derivando tenemos:

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

**Ecuación del péndulo en la coordenada $\theta$**

Sustituyendo {eq}`eq:d2x` y {eq}`eq:d2y` en {eq}`eq:pendulo-x` y {eq}`eq:pendulo-y`, multiplicando la primera por $\cos\theta$ y la segunda por $\sin\theta$, y sumando ambas, se elimina la tensión $T$. Después de la simplificación, se llega a:

$$
\frac{d^2\theta}{dt^2} = -\frac{g}{l}\sin\theta
$$ (eq:pendulo-nolineal)

Esta ecuación diferencial de segundo orden describe la evolución del ángulo $\theta$ para un péndulo simple. Es importante notar que **no es lineal** debido al término $\sin\theta$.

La conocida ecuación lineal del péndulo ideal se obtiene al hacer la **aproximación de ángulos pequeños**: para $\theta \ll 1\,\text{rad}$, $\sin\theta \approx \theta$. Usando esta aproximación se obtiene la ecuación lineal del péndulo, válida para pequeñas oscilaciones:

$$
\frac{d^2\theta}{dt^2} = -\frac{g}{l}\,\theta
$$ (eq:pendulo-lineal)

Esta ecuación diferencial lineal de segundo orden es mucho más sencilla de resolver analíticamente.

En los sistemas multidimensionales en los cuales tenemos varios grados de libertad, el concepto de punto de equilibrio se generaliza y podemos obtener no solo puntos de equilibrio, sino también curvas de equilibrio, superficies de equilibrio, etc. Un ejemplo es la superficie del agua cuando tenemos un barco flotando: el barco está en equilibrio en cualquier punto de esa superficie, independientemente de su posición horizontal. En este caso estaríamos hablando de un **plano de equilibrio**, de una condición de equilibrio bidimensional.

(sec-dinamica-equilibrio)=
## Dinámica alrededor del equilibrio

En un sistema físico, hay dos comportamientos dinámicos principales cuando un sistema es desplazado de su posición de equilibrio estable: el **amortiguamiento** y las **oscilaciones**. El amortiguamiento se refiere a la pérdida de energía a lo largo del tiempo, lo que hace que el sistema evolucione hacia la condición de equilibrio gradualmente, normalmente causado por fuerzas que se oponen al movimiento como la fricción. Por su parte, la oscilación es la variación repetitiva en el tiempo de una o más propiedades físicas de un sistema alrededor de un punto de equilibrio.

Es importante tener en cuenta que estos dos comportamientos **no son mutuamente excluyentes**. Un sistema puede exhibir amortiguamiento y oscilaciones al mismo tiempo. Por ejemplo, un péndulo oscila alrededor de su punto de equilibrio, pero la amplitud de las oscilaciones disminuye con el tiempo debido a la fricción del aire.

(sec-amortiguamiento)=
## Amortiguamiento

El amortiguamiento, en un sistema dinámico, ocurre cuando la tasa de cambio de una variable del sistema es de signo opuesto a la desviación de esa variable con respecto a su valor de equilibrio, como se muestra en la {numref}`fig-amortiguamiento-signo`. Matemáticamente, si la evolución de esa variable viene dada por la ecuación:

$$
\frac{d\eta}{dt} = f(\eta)
$$ (eq:amort-general)

para que el sistema presente amortiguamiento, la función $f(\eta)$ debe cumplir las siguientes condiciones:

- $f(\eta) < 0$ si $\eta > \eta_{eq}$: la fuerza debe actuar para disminuir la variable y acercarla al equilibrio.
- $f(\eta) = 0$ si $\eta = \eta_{eq}$: la fuerza es cero en el equilibrio.
- $f(\eta) > 0$ si $\eta < \eta_{eq}$: la fuerza debe actuar para aumentar la variable y acercarla al equilibrio.

```{figure} ../_static/tema1_images/amortiguamiento_signo.png
---
width: 70%
name: fig-amortiguamiento-signo
align: center
---
Esquema del signo de la función $f(\eta)$ para que haya amortiguamiento: siempre opuesto a la desviación respecto del equilibrio $\eta_{eq}$.
```

Un caso especial es el **amortiguamiento lineal**, en el que $f(\eta)$ es proporcional al desplazamiento desde el equilibrio:

$$
f(\eta) = -C\left(\eta - \eta_{eq}\right)
$$ (eq:amort-lineal)

siendo $C$ una constante positiva. La solución general para este tipo de ecuación diferencial es una función exponencial decreciente, lo que significa que la variable se acerca asintóticamente al valor de equilibrio con el tiempo.

Para entender mejor el concepto de amortiguamiento, vamos a estudiar paso a paso el Ejemplo 2: la caída libre de un objeto esférico en un fluido (ver {numref}`fig-esfera-caida`).

**Definición del problema**

Un objeto cae dentro de un fluido sin causar turbulencias. Actúan sobre él la fuerza de gravedad y la fuerza de arrastre del fluido. Por simplicidad despreciamos el empuje.

**Ecuación de movimiento**

Las dos fuerzas involucradas son la de la gravedad, $F_g = -mg$, y la de arrastre, $F_a = -bv$. La ecuación de movimiento es:

$$
m\frac{dv}{dt} = F_g + F_a = -mg - bv
$$ (eq:caida-libre)

**Condición de equilibrio**

La velocidad de equilibrio $v_{eq}$ se alcanza cuando la aceleración del objeto es cero, $dv/dt = 0$. Resolviendo, obtenemos:

$$
v_{eq} = -\frac{mg}{b}
$$ (eq:vel-eq)

Esto significa que después de un cierto tiempo, el objeto caerá a una velocidad constante $v_{eq}$, determinada por el equilibrio entre la fuerza de gravedad y la fuerza de arrastre.

**Solución de la ecuación de movimiento**

Resolvemos {eq}`eq:caida-libre` por separación de variables:

$$
\frac{dv}{bv + mg} = -\frac{1}{m}\,dt
$$

Integrando ambos lados y despejando la velocidad, obtenemos:

$$
v(t) = \left(v_0 + \frac{mg}{b}\right)e^{-bt/m} - \frac{mg}{b}
$$ (eq:vel-tiempo)

donde $v_0 = v(0)$ es la velocidad inicial.

**Análisis de la solución**

La solución {eq}`eq:vel-tiempo` describe el comportamiento de un sistema amortiguado: la velocidad del objeto se acerca exponencialmente a la velocidad de equilibrio {eq}`eq:vel-eq`. La **constante de tiempo** $\tau = m/b$ determina la rapidez de ese proceso. Cuanto mayor sea la masa del objeto o menor sea la constante de amortiguamiento, mayor será $\tau$ y más lentamente alcanzará el objeto el equilibrio.

(sec-oscilaciones)=
## Oscilaciones

Las oscilaciones en un sistema dinámico se caracterizan por la presencia de una **fuerza restauradora** que se opone al desplazamiento de una variable con respecto a su punto de equilibrio. Esta fuerza siempre actúa en dirección opuesta al desplazamiento, empujando al sistema de vuelta hacia el equilibrio. Sin embargo, debido a la inercia del sistema, este sobrepasa el punto de equilibrio, creando un movimiento de vaivén alrededor de dicho punto.

Matemáticamente, la oscilación se puede describir mediante una ecuación diferencial de segundo orden:

$$
m\frac{d^2\eta}{dt^2} = f(\eta - \eta_{eq})
$$ (eq:oscilacion-general)

donde $f(\eta - \eta_{eq})$ describe la fuerza restauradora. Para que haya oscilaciones debe cumplirse:

- $f(\eta - \eta_{eq}) > 0$ si $\eta < \eta_{eq}$: la fuerza empuja la variable hacia arriba (hacia el equilibrio).
- $f(\eta - \eta_{eq}) = 0$ si $\eta = \eta_{eq}$: la fuerza restauradora es cero en el equilibrio.
- $f(\eta - \eta_{eq}) < 0$ si $\eta > \eta_{eq}$: la fuerza empuja la variable hacia abajo (hacia el equilibrio).

### Ejemplo 5: Sistema masa-muelle

Un ejemplo clásico de oscilación es la dinámica de un sistema masa-muelle:

**Definición del sistema**

El sistema masa-muelle ({numref}`fig-masa-muelle`) se compone de una masa $m$ conectada a un resorte de constante elástica $\kappa$. Consideremos un muelle vertical con un extremo fijo y la masa $m$ suspendida en su extremo libre.

```{figure} ../_static/tema1_images/masa_muelle.png
---
width: 35%
name: fig-masa-muelle
align: center
---
Sistema masa-muelle en la posición de equilibrio con las dos fuerzas que intervienen. El eje $y$ apunta en sentido positivo hacia abajo.
```

Definimos $y(t)$ como la posición de la masa, con el origen $y = 0$ donde el muelle sin la masa no está estirado y sentido positivo hacia abajo. $l_0$ representa la elongación del muelle en la posición de equilibrio.

**Identificación de las fuerzas**

Las fuerzas que actúan sobre la masa son la fuerza de gravedad, $F_g = mg$, y la fuerza restauradora del muelle, $F_k = -\kappa y$.

**Ecuación de movimiento**

Aplicando la segunda ley de Newton:

$$
m\frac{d^2y}{dt^2} = F_g + F_k = mg - \kappa y
$$ (eq:muelle-newton)

**Simplificación y solución**

En la posición de equilibrio ($y = l_0$), la aceleración es cero, por lo que $mg = \kappa l_0$. Sustituyendo en la ecuación de movimiento:

$$
m\frac{d^2y}{dt^2} = -\kappa\left(y - l_0\right)
$$ (eq:muelle-eq)

Esta ecuación diferencial es la de un oscilador con fuerza lineal. Como veremos en el tema siguiente, la solución general es:

$$
y(t) = l_0 + A\cos\left(\omega_0 t + \varphi\right)
$$ (eq:muelle-sol)

donde:
- $A$ es la **amplitud** de la oscilación: el desplazamiento máximo desde la posición de equilibrio.
- $\omega_0$ es la **frecuencia angular** natural, dada por:

$$
\omega_0 = \sqrt{\frac{\kappa}{m}}
$$ (eq:omega0)

- $\varphi$ es la **fase inicial**, que define la posición de la masa en $t = 0$.

Las constantes $A$ y $\varphi$ se determinan a partir de las condiciones iniciales del problema (posición y velocidad iniciales de la masa).

```{admonition} Resumen: dos rutas hacia el equilibrio
:class: tip

- Un sistema está **amortiguado** en una de sus variables si la tasa de cambio de la variable es de signo opuesto a la desviación de esa variable respecto a su valor de equilibrio.
- Un sistema **oscila** en una de sus variables si la fuerza tiene el sentido contrario al desplazamiento respecto del punto de equilibrio.
```

(sec-mapas-energia)=
## Mapas de energía y analogía gravitatoria

La última parte de este tema se centra en los conceptos de energía potencial, mapas de energía potencial y la analogía gravitatoria. Estos conceptos son esenciales para comprender el comportamiento de los sistemas físicos, especialmente aquellos que exhiben movimiento oscilatorio, sin necesidad de resolver ecuaciones de movimiento complejas.

### Energía potencial

La **energía potencial** se define como la energía que posee un objeto debido a su posición o configuración en un campo de fuerza. Es la energía almacenada en un sistema como resultado de la realización de trabajo contra una fuerza conservativa. Recordemos que una **fuerza conservativa** es aquella en la que el trabajo realizado para mover un objeto de un punto a otro no depende de la trayectoria, sino únicamente de los puntos inicial y final.

En un sistema unidimensional, la energía potencial se puede calcular mediante:

$$
U(b) - U(a) = -\int_a^b F(x)\,dx
$$ (eq:energia-potencial)

donde $U$ es la energía potencial, $F(x)$ es la fuerza conservativa que actúa sobre el objeto y $x$ representa la posición.

Un aspecto clave es que la fuerza se puede obtener como la derivada negativa de la energía potencial con respecto a la posición:

$$
F(x) = -\frac{dU(x)}{dx}
$$ (eq:fuerza-potencial)

En sistemas con más dimensiones, la derivada con respecto a la coordenada se sustituye por el gradiente.

### Mapas de energía potencial

Los **mapas de energía potencial** (o diagramas de energía potencial) son representaciones gráficas de $U$ en función de la posición. Como la condición de equilibrio ocurre cuando la fuerza es cero (y por tanto cuando $dU/dx = 0$), los puntos de equilibrio coincidirán con los extremos del mapa de energía potencial:

- Los **mínimos** de $U$ (valles) corresponden a puntos de **equilibrio estable**.
- Los **máximos** de $U$ (cumbres) corresponden a puntos de **equilibrio inestable**.

En la {numref}`fig-mapa-energia` se muestra un ejemplo de mapa de energía potencial.

```{figure} ../_static/tema1_images/mapa_energia_potencial.png
---
width: 60%
name: fig-mapa-energia
align: center
---
Mapa de energía potencial que muestra puntos de equilibrio estables (B y D, mínimos) e inestables (A y C, máximos).
```

Al analizar la forma del mapa de energía potencial podemos predecir el movimiento del sistema. Por ejemplo, en un pozo de potencial, un objeto oscilará alrededor del punto de equilibrio estable.

### Analogía gravitatoria

La **analogía gravitatoria** es una herramienta conceptual que utiliza nuestra experiencia intuitiva con la gravedad para comprender sistemas con diferentes tipos de fuerzas. La idea central es que si dos sistemas tienen mapas de energía potencial con la misma forma —aunque sean de naturaleza física diferente—, sus movimientos serán cualitativamente similares.

En el caso de la energía potencial gravitatoria, la energía es proporcional a la altura $h$, de modo que el propio paisaje topográfico actúa como mapa de energía potencial (una montaña rusa es un ejemplo).

El movimiento de una masa unida a un resorte, que experimenta una fuerza restauradora elástica, se puede visualizar como el movimiento de un objeto en un campo gravitatorio equivalente. La energía potencial de un muelle es proporcional al cuadrado de su deformación respecto a la posición de equilibrio (puedes demostrarlo a partir de {eq}`eq:energia-potencial`):

$$
U(x) = \frac{1}{2}\kappa x^2 \quad \Rightarrow \quad h(x) = \frac{\kappa}{2mg}x^2 = Ax^2
$$ (eq:potencial-muelle)

Esto genera un mapa de energía potencial con forma de **parábola** ({numref}`fig-analogia-gravitatoria`), que predice un movimiento oscilatorio armónico simple alrededor del punto de equilibrio.

```{figure} ../_static/tema1_images/analogia_gravitatoria.png
---
width: 55%
name: fig-analogia-gravitatoria
align: center
---
Analogía gravitatoria del muelle: la energía potencial parabólica $U(x) = \frac{1}{2}\kappa x^2$ equivale a una colina de perfil $h(x) = Ax^2$, prediciendo oscilaciones armónicas simples.
```

Es importante tener en cuenta las **limitaciones** de la analogía gravitatoria:

- No tiene en cuenta fuerzas no conservativas, como la fricción, que pueden disipar energía y modificar el movimiento del sistema.
- En sistemas no inerciales, donde actúan fuerzas ficticias como la fuerza de Coriolis, la analogía no es directamente aplicable sin modificaciones.

En resumen, la energía potencial, los mapas de energía potencial y la analogía gravitatoria son herramientas conceptuales poderosas para comprender el comportamiento de una amplia gama de sistemas físicos. Sin embargo, es crucial ser conscientes de sus limitaciones y considerar la influencia de otros factores, como las fuerzas no conservativas y los sistemas de referencia no inerciales, para obtener una descripción completa del movimiento del sistema.

```{admonition} Resumen del tema 1

**Síntesis de Conceptos**

En este primer tema de la asignatura, hemos explorado el concepto de equilibrio como el punto de referencia indispensable para analizar cualquier sistema dinámico. Hemos visto que, más allá de la idea intuitiva de "ausencia de movimiento", el equilibrio es un estado estacionario donde una propiedad deja de evolucionar en el tiempo. Al aterrizar esta idea en la mecánica, hemos comprendido que la magnitud que realmente está en equilibrio es la velocidad, ya que cuando la fuerza neta es cero, esta permanece constante. Esto nos ha permitido ver que un objeto en reposo es solo un caso particular de este fenómeno más amplio.

A lo largo del capítulo, hemos aprendido a clasificar el equilibrio según su estabilidad, analizando cómo responde un sistema ante pequeñas perturbaciones. A través de analogías visuales, como una pelota en un cuenco o en la cima de una colina, hemos diferenciado entre el equilibrio estable (donde el sistema tiende a regresar a su estado inicial), el inestable (donde la perturbación se amplifica) y el indiferente. Esta distinción ha sido fundamental para conectar la geometría de los mapas de energía potencial con la dinámica: los mínimos de energía actúan como valles de estabilidad, mientras que los máximos actúan como cumbres inestables.

Para simplificar el estudio de sistemas complejos, hemos introducido los grados de libertad, aprendiendo a identificar el número mínimo de coordenadas independientes necesarias para describir un sistema. Hemos visto cómo las ligaduras, como la longitud constante de la cuerda en un péndulo, nos permiten reducir el número de variables y manejar ecuaciones de movimiento mucho más sencillas.

A partir de ahí, hemos estudiado las dos grandes rutas que sigue un sistema cuando es desplazado de su equilibrio estable: el amortiguamiento y la oscilación. Mediante el ejemplo de una esfera cayendo en un fluido, hemos visto cómo las fuerzas disipativas hacen que el sistema pierda energía y busque gradualmente su condición de equilibrio. Por otro lado, hemos analizado cómo las fuerzas restauradoras, como las de un muelle, crean un movimiento repetitivo de vaivén. Finalmente, gracias a la analogía gravitatoria, hemos descubierto que cualquier potencial que tenga forma de parábola generará siempre un movimiento oscilatorio armónico.

**Mapa de Conexiones**

Este último hallazgo es el que nos sirve de puente hacia el resto de la asignatura. El tema 2 nos permitirá profundizar exclusivamente en el oscilador armónico simple. Estudiaremos este modelo universal como la base para entender distintos sistemas físicos antes de lanzarnos al estudio de fenómenos más complejos.
```
