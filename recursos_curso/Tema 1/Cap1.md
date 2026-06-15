**TEMA 1. EQUILIBRIO, AMORTIGUAMIENTO Y OSCILACIONES**

**Equilibrio**

En este primer tema vamos a introducir algunos conceptos que son
necesarios para entender bien lo que estudiaremos a continuación. El
primero de ellos es el concepto de equilibrio. A lo largo de buena parte
de la asignatura vamos a estudiar oscilaciones y ondas, que son
fenómenos dinámicos, pero es necesario empezar por el equilibrio. Aunque
puede parecer que no tiene mucha relación con esos fenómenos, basta
darse cuenta de que las oscilaciones de un sistema se producen
generalmente alrededor de un punto de equilibrio. El concepto de
equilibrio es esencial para el estudio de la dinámica de los sistemas
porque nos proporciona el punto de referencia a partir del cual podemos
analizar y comprender cómo los sistemas cambian y evolucionan en el
tiempo. Por ello, es imprescindible entender bien qué es un punto de
equilibrio y, más en general, a qué nos referimos (al menos en esta
asignatura) cuando hablamos de equilibrio.

La primera idea cuando hablamos de equilibrio es pensar en la ausencia
de movimiento, pero eso no es más que un caso muy particular de
equilibrio. Ni siquiera coincide con lo que es el equilibrio mecánico,
que ocurre cuando la resultante de las fuerzas que actúan sobre un
sistema es igual a cero. Sin embargo, el concepto de equilibrio va más
allá de la mecánica. Sin salirnos de la física, podemos hablar de otros
tipos de equilibrio:

\- Equilibrio térmico: Se refiere a la situación en la que dos o más
sistemas en contacto térmico se encuentran a la misma temperatura. En
este estado, no hay flujo neto de calor entre los sistemas.

\- Equilibrio termodinámico: Un sistema se encuentra en equilibrio
termodinámico cuando no experimenta cambios macroscópicos a lo largo del
tiempo y todas sus partes están en equilibrio mecánico, térmico y
químico. Este tipo de equilibrio implica que las variables
termodinámicas del sistema, como la temperatura, la presión y el
potencial químico, son uniformes.

\- Equilibrio en circuitos eléctricos: En un circuito eléctrico, el
equilibrio se alcanza cuando la corriente y el voltaje en cada punto del
circuito permanecen constantes en el tiempo.

Más allá de la física, podemos hablar de equilibrio en muchas otras
disciplinas:

**-** Equilibrio químico: En química, el equilibrio se refiere al estado
en el cual las concentraciones de reactivos y productos en una reacción
química reversible se mantienen constantes a lo largo del tiempo. En
este punto, las velocidades de la reacción directa e inversa son
iguales, y no hay cambios netos en la composición del sistema.

\- Equilibrio genético: En genética de poblaciones, el equilibrio se
describe como un estado en el cual las frecuencias alélicas y
genotípicas en una población permanecen constantes a través de
generaciones. Este estado se alcanza cuando no hay factores evolutivos
que actúen sobre la población, como la mutación, la selección natural,
la deriva genética, o el flujo genético.

\- Equilibrio social: En sociología, el equilibrio social se refiere a
un estado de relativa estabilidad y orden en una sociedad, donde las
diferentes partes del sistema social funcionan de manera armoniosa. Este
estado implica un equilibrio de poder entre los diferentes grupos
sociales, así como la aceptación generalizada de las normas y valores
sociales.

\- Equilibrio económico: En economía, el equilibrio es un estado en el
cual las fuerzas de la oferta y la demanda están equilibradas. En esta
situación, no hay tendencia a que los precios o las cantidades cambien.

\- Equilibrio en matemáticas: En matemáticas, un punto de equilibrio de
un sistema de ecuaciones diferenciales es un punto en el que el sistema
no cambia con el tiempo. En otras palabras, es un estado estacionario
del sistema.

Para que un sistema esté en equilibrio no basta con que una de sus
propiedades esté en equilibrio, sino que todas las magnitudes que lo
caracterizan deben estarlo. Eso es una condición muy exigente en
sistemas que estén descritos por varias magnitudes. Por eso nosotros
vamos a hablar de equilibrio de las propiedades de un sistema. Un
sistema físico puede estar evolucionando en el tiempo con ciertas
magnitudes, por ejemplo, las velocidades, y sin embargo tener otras
magnitudes que no cambian en el tiempo, como una aceleración constante.

Pensemos por tanto en una magnitud de un sistema que vamos a denotar con
la letra **\$\\eta \$**. Diremos que esa propiedad está en equilibrio si
no evoluciona en el tiempo. Matemáticamente podemos escribirlo con la
expresión

**\\\[\\frac{d}{{dt}}\\eta = 0\\\]**

[Equilibrio mecánico]{.underline}

En el caso del equilibrio mecánico, aunque a veces se hable de
"equilibrio de fuerzas", no es la fuerza la magnitud que está en
equilibrio, sino la velocidad: Dado que la definición de equilibrio
mecánico es que la fuerza neta, y no su derivada, sea cero, **\$\\vec F
= 0\$**, a partir de la segunda ley de Newton, **\$\\vec F = m\\vec
a\$**, y teniendo en cuenta que la aceleración es la derivada de la
velocidad, tenemos que

**\\\[\\frac{d}{{dt}}\\vec v = 0\\\]**,

