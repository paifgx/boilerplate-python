# Python Project Boilerplate

A modern Python 3.12 project boilerplate using uv package manager and Dev Containers.

## Development Setup

### Prerequisites

- [Docker](https://www.docker.com/get-started)
- [Visual Studio Code](https://code.visualstudio.com/)
- [VS Code Remote - Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

### Getting Started

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/python-project.git
   cd python-project
   ```

2. Open the project in VS Code:
   ```bash
   code .
   ```

3. When prompted, click "Reopen in Container" or use the command palette (F1) and select "Dev Containers: Reopen in Container".

4. VS Code will build the container and set up the development environment. This may take a few minutes the first time.

5. Once inside the container, you're ready to develop!

## Project Structure

```
.
├── .devcontainer/       # Dev Container configuration
├── src/                 # Application source code
│   └── app/             # Main application package
│       ├── api/         # API endpoints and routers
│       ├── core/        # Core functionality and config
│       ├── models/      # Data models
│       ├── services/    # Business logic services
│       └── utils/       # Utility functions
├── tests/               # Unit tests
├── pyproject.toml       # Project metadata and dependencies
├── .env.example         # Example environment variables
└── README.md            # This file
```

## Development Workflow

- **Running the application**:
  ```bash
  python -m src.app.main
  ```

- **Running tests**:
  ```bash
  pytest
  ```

- **Installing dependencies**:
  ```bash
  uv pip install package_name
  ```

- **Updating dependencies**:
  ```bash
  uv pip compile
  uv pip sync
  ```

## Commit Guidelines

This project follows the [Conventional Commits](https://www.conventionalcommits.org/) specification:

```
<type>(<scope>): <subject>

<body>

<footer>
```

Examples:
- `feat(api): add user authentication endpoint`
- `fix(database): resolve connection timeout issue`
- `docs: update README with new configuration options`

## License

[MIT](LICENSE) 