# We import BeautifulSoup to parse our HTML code
from bs4 import BeautifulSoup
# We import a custom made class called ConsoleStyles to give styles to our console messages
from utils import ConsoleStyles as Cs


def rule_1_title(html_parser: BeautifulSoup) -> (bool, str):
    """
    This method checks if there is just one tag title contained within the tag head and the tag has text and its text
    is less than or equal to 70 characters. Which is a rule for SEO
    :param html_parser: BeautifulSoup object that contains the HTML of our page parsed
    :return: A couple of variables a boolean that return True if the conditions described above are correct or False
    otherwise and string parameter that contains a report which gives us information about the analysis of the tag title
    """
    # We get the tag head
    heads = html_parser.find_all("head")
    # We get the tags title that are contained within the tag head
    titles = heads[0].find_all("title")
    # For starters we set the flag result to True (it will be set to False if we find that one of those conditions
    # is not true
    result = True
    # We create the parameter report to return the report
    report = ""
    # We check if we have just one tag title
    if len(titles) == 1:
        # We include this information in the report
        report += "Only one tag title within the tag head\n{0}\n".format(titles)
        # We check if the text in title is less than or equal to 70 characters
        if len(titles[0].get_text()) <= 70:
            # We include this information in the report
            report += "Title is shorter than or equal to 70 characters\n"
        # We check if the length in the text in tag title is 0, which means there is no text
        elif len(titles[0].get_text()) == 0:
            # We add this information to the report
            report += "Title is empty\n"
            # This is not correct in terms of SEO, so we set our flag result to False
            result &= False
        else:
            # Otherwise, the title is longer than 70 characters
            # We add this information to the report
            report += "Title is longer than 70 characters\n"
            # This is not correct in terms of SEO, so we set our flag result to False
            result &= False
        # We can return result and report now
        return result, report
    # If we did not have just one tag title, we have to check if we have 0
    elif len(titles) == 0:
        # We add this information to the report
        report += "No tag title\n"
        # We return False and the report
        return False, report
    # Otherwise, we have more than one tag title
    else:
        # We add this information to the report
        report += "More than one tag title: \n"
        # We add each tag title to the report
        for title in titles:
            report += "{0}\n".format(title)
        # We return False and the report
        return False, report


def rule_2_meta_tag_description(html_parser: BeautifulSoup) -> (bool, str):
    """
    This method checks if there is only one tag meta with attribute name='description' and the text of this
    description is less than or equal to 155 and also if it is greater than 0
    :param html_parser: BeautifulSoup object that contains the HTML code parser
    :return: A couple of parameters: A boolean that is True if the conditions are met or False otherwise and a string
    that contains a report detailing the information about this
    """
    # We get the tags meta that has an attribute name = 'description'
    meta_descriptions = html_parser.find_all("meta", {"name": "description"})
    # We set the flag result True
    result = True
    # We create the parameter report to return the report for this rule
    report = ""
    # We check if there is only one tag meta that contains an attribute name = 'description'
    if len(meta_descriptions) == 1:
        # In that case, we add this information to this report
        report += "Only one tag meta with name='description'\n{0}\n".format(meta_descriptions)
        # In that case, we check if this tag is contained within the tag head
        if meta_descriptions[0].find_parent("head") is not None:
            # We add this information to the report
            report += "Tag meta with name = 'description' is contained within tag head\n"
        else:
            # Otherwise, it is not correct, we add this information to the report
            report += "Tag meta with name = 'description' is not contained within tag head\n"
            # We set the flag result to False (because the rule is not met)
            result &= False
        # We check if the text in the length of description is less than or equal to 155 characters
        if len(meta_descriptions[0].get_text()) <= 155:
            # We add this information to the report
            report += "Tag meta with name = 'description' is shorter than or equal to 155\n"
        # We check if the length of the description is 0, which means there is no text, but it is not correct
        elif len(meta_descriptions[0].get_text()) == 0:
            # We add this information to the report
            report += "Description is empty\n"
            # We set the flag result to False
            result &= False
        # Otherwise, the text in description is longer than 155 characters which is not correct either
        else:
            # We add this information to the report
            report += "Tag meta with name = 'description' is longer than 155\n"
            # We set the flag result to False
            result &= False
        # We result result and report
        return result, report
    # We check now if there is no tag meta with attribute name='description', which is not correct in terms of SEO
    elif meta_descriptions is None or len(meta_descriptions) == 0:
        # We add this information to the report
        report += "No tag meta with name='description'\n"
        # We return False and our report
        return False, report
    # Otherwise, we have more than 1 tag meta with attribute name = 'description', which is not correct either
    else:
        # We add this information to our report
        report = "More than one tag meta with name='description': \n"
        # We add the information of each tag to the report
        for meta_description in meta_descriptions:
            report += "{0}\n".format(meta_description)
        # We return False and our report
        return False, report


