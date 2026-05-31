<!-- Convertido automáticamente desde PDF. Revisar y corregir formato si es necesario. -->

## TEMA 1. EQUILIBRIO, AMORTIGUAMIENTO Y OSCILACIONES 

## Equilibrio 

En este primer tema vamos a introducir algunos conceptos que son necesarios para entender bien lo que estudiaremos a continuación. El primero de ellos es el concepto de equilibrio. A lo largo de buena parte de la asignatura vamos a estudiar oscilaciones y ondas, que son fenómenos dinámicos, pero es necesario empezar por el equilibrio. Aunque puede parecer que no tiene mucha relación con esos fenómenos, basta darse cuenta de que las oscilaciones de un sistema se producen generalmente alrededor de un punto de equilibrio. El concepto de equilibrio es esencial para el estudio de la dinámica de los sistemas porque nos proporciona el punto de referencia a partir del cual podemos analizar y comprender cómo los sistemas cambian y evolucionan en el tiempo. Por ello, es imprescindible entender bien qué es un punto de equilibrio y, más en general, a qué nos referimos (al menos en esta asignatura) cuando hablamos de equilibrio. 

La primera idea cuando hablamos de equilibrio es pensar en la ausencia de movimiento, pero eso no es más que un caso muy particular de equilibrio. Ni siquiera coincide con lo que es el equilibrio mecánico, que ocurre cuando la resultante de las fuerzas que actúan sobre un sistema es igual a cero. Sin embargo, el concepto de equilibrio va más allá de la mecánica. Sin salirnos de la física, podemos hablar de otros tipos de equilibrio: 

- Equilibrio térmico: Se refiere a la situación en la que dos o más sistemas en contacto térmico se encuentran a la misma temperatura. En este estado, no hay flujo neto de calor entre los sistemas. 

- Equilibrio termodinámico: Un sistema se encuentra en equilibrio termodinámico cuando no experimenta cambios macroscópicos a lo largo del tiempo y todas sus partes están en equilibrio mecánico, térmico y químico. Este tipo de equilibrio implica que las variables termodinámicas del sistema, como la temperatura, la presión y el potencial químico, son uniformes. 

- Equilibrio en circuitos eléctricos: En un circuito eléctrico, el equilibrio se alcanza cuando la corriente y el voltaje en cada punto del circuito permanecen constantes en el tiempo. 

Más allá de la física, podemos hablar de equilibrio en muchas otras disciplinas: 

- Equilibrio químico: En química, el equilibrio se refiere al estado en el cual las concentraciones de reactivos y productos en una reacción química reversible se mantienen 

Tema 1 - Física IV. Grado en Física, Universidad de Salamanca 

1 

constantes a lo largo del tiempo. En este punto, las velocidades de la reacción directa e inversa son iguales, y no hay cambios netos en la composición del sistema. 

- Equilibrio genético: En genética de poblaciones, el equilibrio se describe como un estado en el cual las frecuencias alélicas y genotípicas en una población permanecen constantes a través de generaciones. Este estado se alcanza cuando no hay factores evolutivos que actúen sobre la población, como la mutación, la selección natural, la deriva genética, o el flujo genético. 

- Equilibrio social: En sociología, el equilibrio social se refiere a un estado de relativa estabilidad y orden en una sociedad, donde las diferentes partes del sistema social funcionan de manera armoniosa. Este estado implica un equilibrio de poder entre los diferentes grupos sociales, así como la aceptación generalizada de las normas y valores sociales. 

- Equilibrio económico: En economía, el equilibrio es un estado en el cual las fuerzas de la oferta y la demanda están equilibradas. En esta situación, no hay tendencia a que los precios o las cantidades cambien. 

- Equilibrio en matemáticas: En matemáticas, un punto de equilibrio de un sistema de ecuaciones diferenciales es un punto en el que el sistema no cambia con el tiempo. En otras palabras, es un estado estacionario del sistema. 

Para que un sistema esté en equilibrio no basta con que una de sus propiedades esté en equilibrio, sino que todas las magnitudes que lo caracterizan deben estarlo. Eso es una condición muy exigente en sistemas que estén descritos por varias magnitudes. Por eso nosotros vamos a hablar de equilibrio de las propiedades de un sistema. Un sistema físico puede estar evolucionando en el tiempo con ciertas magnitudes, por ejemplo, las velocidades, y sin embargo tener otras magnitudes que no cambian en el tiempo, como una aceleración constante. 

Pensemos por tanto en una magnitud de un sistema que vamos a denotar con la letra  . Diremos que esa propiedad está en equilibrio si no evoluciona en el tiempo. Matemáticamente podemos escribirlo con la expresión 

**==> picture [233 x 24] intentionally omitted <==**

## Equilibrio mecánico 

En el caso del equilibrio mecánico, aunque a veces se hable de “equilibrio de fuerzas”, no es la fuerza la magnitud que está en equilibrio, sino la velocidad: Dado que la definición de 

