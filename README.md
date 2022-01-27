# comp410_spring_2022
Using python to identify personally identifiable information
## Team Discussions
For students, here is a link to the [Comp410Spring2022 Discussions](https://github.com/orgs/NCATComp410/teams/comp410spring2022class/discussions) - note this link will only work if you have been added to the GitHub team.
## Installation
* Anaconda environment is highly recommended.  Download the version appropriate for your system [here](https://www.anaconda.com/products/individual)
* This project is currently based on Python 3.9 - here is a [link](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html) to the Anaconda getting started guide. Note that the Anaconda Navigator [GUI](https://docs.anaconda.com/anaconda/navigator/getting-started) can be used instead of CLI.
  * Install git (if you don't have it installed already)
    * https://git-scm.com/downloads
  * Open a conda shell
    * conda update conda 
    * conda create --name py39 python=3.9
  * Activate your new venv
    * conda activate py39

  * Fork this project and clone your fork 
    * cd to directory you want to put this in 
    * git clone (Your fork URL - Green clone button)
    * cd comp410_spring_2022
    * To keep your fork in sync with upstream we'll follow [these](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/working-with-forks) instructions.
  * python pii_data.py 
    * Runs a quick demo
  * Testing
    * conda install pytest-cov
    * pytest
## Pull Request Requirements
* All pull requests much attach output from pytest showing all test cases passed along with the coverage report or pull request will be rejected.

