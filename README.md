# on_page_basic_SEO_checker
 This project provides methods and utils to make basic checks in the SEO of an instance of a page using the URL of this page or a webdriver instance that is browsing that page at the moment

- API: This folder contains the following modules:
  - SEOChecker.py: Contains the method <b>preliminar_seo_rules_check</b>, which is the method you should execute to perform the SEO analysis.
  - SEORules.py: Contains the method that perform the different tasks needed to perform our SEO analysis
 
 - reports: This folder will store the different reports that preliminar_seo_rules_check will generate
 
 - utils: This folder contains modules that are used in this project to perform and simplify tasks:
   - ConsoleStyles.py: This class provides different attributes to apply styles to the strings that our report generates that will be displayed in console
   - HTMLParserAPI.py: This module performs the parsing of our HTML page, we can use a URL or a webdriver instance that is browsing that URL
   
- webdrivers: In this folder you can store the webdrivers that you need

- SEOCheckCmdLine.py: This script can be executed to perform the SEO analysis from the comand line

- Test.py: This script provides a test and example of how project works
