# Speech-to-Speech Integration Using OpenAI Realtime API in VBAIgame
## Venture Builder AI

An interactive 3D office environment built with Python, PyGame, and OpenGL, featuring AI-powered NPCs.

## Prerequisites

- Python 3.8+
- OpenGL support
- PyGame

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/GetieBalew24/VBAIgame.git
   cd VBAIgame
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and add your OpenAI API key:
   ```plaintext
   OPENAI_API_KEY=your_api_key_here
   ```

## Project Structure

```
VBAIGAME/
├── scripts/
│   ├── _pvcache__/
│   ├── app.py
│   ├── audio_processing.py
│   ├── constant.py
│   ├── dialogue_system.py
│   ├── game_3d.py
│   ├── menu_screen.py
│   ├── npc.py
│   ├── player.py
│   ├── realtime_speech_to_speech.py
│   ├── realtime_speech.py
│   ├── shapes.py
│   ├── speech_system.py
│   ├── text_to_speech.py
│   ├── texture_generator.py
│   └── world.py
├   ├── textures/
├── venv/
├── .env
├── .gitignore
├── Readme.md
└── requirements.txt
```
## Features

- 3D environment rendering using PyGame and OpenGL
- Procedurally generated textures
- AI-powered interactions using OpenAI API

## Usage

1. Generate textures (if not already present):
   ```bash
   python texture_generator.py
   ```

2. Run the main application:
   ```bash
   python app.py
   ```
3. To Start The VBAI game press enter and after that press CTRL + w
4. After step 3 forto start real time speech to speech communication press SHIFT + T and to stop press SHIFT + y

## Acknowledgments
- OpenAI for providing the AI capabilities
- PyGame community for the gaming framework
- OpenGL for 3D rendering support
```
