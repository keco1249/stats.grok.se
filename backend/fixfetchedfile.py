import re,os

FETCHED_FILE = "fetched2.txt"

def fixFetched():
    expr = re.compile("pagecounts_[0-9]{8}_[0-9]{2}")

    files = os.listdir(".")
    pagecounts = [e for e in files if expr.match(e)]
    
    f = file(FETCHED_FILE,"w")
    f.writelines([x+"\n" for x in pagecounts])
    f.close()
    
if __name__ == "__main__":
    fixFetched()