Tema 1 - Física IV. Grado en Física, Universidad de Salamanca 

2 

 equilibrio mecánico es que la fuerza neta, y no su derivada, sea cero, _F_  0 , a partir de la   segunda ley de Newton, _F_  _ma_ , y teniendo en cuenta que la aceleración es la derivada de la velocidad, tenemos que 

**==> picture [234 x 23] intentionally omitted <==**

por lo que es la velocidad la magnitud que está en equilibrio. 

En cuanto a la posición, no es una propiedad que tenga que estar en equilibrio cuando hablamos de equilibrio mecánico. Un objeto que está en reposo y no se desplaza en un sistema de referencia dado es solo un caso particular de equilibrio mecánico. 

Veamos unos cuantos ejemplos de equilibrio en física: 

Ejemplo 1. Condición de equilibrio de un péndulo simple 

La condición de equilibrio en un péndulo se produce cuando la velocidad del péndulo es constante. Esto ocurre cuando el péndulo está en reposo en su posición vertical inferior (ángulo cero con respecto a la vertical). 

**==> picture [166 x 164] intentionally omitted <==**

Figura 1.1 Esquema de las fuerzas que intervienen en el péndulo simple. 

Veamos cómo deducirlo matemáticamente paso a paso: 

## 1. Identificar las fuerzas: 

Las fuerzas que actúan sobre la masa del péndulo (Figura 1.1) son la tensión _T_ de la cuerda y el peso _Fg_  _mg_ . El signo menos indica que apunta en sentido negativo del eje vertical. 

## 2. Proyectar las fuerzas en los ejes: 

Se descomponen las fuerzas en sus componentes horizontal (eje _x_ ) y vertical (eje _y_ ). 

Tema 1 - Física IV. Grado en Física, Universidad de Salamanca 

3 

**==> picture [256 x 28] intentionally omitted <==**

## 3. Aplicar la condición de equilibrio: 

Para que la velocidad sea constante, la aceleración debe ser cero. Según la segunda ley de Newton, esto implica que la suma de las fuerzas en cada eje debe ser igual a cero. 

- Equilibrio en x: _[F] x_  _T_ sin   0 

- Equilibrio en y: _[F] y_  _mg_  _T_ cos   0 

## 4. Resolver las ecuaciones: 

La ecuación para el eje horizontal implica que sin  0 , lo que significa que  0  (posición vertical). Sustituyendo esta condición en la ecuación para el eje _y_ , se obtiene _T_  _mg_ , lo que significa que la tensión es igual al peso en la posición de equilibrio. 

## Conclusión: 

> La condición de equilibrio en un péndulo simple se cumple cuando el ángulo  es cero, lo que corresponde a la posición vertical inferior. En este punto, la tensión de la cuerda es igual al peso y, además de no haber aceleración, la velocidad es cero ya que si no lo fuera variaría el ángulo del péndulo y dejaría de estar en equilibrio. 

## Ejemplo 2. Condición de equilibrio de una esfera en caída libre con rozamiento 

En el caso de un objeto esférico que cae en un fluido con rozamiento, el equilibrio mecánico también viene dado por la compensación de las fuerzas que actúan sobre la esfera. Para simplificar las cosas, pensemos que el medio en el que se produce la caída es el aire y que, al ser su densidad mucho menor que la de la esfera, podemos despreciar el empuje. En ese caso, las dos fuerzas que actúan sobre el objeto son el peso y la fuerza de arrastre (Figura 1.2), que da cuenta del efecto del rozamiento. Dependiendo de las características del fluido y si la velocidad de caída no es muy grande, podemos asumir que la fuerza de arrastre es proporcional a la velocidad _v_ (ley de Stokes). Concretamente, para una esfera la fuerza de arrastre es _[F] a_  6  _rv_  _bv_ , siendo  la viscosidad dinámica y _r_ el radio de la esfera. 

**==> picture [210 x 114] intentionally omitted <==**

Figura 1.2 Fuerzas que actúan sobre una esfera en caída libre 

Tema 1 - Física IV. Grado en Física, Universidad de Salamanca 

4 

Puedes intentar encontrar la condición de equilibrio en este caso. Veamos ahora otros ejemplos no mecánicos de equilibrio. 

## Ejemplo 3. Equilibrio térmico 

Como sabemos, dos objetos en contacto están en equilibrio térmico si no hay transferencia de energía térmica entre ellos. Supongamos una geometría como la que se muestra en la figura 1.3. La ecuación que rige la dinámica del sistema es: 

**==> picture [258 x 23] intentionally omitted <==**

donde _q_ es la energía calórica, _A_ es el área de la zona de la unión, _k_ es su conductividad térmica, _L_ es su longitud, _T_ 1 es la temperatura del primer cuerpo y _T_ 2 es la temperatura del segundo. Una simple ojeada a esta ecuación nos indica que el equilibrio térmico se produce cuando las temperaturas de los dos cuerpos son iguales. 

