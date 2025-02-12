# Dynamic Tool Generation Framework

## Overview

This project implements a flexible and extensible framework for creating AI agents with dynamic tool generation capabilities. The system is designed to allow AI agents to safely interact with various tools and resources while maintaining a clear separation of concerns and robust error handling.

## Project Structure

```
dynamic-tool-gen/
├── resources/
│   ├── data/                    # Data files (e.g., traffic_accidents.csv)
│   ├── object_oriented_agents/  # Core framework components
│   │   ├── core_classes/       # Base classes and interfaces
│   │   ├── services/          # Service implementations (OpenAI, etc.)
│   │   └── utils/            # Utility functions and logging
│   └── registry/             # Agent and tool implementations
│       ├── agents/          # Concrete agent implementations
│       └── tools/          # Concrete tool implementations
├── tests/                  # Test files
├── requirements.txt       # Project dependencies
└── .env                 # Environment variables (not in version control)
```

## Key Components

### Core Classes

-   **BaseAgent**: Abstract base class for all agents
-   **ToolInterface**: Interface for implementing new tools
-   **ToolManager**: Manages tool registration and execution
-   **AgentSignature**: Handles agent configuration and signatures
-   **ChatMessages**: Manages conversation history and message formatting

### Services

-   **OpenAILanguageModel**: Implementation of language model interface using OpenAI's API
-   **OpenAIClientFactory**: Factory class for creating OpenAI client instances
-   **LanguageModelInterface**: Abstract interface for language model implementations

### Agents

Currently implemented agents:

-   **FileAccessAgent**: Specialized agent for secure file operations
    -   Capabilities: Reading CSV files
    -   Security: Implements sandboxed file access through Docker containers

### Tools

-   **FileAccessTool**: Secure file access implementation
    -   Features:
        -   Safe file reading
        -   Docker container integration
        -   File transfer management
        -   Error handling and logging

## Setup and Installation

### Prerequisites

-   Python 3.10.12 or higher
-   Docker installed and running
-   OpenAI API key

### Environment Setup

1. Clone the repository:

```bash
git clone [repository-url]
cd dynamic-tool-gen
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file with your OpenAI API key:

```
OPENAI_API_KEY=your_api_key_here
```

### Docker Setup

The framework uses Docker for sandboxed file operations. Ensure:

1. Docker is installed and running
2. A sandbox container is available and running
3. Proper permissions are set up for container operations

## Usage

### Basic Usage Example

```python
from resources.registry.agents.file_access_agent import FileAccessAgent

# Create an instance of the FileAccessAgent
agent = FileAccessAgent()

# Use the agent to read a CSV file
response = agent.task("Can you show me the first few lines of traffic_accidents.csv?")
print(response)
```

### Running Tests

```bash
python test_agent.py
```

## Security Considerations

-   File operations are sandboxed in Docker containers
-   API keys are managed through environment variables
-   Input validation and error handling throughout the system
-   Logging system for monitoring and debugging

## Current Limitations and TODOs

1. File operations currently copy files to container on every run
2. Need to implement file caching mechanism
3. Consider adding file checksum verification
4. Potential for more efficient container resource usage

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

[Specify License]

## Contact

[Specify Contact Information]
