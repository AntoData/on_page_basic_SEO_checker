"""
Example of how to use this SEO checker
"""
# We import preliminar_seo_rules_check to perform the check
from API.SEOChecker import preliminar_seo_rules_check

# We will perform this test in this url
url = "https://www.worldometers.info/coronavirus/"
# We will check if it is developed for the following hreflang codes
languages = ["es", "en"]
# We call this method but we don't give it the parameter rules, so it will check all rules
result, report = preliminar_seo_rules_check(url=url,languages=languages)
# We got the result that tells us if all rules went OK or one returned KO
print(result)
# We print the report that gives us information about how this went
print(report)