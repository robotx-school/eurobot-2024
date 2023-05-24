<p align="center">
  <img src="https://github.com/robotx-school/eurobot-2024/assets/55328925/cf0189a9-7b9f-4360-82ae-581df471cc9a" />
</p>

# Universal robotics board
Connectable components: 
* Stepper motors - 4
* Servo motors with feedback - 8
* DC motors with L298N driver - 4
* Motor encoders - 2
* Extra Arduino with UART connection for NRF24L01 radio module
* Laser distancemeters
* LCD 1602 display by I2C protocol
* address LEDs strips
* Raspberry Pi or others with SPI support for high-level protocol
* And others

## Usage example
![image2](https://github.com/robotx-school/eurobot-2024/assets/55328925/a6356045-898c-4e7c-84c2-4df54881928e)

## Arduino Mega 2560 pinout
![image3](https://github.com/robotx-school/eurobot-2024/assets/55328925/4bf57153-bd31-410b-bea8-f33cd5dd83fb)

## Arduino Mega PRO pinout
![image4](https://github.com/robotx-school/eurobot-2024/assets/55328925/259c161b-57c0-454e-ab90-29ce38614894)

## Standart Arduino Mega ports defines table
Ind| Port      | Description                   |
|--|-----------|-------------------------------|
|0 | RX0       | Reserved for sketch uploading |
|1 | TX0       | Reserved for sketch uploading |
|2 | Interrupt | Encoders connection           |
|3 | Interrupt | Encoders connection           |
|4 | CE        | For builtin NRF24             |
|5 |           |                               |
|6 | PWM       | DC motor 0                    |
|7 | PWM       | DC motor 0                    |
|8 | PWM       | DC motor 1                    |
|9 | PWM       | DC motor 1                    |
|10| PWM       | DC motor 2                    |
|11| PWM       | DC motor 2                    |
|12| PWM       | DC motor 3                    |
|13| PWM       | DC motor 3                    |
|14| TX3       | Extra Arduino                 |
|15| RX3       | Extra Arduino                 |
|16| TX2       | Back distance meter           |
|17| RX2       | Back distance meter           |
|18| TX1       | Front distance meter          |
|19| RX1       | Front distance meter          |
|20| SDA       | Display output                |
|21| SCL       | Display output                |
|22|           | address LEDs. 2 on the board, connector for external connection                |
|23|           | address LEDs. Robot illumination                |
|24|           | Side selection                |
|25|           | Start Pin                     |
|30|           | Servo 0                       |
|32|           | Servo 1                       |
|34|           | Servo 2                       |
|35|           | Enable stepper 2 and 3 step   |
|36|           | Servo 3                       |
|37|           | Stepper 2 Step                |
|38|           | Servo 4                       |
|39|           | Stepper 2 - DIR               |
|40|           | Servo 5                       |
|41|           | Stepper 3 - STEP              |
|42|           | Servo 6                       |
|43|           | Stepper 3 - DIR               |
|44|           | Servo 7                       |
|45|           | Enable steppers 0 and 1 step  |
|46|           | Stepper 0 - STEP              |
|47|           | Stepper 0 - DIR               |
|48|           | Stepper 1 - STEP              |
|49|           | Stepper 1 - DIR               |
|50| MISO      | RPi Connection                |
|51| MOSI      | RPi Connection                |
|52| SCK       | RPi Connection                |
|53| SS        | RPi Connection                |


## Arduino Mega ports usage
### Special ports 
* UART
  * 0, 1 - Reserved by programmer
  * 18(TX1), 19(RX1) – Serial1
  * 16(TX2), 17(RX2) – Serial2
  * 14(TX3), 15(RX3) – Serial3
* I2C
  * 20 – SDA, 21 – SCL
* SPI
  * 50 - MISO
  * 51  - MOSI
  * 52 – SCK
  * 53 – SS
* Interrupts
  * 2, 3, (18, 19, 20, 21 – can be used without UART)

### Analog input

* A0 – A15; for reading analog signal, processed with ADC
### PWM

Ports with hardware PWM can be used to connect DC motors
* 2 - 13 
