import argparse
import cfscrape

parser = argparse.ArgumentParser(description="pwned or not?")
parser.add_argument("-e", dest="email")
parser.add_argument("-f", dest="filename")
args = parser.parse_args()

email = str(args.email)
filename = str(args.filename)


def checkEmail(email):
    scraper = cfscrape.create_scraper()
    result = scraper.get("https://haveibeenpwned.com/api/breachedaccount/" + email + "?includeUnverified=true")
    if str(result.status_code) == "404": # not breached
        print email + " has not been breached."
    elif str(result.status_code) == "200": # breached
        print email + " has been breached and the sites are the following ..."
        print result.content
    elif str(result.status_code) == "429": # Rate limit triggered
        print "Rate limit - " + check.headers['Retry-After'] + " seconds"
    else:
        print "Something went wrong" + email
        
        
if __name__ == "__main__":        
    if email != "None":
        checkEmail(email)
    elif filename != "None":
        eachemail = [line.rstrip('\n') for line in open(filename)]
        for email in eachemail:
            checkEmail(email)
    else:
        print "nothing to do here"
