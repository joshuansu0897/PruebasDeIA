# Apuntes y Definiciones

## **Inteligencia Artificial**
Intento de hacer a un dispositivo tan o más inteligente que un humano. Darle la capacidad de razonar o pensar en función a los datos que se le está pasando.

Niveles de Inteligencia Artificial:

- **Inteligencia Artifical Débil:** Son cosas como nuestros asistentes virtuales. Alexa, Cortana, Google Assistant. Solo puede hacer un objetivo. Ejemplo, un asistente de celular como Siri. No rebasan la línea de lo que están programados para hacer.

- **Inteligencia Artifical Fuerte:** Tiene la habilidad de reconocer patrones en el comportamiento humano y/o el ambiente. Tambien puede hacer varios objetivos, saber como me siento por mis expresiones, saber donde estoy, etc.

- **Super Inteligencia Artificial:** Supera la inteligencia de un humano, incluso alguno considerado genio. Tiene la capacidad de tomar decisiones propias. Es la que nos va a reemplazar sin darnos cuenta, puede pensar en millones de cosas a la vez.

**Singularity:**
Es el nombre que se le da al concepto del momento en el que la Super Inteligencia Artificial va a dominar.

## **Anatomia** de una Inteligencia Artificial
La anatomia de IA consta de 5 partes:
- **Percepción.** A través de sensores.
- **Procesamiento natural del lenguaje.**
- **Representación del conocimiento.** Darle una imagen gráfica a los conocimientos o eventos.
- **Razonamiento.** Capacidad para tomar una decisión.
- **Planeación y Navegación.** La forma de reaccionar ante situaciones inesperadas.

**Nota:**
Una inteligencia *Debil* no necesita implementar las 5, puede implementar una o varias, pero en el caso de la *Super* y *Fuerte* si es necesario.

## **Machine Learning (ML)**
Serie de algoritmos que hacen que un sistema sea artificialmente inteligente. Tambien puede ser visto como, Es la manera de hacer que algo sea artificialmente inteligente.

Los algoritmos se dividen en 2 partes:

- **Aprendizaje supervisado.** En este aprendizaje somos nosotros los que guiamos al algoritmo a la respuesta correcta. Ejemplo, es como cuando nos enseñan a escribir.

- **Aprendizaje sin supervisión.** El algoritmo detecta patrones y agrupa la información con estos patrones. Aquí nosotros podemos darle características a los algoritmos y éstos agrupan todo mediante patrones relacionados con esa información. Se basa en la información que le doy para agrupar eso.

**NOTA:** puedes ver como si la **Inteligencia Artificial** fuera un *carro* y **Machine Learning** la *mecanica automotriz (motor)*

## **Probabilidad y Estadística**
**Machine Learning** utiliza una serie de técnicas de **Probabilidad y Estadística** para predecir un valor basado en la información que le proveemos, es por esto que es muy importante que tengamos claro algunos conceptos.

