# P1 Pregunta de Diseño

### Diagrama de conexiones electricas:
Foto diagrama

### Componentes
El esquema cuenta con:
Dos motores marca JMC, modelo IHSS60-36-30 (M1 y M2).\
Arduino uno\
Raspberry Pi\

### Conexiones:
Se escoge conectar los motores de la forma *Differential Signal*:
Foto diferencial Signal motores

En el diagrama solo se muestran las conexiones al motor para su control desde el Arduino. Ademas, se incluyen la conexión serial entre arduino y el sistema embebido, el cual en este caso sera un Raspberry Pi 3. \

No se incluyen octocupulas de protección ya que en el diagrama entregado por el fabricante se ve que ya cuenta con estas.\

[Link Datasheet utilizado](https://www.jmc-motor.com/product/954.html)
