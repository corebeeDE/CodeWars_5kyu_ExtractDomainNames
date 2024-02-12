import re
import unittest

class TestDomains(unittest.TestCase):
    dictionary =\
                    {
                        'google1':      'http://google1.com',
                        'google2':      'http://google2.co.jp',
                        '123':          'http://123.net',
                        'hyphen-site':  'https://hyphen-site.org',
                        'codewars1':     'http://codewars1.com',
                        'xakep':        'www.xakep.ru',
                        'youtube':      'https://youtube.com',
                        'codewars2':    'http://www.codewars2.com/kata/',
                        'icann':        'icann.org',
                    }

    def test_urls_normal(self):
        for domain, test_case in self.dictionary.items():
            self.assertEqual(CodeWarsKata.get_domain_name_regex(test_case), domain)

    def test_urls_alternative(self):
        for domain, test_case in self.dictionary.items():
            self.assertEqual(CodeWarsKata.get_domain_name_split_only(test_case), domain)



class CodeWarsKata():
    def get_domain_name_regex(url):
        return re.split(r'\.\b.*$', re.split(r'http\w?\:\/\/www.|http\w?\:\/\/|www.', url)[-1])[0]

    def get_domain_name_split_only(url):
        return url.split('//')[-1].split('www.')[-1].split('.')[0]



def main():
    unittest.main()

if __name__ == "__main__":
    main()