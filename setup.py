import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyk3x",
    author="Roming22",
    author_email="roming22@gmail.com",
    description="API to simplify k3d deployments",
    keywords="kuberbetes, k3s, k3d, k3x, cluster",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Roming22/pyk3x",
    project_urls={
        "Documentation": "https://github.com/Roming22/pyk3x",
        "Bug Reports": "https://github.com/Roming22/pyk3x/issues",
        "Source Code": "https://github.com/Roming22/pyk3x",
        # 'Funding': '',
        # 'Say Thanks!': '',
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    classifiers=[
        # see https://pypi.org/classifiers/
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    # install_requires=['Pillow'],
    extras_require={
        "dev": ["check-manifest"],
        # 'test': ['coverage'],
    },
    # entry_points={
    #     'console_scripts': [  # This can provide executable scripts
    #         'run=k3x:main',
    # You can execute `run` in bash to run `main()` in src/k3x/__init__.py
    #     ],
    # },
)