**==> picture [187 x 108] intentionally omitted <==**

Figura 1.3 Dos objetos a diferente temperatura con una zona de unión. 

## Ejemplo 4. Equilibrio en un circuito eléctrico 

Pensemos por ejemplo en un circuito RL en serie como el de la figura 1.4, con una resistencia y una bobina, en el que queremos encontrar la condición de equilibrio de la intensidad de corriente. 

**==> picture [211 x 122] intentionally omitted <==**

Figura 1.4 Circuito RL en serie 

Tema 1 - Física IV. Grado en Física, Universidad de Salamanca 

5 

¿Cómo hallarías esa condición de equilibrio? 

## Puntos de equilibrio 

En general, la condición de equilibrio para una magnitud no se va a dar para todos los valores de las variables de las que depende sino solamente para algunos. Por ejemplo, si el sistema que consideramos depende de dos variables,  y _x_ , y la ecuación de movimiento es: 

**==> picture [242 x 23] intentionally omitted <==**

Entonces _x_ 0 es un punto de equilibrio si _f_ (  , _x_ 0 )  0 , de forma que en ese punto se cumple que: 

**==> picture [253 x 23] intentionally omitted <==**

El concepto de punto de equilibrio no es estrictamente geométrico, la variable _x_ puede ser una posición, pero también una temperatura, una concentración química, etc. 

En el caso del equilibrio mecánico, sabemos que la condición que lo define es que la fuerza total sea nula. Cuando la fuerza no es homogénea en todo el espacio, tendremos que el  equilibrio se producirá en los puntos _[r]_[] 0[ en los que ] _F_ ( _r_ 0 )  0 . 

Retomemos el caso del péndulo simple (ejemplo 1). Habíamos visto que el equilibrio se producía cuando sin  0 . Como en nuestro sistema de coordenadas (figura 1.1) _x_  _l_ sin  , _y_  _l_ (1  cos  ) , el punto de equilibrio del sistema será ( _xeq_ , _yeq_ )  (0,0) , es decir, nuestro origen de coordenadas. 

Puedes intentar hallar los puntos de equilibrio en otros sistemas, por ejemplo un muelle del que cuelga una masa, o un objeto que flota parcialmente sumergido en un líquido. 

## Estabilidad del equilibrio 

El equilibrio de un sistema puede ser clasificado en tres tipos principales: estable, inestable e indiferente (Figura 1.5). Esta clasificación se basa en la respuesta del sistema ante pequeñas perturbaciones o desplazamientos desde su posición de equilibrio. 

● Equilibrio estable: Un sistema se encuentra en equilibrio estable si, al ser desplazado ligeramente de su posición de equilibrio, experimenta una fuerza o influencia que lo impulsa a regresar a dicha posición. En otras palabras, un equilibrio estable se caracteriza por la tendencia del sistema a restaurar su estado inicial después de una perturbación. Imaginemos Tema 1 - Física IV. Grado en Física, Universidad de Salamanca 6 

una pelota en el fondo de un cuenco: si la desplazamos un poco de su posición de reposo, la gravedad la hará oscilar alrededor del punto más bajo del cuenco hasta que, si hay rozamiento, finalmente se detenga de nuevo en el fondo. Si no hay rozamiento, el sistema oscilará alrededor del punto de equilibrio sin alejarse de él más allá de una región limitada. Como veremos, este comportamiento se debe a que la energía potencial del sistema es mínima en la posición de equilibrio, asemejándose a un valle en un mapa de energía potencial. Cualquier desplazamiento desde esta posición implica un aumento de la energía potencial, generando una fuerza que busca llevar al sistema de regreso al punto de mínima energía. 

**==> picture [400 x 73] intentionally omitted <==**

Figura 1.5 Esquema con los tres tipos de equilibrio: estable (izquierda), inestable (centro) e indiferente (derecha). 

● Equilibrio inestable: Un sistema está en equilibrio inestable si, al ser desplazado levemente de su posición de equilibrio, las fuerzas o influencias presentes lo alejan aún más de dicha posición. En este caso, la perturbación inicial no es contrarrestada, sino que se amplifica, provocando que el sistema se aleje indefinidamente de su estado inicial. Un ejemplo clásico es una pelota en la cima de una colina: cualquier pequeño desplazamiento hará que la pelota ruede cuesta abajo, alejándose cada vez más de la cima. Desde el punto de vista de la energía potencial, un equilibrio inestable corresponde a un máximo en el mapa de energía potencial, como la cima de una montaña. Cualquier movimiento desde esta posición llevará al sistema a un punto de menor energía potencial, impidiendo que regrese a su estado inicial. 