def rule_3_h1(html_parser: BeautifulSoup) -> (bool, str):
    """
    This method checks if there is only one tag h1 and it has text (rules needed for SEO)
    :param html_parser: BeautifulSoup object that contains the HTML code of our page parsed
    :return: We return a couple of variables, a boolean that is True is the conditions described above are met and False
    otherwise and a string that is a report giving information about our page
    """
    # We get all tags h1
    h1s = html_parser.find_all("h1")
    # We create our parameter report that we will return
    report = ""
    # If there is only one tag h1
    if len(h1s) == 1:
        # We add this information to our report
        report += "Only one tag h1\n{0}\n".format(h1s)
        # Now we check if our h1 that text
        if len(h1s[0].get_text()) > 0:
            # We add this information to our report
            report += "Tag has text\n"
            # We return True and our report (the conditions have been met correctly)
            return True, report
        # Otherwise, our tag h1 does not contain text, which is wrong
        else:
            # We add this information to the parameter report
            report += "Tag has not text\n"
            # We return False and our report
            return False, report
    # We check if there are no tags h1, which is not correct
    elif len(h1s) == 0:
        # We add this information to our report
        report += "No tag h1\n"
        # We return False and our report
        return False, report
    # Otherwise, there are more than one tag h1
    else:
        # We add this information ot our report
        report += "More than one tag h1:\n"
        # We add the details of each tag h1
        for h1 in h1s:
            report += "{0}\n".format(h1)
        # We return False and our report
        return False, report


def rule_3_headings_structure(html_parser: BeautifulSoup) -> (bool, str):
    """
    This method checks if headings have the right structure according to SEO (which is H1 is first, then we
    should have an H2, then H3s... and so one. Headings must follow each order in order, if we want to start over again
    we should start again with an H2 (remember we should only have one tag H1) then H3s...
    :param html_parser: BeautifulSoup object that contains the HTML code of our page parsed
    :return: We return a boolean that will be True if conditions are met or False otherwise. We also return a string
    called report with information about how the checking of this rule went
    """
    # We get all headings in the order they appear in our page
    headings = html_parser.select("h1, h2, h3, h4, h5, h6")
    # We create the variable that will contain the structure of these headings
    headings_structure = ""
    # We set the flag result True
    result = True
    # We are going to get on each iterations two headings, at first the first two and then we will get the second one in
    # the previous iteration and the next one so we can compare them
    # In order to do so, we go from 0 to the number of heading minus 2 (range(x,y) only gets to y-1) so we can use
    # two pointers to get the two headings in each iteration
    for i in range(0, len(headings) - 1):
        # We get the first heading for this iteration
        heading_i = headings[i]
        # We get the next heading for this iteration
        heading_j = headings[i + 1]
        # We turn these headings into the same number as the heading (for instance h1 to 1, h2 to 2...)
        hi = int(heading_i.name.replace("h", ""))
        hj = int(heading_j.name.replace("h", ""))
        # If we are checking the first heading in our HTML code
        if i == 0:
            # We check if that heading is h1, if it is not (remember now it is represented by the number of heading)
            if hi != 1:
                # We add this information first to the structure
                headings_structure += "H1 is not the first tag"
                # We add the heading in the correct format
                headings_structure += print_heading_structure(hi, heading_i.get_text())
            else:
                # Otherwise we just add the heading in the right format to the variable that contains the structure
                # of headings that we will return
                headings_structure += print_heading_structure(hi, heading_i.get_text())
        # We also check if the following header is a h1 too, in that case we just add this heading in the right format
        # to the variable that will return the structure of our headings
        if hj == 1:
            headings_structure += print_heading_structure(hj, heading_j.get_text())
        # Otherwise we compare our headings
        else:
            # If our parent heading is just one level above our child heading (for instance h1 and h2 or h2 and h3)
            # this is a correct structure
            if hi + 1 == hj:
                # We add the child heading to the variable headings_structure in the right format
                headings_structure += print_heading_structure(hj, heading_j.get_text())
            # If our parent heading is higher than our child, it means that we are starting from again with a new part
            # of the structure
            elif hi > hj:
                headings_structure += print_heading_structure(hj, heading_j.get_text())
            # If our parent heading is the same as our child heading is also correct
            elif hi == hj:
                headings_structure += print_heading_structure(hj, heading_j.get_text())
            # Otherwise, that means our parent tag and our child tag are separted by more than one level, which is not
            # correct
            else:
                # We add the missing that with a message error in red to the variable headings_structure
                headings_structure += print_heading_structure(hj - 1, Cs.ConsoleStyles.RED + "X Missing tag! X"
                                                              + Cs.ConsoleStyles.END)
                # We add our child heading to the variable headings_structure
                headings_structure += print_heading_structure(hj, heading_j.get_text())
                # We set the tag result False
                result &= False
    # We return result and headings_structure
    return result, headings_structure