Conceptos:
- **Media o Promedio:** La suma de las medidas dividida entre el número total de datos.
    
    ![](https://craneoprevilegiado.com/wp-content/uploads/2015/03/media-formula.jpg?raw=true)

- **Moda:** Es el valor con mayor frecuencia en una distribución de datos.

- **Mediana:** Es el valor que ocupa el lugar central de todos los datos cuando están agrupados de menor a mayor.

- **Varianza:** Es una medida de dispersión definida como la esperanza del cuadrado de la desviación de dicha variable respecto a la media, o dicho de otra forma, es la media de los residuos al cuadrado.
    
    ![](https://i.imgur.com/V4Wz8XI.png?raw=true)

- **Desviación Estándar:** Es la raíz cuadrada de la varianza de la variable.

    ![](https://es.plusmaths.com/wp-content/uploads/sites/2/2015/09/formula-de-la-desviacion-estandar.jpg?raw=true)

## **Algoritmos**
Conjunto de instrucciones específicas y finitas, esto significa que son pasos determinados que tienen un inicio y un fin. Estos pasos nos ayudan a completar una tarea.

### **Regresión Lineal**
Es el algoritmo por defecto y es un algoritmo de aprendizaje supervisado. Ayuda a predecir el valor esperado de una variable a cuando **b** tiene un cierto valor.

Para poder hacer una regresión lineal, asumimos que los valores tienen una relación lineal, por esto es necesario analizar nuestros datos antes de hacer una predicción para verificar que sea así.

Esta es la fórmula para poder calcular el **pronóstico**:

![](https://i.imgur.com/gc5KRml.png?raw=true)

**Pronóstico = Intersección + [Pendiente * Período de Tiempo]**

El primer paso para calcular el pronóstico es calcular la pendiente, ésta es la fórmula:

![](https://i.imgur.com/8PRnBf7.png?raw=true)

Lo segundo es calcular la intersección de la línea para lo que tenemos la siguiente fórmula:

![](https://i.imgur.com/tg4Ubx4.png?raw=true)

**Ejemplo:**
Tenemos los metros cuadrados de 4 casas y sus precios, ahora vamos a calcular la pendiente y la intersección para así predecir el precio de una casa 35 metros cuadrados

- **n** = Cantidad de casas
- **X** = Metros
- **t** = Precios

Metros Cuadrados (t) | Precio (t)
-- | --
5  | 375
15 | 487
20 | 450
25 | 500

**Resultado:**

![](https://imgur.com/QCEJasb.jpg?raw=true)

### **Regresión Logística**
La Regresión Logística es un algoritmo que nos sirve para predecir la probabilidad de que un evento pase o no. También es conocida como Regresión Binaria ya que solamente puede predecir entre 0 o 1.

Se usa mucho para la clasificacion, como seria el caso:

- Correos **No** deseados / Correos **Si** deseados
- Enfermo / **No** Enfermo

La **Regresión Logística** la utilizamos para clasificar y esta es la formula que lo explica:


![](https://i.imgur.com/hAyuSMX.png?raw=true)

Donde:
- **0** = Clase negativa
- **1** = Clase positiva

Todos los elementos que cumplen con los patrones que sigue el *algoritmo* que estamos programando pertenecen a la **clase positiva**.

### **Regresión Logística Multinomial**
La **Regresión Logística** es la probabilidad de que un evento ocurra o no, en este caso, con la **Regresión Logística Multinomial** ya tenemos diferentes tipos de eventos, por tanto, en su definición es la probabilidad de que ocurra cualquiera de estos eventos.

Este también considerado un *algoritmo* de clasificación.

### **Redes Neuronales**
El concepto de **Redes Neuronales** llega gracias a un científico que experimentaba con tejido animal. En uno de sus experimentos con un cerebro, se dio cuenta que si desconectaba la parte que estaba conectada al ojo, es decir, la parte que tenía la capacidad de recibir y procesar imágenes, y la conectaba al oído, esta parte desarrollaba la capacidad de escuchar. Con esto llegó a la conclusión de que nuestro cerebro tiene un *algoritmo de aprendizaje*. Todo depende de la entrada de información que se le provea.

Como resultado de este descubrimiento decidió replicarlo en un *algoritmo matemático*.

Las **Redes Neuronales** existen hace más de 60 años. En los años 80´s eran muy utilizadas, pero en los años 90´s decayeron considerablemente debido a que el costo computacional para entrenar una *red neuronal era* muy elevado.

Hoy en día ha tomado fuerza nuevamente debido a los grandes avances tecnológicos y al hecho de que existe un alto grado de precisión que tienen los resultados de las predicciones que se hacen con estas **Redes Neuronales**.

**Notas:**
- Las **Redes Neuronales** son el *algoritmo* más utilizado hoy en día.

- Las *neuronas*, como lo vimos en el tema de **Regresión Lineal**, disparan solamente valores de 0 y 1, es decir, ejecutan o no ejecutan

- En las **Redes Neuronales** artificiales todos los resultados caen entre 0 y 1.

- Una **Red Neuronal** se mide por capas. En el *esquema* que describe a las **Redes Neuronales**, tenemos por defecto la capa de entrada y de salida, por lo que depende del número de capas de en medio la medición de éstas.

- Las **compuertas lógicas** realizan operaciones basadas en las condiciones lógicas por las que están diseñadas. 

- Las **compuertas lógicas** pueden sumar, restar, multiplicar, negar o afirmar un valor.

- Las **operaciones sigmoidales** solo dan resultado o **0** o **1**

### **Algoritmo K-Means**
Algoritmo K-Means es un *algoritmo* sin supervisión. Sirve para agrupar los datos en función de ciertos patrones.

Dado un conjunto inicial de **k** centros (donde **k** es cualquier número o cualquier variable) el *algoritmo* continúa iterando entre dos pasos.

- **Paso de asignación:** Asigna cada dato al grupo con la media más cercana, es decir, la partición de las observaciones generadas por los centros.

- **Paso de actualización:** Calcula nuevos centros como el centro de las observaciones en el grupo o partición.

**Pasos:**

1) **k** centros iniciales, son generados aleatoriamente en un conjunto de datos

    ![](https://i.imgur.com/ba8m2PY.png?raw=true)

2) **k** grupos son generados, asociando el dato con la media mas cercana.

    ![](https://i.imgur.com/KZVkLBJ.png?raw=true)

3) El centro de cada uno de los **k** grupos se recalculan basado en la media de la particion antes asignada

    ![](https://i.imgur.com/wfXyuQQ.png?raw=true)

4) Paso 2 y 3 se repiten hasta que los centros dejen de recalcularce

    ![](https://i.imgur.com/zJJPpJ7.png?raw=true)

**Nota:** El *algoritmo* se considera que converge cuando los centros ya no cambian.

### **Deep Learning (Aprendizaje Profundo)**
Debido a su muy reciente auge, no se ha llegado a una definición definitiva de **Deep Learning** como concepto, sin embargo, aquí hay algunas de las definiciones que hay actualmente:

- Se utiliza una cascada de capas con unidades de procesamiento no lineal para extraer y transformar variables.

- Cada capa utiliza la salida de la capa anterior como entrada.

- Se puede utilizar con algoritmos de aprendizaje supervisado o de aprendizaje sin supervisión.

- Las características de más alto nivel se derivan de las características de nivel inferior, formando una representación jerárquica. Tambien se puede ver de esta forma.
Las características de más alto nivel se derivan de las de bajo nivel

**Ejemplo con 3 capas y un texto:** Ponemos un texto cortado en pedazos
- Capa 1: Descifra el idioma
- Capa 2: Organiza el texto ya qué sabe qué idioma es y cómo se compone
- Capa 3: Da el texto ya ordenado para la lectura

Estos son algunos de los algoritmos de **Deep Learning**:

- **Deep Neural Networks** (Redes Neuronales Profundas)
- **Convolutional Neural Networks** (Redes Neuronales Convolucionales)
- **Deep Belief Networks** (Redes de Creencias Profundas)

Estas son algunas áreas donde se utiliza **Deep Learning**:

- Computer Vision
- Reconocimiento del habla
- Reconocimiento de audio

### **Problemas Frecuentes en Machine Learning**
Estos son los problemas más comunes que pueden surgir en el proceso de entrenar *algoritmos*:

- **Underfitting (Subajustar):** Se presenta cuando un modelo no puede capturar la tendencia de los datos. Es generalmente el resultado de un modelo extremadamente simple.

- **Overfitting (Sobreajustar):** Se presenta cuando un algoritmo está perfectamente adaptado a los datos con los que lo entrenamos., pero si tratamos de predecir nuevos datos , lo más probable es que nos de error.


    ![](https://i.imgur.com/BSSOICK.png?raw=true)

Consejo para resolver el **Underfitting**:

- Se recomienda tratar de agregar más features al dataset, es decir, agregar más columnas con condiciones al modelo.

Consejos para resolver el **Overfitting**:

- Se recomienda disminuir la cantidad de features al dataset, es decir, quitar columnas con condiciones al modelo.

- También se recomienda agregar más ejemplos para el entrenamiento, es decir, agregar renglones con ejemplos de datos para el modelo.

### **Machine Learning in emoji**
![](https://static1.squarespace.com/static/57293859b09f959325ac2e33/t/574cc10db654f95fce4cda28/1464650023923/)