● Equilibrio indiferente o neutro: Un sistema se encuentra en equilibrio indiferente si, al ser desplazado de su posición de equilibrio, permanece en la nueva posición sin experimentar fuerzas que lo impulsen a regresar a la posición original o a alejarse aún más. En este tipo de equilibrio, cualquier punto dentro de un cierto rango puede ser considerado una posición de equilibrio, ya que el sistema no muestra preferencia por un estado particular dentro de esa región. Un ejemplo sería una pelota en una superficie plana: al desplazar la pelota, esta se detendrá en la nueva posición sin experimentar fuerzas que la obliguen a moverse. En términos de energía potencial, un equilibrio indiferente se caracteriza por una energía potencial constante dentro de un cierto rango. Esto significa que el sistema no experimenta cambios en su energía potencial al ser desplazado dentro de esta región, por lo que no hay fuerzas que lo impulsen a moverse en una dirección particular. 

Hay situaciones menos habituales, como el equilibrio semiestable, que ocurre cuando las fuerzas son atractivas desde uno de los lados y repulsivas desde el otro. Además, en Tema 1 - Física IV. Grado en Física, Universidad de Salamanca 7 

sistemas cuya dinámica ocurre en más de una dimensión, la fenomenología puede ser todavía más complicada. 

Es importante destacar que la clasificación del equilibrio como estable, inestable o indiferente depende del sistema en cuestión y de las fuerzas que actúan sobre él. Un mismo sistema puede presentar diferentes tipos de equilibrio dependiendo de las condiciones en las que se encuentre. 

## Grados de libertad de un sistema físico 

Los grados de libertad en un sistema físico se refieren al número mínimo de coordenadas independientes necesarias para describir completamente el estado o la configuración de un sistema en el espacio. En otras palabras, los grados de libertad representan la capacidad del sistema para moverse y cambiar de posición en el espacio. Para comprender mejor este concepto, consideremos los siguientes ejemplos: 

● Un muelle que solo se mueve verticalmente: Este sistema solo tiene un grado de libertad, ya que solo necesitamos una coordenada, la altura, para describir su posición. No es necesario considerar su movimiento horizontal, ya que se asume que permanece constante. 

● Un péndulo simple: Aunque el péndulo se mueve en un plano bidimensional (descrito por las coordenadas _x_ e _y_ ), en realidad solo tiene un grado de libertad porque ambas coordenadas no son independientes entre sí. Esto se debe a que la longitud del péndulo es constante, lo que impone una restricción al movimiento. La posición del péndulo se puede determinar completamente conociendo el ángulo  que forma con la vertical. Este tipo de restricciones se denominan ligaduras. 

● Un insecto flotando en agua: Este sistema tiene dos grados de libertad, ya que puede moverse libremente en la superficie del agua, un plano bidimensional. 

En general, el número de grados de libertad será igual al número de variables del sistema menos el número de ligaduras entre ellas. 

La identificación de los grados de libertad en un sistema físico es crucial para simplificar su análisis. Al utilizar las coordenadas independientes que respetan las restricciones del sistema, las ecuaciones de movimiento se vuelven más sencillas y manejables. 

Por ejemplo, al analizar el movimiento de un péndulo simple, es mucho más fácil trabajar con una sola ecuación de movimiento que involucre el ángulo  , en lugar de tener que lidiar con dos ecuaciones (para _x_ e _y_ ) que contienen la restricción de la longitud del péndulo. Veámoslo: Para deducir la ecuación del péndulo simple en la coordenada angular  , se debe considerar que el péndulo se mueve en un plano bidimensional sujeto a la fuerza gravitatoria y la tensión de la cuerda que lo sostiene. La clave para simplificar el problema es aprovechar que la 

Tema 1 - Física IV. Grado en Física, Universidad de Salamanca 

8 

longitud de la cuerda ( _l_ ) permanece constante durante el movimiento, lo que reduce los grados de libertad a uno, representado por el ángulo  . Seguiremos los siguientes pasos: 

## 1. Expresión de las ecuaciones de movimiento en _x_ e _y_ : 

A partir de las fuerzas que intervienen en el problema (ecuación (1.3)) podemos escribir las ecuaciones de movimiento 

**==> picture [264 x 54] intentionally omitted <==**

2. Cálculo de los operadores diferenciales en coordenadas polares ( _l_ ,  ) : Como la relación entre los dos sistemas de coordenadas es _x_  _l_ sin  , _y_  _l_ (1  cos  ) , derivando tenemos: 

**==> picture [288 x 117] intentionally omitted <==**

3. Obtención de la ecuación del péndulo simple para la coordenada  : 

Sustituyendo las expresiones de la segunda derivada de _x_ e _y_ en las ecuaciones de movimiento, y luego multiplicando la ecuación en _x_ por cos  y la ecuación en _y_ por sin  , se logra eliminar la tensión al sumar ambas ecuaciones. Después de la simplificación, se llega a la siguiente ecuación: 

