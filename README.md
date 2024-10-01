
# Fluid Simulator in VPython

This is a particle-based fluid simulator that uses VPython for visual representation. It implements numerical methods such as Euler integration and collision models to simulate fluids in a 3D environment. Additionally, the simulator exports data in binary format, which can be rendered in specialized software like RealFlow to generate simulation videos.

## Main Features

- Particle simulation using the Smoothed Particle Hydrodynamics (SPH) model.
- Handling of collisions with the boundaries of the container.
- Export of data in binary format compatible with RealFlow for advanced visualization.
- Real-time visual representation of the simulation using VPython.
- Axis visualization options for easy spatial reference.

## Requirements

This project uses **Python 2.7**, so it's important to ensure you have this version installed, along with the following dependencies:

- VPython (`pip install vpython`)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your_username/fluid-simulator.git
   cd fluid-simulator
   ```

2. Install the necessary dependencies:
   ```bash
   pip install vpython
   ```

## Usage

To run the simulation, simply run the `main.py` file:
```bash
python main.py
```

### Simulation Parameters

- **Viscosity**: Controls the internal friction of the fluid. You can modify this value in the `main.py` file.
- **Time step**: The step size for each iteration of the simulation. Defined as `pasoTiempo`.
- **Number of particles**: Configurable in the `main.py` file under the variables `numParticulasX`, `numParticulasY`, `numParticulasZ`.

### Exporting to Binary Format

The simulation data can be exported in binary format, compatible with RealFlow software for more detailed visualization and video creation. Binary files are generated in the `Frame_binarios/` folder and can be processed in RealFlow or other software that supports this format.

## Project Structure

The project is organized into the following modules:

- **main.py**: Main script that initializes the simulation and controls the simulation loop.
- **SistemaParticulas.py**: Defines the `SistemaParticulas` class, which manages the set of particles.
- **ClaseParticula.py**: Defines the `Particula` class, representing each individual particle in the simulation.
- **Fuente.py**: Contains the method to generate a flow of particles in the form of a column.
- **Dinamica.py** and **DinamicaEstable.py**: Calculate the internal forces between particles using the SPH method.
- **GestorColisiones.py**: Implements the detection and response of collisions with the boundaries of the container.
- **OperacionesVectoriales.py**: Provides basic vector operations such as addition, subtraction, and multiplication.
- **MetodosIntegracion.py**: Implements the Euler method for updating the kinematics of the particles.
- **Vecinas.py** and **vecinasHash.py**: Calculate the neighboring particles either through brute force or using a hash table for optimization.
- **Canvas.py**: Allows for axis visualization in the simulation environment.
- **Binario.py**: Exports simulation data to a binary file to be rendered in RealFlow.

## Simulation Example

In the simulation, a column of fluid is generated, which interacts through pressure and viscosity forces. The particles collide with the container boundaries and each other. The results can be exported as binary files for later rendering.

### Test Video

I have made a test of the simulation by rendering the binary files in RealFlow. You can watch the resulting video [here](link_to_your_video). The video shows the behavior of the fluid in an enclosed environment. You can create similar videos by following these steps:

1. Run the simulation and let the binary files be generated.
2. Import the binary files into RealFlow or another fluid simulation software.
3. Render the video using the software tools.

## Contribution

If you want to contribute to this project, feel free to open an issue or submit a pull request. Suggestions and improvements are welcome.

