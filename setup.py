from setuptools import setup 

# reading long description from file 
with open('DESCRIPTION.txt') as file: 
	long_description = file.read() 


# specify requirements of your package here 
REQUIREMENTS = ['PyMuPDF'] 

# some more details 
CLASSIFIERS = [ 
	'Development Status :: 4 - Beta', 
	'Intended Audience :: Developers', 
	'Topic :: Internet', 
	'License :: OSI Approved :: MIT License', 
	'Programming Language :: Python', 
	'Programming Language :: Python :: 2', 
	'Programming Language :: Python :: 2.6', 
	'Programming Language :: Python :: 2.7', 
	'Programming Language :: Python :: 3', 
	'Programming Language :: Python :: 3.3', 
	'Programming Language :: Python :: 3.4', 
	'Programming Language :: Python :: 3.5', 
	] 

# calling the setup function 
setup(name='getwordcoords', 
	version='1.0.0', 
	description='A package which gets the word coordinates for a pdf page.', 
	long_description=long_description, 
	url='https://github.com/nikitha/getwordcoords', 
	author='Nikitha', 
	author_email='niki.nikitha6666@gmail.com', 
	license='MIT', 
	packages=['wordcoords'], 
	classifiers=CLASSIFIERS, 
	install_requires=REQUIREMENTS, 
	keywords='Word coordinates'
	) 