**==> picture [250 x 25] intentionally omitted <==**

Esta ecuación diferencial de segundo orden describe la evolución del ángulo  en función del tiempo para un péndulo simple. Es importante notar que esta ecuación no es lineal debido al término sin  . 

La conocida ecuación lineal del péndulo ideal se obtiene al hacer la aproximación de ángulos pequeños, que se basa en el hecho de que para ángulos pequeños (   1 radián ), el valor 

Tema 1 - Física IV. Grado en Física, Universidad de Salamanca 

9 

del seno del ángulo es aproximadamente igual al valor del ángulo expresado en radianes. Usando esta aproximación se obtiene la ecuación lineal del péndulo, válida para pequeñas oscilaciones: 

**==> picture [242 x 25] intentionally omitted <==**

Esta ecuación diferencial lineal de segundo orden es mucho más sencilla de resolver analíticamente que la ecuación del péndulo sin la aproximación de pequeñas oscilaciones. En los sistemas multidimensionales en los cuales tenemos varios grados de libertad, el concepto de punto de equilibrio se generaliza y podemos obtener no solo puntos de equilibrio, sino también curvas de equilibrio, superficies de equilibrio, etc., es decir, regiones en las cuales el sistema está en equilibrio y que tienen varias dimensiones. 

Un ejemplo es la superficie del agua cuando tenemos un barco flotando (despreciando el efecto de las olas). El barco está en equilibrio en cualquier punto de esta superficie del agua, luego la condición de equilibrio es únicamente que la parte hundida del barco sea una cierta cantidad, pero el barco puede estar en cualquier posición del plano que forma la superficie del agua. En este caso, estaríamos hablando de un plano de equilibrio, de una condición de equilibrio bidimensional. 

## Dinámica alrededor del equilibrio 

En un sistema físico, hay dos comportamientos dinámicos principales (no son los únicos) cuando un sistema es desplazado de su posición de equilibrio estable, que son el amortiguamiento y las oscilaciones. El amortiguamiento se refiere a la pérdida de energía a lo largo del tiempo, lo que hace que el sistema evolucione hacia la condición de equilibrio gradualmente. Este fenómeno suele estar causado por fuerzas que se oponen al movimiento, como la fricción. Por su parte, la oscilación puede entenderse como la variación repetitiva en el tiempo de una o más propiedades físicas de un sistema alrededor de un punto de equilibrio. Es importante tener en cuenta que estos dos comportamientos no son mutuamente excluyentes. Un sistema puede exhibir amortiguamiento y oscilaciones al mismo tiempo. Por ejemplo, como veremos, un péndulo oscila alrededor de su punto de equilibrio, pero la amplitud de las oscilaciones disminuye con el tiempo debido a la fricción del aire, lo que sería un tipo de amortiguamiento. 

Analicemos estos dos tipos de comportamiento con un poco más de profundidad. 

## Amortiguamiento 

El amortiguamiento, en un sistema dinámico, ocurre cuando la tasa de cambio de una variable del sistema es de signo opuesto a la desviación de esa variable con respecto a su valor de 

Tema 1 - Física IV. Grado en Física, Universidad de Salamanca 

10 

equilibrio, como se muestra en la figura 1.6. Matemáticamente, si la evolución de esa variable viene dada por la ecuación: 

**==> picture [239 x 23] intentionally omitted <==**

para que el sistema presente amortiguamiento, la función _f_ (  ) debe cumplir las siguientes condiciones: 

● _f_ (  )  0 si   _eq_ : Si la variable es mayor que su valor de equilibrio  _eq_ , la fuerza debe ser negativa, es decir, debe actuar para disminuir la variable y acercarla al equilibrio. ● _f_ (  )  0 si   _eq_ : Si la variable es igual a su valor de equilibrio, la fuerza debe ser cero, lo que significa que no hay ninguna fuerza actuando sobre la variable y se mantendrá en equilibrio. 

● _f_ (  )  0 si   _eq_ : Si la variable es menor que su valor de equilibrio, la fuerza debe ser positiva, es decir, debe actuar para aumentar la variable y acercarla al equilibrio. 

Un caso especial de amortiguamiento es el amortiguamiento lineal. En este caso, la función _f_ (  ) es una función lineal de la variable, lo que significa que la fuerza es proporcional al desplazamiento de la variable desde su valor de equilibrio: 

**==> picture [255 x 17] intentionally omitted <==**

siendo _C_ una constante positiva que representa la magnitud de la fuerza de amortiguamiento. La solución general para este tipo de ecuación diferencial es una función exponencial decreciente, lo que significa que la variable se acerca asintóticamente al valor de equilibrio con el tiempo. 

**==> picture [341 x 154] intentionally omitted <==**

Figura 1.6 Esquema del signo de la fuerza para que haya amortiguamiento. 

Tema 1 - Física IV. Grado en Física, Universidad de Salamanca 

11 

