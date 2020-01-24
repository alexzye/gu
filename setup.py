import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
	name="gux",
	version="0.0.3",
	author="Alex Ye",
	author_email="alexzye1@gmail.com",
	description="git user switcher",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/azye/gux",
	scripts=['./scripts/gux'],
	packages=setuptools.find_packages(),
	python_requires='>=3.6',
)
