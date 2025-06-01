#!/usr/bin/env python3
import os
import subprocess
import sys
import shutil
import platform

def get_target_arch():
    # Check if we're cross-compiling
    if os.environ.get('CC', '').startswith('aarch64-linux-gnu'):
        return 'arm64'
    return platform.machine()

def build_executable():
    # Ensure we're in the right directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Clean previous builds
    if os.path.exists('dist'):
        shutil.rmtree('dist')
    if os.path.exists('build'):
        shutil.rmtree('build')
    
    target_arch = get_target_arch()
    print(f"Building for architecture: {target_arch}")
    
    # Set PyInstaller options based on architecture
    pyinstaller_opts = [
        '--onefile',  # Create a single executable
        '--name', 'browser-agent',
        '--clean',  # Clean PyInstaller cache
        '--add-data', 'browser_agent_cli:browser_agent_cli',  # Include package data
    ]
    
    # Add architecture-specific options
    if target_arch == 'arm64':
        pyinstaller_opts.extend([
            '--target-architecture', 'aarch64',
        ])
    
    # Add the main script
    pyinstaller_opts.append('browser_agent_cli/cli.py')
    
    # Build the executable
    subprocess.run(['pyinstaller'] + pyinstaller_opts, check=True)
    
    print("\nBuild completed! Executable is available at: dist/browser-agent")
    print("\nTo install in a Docker container, copy the executable to /usr/local/bin/")
    print("Example:")
    print("  COPY dist/browser-agent /usr/local/bin/")
    print("  RUN chmod +x /usr/local/bin/browser-agent")

if __name__ == '__main__':
    try:
        build_executable()
    except subprocess.CalledProcessError as e:
        print(f"Build failed: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1) 