Es importante recordar que esta definición matemática describe el comportamiento de una sola variable en un sistema. Un sistema complejo puede tener varias variables, cada una con su propio tipo de amortiguamiento. 

Para entender mejor el concepto de amortiguamiento, vamos a estudiar paso a paso un caso de amortiguamiento lineal, la caída libre de un objeto en un fluido, que habíamos planteado en el ejemplo 3 (figura 1.2). 

## 1. Definición del problema: 

Un objeto cae dentro de un fluido, sin causar turbulencias. La ecuación que rige este movimiento es la segunda ley de Newton, que establece que la masa del objeto multiplicada por su aceleración es igual a la suma de las fuerzas que actúan sobre él. En este caso tenemos dos fuerzas principales: la fuerza de gravedad y la fuerza de arrastre del fluido. Por simplicidad despreciamos el empuje asumiendo que la densidad del fluido es mucho menor que la del objeto. 

## 2. Ecuación de movimiento: 

Las dos fuerzas involucradas son las de la figura 1.2, la de la gravedad, _Fg_  _mg_ , y la de arrastre, _[F] a_  _bv_ . La ecuación de movimiento es: 

**==> picture [273 x 24] intentionally omitted <==**

## 3. Condición de equilibrio: 

La velocidad de equilibrio _veq_ se alcanza cuando la fuerza de arrastre se iguala a la fuerza de gravedad, es decir, cuando la aceleración del objeto es cero. Al resolver la ecuación de movimiento para _dv_ / _dt_  0 , obtenemos la velocidad de equilibrio: _veq_  _mg_ / _b_ . Esto significa que después de un cierto tiempo, el objeto caerá a una velocidad constante, _veq_ , determinada por el equilibrio entre la fuerza de gravedad y la fuerza de arrastre. 

## 4. Solución de la ecuación de movimiento: 

Para obtener la velocidad del objeto en función del tiempo, necesitamos resolver la ecuación diferencial. Podemos utilizar el método de separación de variables para resolver esta ecuación: 

**==> picture [92 x 25] intentionally omitted <==**

## 4.1. Reordenamos la ecuación: 

**==> picture [313 x 24] intentionally omitted <==**

Tema 1 - Física IV. Grado en Física, Universidad de Salamanca 

12 

1 _t_ 4.3. Resolvemos las integrales: _ln_  _bv_  _mg_    _C_ , donde _C_ es una constante de _b m_ 

integración. 

**==> picture [274 x 29] intentionally omitted <==**

donde la velocidad inicial, _v_ 0  _v_ (0) , determina el valor de la constante de integración _C_ . 

## 5. Análisis de la solución: 

La solución obtenida para _v t_ ( ) describe el comportamiento de un sistema amortiguado. Observamos que la velocidad del objeto se acerca exponencialmente a la velocidad de equilibrio, _veq_  _mg_ / _b_ , a medida que el tiempo tiende a infinito. La constante de tiempo  _m_ / _b_ determina la rapidez con la que el objeto alcanza la velocidad de equilibrio. Cuanto mayor sea la masa del objeto ( _m_ ) o menor sea la constante de amortiguamiento ( _b_ ), mayor será la constante de tiempo y más lentamente alcanzará el objeto la velocidad de equilibrio. 

La solución también muestra que la velocidad inicial del objeto influye en su velocidad en cualquier instante de tiempo, pero no afecta al valor final de la velocidad de equilibrio. 

## Oscilaciones 

Las oscilaciones en un sistema dinámico se caracterizan por la presencia de una fuerza o influencia restauradora que se opone al desplazamiento de una variable con respecto a su punto de equilibrio. Esta fuerza siempre actúa en dirección opuesta al desplazamiento, empujando al sistema de vuelta hacia el equilibrio. Sin embargo, debido a la inercia del sistema, este sobrepasa el punto de equilibrio, creando un movimiento de vaivén alrededor de dicho punto. 

Matemáticamente, la oscilación se puede describir mediante una ecuación diferencial de segundo orden de la siguiente forma: 

**==> picture [258 x 25] intentionally omitted <==**

donde _f_ (   _eq_ ) describe la fuerza restauradora que depende del desplazamiento desde el  punto de equilibrio,   _eq_[. ] 

Para que haya oscilaciones, la fuerza restauradora debe cumplir las siguientes condiciones: 

● _f_ (  _eq_ )  0 si   _eq_ : Si el valor de la variable es inferior a su valor de equilibrio, la fuerza debe ser positiva, actuando para aumentar su valor y llevar el sistema hacia el equilibrio. ● _f_ (  _eq_ )  0 si   _eq_ : En el valor de equilibrio, la fuerza restauradora debe ser cero. 

Tema 1 - Física IV. Grado en Física, Universidad de Salamanca 

13 

● _f_ (   _eq_ )  0 si   _eq_ : Si la variable está por encima de su valor de equilibrio, la fuerza debe ser negativa, actuando para disminuir su valor y llevar el sistema hacia el equilibrio. 

