# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:
# url = "http://github.com/carbonfive/raygun" -> domain name = "github"#
# url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
# url = "https://www.cnet.com"                -> domain name = cnet"

def domain_name(url):
    domain = url.replace('http://', '').replace('https://', '').replace('www.', '')
    return domain.split('.')[0]

def domain_name2(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]

#Pruebas en consola / console tests
print (domain_name('http://google.com'), 'google')
print (domain_name("http://google.com"), "google")
print (domain_name("http://google.co.jp"), "google")
print (domain_name("https://123.net"), "123")
print (domain_name("https://hyphen-site.org"), "hyphen-site")
print (domain_name2("http://codewars.com"), "codewars")
print (domain_name2("www.xakep.ru"), "xakep")
print (domain_name2("https://youtube.com"), "youtube")
print (domain_name2("http://www.codewars.com/kata/"), "codewars")
print (domain_name2("icann.org"), "icann")


