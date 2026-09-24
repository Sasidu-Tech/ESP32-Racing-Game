# 🏎️ ESP32 Racing Game Controller

![ESP32 Wi-Fi Scanner](images/esp32-wifi-scanner.png)

A simple racing game controlled using an **ESP32 and physical push buttons**.

The ESP32 works as a hardware game controller and communicates with a Python/Pygame racing game through **USB Serial Communication**.

This project combines **Embedded Systems + ESP32 + Python + Pygame** into one simple interactive project.

---

## 🎮 Project Demo

### 🎯 Controls

| Button | Function |
|---|---|
| 🔵 LEFT | Move car left |
| 🟢 RIGHT | Move car right |
| 🔴 START | Start / Restart game |

Keyboard controls are also available for testing:

| Keyboard | Function |
|---|---|
| ⬅️ Left Arrow | Move left |
| ➡️ Right Arrow | Move right |
| `R` | Restart |

---

## 🧠 How It Works


┌──────────────────────┐
│   Physical Buttons   │
│ LEFT / RIGHT / START │
└──────────┬───────────┘
           │
           ▼
      ┌──────────┐
      │   ESP32  │
      └────┬─────┘
           │
           │ USB Serial
           ▼
    ┌───────────────┐
    │ Python +      │
    │ Pygame        │
    └───────┬───────┘
            │
            ▼
       🏎️ Racing Game

When a button is pressed, the ESP32 sends a command through Serial:
LEFT
RIGHT
START
Python receives these commands and controls the racing game.

🔧 Hardware Requirements

ESP32 Development Board
3 × Push Buttons
Breadboard
Jumper Wires
USB Cable
Computer / Laptop

🔌 Wiring

Pin Mapping
Function
ESP32 GPIO
🔵 LEFT Button
GPIO 25
🟢 RIGHT Button
GPIO 26
🔴 START Button
GPIO 27
GND
GND

Button Connection
Each push button is connected between the ESP32 GPIO pin and GND.
LEFT Button
GPIO 25 ───── Button ───── GND

RIGHT Button
GPIO 26 ───── Button ───── GND

START Button
GPIO 27 ───── Button ───── GND
The project uses INPUT_PULLUP, so external pull-up resistors are not required.

💻 Software Requirements

Arduino
Arduino IDE
ESP32 Board Package
Python
Python 3.x
Pygame
PySerial

Install the required Python libraries:

pip install pygame pyserial
📡 ESP32 Controller Code
#define LEFT_BUTTON 25
#define RIGHT_BUTTON 26
#define START_BUTTON 27

void setup() {
  Serial.begin(115200);

  pinMode(LEFT_BUTTON, INPUT_PULLUP);
  pinMode(RIGHT_BUTTON, INPUT_PULLUP);
  pinMode(START_BUTTON, INPUT_PULLUP);
}

void loop() {

  if (digitalRead(LEFT_BUTTON) == LOW) {
    Serial.println("LEFT");
    delay(50);
  }

  if (digitalRead(RIGHT_BUTTON) == LOW) {
    Serial.println("RIGHT");
    delay(50);
  }

  if (digitalRead(START_BUTTON) == LOW) {
    Serial.println("START");
    delay(200);
  }
}

🐍 Python Racing Game

The racing game is developed using Pygame.
The Python program:
Connects to the ESP32 through Serial
Receives button commands
Moves the player car
Generates enemy cars
Detects collisions
Tracks score
Increases enemy speed
Restarts the game

🔗 Serial Communication
The ESP32 communicates with Python using:
Baud Rate: 115200
Example commands:
LEFT
RIGHT
START
Python connection:
ESP32_PORT = "COM8"
BAUD_RATE = 115200

⚠️ Change COM8 to the COM port assigned to your ESP32.
🎮 Game Features
🏎️ Player racing car
🚙 Enemy cars
🛣️ Road and lane system
🎮 Physical ESP32 controller
⬅️ Left / Right movement
🔄 Start / Restart button
💥 Collision detection
🏆 Score system
⚡ Increasing enemy speed
⌨️ Keyboard backup controls
🔌 USB Serial communication
💥 Collision Detection

The game uses Pygame rectangle collision detection.
When the player car touches an enemy car:
💥 COLLISION
      ↓
  GAME OVER
      ↓
Press START
      ↓
  Restart Game
  
🏆 Score System
Every time an enemy car successfully passes the player:
Score +1
Example:
Score: 5
The enemy speed gradually increases as the game continues.

📁 Project Structure
ESP32-Racing-Game/
│
├── game.py
│
├── esp32_controller/
│   └── esp32_controller.ino
│
├── test/
│   └── serial_test.py
│
├── images/
│   └── wiring-diagram.png
│
├── demo/
│   └── racing-game.mp4
│
└── README.md

🛠️ Troubleshooting

❌ Python cannot open COM port
Check the ESP32 COM port in:
Windows Device Manager
→ Ports (COM & LPT)

Then update:
ESP32_PORT = "COM8"
❌ UnicodeDecodeError
Serial data can sometimes contain invalid bytes.
Use:

command = esp32.readline().decode(
    "utf-8",
    errors="ignore"
).strip()
❌ Buttons work in Arduino but not Python
Make sure:

Arduino Serial Monitor is closed.
The correct COM port is selected.
Baud rate is 115200.
ESP32 is connected through USB.
pyserial is installed.
pip install pyserial

📚 Learning Outcomes
Through this project, I learned:
ESP32 GPIO programming
Push button interfacing
INPUT_PULLUP
Serial communication
Python Serial communication
Pygame game development
Player movement
Collision detection
Score systems
Game restart logic
Hardware and software integration
Basic debugging of COM-port and serial communication issues

🚀 Future Improvements

Possible future upgrades:
🎮 Joystick controller
🔊 Game sound effects
🎵 Background music
🏆 High-score saving
❤️ Multiple lives
⚡ Speed boost
🚙 More enemy vehicles
🛣️ Multiple levels
📟 OLED/LCD game information
📡 Wireless ESP32 controller
🎨 Improved car and road graphics
🧰 Technologies Used
ESP32
Arduino IDE
C/C++
Python
Pygame
PySerial
USB Serial Communication
GPIO

👨‍💻 Author
Sasidu-Tech
BICT Student | Networking & Cyber Security Enthusiast

Interested in:
🌐 Networking
🔐 Cyber Security
🤖 IoT & Embedded Systems
⚡ ESP32
🐍 Python
🔧 Arduino

📜 License

This project is licensed under the MIT License.
Copyright © 2026 Sasidu-Tech
⭐ If you found this project useful, consider giving the repository a Star!