Un ejemplo clásico de oscilación es la dinámica de un muelle. Para comprender cómo se resuelve la dinámica de un muelle matemáticamente, seguiremos el siguiente proceso: 

## 1. Definición del sistema: 

Empezamos por definir un sistema básico masa-resorte (figura 1.7). Este sistema se compone de una masa _m_ conectada a un resorte de constante elástica  . Para facilitar el análisis, generalmente se desprecia la masa del muelle. Consideremos un muelle vertical con un extremo fijo y una masa _m_ suspendida en su extremo libre. 

**==> picture [149 x 127] intentionally omitted <==**

Figura 1.7 Sistema masa-muelle en la posición de equilibrio con las dos fuerzas que intervienen. Elegimos el eje _y_ en sentido negativo del eje vertical. 

Definimos _y t_ ( ) como la posición de la masa en función del tiempo, con el origen _y_  0 en la posición donde el muelle sin la masa no está estirado y sentido positivo hacia abajo (cuando el muelle se estira). _l_ 0 representa la elongación del muelle en la posición de equilibrio con la masa, es decir, cuando _y_  _l_ 0 la fuerza del muelle compensa la fuerza de gravedad que actúa sobre la masa. 

## 2. Identificación de las fuerzas: 

Las fuerzas que actúan sobre la masa son la fuerza de gravedad, _Fg_  _mg_ , y la fuerza restauradora del muelle, _[F] k_  _y_ . 

## 3. Ecuación de movimiento: 

Aplicando la segunda ley de Newton, tenemos que: 

**==> picture [272 x 25] intentionally omitted <==**

Tema 1 - Física IV. Grado en Física, Universidad de Salamanca 

14 

## 4. Simplificación y solución: 

En la posición de equilibrio del muelle con la masa ( _y_  _l_ 0 ), la aceleración es cero. Por lo tanto, _mg_   _l_ 0 . Sustituyendo en la ecuación de movimiento, obtenemos: 

**==> picture [257 x 25] intentionally omitted <==**

Esta ecuación diferencial es claramente la de un oscilador con una fuerza lineal. Como veremos en el tema siguiente, la solución general de esta ecuación es _y t_ ( )  _l_ 0  _A_ cos  0 _t_  , donde _A_ es la amplitud de la oscilación, que se refiere al desplazamiento máximo de la masa desde la posición de equilibrio; 0 es la frecuencia angular de la oscilación y se relaciona con la masa y la constante del resorte mediante la fórmula  0   _m_ ;  es la fase inicial, que define la posición de la masa en _t_  0 . Las constantes _A_ y  se determinan a partir de las condiciones iniciales del problema, que son la posición inicial y la velocidad inicial de la masa. 

Como resumen de las dos rutas hacia el equilibrio que hemos estudiado podemos decir: 

- Un sistema está amortiguado en una de sus variables si la tasa de cambio de la variable es de signo opuesto a la desviación de esa variable con respecto a su valor de equilibrio. - Un sistema oscila en una de sus variables si la fuerza tiene el sentido contrario al desplazamiento respecto del punto de equilibrio. 

## Mapas de energía y analogía gravitatoria 

La última parte de este tema se centra en los conceptos de energía potencial, mapas de energía potencial y la analogía gravitatoria. Estos conceptos son esenciales para comprender el comportamiento de los sistemas físicos, especialmente aquellos que exhiben movimiento oscilatorio, sin necesidad de resolver ecuaciones de movimiento complejas. 

## Energía potencial 

La energía potencial se define como la energía que posee un objeto debido a su posición o configuración en un campo de fuerza. En otras palabras, es la energía almacenada en un sistema como resultado de la realización de trabajo contra una fuerza conservativa. Recordemos que fuerza conservativa es aquella en la que el trabajo realizado para mover un objeto de un punto a otro no depende de la trayectoria seguida, sino únicamente de los puntos inicial y final. 

Tema 1 - Física IV. Grado en Física, Universidad de Salamanca 

15 

En un sistema unidimensional, la energía potencial se puede calcular utilizando la siguiente fórmula: 

**==> picture [274 x 19] intentionally omitted <==**

donde _U_ es la energía potencial, _F_ ( _x_ ) es la fuerza conservativa que actúa sobre el objeto y _x_ representa la posición del objeto. 

Un aspecto clave es que la energía potencial está asociada a la fuerza. La fuerza se puede obtener como la derivada negativa de la energía potencial con respecto a la posición: 

**==> picture [249 x 24] intentionally omitted <==**

En sistemas con más dimensiones, la derivada con respecto a la coordenada se sustituye por el gradiente. 

## Mapas de energía potencial 

