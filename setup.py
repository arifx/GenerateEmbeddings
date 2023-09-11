from setuptools import setup, find_packages




setup(
    name="EmbeddingGenerator",
    version="2.2.2",
    author="Arif Yilmaz",
    author_email="arif.yilmaz@wolterskluwer.com",
    description="Dutch text embeddings",
    long_description=readme,
    long_description_content_type="text/markdown",
    license="Apache License 2.0",
    url="https://github.com/arifx/GenerateEmbeddings",
    download_url="https://github.com/arifx/GenerateEmbeddings",
    packages=find_packages(),
    python_requires=">=3.6.0",
    install_requires=[
        'transformers>=4.6.0,<5.0.0',
        'tqdm',
        'torch>=1.6.0',
        'torchvision',
        'numpy',
        'scikit-learn',
        'scipy',
        'nltk',
        'sentencepiece',
        'huggingface-hub>=0.4.0'
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.6",
        "Topic :: Scientific/Engineering :: Artificial Intelligence"
    ],
    keywords="Dutch, NLP, Embedding, deep learning"
)
