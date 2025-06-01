# Browser Agent CLI

A command-line tool for browser automation using browser-use.

## Quick Start

### Download Pre-built Executable

You can download pre-built executables from the [GitHub Releases](https://github.com/yourusername/browser-agent-cli/releases) page:

- For Linux: `browser-agent-linux`
- For macOS: `browser-agent-macos`

After downloading, make it executable and install:
```bash
# For Linux
chmod +x browser-agent-linux
sudo mv browser-agent-linux /usr/local/bin/browser-agent

# For macOS
chmod +x browser-agent-macos
sudo mv browser-agent-macos /usr/local/bin/browser-agent
```

### Running in Docker

To use the tool in a Docker container, simply copy the Linux executable:

```dockerfile
# In your Dockerfile
COPY browser-agent-linux /usr/local/bin/browser-agent
RUN chmod +x /usr/local/bin/browser-agent
```

## Development

### Installation from Source

```bash
# Clone the repository
git clone <your-repo-url>
cd browser-agent-cli

# Install in development mode
pip install -e .[dev]
```

### Building Executables

To build executables locally:

```bash
# Install development dependencies
pip install -e .[dev]

# Build executable
python build.py
```

The executable will be available in the `dist` directory.

## Usage

```bash
browser-agent --url "http://example.com" --task "Your task description"
```

### Available Options

- `--url`: URL to open in the browser (required)
- `--task`: Task description for the agent (required)
- `--logs-path`: Path to save conversation logs (default: ./logs/conversation)
- `--model`: OpenAI model to use (default: gpt-4)
- `--use-vision`: Enable vision capabilities (flag)

### Example

```bash
browser-agent \
  --url "http://localhost:3001" \
  --task "Review the website and share suggestions on what can be improved" \
  --logs-path "./custom/logs" \
  --use-vision
```

## Requirements

- For running the executable:
  - Linux or macOS
  - OpenAI API key (set in environment variable)

- For development:
  - Python 3.11 or higher
  - For Linux: build-essential package
  - For macOS: openssl (via brew) 