por lo que es la velocidad la magnitud que está en equilibrio.

En cuanto a la posición, no es una propiedad que tenga que estar en
equilibrio cuando hablamos de equilibrio mecánico. Un objeto que está en
reposo y no se desplaza en un sistema de referencia dado es solo un caso
particular de equilibrio mecánico.

Veamos unos cuantos ejemplos de equilibrio en física:

[Ejemplo 1. Condición de equilibrio de un péndulo simple]{.underline}

La condición de equilibrio en un péndulo se produce cuando la velocidad
del péndulo es constante. Esto ocurre cuando el péndulo está en reposo
en su posición vertical inferior (ángulo cero con respecto a la
vertical).

![Diagrama, Gráfico de cajas y bigotes Descripción generada
automáticamente](./media/image1.png){width="2.427100831146107in"
height="2.4062674978127734in"}

Figura 1.1 Esquema de las fuerzas que intervienen en el péndulo simple.

Veamos cómo deducirlo matemáticamente paso a paso:

1\. Identificar las fuerzas:

Las fuerzas que actúan sobre la masa del péndulo (Figura 1.1) son la
tensión *T* de la cuerda y el peso **\${F_g} = - \\,mg\$**. El signo
menos indica que apunta en sentido negativo del eje vertical.

2\. Proyectar las fuerzas en los ejes:

Se descomponen las fuerzas en sus componentes horizontal (eje *x*) y
vertical (eje *y*).

**\$\\begin{array}{l}**

**{F_x} = - T\\,\\sin \\theta \\\\**

**{F_y} = - mg + T\\,\\cos \\theta**

**\\end{array}\$**

3\. Aplicar la condición de equilibrio:

Para que la velocidad sea constante, la aceleración debe ser cero. Según
la segunda ley de Newton, esto implica que la suma de las fuerzas en
cada eje debe ser igual a cero.

\- Equilibrio en x: **\${F_x} = - T\\,\\sin \\theta = 0\$**

\- Equilibrio en y: **\${F_y} = - mg + T\\,\\cos \\theta = 0\$**

4\. Resolver las ecuaciones:

La ecuación para el eje horizontal implica que **\$\\sin \\theta =
0\$**, lo que significa que **\$\\theta = 0\$** (posición vertical).
Sustituyendo esta condición en la ecuación para el eje *y*, se obtiene
**\$T = mg\$**, lo que significa que la tensión es igual al peso en la
posición de equilibrio.

Conclusión:

La condición de equilibrio en un péndulo simple se cumple cuando el
ángulo **\$\\theta \$** es cero, lo que corresponde a la posición
vertical inferior. En este punto, la tensión de la cuerda es igual al
peso y, además de no haber aceleración, la velocidad es cero ya que si
no lo fuera variaría el ángulo del péndulo y dejaría de estar en
equilibrio.

[Ejemplo 2. Condición de equilibrio de una esfera en caída libre con
rozamiento]{.underline}

![Diagrama El contenido generado por IA puede ser
incorrecto.](./media/image2.png){width="3.074803149606299in"
height="1.6653543307086613in"}En el caso de un objeto esférico que cae
en un fluido con rozamiento, el equilibrio mecánico también viene dado
por la compensación de las fuerzas que actúan sobre la esfera. Para
simplificar las cosas, pensemos que el medio en el que se produce la
caída es el aire y que, al ser su densidad mucho menor que la de la
esfera, podemos despreciar el empuje. En ese caso, las dos fuerzas que
actúan sobre el objeto son el peso y la fuerza de arrastre (Figura 1.2),
que da cuenta del efecto del rozamiento. Dependiendo de las
características del fluido y si la velocidad de caída no es muy grande,
podemos asumir que la fuerza de arrastre es proporcional a la velocidad
*v* (ley de Stokes). Concretamente, para una esfera la fuerza de
arrastre es **\\\[{F_a} = - {\\rm{ }}6\\pi \\mu rv = - {\\rm{
}}bv\\\]**, siendo **\\\[\\mu \\\]** la viscosidad dinámica y
**\\\[r\\\]** el radio de la esfera.

Figura 1.2 Fuerzas que actúan sobre una esfera en caída libre

Puedes intentar encontrar la condición de equilibrio en este caso.
Veamos ahora otros ejemplos no mecánicos de equilibrio.

[Ejemplo 3. Equilibrio térmico]{.underline}

Como sabemos, dos objetos en contacto están en equilibrio térmico si no
hay transferencia de energía térmica entre ellos. Supongamos una
geometría como la que se muestra en la figura 1.3. La ecuación que rige
la dinámica del sistema es:

**\\\[\\frac{{dq}}{{dt}} = - A\\frac{k}{L}({T_2} - {T_1})\\\]**,

donde **\\\[q\\\]** es la energía calórica, **\\\[A\\\]** es el área de
la zona de la unión, **\\\[k\\\]** es su conductividad térmica,
**\\\[L\\\]** es su longitud, **\\\[{T_1}\\\]**es la temperatura del
primer cuerpo y **\\\[{T_2}\\\]** es la temperatura del segundo. Una
simple ojeada a esta ecuación nos indica que el equilibrio térmico se
produce cuando las temperaturas de los dos cuerpos son iguales.

![Diagrama Descripción generada
automáticamente](./media/image3.png){width="2.7395833333333335in"
height="1.5776509186351706in"}

