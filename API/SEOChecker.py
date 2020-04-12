# We import SEORules to call to the methods that perform the verifications for each SEO rules
# We import HTMLParserAPI to parse the HTML code of our page
# We import ConsoleStyles to give style to the messages in our report
from API import SEORules as Sr
from utils import ConsoleStyles as Cs, HTMLParserAPI as Hp
# We import webdriver to get the source code of the page from our webdriver
from selenium import webdriver


def preliminar_seo_rules_check(url: str = None, browser: webdriver = None, rules: list = None, languages: list = None)\
        -> (bool, str):
    """
    This method gets the string url and performs a request to get the HTML code or takes an instance of webdriver and
    gets the page source code from it, parses it and checks the rules set in the list rules with number (1 to 6) and
    return a boolean telling us if all those rules are met and a string report telling us how those verifications went
    :param url: A string to the URL we want to check, by default None
    :param browser: An instance of webdriver we can use alternatively to get the source code of our page, by default
    None
    :param rules: This is a list where we add the number of the rules we want to check, by default None in which case
    we will set this list to [1,2,3,4,5,6] so every rule is checked
    :param languages: In case we want to check rule for hreflang (rule 6) we need to provide a list of hreflang
    code our page should have
    :return: We return a boolean parameter that is true is all rules checked return True and a string with a report
    with the information about how the process went
    """
    # We create the variable that will contain the html code parsed to None at first
    html_parser = None
    # If rules is None, it is because we did not pass it as a parameter which means we want to check all rules
    if rules is None:
        # So we add values 1 to 6 to our list of rules
        rules = [i for i in range(1, 7)]
    # If url is not None, it is the parameter we use to get the HTML code of our page
    if url is not None:
        # We use our custom made method to get our HTML code parsed
        html_parser = Hp.get_from_url(url)
    # Otherwise, we should be using a webdriver instance
    else:
        # If our webdriver parameter is not None
        if browser is not None:
            # We use our custom made method to get the HTML code parsed
            html_parser = Hp.get_from_web_driver(browser)
    # We set the flag result to True
    result = True
    # We create the parameter report that we will return
    report = ""
    # We go through every rule we set to check
    for rule in rules:
        # We create an auxiliary parameter for the result in each step of checking SEO rules
        aux_result = None
        # If rule is 1, we have to check the tag title
        if rule == 1:
            # We add a header to our report stating we are checking tag title
            report += Cs.ConsoleStyles.BOLD + "Checking tag title:\n" + Cs.ConsoleStyles.END
            # We call to method rule_1_title we developed to check the SEO of tag title
            aux_result, aux_report = Sr.rule_1_title(html_parser)
            # We perform result & aux_result to add the result of this step to the overall result
            result &= aux_result
            # We add the report for this step to the overall report
            report += aux_report
        # If rule is 2, we have to check the tag meta that has description
        if rule == 2:
            # We add a header for this rule to our report
            report += Cs.ConsoleStyles.BOLD + "Checking metatag description:\n" + Cs.ConsoleStyles.END
            # We use the custom made method rule_2_meta_tag_description to check our tag meta with description
            aux_result, aux_report = Sr.rule_2_meta_tag_description(html_parser)
            # We add the result of this rule to the overall result of this process
            result &= aux_result
            # We add the report for this step to the overall report
            report += aux_report
        # If rule is 3, we check the structure of heading in our page
        if rule == 3:
            # We add a header for this to our report
            report += Cs.ConsoleStyles.BOLD + "Checking headings structure:\n" + Cs.ConsoleStyles.END
            # We call our custom made method rule_3_h1 to check if we have just one heading h1 with text
            aux_result, aux_report = Sr.rule_3_h1(html_parser)
            # We add the result of this method to our overall result
            result &= aux_result
            # We add the string report for this rule to our overall report
            report += aux_report
            # Now, we check the structure of headings in our page
            aux_result, aux_report = Sr.rule_3_headings_structure(html_parser)
            # We add the result of this method to our overall result
            result &= aux_result
            # We add the report given by this method to our overall report
            report += aux_report
        # If rule is 4, it means we have to check if every tag img has an attribute alt with text
        if rule == 4:
            # We add a header stating we are checking this rule
            report += Cs.ConsoleStyles.UNDERLINE + "Checking attribute alt in images:\n" + Cs.ConsoleStyles.END
            # We call to our custom made method rule_4_img_alt to check this rule
            aux_result, aux_report = Sr.rule_4_img_alt(html_parser)
            # We add the result of this method to our overall result
            result &= aux_result
            # We add the report that was returned by this method to our overall report
            report += aux_report
        # If rule is 5, we check which links in our page are no follow links
        if rule == 5:
            # We add a header stating this information to our report
            report += Cs.ConsoleStyles.BOLD + "Checking no follow links:\n" + Cs.ConsoleStyles.END
            # We add the report result of this method to our overall report
            report += Sr.rule_5_no_follow_links(html_parser) + "\n\n"
        # If rule is 6, we have to check the tags link within tag head and check if we have one canonical link and
        # also one for each language set in our list languages, so we should use it in this case.
        if rule == 6:
            # We add a header to our overall report
            report += Cs.ConsoleStyles.BOLD + "Checking href and hreflang tags:\n" + Cs.ConsoleStyles.END
            # If we provided a list of hreflang codes in list languages
            if languages is not None:
                # We call to the custom made method rule_6_hreflang that checks the rules described above
                aux_result, aux_report = Sr.rule_6_hreflang(html_parser, languages)
                # We add the current result of this rule to the overall result of our process
                result &= aux_result
                # We add the report returned by the method to the overall report
                report += aux_report
        # If aux_result is not None and it is True
        if aux_result is not None and aux_result:
            # We add to our report the text OK in green to state the rule in this iteration went well
            report += Cs.ConsoleStyles.GREEN + "OK\n\n" + Cs.ConsoleStyles.END
        # If aux_result is not None and is False
        elif aux_result is not None and not aux_result:
            # We add to our report the text KO in red to state that the rule in this iteration did not go well
            report += Cs.ConsoleStyles.RED + "KO\n\n" + Cs.ConsoleStyles.END
    # We return result and report
    return result, report
