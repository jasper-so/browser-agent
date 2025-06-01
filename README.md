# Browser Agent CLI

A command-line tool for browser automation using browser-use.

## Quick Start

### Download Pre-built Executable

You can download pre-built executables from the [GitHub Releases](https://github.com/neilxchen/browser-agent/releases) page:

- For Linux: `browser-agent-linux`
- For macOS: `browser-agent-macos`

### System Dependencies

#### Ubuntu/Debian
```bash
# Install required system dependencies
sudo apt-get update
sudo apt-get install -y \
    libnss3 \
    libnspr4 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdrm2 \
    libxkbcommon0 \
    libxcomposite1 \
    libxdamage1 \
    libxfixes3 \
    libxrandr2 \
    libgbm1 \
    libasound2 \
    libpango-1.0-0 \
    libcairo2 \
    libatspi2.0-0

# Install Chromium
sudo apt-get install -y chromium-browser

# Install and make executable
chmod +x browser-agent-linux
sudo mv browser-agent-linux /usr/local/bin/browser-agent
```

#### macOS
```bash
# Install required system dependencies
brew install openssl

# Install Chromium
brew install --cask chromium

# Install and make executable
chmod +x browser-agent-macos
sudo mv browser-agent-macos /usr/local/bin/browser-agent
```

### Running in Docker

To use the tool in a Docker container, you'll need to install the same system dependencies and Chromium:

```dockerfile
# In your Dockerfile
RUN apt-get update && apt-get install -y \
    libnss3 \
    libnspr4 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdrm2 \
    libxkbcommon0 \
    libxcomposite1 \
    libxdamage1 \
    libxfixes3 \
    libxrandr2 \
    libgbm1 \
    libasound2 \
    libpango-1.0-0 \
    libcairo2 \
    libatspi2.0-0 \
    chromium-browser

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

# Install Playwright browsers
playwright install chromium
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
- `--headless`: Run the browser in headless mode (flag)

### Example

```bash
browser-agent \
  --url "http://localhost:3001" \
  --task "Review the website and share suggestions on what can be improved" \
  --logs-path "./custom/logs" \
  --use-vision \
  --headless
```

## Requirements

- For running the executable:
  - Linux or macOS
  - System dependencies (see System Dependencies section above)
  - Chromium browser installed
  - OpenAI API key (set in environment variable)

- For development:
  - Python 3.11 or higher
  - For Linux: build-essential package
  - For macOS: openssl (via brew)
  - Playwright browsers installed (`playwright install chromium`) 