Figura 1.3 Dos objetos a diferente temperatura con una zona de unión.

[Ejemplo 4. Equilibrio en un circuito eléctrico]{.underline}

Pensemos por ejemplo en un circuito RL en serie como el de la figura
1.4, con una resistencia y una bobina, en el que queremos encontrar la
condición de equilibrio de la intensidad de corriente.

![](./media/image4.png){width="3.088542213473316in"
height="1.7802580927384077in"}

Figura 1.4 Circuito RL en serie

¿Cómo hallarías esa condición de equilibrio?

**Puntos de equilibrio**

En general, la condición de equilibrio para una magnitud no se va a dar
para todos los valores de las variables de las que depende sino
solamente para algunos. Por ejemplo, si el sistema que consideramos
depende de dos variables, **\$\\eta \\,\\,{\\rm{y }}x\$**, y la ecuación
de movimiento es:

**\\\[\\frac{d}{{dt}}\\eta = f(\\eta ,x)\\\]**

Entonces **\${x_0}\$** es un punto de equilibrio si **\\\[f(\\eta
,{x_0}) = 0\\\]**, de forma que en ese punto se cumple que:

**\\\[\\frac{d}{{dt}}\\eta = f(\\eta ,{x_0}) = 0\\\]**

El concepto de punto de equilibrio no es estrictamente geométrico, la
variable *x* puede ser una posición, pero también una temperatura, una
concentración química, etc.

En el caso del equilibrio mecánico, sabemos que la condición que lo
define es que la fuerza total sea nula. Cuando la fuerza no es homogénea
en todo el espacio, tendremos que el equilibrio se producirá en los
puntos **\${\\vec r_0}\$** en los que **\$\\vec F({\\vec r_0}) = 0\$**.

Retomemos el caso del péndulo simple (ejemplo 1). Habíamos visto que el
equilibrio se producía cuando **\$\\sin \\theta = 0\$**. Como en nuestro
sistema de coordenadas (figura 1.1) **\$x = l\\sin \\theta \$**, **\$y =
l\\,(1 - \\cos \\theta )\$**, el punto de equilibrio del sistema será
**\\\[({x\_{eq}},{\\rm{ }}{y\_{eq}}) = (0,0)\\\]**, es decir, nuestro
origen de coordenadas.

Puedes intentar hallar los puntos de equilibrio en otros sistemas, por
ejemplo un muelle del que cuelga una masa, o un objeto que flota
parcialmente sumergido en un líquido.

**Estabilidad del equilibrio**

El equilibrio de un sistema puede ser clasificado en tres tipos
principales: estable, inestable e indiferente (Figura 1.5). Esta
clasificación se basa en la respuesta del sistema ante pequeñas
perturbaciones o desplazamientos desde su posición de equilibrio.

● [Equilibrio estable]{.underline}: Un sistema se encuentra en
equilibrio estable si, al ser desplazado ligeramente de su posición de
equilibrio, experimenta una fuerza o influencia que lo impulsa a
regresar a dicha posición. En otras palabras, un equilibrio estable se
caracteriza por la tendencia del sistema a restaurar su estado inicial
después de una perturbación. Imaginemos una pelota en el fondo de un
cuenco: si la desplazamos un poco de su posición de reposo, la gravedad
la hará oscilar alrededor del punto más bajo del cuenco hasta que, si
hay rozamiento, finalmente se detenga de nuevo en el fondo. Si no hay
rozamiento, el sistema oscilará alrededor del punto de equilibrio sin
alejarse de él más allá de una región limitada. Como veremos, este
comportamiento se debe a que la energía potencial del sistema es mínima
en la posición de equilibrio, asemejándose a un valle en un mapa de
energía potencial. Cualquier desplazamiento desde esta posición implica
un aumento de la energía potencial, generando una fuerza que busca
llevar al sistema de regreso al punto de mínima energía.

![Imagen que contiene Icono Descripción generada
automáticamente](./media/image5.png){width="5.879181977252843in"
height="1.0572922134733158in"}

Figura 1.5 Esquema con los tres tipos de equilibrio: estable
(izquierda), inestable (centro) e indiferente (derecha).

● [Equilibrio inestable]{.underline}: Un sistema está en equilibrio
inestable si, al ser desplazado levemente de su posición de equilibrio,
las fuerzas o influencias presentes lo alejan aún más de dicha posición.
En este caso, la perturbación inicial no es contrarrestada, sino que se
amplifica, provocando que el sistema se aleje indefinidamente de su
estado inicial. Un ejemplo clásico es una pelota en la cima de una
colina: cualquier pequeño desplazamiento hará que la pelota ruede cuesta
abajo, alejándose cada vez más de la cima. Desde el punto de vista de la
energía potencial, un equilibrio inestable corresponde a un máximo en el
mapa de energía potencial, como la cima de una montaña. Cualquier
movimiento desde esta posición llevará al sistema a un punto de menor
energía potencial, impidiendo que regrese a su estado inicial.

