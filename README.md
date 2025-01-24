# Pygame Template Project

This project is a minimal template to quickly start a project with Pygame.
It provides a basic structure to organize your code and simplify the initial setup process.

## Prerequisites

- **Python 3.13.1**: Make sure this version of Python is installed on your machine.
- **Tiled**: A map editor used to create game maps. You can download it from [mapeditor.org](https://mapeditor.org).

## Installation

1. **Clone this repository to your machine:**

   ```bash
   git clone https://github.com/ThomasDeOliv/PyGameTemplate
   cd PyGameTemplate
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   ```

   - On Linux:

   ```bash
   source venv/bin/activate
   ```

   - On Windows:

   ```powershell
   venv\Scripts\activate
   ```

3. **Install the dependencies:**

   ```bash
   pip install pygame pyopengl pyinstaller
   ```

   **Note:** A virtual environment isolates the project's dependencies, so any libraries installed will only be available within this environment and will not affect your global Python installation.

4. **Set up the `config.json` file:**

   - An example file, `config.example.json`, is provided at the root of the project.
   - Create a `config.json` file based on the `config.example.json` example file :

   ```bash
   cp config.example.json config.json
   ```

   - Edit `config.json` as needed.

## Exiting the Virtual Environment

When you are done working in the virtual environment, you can deactivate it by running:

```bash
deactivate
```

## Project Structure

```bash
pygame-template/
├── assets/             # Folder containing all game assets (images, sounds, etc.)
├── src/                # Source code for the project
├── .gitignore          # Files to ignore in repository
├── config.example.json # Example configuration file
├── config.json         # Configuration file (created by the user)
├── LICENSE             # License file
├── main.py             # Main entry point
└── README.md           # Project documentation
```

## Running the Project

To run the project from this source code, simply execute:

```bash
python main.py
```

## Build Solution

**Important:** The build will only be compatible with the platform (Windows, macOS, or Linux) on which it is created. For cross-platform builds, you must use appropriate tools for each platform.

- On macOS / Linux:

```bash
pyinstaller --onefile -w \
   --add-data "config.json:." \
   --add-data "assets/*:assets" \
   --name "PyGameTemplateExampleName" \
   --icon="assets/icon.ico" \
   main.py
```

- On Windows:

```powershell
pyinstaller --onefile -w `
   --add-data "config.json;." `
   --add-data "assets\*;assets" `
   --name "PyGameTemplateExampleName" `
   --icon="assets\icon.ico" `
   main.py
```

After running the build command, the generated executable file will be located in the `dist/` folder. You can distribute this file to run your project without requiring Python or its dependencies.

## About Assets

To use assets such as images, music, or videos in this project, they must be placed in the `assets` folder.

Use the `fetch` function in the `ResourceLocator` class, located in the `src/services/resource_locator` module, by providing the name of the targeted asset. **Avoid using relative paths to import assets.**

All assets used in the project should adhere to the following guidelines:

### Map:

- Editor: Use [Tiled](https://www.mapeditor.org/) to create your map using a single texture image file, and export it in JSON format.
- Placement: Save the exported JSON file in the `assets` folder, along with the texture file.
- Resolution Match: Ensure the map's resolution matches the resolution defined in your `config.json` file.
- Configuration:
  - Remember to add the name of the map's JSON file and textures image file to the `map` section in your `config.json` file.
  - Specify the names of the layers that should be collision-enabled in the collisionables field of the `map` section in your `config.json` file.

### Sprite:

Sprites used for gameplay must follow this format:

A 4 x 4 sprite sheet where:

- Row 0: Character sprite facing down
- Row 1: Character sprite facing right
- Row 2: Character sprite facing left
- Row 3: Character sprite facing up

### Executable icon:

When building executables, the required icon formats depend on the target platform:

- Windows: .ico files
- macOS: .icns files (recommended), .ico, or .png
- Linux: .png files or .ico

## License

This project is licensed. See the [LICENSE](LICENSE) file at the root of the project for details.