Los mapas de energía potencial, también conocidos como diagramas de energía potencial, son representaciones gráficas de la energía potencial de un sistema en función de la posición o configuración. Estos mapas proporcionan una visualización intuitiva del comportamiento del sistema. Como la condición de equilibrio ocurre cuando la fuerza es cero, los puntos de equilibrio coincidirán con los máximos y mínimos del mapa de energía potencial, que son aquellos en los que su derivada se anula. Los puntos de equilibrio estable corresponden a mínimos de energía potencial, como los valles en un mapa topográfico, mientras que los puntos de equilibrio inestable se representan como máximos, como las cumbres de las montañas. En la figura 1.8 se muestra un mapa de energía potencial. 

**==> picture [212 x 132] intentionally omitted <==**

Figura 1.8 Mapa de energía potencial que muestra puntos de equilibrio estables (B y D) e inestables (A y C). 

Tema 1 - Física IV. Grado en Física, Universidad de Salamanca 

16 

Al analizar la forma del mapa de energía potencial, podemos predecir el movimiento del sistema. Por ejemplo, en un pozo de potencial, un objeto oscilará alrededor del punto de equilibrio estable. 

## Analogía gravitatoria 

La analogía gravitatoria es una herramienta conceptual que utiliza nuestra experiencia intuitiva con la gravedad para comprender sistemas con diferentes tipos de fuerzas. La idea central es que si dos sistemas, incluso si son de naturaleza física diferente, tienen mapas de energía potencial con la misma forma, entonces sus movimientos serán cualitativamente similares. En el caso de la energía potencial gravitatoria, la energía es proporcional a la altura. Esto hace que, por ejemplo, una montaña rusa sea un mapa de energía potencial. 

**==> picture [199 x 143] intentionally omitted <==**

**==> picture [205 x 25] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 2  2 2<br>U x ( )  mgh x ( )   x  h x ( )  x  Ax<br>2 2 mg<br>**----- End of picture text -----**<br>


Figura 1.9 Analogía de la energía potencial de un muelle con la energía gravitatoria. 

El movimiento de una masa unida a un resorte, que experimenta una fuerza restauradora elástica, se puede visualizar como el movimiento de un objeto en un campo gravitatorio que sigue una trayectoria equivalente a la forma del mapa de energía potencial del resorte. La energía potencial de un muelle es proporcional al cuadrado de su deformación respecto a la 2 posición de equilibrio ( _U x_ ( )  1 / 2  _x_ , puedes demostrarlo). Esto genera un mapa de energía potencial con forma de parábola, que predice un movimiento oscilatorio armónico simple alrededor del punto de equilibrio (figura 1.9). 

Es importante tener en cuenta que la analogía gravitatoria tiene sus limitaciones: 

- No tiene en cuenta fuerzas no conservativas, como la fricción, que pueden disipar energía y modificar el movimiento del sistema. 

- En sistemas no inerciales, donde actúan fuerzas ficticias como la fuerza de Coriolis, la analogía gravitatoria no es directamente aplicable sin modificaciones. 

En resumen, la energía potencial, los mapas de energía potencial y la analogía gravitatoria son herramientas conceptuales poderosas que nos permiten comprender el comportamiento de una amplia gama de sistemas físicos. Sin embargo, es crucial ser conscientes de las 

Tema 1 - Física IV. Grado en Física, Universidad de Salamanca 

17 

limitaciones de la analogía gravitatoria y considerar la influencia de otros factores, como las fuerzas no conservativas y los sistemas de referencia no inerciales, para obtener una descripción completa del movimiento del sistema. 

Tema 1 - Física IV. Grado en Física, Universidad de Salamanca 

18 



---

## Imágenes extraídas


```{image} Física IV - Tema 1_images/page3_img1.jpeg
:alt: Imagen extraída del PDF
:width: 80%
:align: center
```


```{image} Física IV - Tema 1_images/page4_img1.jpeg
:alt: Imagen extraída del PDF
:width: 80%
:align: center
```


```{image} Física IV - Tema 1_images/page5_img1.jpeg
:alt: Imagen extraída del PDF
:width: 80%
:align: center
```


```{image} Física IV - Tema 1_images/page5_img2.jpeg
:alt: Imagen extraída del PDF
:width: 80%
:align: center
```


```{image} Física IV - Tema 1_images/page7_img1.jpeg
:alt: Imagen extraída del PDF
:width: 80%
:align: center
```


```{image} Física IV - Tema 1_images/page11_img1.jpeg
:alt: Imagen extraída del PDF
:width: 80%
:align: center
```


```{image} Física IV - Tema 1_images/page14_img1.jpeg
:alt: Imagen extraída del PDF
:width: 80%
:align: center
```


```{image} Física IV - Tema 1_images/page16_img1.jpeg
:alt: Imagen extraída del PDF
:width: 80%
:align: center
```


```{image} Física IV - Tema 1_images/page17_img1.jpeg
:alt: Imagen extraída del PDF
:width: 80%
:align: center
```