● [Equilibrio indiferente o neutro]{.underline}: Un sistema se encuentra
en equilibrio indiferente si, al ser desplazado de su posición de
equilibrio, permanece en la nueva posición sin experimentar fuerzas que
lo impulsen a regresar a la posición original o a alejarse aún más. En
este tipo de equilibrio, cualquier punto dentro de un cierto rango puede
ser considerado una posición de equilibrio, ya que el sistema no muestra
preferencia por un estado particular dentro de esa región. Un ejemplo
sería una pelota en una superficie plana: al desplazar la pelota, esta
se detendrá en la nueva posición sin experimentar fuerzas que la
obliguen a moverse. En términos de energía potencial, un equilibrio
indiferente se caracteriza por una energía potencial constante dentro de
un cierto rango. Esto significa que el sistema no experimenta cambios en
su energía potencial al ser desplazado dentro de esta región, por lo que
no hay fuerzas que lo impulsen a moverse en una dirección particular.

Hay situaciones menos habituales, como el equilibrio semiestable, que
ocurre cuando las fuerzas son atractivas desde uno de los lados y
repulsivas desde el otro. Además, en sistemas cuya dinámica ocurre en
más de una dimensión, la fenomenología puede ser todavía más complicada.

Es importante destacar que la clasificación del equilibrio como estable,
inestable o indiferente depende del sistema en cuestión y de las fuerzas
que actúan sobre él. Un mismo sistema puede presentar diferentes tipos
de equilibrio dependiendo de las condiciones en las que se encuentre.

**Grados de libertad de un sistema físico**

Los grados de libertad en un sistema físico se refieren al número mínimo
de coordenadas independientes necesarias para describir completamente el
estado o la configuración de un sistema en el espacio. En otras
palabras, los grados de libertad representan la capacidad del sistema
para moverse y cambiar de posición en el espacio. Para comprender mejor
este concepto, consideremos los siguientes ejemplos:

● Un muelle que solo se mueve verticalmente: Este sistema solo tiene un
grado de libertad, ya que solo necesitamos una coordenada, la altura,
para describir su posición. No es necesario considerar su movimiento
horizontal, ya que se asume que permanece constante.

● Un péndulo simple: Aunque el péndulo se mueve en un plano
bidimensional (descrito por las coordenadas *x* e *y*), en realidad solo
tiene un grado de libertad porque ambas coordenadas no son
independientes entre sí. Esto se debe a que la longitud del péndulo es
constante, lo que impone una restricción al movimiento. La posición del
péndulo se puede determinar completamente conociendo el ángulo
**\$\\theta \$** que forma con la vertical. Este tipo de restricciones
se denominan ligaduras.

● Un insecto flotando en agua: Este sistema tiene dos grados de
libertad, ya que puede moverse libremente en la superficie del agua, un
plano bidimensional.

En general, el número de grados de libertad será igual al número de
variables del sistema menos el número de ligaduras entre ellas.

La identificación de los grados de libertad en un sistema físico es
crucial para simplificar su análisis. Al utilizar las coordenadas
independientes que respetan las restricciones del sistema, las
ecuaciones de movimiento se vuelven más sencillas y manejables.

Por ejemplo, al analizar el movimiento de un péndulo simple, es mucho
más fácil trabajar con una sola ecuación de movimiento que involucre el
ángulo **\$\\theta \$**, en lugar de tener que lidiar con dos ecuaciones
(para *x* e *y*) que contienen la restricción de la longitud del
péndulo. Veámoslo:

Para deducir la ecuación del péndulo simple en la coordenada angular
**\$\\theta \$**, se debe considerar que el péndulo se mueve en un plano
bidimensional sujeto a la fuerza gravitatoria y la tensión de la cuerda
que lo sostiene. La clave para simplificar el problema es aprovechar que
la longitud de la cuerda (*l*) permanece constante durante el
movimiento, lo que reduce los grados de libertad a uno, representado por
el ángulo **\$\\theta \$**. Seguiremos los siguientes pasos:

1\. Expresión de las ecuaciones de movimiento en *x* e *y*:

A partir de las fuerzas que intervienen en el problema (ecuación (1.3))
podemos escribir las ecuaciones de movimiento

**\$\\begin{array}{l}**

**m\\frac{{{d\^2}x}}{{d{t\^2}}} = - T\\,\\sin \\theta \\\\**

**m\\frac{{{d\^2}y}}{{d{t\^2}}} = - mg + T\\,\\cos \\theta**

**\\end{array}\$**

2\. Cálculo de los operadores diferenciales en coordenadas polares
**\\\[(l,{\\rm{ }}\\theta )\\\]**:

Como la relación entre los dos sistemas de coordenadas es **\$x =
l\\,\\sin \\theta \$**, **\$y = l\\,(1 - \\cos \\theta )\$**, derivando
tenemos:

**\\\[\\begin{array}{l}**

**\\frac{{dx}}{{dt}} = l\\,\\cos \\theta \\,\\frac{{d\\theta
}}{{dt}}\\\\**

**\\frac{{{d\^2}x}}{{d{t\^2}}} = - l\\,\\sin \\theta \\,{\\left(
{\\frac{{d\\theta }}{{dt}}} \\right)\^2} + l\\,\\cos \\theta
\\,\\,\\frac{{{d\^2}\\theta }}{{d{t\^2}}}\\\\**

**\\frac{{dy}}{{dt}} = l\\,\\sin \\theta \\,\\,\\frac{{d\\theta
}}{{dt}}\\\\**

**\\frac{{{d\^2}y}}{{d{t\^2}}} = l\\,\\cos \\theta \\,{\\left(
{\\frac{{d\\theta }}{{dt}}} \\right)\^2} + l\\,\\sin \\theta
\\,\\,\\frac{{{d\^2}\\theta }}{{d{t\^2}}}**

**\\end{array}\\\]**

