#!/usr/bin/python
# This module was made for we can execute this project from a script
# We have to execute it like this: <folder>: python SEOCheckCmdLine.py <url> "<language 1>,<language 2>,..."
# We import sys so we can access the argument we pass as parameters to this script
import sys
# We import this custom made method which is the one that will perform our SEO analysis
from API.SEOChecker import preliminar_seo_rules_check


def parse_languages(languages: str) -> list:
    """
    This method turn the argument given for the languages to a proper list of hreflang codes/languages
    :param languages: Argument for languages "<language 1>,<language 2>,..."
    :return: A list of str that contains the different hreflang codes or languages
    """
    # We remove the " symbol from our str
    languages = languages.replace("\"", "")
    # We split the str by , to get a list of languages
    return languages.split(",")


def main():
    """
    This method is the main method of this project to be executed in cmd line
    :return: None
    """
    # We get the first argument given to this script, which should be a URL
    url = sys.argv[1]
    # We create this parameter list_languages to pass it to the method that will perform the analysis
    list_languages = None
    # If the number of arguments is 3, it is because we provided also a list of languages in which our page should be
    if len(sys.argv) == 3:
        # We get the second argument given to this script, which should be a list of languages in this format
        # "<language 1>,<language 2>, ..."
        languages = sys.argv[2]
        # We call to this method described previously to get the list of languages ready to be used in our project
        list_languages = parse_languages(languages)
    # We call preliminar_seo_rules_check to perform the SEO analysis and store its return
    result, report = preliminar_seo_rules_check(url=url, languages=list_languages)
    # We print if the process was OK or not
    print("Was it all correct? {0}".format(result))
    # We print the report
    print(report)


if __name__ == "__main__":
    main()