def print_heading_structure(h: int, text: str) -> str:
    """
    This method prints our heading, represented as an integer (which is the level of the heading, h1 is 1 ...)
    :param h: Integer that represents our headings (which is the level of the heading, h1 is 1 ...)
    :param text: Text to add to our headings, in our case the text of the heading tag
    :return: We return a string that contains the heading in the format described above
    """
    # We leave as many two blank spaces as the level of the heading ("  "*h) so for instance for h1 we will leave "  "
    # for h2 we leave "    " and so on, then we print hx (x being the level of the heading) and then the text
    heading = "  " * h + "h{0}: - {1}\n".format(h, text.replace("\n", ""))
    # We return the str
    return heading


def rule_4_img_alt(html_parser: BeautifulSoup) -> (bool, str):
    """
    This method checks if all our images (tag img only) have the attribute alt with content
    :param html_parser: BeautifulSoup object that contains the HTML code of our page parsed
    :return: A boolean that tells us if the conditions described above are met and a str that is a report that gives us
    information about how this check went
    """
    # We get all tags img
    imgs = html_parser.find_all("img")
    # We create the variable report that we will report with information about how this process went
    report = ""
    # We set the flag result to True
    result = True
    # We go through every tag image
    for img in imgs:
        # If the tag img does not contain an attribute alt or that attribute does not contain text
        if img.get("alt") is None or img.get("alt") == "":
            # We add the information of this tag to our report
            report += "{0}\n".format(img)
            # We set our flag result to False
            result = False
    # We return result and report
    return result, report


def rule_5_no_follow_links(html_parser: BeautifulSoup) -> str:
    """
    This method returns a report with all links in our page that are no follow
    :param html_parser: BeautifulSoup object with the HTML of our page parsed
    :return: A string report with the links that are no follow
    """
    # We get all tags a that have an attribute rel='nofollow'
    as_nofollow = html_parser.find_all("a", {"rel": "nofollow"})
    # We check if there are more tags a that are no follow and add the corresponding message
    if len(as_nofollow) > 0:
        report = "The following links using the tag 'a' have attribute rel='nofollow': \n"
    else:
        report = "No links using the tag 'a' have attribute rel='nofollow' \n"
    # We go through every tag a that is no follow and add it to the report
    for a_nofollow in as_nofollow:
        report += "{0}\n".format(a_nofollow)
    # We get all tags link that are no follow
    links_nofollow = html_parser.find_all("link", {"rel": "nofollow"})
    # We check if there are or aren't any tags link that are no follow
    # And add the corresponding message
    if len(links_nofollow) > 0:
        report += "The following tags 'link' have attribute rel='nofollow': \n"
    else:
        report += "No tags 'link' have the attribute rel='nofollow' \n"
    # We go through every tag link that are no follow and add it to the report
    for link_nofollow in links_nofollow:
        report += "{0}\n".format(link_nofollow)
    # We return the report
    return report


