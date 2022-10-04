# P1 Pregunta de Diseño

### Diagrama de conexiones electricas:

<img src="https://github.com/acastro4/PalTech/blob/main/P1/1_pregunta_de_disen%CC%83o_v2.png" alt="drawing" width="800"/>


### Componentes
El esquema cuenta con:
Dos motores marca JMC, modelo IHSS60-36-30 (M1 y M2).\
Arduino uno\
Raspberry Pi

### Conexiones:
Se escoge conectar los motores de la forma *Differential Signal*:\
<img src="https://github.com/acastro4/PalTech/blob/main/P1/Diagrama_motor.png" alt="drawing" width="400"/>

En el diagrama solo se muestran las conexiones al motor para su control (No se incluye ni poder, ni alarma) desde un Arduino. Ademas, se incluyen la conexión serial entre arduino y el sistema embebido, el cual en este caso sera un Raspberry Pi 3.

No se incluyen octocupulas de protección ya que en el diagrama entregado por el fabricante se ve que ya cuenta con estas.

[Link Datasheet utilizado](https://www.jmc-motor.com/file/1806080877.pdf)
