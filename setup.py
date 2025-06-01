from setuptools import setup, find_packages

setup(
    name="browser-agent-cli",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "browser-use",
        "langchain-openai",
        "python-dotenv",
        "playwright",
    ],
    extras_require={
        'dev': [
            'pyinstaller',  # Only needed for building the executable
        ],
    },
    entry_points={
        'console_scripts': [
            'browser-agent=browser_agent_cli.cli:main',
        ],
    },
    python_requires=">=3.11",
    author="Neil Chen",
    author_email="neil@vela.studio",
    description="A CLI tool for browser automation using browser-use",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    # Build system requirements
    setup_requires=["setuptools>=68.0.0", "wheel>=0.41.0"],
    # Include package data
    include_package_data=True,
    package_data={
        "browser_agent_cli": ["py.typed"],
    },
) 