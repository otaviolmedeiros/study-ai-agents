from setuptools import setup, find_packages

setup(
    name='study-ai-agents',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'python-dotenv==1.0.0',
        'pydantic==2.4.2',
        'openai==1.3.0',
        'langchain==0.0.335',
        'colorama==0.4.6',
        'tqdm==4.66.1',
        'setuptools==65.5.0',
        'wheel==0.36.2'
    ],
    entry_points={
        'console_scripts': [
            'study-ai-agent=main:main',
        ],
    },
    python_requires='>=3.6',
    author='Your Name',
    author_email='your.email@example.com',
    description='A Python framework for developing and studying AI agents',
    long_description='''A modular framework for creating, testing and deploying AI agents with various capabilities.
Features include a skill-based architecture, environment configuration, and testing utilities.
Provides infrastructure for agent communication, learning mechanisms, and cognitive processing.''',
    url='https://github.com/yourusername/study-ai-agents',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Artificial Intelligence'
    ],
)