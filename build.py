#!/usr/bin/env python3
import os
import subprocess
import sys
import shutil

def build_executable():
    # Ensure we're in the right directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Clean previous builds
    if os.path.exists('dist'):
        shutil.rmtree('dist')
    if os.path.exists('build'):
        shutil.rmtree('build')
    
    # Build the executable using uv run
    subprocess.run([
        'uv', 'run', 'pyinstaller',
        '--onefile',  # Create a single executable
        '--name', 'browser-agent-arm64',
        '--clean',  # Clean PyInstaller cache
        '--add-data', 'browser_agent_cli:browser_agent_cli',  # Include package data
        'browser_agent_cli/cli.py',  # Main script
    ], check=True)
    
    # Make executable
    os.chmod('dist/browser-agent-arm64', 0o755)
    
    print("\nBuild completed! Executable is available at: dist/browser-agent-arm64")

if __name__ == '__main__':
    try:
        build_executable()
    except subprocess.CalledProcessError as e:
        print(f"Build failed: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1) 