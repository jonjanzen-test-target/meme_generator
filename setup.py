from setuptools import setup, find_packages

setup(
    name="meme_generator",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "Pillow",
        "torch",
        "transformers",
        "scikit-learn",
        "nltk",
        "requests"
    ]
)