def rule_6_hreflang(html_parser: BeautifulSoup, languages: list) -> (bool, str):
    """
    This method check the languages, href and hreflang and canonical links in tag head
    :param html_parser: BeautifulSoup object that contains HTML code of our page parsed
    :param languages: List of hreflang codes that our page must have
    :return: A boolean that will be True if there is one link that is canonical and our for each hreflang but False
    if one these is not True or there are more than one of those and also a string that contains a report giving
    information about how this checking went
    """
    # We get the tag head
    head = html_parser.find("head")
    # We get all the links in tag head
    links = head.find_all("link")
    # We create this dictionary, in this dictionary we will save how many canonical links we found and how many of each
    # hreflang links we found. Key is canonical or the hreflang attribute and value the number of those found
    search = {}
    # We set the flag result to True
    result = True
    # We create the variable report to return this report
    report = ""
    # We go through every tag link in head
    for link in links:
        # we get the attributes rel in that tag
        rels = link.get_attribute_list("rel")
        # We go through every tag rel (we will only have one)
        for rel in rels:
            # We get the attribute href
            href = link.get_attribute_list("href")
            # If rel is not None
            if rel is not None:
                # We check if the attribute rel is 'alternate'
                if rel == "alternate":
                    # In that case, we have to check the attribute hreflang
                    hreflangs = link.get_attribute_list("hreflang")
                    # We check now that attribute
                    for hreflang in hreflangs:
                        # If our hreflang is one of the language in which this page should be
                        if hreflang in languages:
                            # If it is not one of the dictionary keys, it is because it is the first time we found
                            # this hreflang
                            if hreflang not in search.keys():
                                # We set that hreflang to 1, as we found it once so far
                                search[hreflang] = 1
                                # We add this information to the report
                                report += "href: {0} - hreflang: {1}\n".format(href, hreflang)
                            # Otherwise, it is not the first time we found this, so we add one to the times we have
                            # already found this keys/hreflang
                            else:
                                search[hreflang] += 1
                                # We add this information to the report in red (as it is wrong to have more than one
                                # link with hreflang)
                                report += Cs.ConsoleStyles.RED + "XXX href: {0} - hreflang: {1} n={2} " \
                                                                 "XX" + Cs.ConsoleStyles.END + ""\
                                    .format(href, hreflang, search[hreflang])
                                # We set the flag result to False
                                result &= False
                        # If the attribute hreflang in tag link is not one of the languages, that is not correct
                        else:
                            # We add this information to this report
                            report += Cs.ConsoleStyles.RED + "XXX href: {0} - hreflang: {1} hreflang is not correct " \
                                                             "XX" + Cs.ConsoleStyles.END + "".format(href, hreflang)
                            # We set our flag result to False
                            result &= False
                # If attribute rel is canonical
                if rel == "canonical":
                    # If attribute rel = 'canonical' is not part of our dictionary of languages, it is because it is
                    # the first time we found it
                    if rel not in search.keys():
                        # We add this key "canonical" and give it value 1
                        search[rel] = 1
                        # Also we add this information to the report
                        report += "canonical link href: {0}\n".format(href)
                    else:
                        # Otherwise, we had already found an instance of rel='canonical' so we add this instance
                        # to the number of instances we found of this
                        search[rel] += 1
                        # We add this information to the report
                        report += Cs.ConsoleStyles.RED + "XXX Canonical link n: {0} href: {1} more than one canonical" \
                                                         "link XX" + Cs.ConsoleStyles.END + "\n".format(search[rel],
                                                                                                        href)
                        # We set the flag result to False
                        result &= False
    # If we have no keys, we did not find a canonical link or links with reflang in the right languages
    if len(search.keys()) == 0:
        # So we add this information to the report
        report += "No canonical link or links with hreflang in the right languages\n"
        # We add False to the result of this process
        result &= False
    # Now, we finally check if we found an attribute rel='canonical' and every language in hreflang once
    # We create a list with canonical
    v_keys = ["canonical"]
    # We add the list of languages/hreflang codes passed as parameter
    v_keys = v_keys + languages
    # We check if we found all of these
    for v_key in v_keys:
        # If the one of the elements in language or canonical were not added to the dictionary search is because we
        # didn't find it, which is not correct
        if v_key not in search.keys() or search[v_key] is None or search[v_key] == 0:
            # We add the corresponding information to the string report
            if v_key == "canonical":
                report += "No link with canonical\n"
            else:
                report += "No link with reflang: {0}\n".format(v_key)
            # We set the flag result to False
            result &= False
    # We return result and report
    return result, report
