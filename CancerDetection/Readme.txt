Readme

Instructions for getting and running the code
	1. Download the code from: https://github.com/angusman/canClassTrees click on the green "clone or download" button

	2. make sure you have python 3 installed. We recomend using the Anaconda distribution of python3 find it here: (https://www.continuum.io/downloads)

	3. make sure that you have R if you want to use the provided scripts for generating graphs of the results find it here (https://www.r-project.org)

	4. you might also want to get R-studio: (https://www.rstudio.com)

	5. The data has been prelabeled and proccessed, if you are interested in how that is done see the datalabeling script in the etc/ folder

	6. to run the sklearnmodels use sklearnmodels.py script, to use the from scratch tree models, run ourtreemodels.py


sklearnmodels.py
	The sklearnmodel script contains 6 different case studies, each one is sectioned off by a block of """ """ comments detailing what is being tested in the area. Feel free to try different experiments, just make sure that you follow the right structure, also keep in mind some classifiers are slower than others, so start with a small number of trees for ensemble methods before scaling up.

ourtreemodel.py
	Our tree model script implements a random forest at varying tree levels to compare accuracy as tree numbers increase. Warning! this approach was discontinued due to the necessary computation time. At last check it took over 4.5 hours to finish running the script.

objects/:
	In learning about how ensemble tree methods work we build and completed a decision tree classifier and a random forest classifer they can be found in the objects/ folder. The decision tree model is based off of a variant of the ID3 algorithm, and the random forest off of the 2001 paper by Leo Breiman.

Data:
	Data is stored in two primary locations:
		1. data/DNA:
			contains the imputed dna data provided as well as labled versions which have been transposed and labeled with a cancer column

		2. data/results
			- the results folder holds results from the scripts testing out the various case studies
			- the casestudiesNEW folder contains results from an additional running of sklearnmodels.py where the full acc vector was recorded for further analysis of accuracy.


Results:
	All of the results generated from the sklearnmodels are labeled with the convention casestudy*.csv, some notes related to the data stored in there:
		- casestudy1.csv and casestudy1a.csv both contain results from a decision tree classifer that indicates through its ntrees column that we are using more than a single tree for the data row, that is not the case only a single decision tree was involved.

	The files sklearndata.csv and homebrew.csv contain results from an early test of performance of sklearn's random forest and our own model. The data columns in this file slightly differ than the case study data since it was from ealier in the project.

	Visualizations of the results can be found in the data/results/*vis folders. These visuals were produced with the visuals.r and visualsnew.r R scripts in the CancerDectrion/ folder. While most likely the visualizations stored in these folders reflect the current data csvs, there is a chance that the data may have been updated or a test was altered, one can rerun R scripts to ensure that the visuals are up to date.

The Etc folder
	In cleaning up the repo I moved randomly accumulated files into etc/, any scripts in there might not run without changing the file path specifications, I recomend adding either "../" or "../../" before any file names inside of the scripts. Otherwise consider this folder the junk drawer.






