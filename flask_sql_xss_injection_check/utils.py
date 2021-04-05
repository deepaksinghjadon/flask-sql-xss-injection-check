import re
import logging

LOG = logging.getLogger(__name__)


def has_sql(content):
    """
    regex reference: http://www.symantec.com/connect/articles/detection-sql-injection-and-cross-site-scripting-attacks
    """
    match = (
        re.search(r'(\%27)|(\')|(\-\-)|(\%23)|(#)', content, re.IGNORECASE) or
        re.search(r'((\%3D)|(=))[^\n]*((\%27)|(\')|(\-\-)|(\%3B)|(;))', content, re.IGNORECASE) or
        re.search(r'\w*((\%27)|(\'))((\%6F)|o|(\%4F))((\%72)|r|(\%52))', content, re.IGNORECASE) or
        re.search(r'((\%27)|(\'))union', content, re.IGNORECASE)
    )
    print("Content type is:",type(content))
    if match:
        LOG.info("SQL injection vulnerability found:", content, match)
        print("SQL injection vulnerability found:", content, match)
        return True
    return False

def has_xss(content):
    """
    regex reference: http://www.symantec.com/connect/articles/detection-sql-injection-and-cross-site-scripting-attacks
    """
    match = (
        re.search(r'((\%3C)|<)((\%2F)|\/)*[a-z0-9\%]+((\%3E)|>)', content, re.IGNORECASE) or
        re.search(r'((\%3C)|<)((\%69)|i|(\%49))((\%6D)|m|(\%4D))((\%67)|g|(\%47))[^\n]+((\%3E)|>)', content, re.IGNORECASE) or
        re.search(r'((\%3C)|<)[^\n]+((\%3E)|>)', content, re.IGNORECASE) 
    )
    if match:
        LOG.info("XSS injection vulnerability found:", content, match)
        print("XSS injection vulnerability found:", content, match)
        return True
    return False