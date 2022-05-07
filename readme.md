<div id="top"></div>
<!--
*** Thanks for checking out my project
*** Dr Donald O. Besong
-->


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="http://github.com/Donald-Besong">
    <img src="src/data/images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Donald's Calculations</h3>

  <p align="center">
    project_description
    <br />
    <a href="http://github.com/Donald-Besong/Banking_Test"><strong>Explore the docs »</strong></a>
  </p>
</div>



<!-- GETTING STARTED -->
## Getting Started

Instructions


1. Clone the repository
2. Make sure that in your command line, you are in the root folder, which contains
   requirements.txt, and all the code.
3. virtualenv -p python3 bank_env3

4. Activate the virtual environment  . bank_env3/bin/activate

5. Install python packages in requirements.txt using pip in your python3
environment   
  

5. Run the following command, changing the argument values:
<p align="center"> python3 src/main_program.py --test_number=2 </p>
However, you can run a more gereral case: That is, the program is flexible so for each question you can specify the values you want to solve for,
so that the default filters you asked for in the test can be modified by your commandline in-put. Here is how to 
run the general case:
<p align="center"> python3 src/main_program.py --data_source=fullpath_of_data --cutoff_date=01/01/1995 --risk_rating=Low --test_number=2 --dob_filter=01/09/2003 --fee_str=transaction</p>

Here are the meanings of the arguments:
<p align="center"> data_source: This is the fullpath of the xlsx file, but it must have the same sheet names and column names as in the test. If empty, the program will use the default which is the file you provided for the test. The xlsx file is located in src/data</p>
<p align="center"> cutoff_date: This is the date filter for test1. If empty, it uses the default you gave in the test </p>
<p align="center">risk_rating: This is the risk filter in test1. If empty, it uses the default filter you gave for test1 </p>
<p align="center">test_number: This is for an integer 1, or 2) used to select which test to run and print its results. Default is 1 for test1 </p>
<p align="center"> dob_filter: This is the datae of birth filter in test2. Should be formatted as in the above example. If empty, it uses the default DOB you provided in test2 </p>
<p align="center"> fee_str: This is a string which will be searched in the feeTypeMapping. The default is Overdraft which is what you asked for in the test. Should be left empty for this default, but if you are cusrious you can enter Transaction, or even Replacement Debit</p>
Here are the arguments to run the code:


 