3\. Obtención de la ecuación del péndulo simple para la coordenada
**\$\\theta \$**:

Sustituyendo las expresiones de la segunda derivada de *x* e *y* en las
ecuaciones de movimiento, y luego multiplicando la ecuación en *x* por
**\$\\cos \\theta \$** y la ecuación en *y* por **\$\\sin \\theta \$**,
se logra eliminar la tensión al sumar ambas ecuaciones. Después de la
simplificación, se llega a la siguiente ecuación:

**\\\[\\frac{{{d\^2}\\theta }}{{d{t\^2}}} = - \\frac{g}{l}\\,\\sin
\\theta \\,\\\]**.

Esta ecuación diferencial de segundo orden describe la evolución del
ángulo **\$\\theta \$** en función del tiempo para un péndulo simple. Es
importante notar que esta ecuación no es lineal debido al término
**\$\\sin \\theta \$**.

La conocida ecuación lineal del péndulo ideal se obtiene al hacer la
aproximación de ángulos pequeños, que se basa en el hecho de que para
ángulos pequeños (**\$\\theta \\ll 1\\,\\,{\\rm{radi\\\'a n}}\$**), el
valor del seno del ángulo es aproximadamente igual al valor del ángulo
expresado en radianes. Usando esta aproximación se obtiene la ecuación
lineal del péndulo, válida para pequeñas oscilaciones:

**\\\[\\frac{{{d\^2}\\theta }}{{d{t\^2}}} = - \\frac{g}{l}\\,\\theta
\\\]**.

Esta ecuación diferencial lineal de segundo orden es mucho más sencilla
de resolver analíticamente que la ecuación del péndulo sin la
aproximación de pequeñas oscilaciones.

En los sistemas multidimensionales en los cuales tenemos varios grados
de libertad, el concepto de punto de equilibrio se generaliza y podemos
obtener no solo puntos de equilibrio, sino también curvas de equilibrio,
superficies de equilibrio, etc., es decir, regiones en las cuales el
sistema está en equilibrio y que tienen varias dimensiones.

Un ejemplo es la superficie del agua cuando tenemos un barco flotando
(despreciando el efecto de las olas). El barco está en equilibrio en
cualquier punto de esta superficie del agua, luego la condición de
equilibrio es únicamente que la parte hundida del barco sea una cierta
cantidad, pero el barco puede estar en cualquier posición del plano que
forma la superficie del agua. En este caso, estaríamos hablando de un
plano de equilibrio, de una condición de equilibrio bidimensional.

**Dinámica alrededor del equilibrio**

En un sistema físico, hay dos comportamientos dinámicos principales (no
son los únicos) cuando un sistema es desplazado de su posición de
equilibrio estable, que son el amortiguamiento y las oscilaciones. El
amortiguamiento se refiere a la pérdida de energía a lo largo del
tiempo, lo que hace que el sistema evolucione hacia la condición de
equilibrio gradualmente. Este fenómeno suele estar causado por fuerzas
que se oponen al movimiento, como la fricción. Por su parte, la
oscilación puede entenderse como la variación repetitiva en el tiempo de
una o más propiedades físicas de un sistema alrededor de un punto de
equilibrio.

Es importante tener en cuenta que estos dos comportamientos no son
mutuamente excluyentes. Un sistema puede exhibir amortiguamiento y
oscilaciones al mismo tiempo. Por ejemplo, como veremos, un péndulo
oscila alrededor de su punto de equilibrio, pero la amplitud de las
oscilaciones disminuye con el tiempo debido a la fricción del aire, lo
que sería un tipo de amortiguamiento.

Analicemos estos dos tipos de comportamiento con un poco más de
profundidad.

**Amortiguamiento**

El amortiguamiento, en un sistema dinámico, ocurre cuando la tasa de
cambio de una variable del sistema es de signo opuesto a la desviación
de esa variable con respecto a su valor de equilibrio, como se muestra
en la figura 1.6. Matemáticamente, si la evolución de esa variable viene
dada por la ecuación:

**\\\[\\frac{d}{{dt}}\\eta = f(\\eta )\\\]**,

para que el sistema presente amortiguamiento, la función **\\\[f(\\eta
)\\\]** debe cumplir las siguientes condiciones:

● **\\\[f(\\eta ) \< 0{\\rm{ si }}\\eta \> {\\eta \_{eq}}\\\]**: Si la
variable es mayor que su valor de equilibrio **\\\[{\\eta \_{eq}}\\\]**,
la fuerza debe ser negativa, es decir, debe actuar para disminuir la
variable y acercarla al equilibrio.

● **\\\[f(\\eta ) = 0{\\rm{ si }}\\eta = {\\eta \_{eq}}\\\]**: Si la
variable es igual a su valor de equilibrio, la fuerza debe ser cero, lo
que significa que no hay ninguna fuerza actuando sobre la variable y se
mantendrá en equilibrio.

● **\\\[f(\\eta ) \> 0{\\rm{ si }}\\eta \< {\\eta \_{eq}}\\\]**: Si la
variable es menor que su valor de equilibrio, la fuerza debe ser
positiva, es decir, debe actuar para aumentar la variable y acercarla al
equilibrio.

Un caso especial de amortiguamiento es el amortiguamiento lineal. En
este caso, la función **\\\[f(\\eta )\\\]** es una función lineal de la
variable, lo que significa que la fuerza es proporcional al
desplazamiento de la variable desde su valor de equilibrio:

**\\\[f(\\eta ) = - \\,C\\left( {\\eta - {\\eta \_{eq}}} \\right)\\\]**,

siendo *C* una constante positiva que representa la magnitud de la
fuerza de amortiguamiento. La solución general para este tipo de
ecuación diferencial es una función exponencial decreciente, lo que
significa que la variable se acerca asintóticamente al valor de
equilibrio con el tiempo.

![](./media/image6.png){width="5.008333333333334in"
height="2.253325678040245in"}

Figura 1.6 Esquema del signo de la fuerza para que haya amortiguamiento.

Es importante recordar que esta definición matemática describe el
comportamiento de una sola variable en un sistema. Un sistema complejo
puede tener varias variables, cada una con su propio tipo de
amortiguamiento.

Para entender mejor el concepto de amortiguamiento, vamos a estudiar
paso a paso un caso de amortiguamiento lineal, la caída libre de un
objeto en un fluido, que habíamos planteado en el ejemplo 3 (figura
1.2).

1\. Definición del problema:

Un objeto cae dentro de un fluido, sin causar turbulencias. La ecuación
que rige este movimiento es la segunda ley de Newton, que establece que
la masa del objeto multiplicada por su aceleración es igual a la suma de
las fuerzas que actúan sobre él. En este caso tenemos dos fuerzas
principales: la fuerza de gravedad y la fuerza de arrastre del fluido.
Por simplicidad despreciamos el empuje asumiendo que la densidad del
fluido es mucho menor que la del objeto.

2\. Ecuación de movimiento:

Las dos fuerzas involucradas son las de la figura 1.2, la de la
gravedad, **\\\[{F_g} = - \\,mg\\\]**, y la de arrastre, **\\\[{F_a} = -
\\,bv\\\]**. La ecuación de movimiento es:

**\\\[m\\frac{{dv}}{{dt}} = {F_g} + {F_a} = - \\,mg - bv\\\]**

3\. Condición de equilibrio:

La velocidad de equilibrio **\\\[{v\_{eq}}\\\]** se alcanza cuando la
fuerza de arrastre se iguala a la fuerza de gravedad, es decir, cuando
la aceleración del objeto es cero. Al resolver la ecuación de movimiento
para **\\\[dv/dt{\\rm{ }} = {\\rm{ }}0\\\]**, obtenemos la velocidad de
equilibrio: **\\\[{v\_{eq}} = - mg/b\\\]**. Esto significa que después
de un cierto tiempo, el objeto caerá a una velocidad constante,
**\\\[{v\_{eq}}\\\]**, determinada por el equilibrio entre la fuerza de
gravedad y la fuerza de arrastre.

4\. Solución de la ecuación de movimiento:

Para obtener la velocidad del objeto en función del tiempo, necesitamos
resolver la ecuación diferencial. Podemos utilizar el método de
separación de variables para resolver esta ecuación:

4.1. Reordenamos la ecuación: **\\\[\\frac{{dv}}{{bv{\\rm{ }} + {\\rm{
}}mg}} = - \\frac{1}{m}dt\\\]**.

4.2. Integramos ambos lados de la ecuación: **\\\[\\int
{\\frac{{dv}}{{bv{\\rm{ }} + {\\rm{ }}mg}}} = - \\frac{1}{m}\\int {dt}
\\\]**.

4.3. Resolvemos las integrales: **\\\[\\frac{1}{b}ln\\left( {bv + mg}
\\right) = - \\frac{t}{m} + C\\\]**, donde *C* es una constante de
integración.

4.4. Despejamos la velocidad: **\$v(t) = \\left( {{v_0} +
\\frac{{mg}}{b}} \\right)\\,{e\^{ - b\\,t/m}} - \\frac{{mg}}{b}\$**,

donde la velocidad inicial, **\${v_0} = v(0)\$**, determina el valor de
la constante de integración *C*.

5\. Análisis de la solución:

La solución obtenida para **\$v(t)\$** describe el comportamiento de un
sistema amortiguado. Observamos que la velocidad del objeto se acerca
exponencialmente a la velocidad de equilibrio, **\\\[{v\_{eq}} = -
mg/b\\\]**, a medida que el tiempo tiende a infinito.

La constante de tiempo **\\\[\\tau = m/b\\\]** determina la rapidez con
la que el objeto alcanza la velocidad de equilibrio. Cuanto mayor sea la
masa del objeto (*m*) o menor sea la constante de amortiguamiento (*b*),
mayor será la constante de tiempo y más lentamente alcanzará el objeto
la velocidad de equilibrio.

La solución también muestra que la velocidad inicial del objeto influye
en su velocidad en cualquier instante de tiempo, pero no afecta al valor
final de la velocidad de equilibrio.

**Oscilaciones**

Las oscilaciones en un sistema dinámico se caracterizan por la presencia
de una fuerza o influencia restauradora que se opone al desplazamiento
de una variable con respecto a su punto de equilibrio. Esta fuerza
siempre actúa en dirección opuesta al desplazamiento, empujando al
sistema de vuelta hacia el equilibrio. Sin embargo, debido a la inercia
del sistema, este sobrepasa el punto de equilibrio, creando un
movimiento de vaivén alrededor de dicho punto.

Matemáticamente, la oscilación se puede describir mediante una ecuación
diferencial de segundo orden de la siguiente forma:

**\\\[m\\frac{{{d\^2}}}{{d{t\^2}}}\\eta = f(\\eta - {\\eta
\_{eq}})\\\]**,

donde **\\\[f(\\eta - {\\eta \_{eq}})\\\]** describe la fuerza
restauradora que depende del desplazamiento desde el punto de
equilibrio, **\\\[\\eta - {\\eta \_{eq}}\\\]**.

Para que haya oscilaciones, la fuerza restauradora debe cumplir las
siguientes condiciones:

● **\\\[f(\\eta - {\\eta \_{eq}}) \> 0{\\rm{ si }}\\eta \< {\\eta
\_{eq}}\\\]**: Si el valor de la variable es inferior a su valor de
equilibrio, la fuerza debe ser positiva, actuando para aumentar su valor
y llevar el sistema hacia el equilibrio.

● **\\\[f(\\eta - {\\eta \_{eq}}) = 0{\\rm{ si }}\\eta = {\\eta
\_{eq}}\\\]**: En el valor de equilibrio, la fuerza restauradora debe
ser cero.

● **\\\[f(\\eta - {\\eta \_{eq}}) \< 0{\\rm{ si }}\\eta \> {\\eta
\_{eq}}\\\]**: Si la variable está por encima de su valor de equilibrio,
la fuerza debe ser negativa, actuando para disminuir su valor y llevar
el sistema hacia el equilibrio.

Un ejemplo clásico de oscilación es la dinámica de un muelle. Para
comprender cómo se resuelve la dinámica de un muelle matemáticamente,
seguiremos el siguiente proceso:

1\. Definición del sistema:

Empezamos por definir un sistema básico masa-resorte (figura 1.7). Este
sistema se compone de una masa *m* conectada a un resorte de constante
elástica **\$\\kappa \$**. Para facilitar el análisis, generalmente se
desprecia la masa del muelle. Consideremos un muelle vertical con un
extremo fijo y una masa *m* suspendida en su extremo libre.

![Diagrama, Esquemático Descripción generada
automáticamente](./media/image7.png){width="2.168847331583552in"
height="1.8504057305336832in"}

Figura 1.7 Sistema masa-muelle en la posición de equilibrio con las dos
fuerzas que intervienen. Elegimos el eje *y* en sentido negativo del eje
vertical.

Definimos **\\\[y(t)\\\]** como la posición de la masa en función del
tiempo, con el origen **\\\[y = 0\\\]** en la posición donde el muelle
sin la masa no está estirado y sentido positivo hacia abajo (cuando el
muelle se estira). **\\\[{l_0}\\\]** representa la elongación del muelle
en la posición de equilibrio con la masa, es decir, cuando **\\\[y =
\\,\\,{l_0}\\\]** la fuerza del muelle compensa la fuerza de gravedad
que actúa sobre la masa.

2\. Identificación de las fuerzas:

Las fuerzas que actúan sobre la masa son la fuerza de gravedad,
**\\\[{F_g} = mg\\\]**, y la fuerza restauradora del muelle, **\\\[{F_k}
= - \\kappa \\,\\,y\\\]**.

3\. Ecuación de movimiento:

Aplicando la segunda ley de Newton, tenemos que:

**\\\[m\\frac{{{d\^2}y}}{{d{t\^2}}} = {F_g} + {F_k} = mg - \\kappa
\\,y\\\]**

4\. Simplificación y solución:

En la posición de equilibrio del muelle con la masa (**\\\[y =
\\,\\,{l_0}\\\]**), la aceleración es cero. Por lo tanto, **\\\[mg =
\\kappa \\,{l_0}\\\]**. Sustituyendo en la ecuación de movimiento,
obtenemos:

**\\\[m\\frac{{{d\^2}y}}{{d{t\^2}}} = - \\kappa \\left( {y -
\\,\\,{l_0}} \\right)\\\]**

Esta ecuación diferencial es claramente la de un oscilador con una
fuerza lineal. Como veremos en el tema siguiente, la solución general de
esta ecuación es **\\\[y(t) = {l_0} + A\\cos \\left( {{\\omega \_0}t +
\\varphi } \\right)\\\]**, donde *A* es la amplitud de la oscilación,
que se refiere al desplazamiento máximo de la masa desde la posición de
equilibrio; **\\\[{\\omega \_0}\\\]** es la frecuencia angular de la
oscilación y se relaciona con la masa y la constante del resorte
mediante la fórmula **\\\[{\\omega \_0} = \\sqrt {{\\kappa
\\mathord{\\left/**

**{\\vphantom {\\kappa m}} \\right.**

**\\kern-\\nulldelimiterspace} m}} \\\]**; **\\\[\\varphi \\\]** es la
fase inicial, que define la posición de la masa en **\\\[t = 0\\\]**.

Las constantes **\\\[A{\\rm{ y }}\\varphi \\\]** se determinan a partir
de las condiciones iniciales del problema, que son la posición inicial y
la velocidad inicial de la masa.

Como resumen de las dos rutas hacia el equilibrio que hemos estudiado
podemos decir:

\- Un sistema está amortiguado en una de sus variables si la tasa de
cambio de la variable es de signo opuesto a la desviación de esa
variable con respecto a su valor de equilibrio.

\- Un sistema oscila en una de sus variables si la fuerza tiene el
sentido contrario al desplazamiento respecto del punto de equilibrio.

**Mapas de energía y analogía gravitatoria**

La última parte de este tema se centra en los conceptos de energía
potencial, mapas de energía potencial y la analogía gravitatoria. Estos
conceptos son esenciales para comprender el comportamiento de los
sistemas físicos, especialmente aquellos que exhiben movimiento
oscilatorio, sin necesidad de resolver ecuaciones de movimiento
complejas.

[Energía potencial]{.underline}

La energía potencial se define como la energía que posee un objeto
debido a su posición o configuración en un campo de fuerza. En otras
palabras, es la energía almacenada en un sistema como resultado de la
realización de trabajo contra una fuerza conservativa. Recordemos que
fuerza conservativa es aquella en la que el trabajo realizado para mover
un objeto de un punto a otro no depende de la trayectoria seguida, sino
únicamente de los puntos inicial y final.

En un sistema unidimensional, la energía potencial se puede calcular
utilizando la siguiente fórmula:

**\\\[U(b) - U(a){\\rm{ }} = {\\rm{ }} - \\int_a\^b {F(x)\\,dx} \\\]**,

donde *U* es la energía potencial, **\\\[F(x)\\\]** es la fuerza
conservativa que actúa sobre el objeto y *x* representa la posición del
objeto.

Un aspecto clave es que la energía potencial está asociada a la fuerza.
La fuerza se puede obtener como la derivada negativa de la energía
potencial con respecto a la posición:

**\\\[F(x) = - {\\rm{ }}\\frac{{dU(x)}}{{dx}}\\\]**.

En sistemas con más dimensiones, la derivada con respecto a la
coordenada se sustituye por el gradiente.

[Mapas de energía potencial]{.underline}

Los mapas de energía potencial, también conocidos como diagramas de
energía potencial, son representaciones gráficas de la energía potencial
de un sistema en función de la posición o configuración. Estos mapas
proporcionan una visualización intuitiva del comportamiento del sistema.
Como la condición de equilibrio ocurre cuando la fuerza es cero, los
puntos de equilibrio coincidirán con los máximos y mínimos del mapa de
energía potencial, que son aquellos en los que su derivada se anula. Los
puntos de equilibrio estable corresponden a mínimos de energía
potencial, como los valles en un mapa topográfico, mientras que los
puntos de equilibrio inestable se representan como máximos, como las
cumbres de las montañas. En la figura 1.8 se muestra un mapa de energía
potencial.

![Gráfico, Gráfico de líneas Descripción generada
automáticamente](./media/image8.png){width="3.104189632545932in"
height="1.9270975503062118in"}

Figura 1.8 Mapa de energía potencial que muestra puntos de equilibrio
estables (B y D) e inestables (A y C).

Al analizar la forma del mapa de energía potencial, podemos predecir el
movimiento del sistema. Por ejemplo, en un pozo de potencial, un objeto
oscilará alrededor del punto de equilibrio estable.

[Analogía gravitatoria]{.underline}

La analogía gravitatoria es una herramienta conceptual que utiliza
nuestra experiencia intuitiva con la gravedad para comprender sistemas
con diferentes tipos de fuerzas. La idea central es que si dos sistemas,
incluso si son de naturaleza física diferente, tienen mapas de energía
potencial con la misma forma, entonces sus movimientos serán
cualitativamente similares. En el caso de la energía potencial
gravitatoria, la energía es proporcional a la altura. Esto hace que, por
ejemplo, una montaña rusa sea un mapa de energía potencial.

![](./media/image9.png){width="2.9218755468066493in"
height="2.100097331583552in"}

**\\\[U(x) = mgh(x) = \\frac{1}{2}{\\rm{ }}\\kappa \\,{x\^2}\\,
\\Rightarrow h(x) = \\frac{\\kappa }{{2mg}}{x\^2} = A{x\^2}\\\]**

Figura 1.9 Analogía de la energía potencial de un muelle con la energía
gravitatoria.

El movimiento de una masa unida a un resorte, que experimenta una fuerza
restauradora elástica, se puede visualizar como el movimiento de un
objeto en un campo gravitatorio que sigue una trayectoria equivalente a
la forma del mapa de energía potencial del resorte. La energía potencial
de un muelle es proporcional al cuadrado de su deformación respecto a la
posición de equilibrio (**\\\[U(x) = 1/2{\\rm{ }}\\kappa
\\,{x\^2}\\\]**, puedes demostrarlo). Esto genera un mapa de energía
potencial con forma de parábola, que predice un movimiento oscilatorio
armónico simple alrededor del punto de equilibrio (figura 1.9).

Es importante tener en cuenta que la analogía gravitatoria tiene sus
limitaciones:

\- No tiene en cuenta fuerzas no conservativas, como la fricción, que
pueden disipar energía y modificar el movimiento del sistema.

\- En sistemas no inerciales, donde actúan fuerzas ficticias como la
fuerza de Coriolis, la analogía gravitatoria no es directamente
aplicable sin modificaciones.

En resumen, la energía potencial, los mapas de energía potencial y la
analogía gravitatoria son herramientas conceptuales poderosas que nos
permiten comprender el comportamiento de una amplia gama de sistemas
físicos. Sin embargo, es crucial ser conscientes de las limitaciones de
la analogía gravitatoria y considerar la influencia de otros factores,
como las fuerzas no conservativas y los sistemas de referencia no
inerciales, para obtener una descripción completa del movimiento del
sistema.
