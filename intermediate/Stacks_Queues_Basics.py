import re
import matplotlib.pyplot as plt


MOCK_PAGES = {
    "https://python.org": {"title": "Welcome to Python.org"},
    "http://data.pr4e.org": {"title": "Data for Programming for Everybody"},
    "https://www.wikipedia.org": {"title": "Wikipedia"},
    "https://docs.python.org": {"title": "Python 3 Documentation"},
    "https://peps.python.org": {"title": "PEP 0 – Index of Python Enhancement Proposals"},
    "https://pypi.org": {"title": "PyPI · The Python Package Index"},
}

class CrawlerSession:
    def __init__(self):
        self.to_visit = []
        self.history = []
        self.metadata = {}

        self.url_pattern = re.compile(
            r'^https?://'
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|' 
            r'localhost|' 
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' 
            r'(?::\d+)?' 
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    def add_url(self, url):
        """Validate and add URL to to_visit if valid and not already seen"""
        if self._is_valid_url(url) and url not in self.to_visit and url not in self.history:
            self.to_visit.append(url)
            print(f"Added: {url}")
            return True
        return False

    def _is_valid_url(self, url):
        """Validate URL using regex"""
        return bool(self.url_pattern.match(url))

    def crawl_next(self):
        """
        Remove next URL from to_visit, add to history, fetch metadata.
        Returns the URL being crawled, or None if queue empty.
        """
        if not self.to_visit:
            return None

        url = self.to_visit.pop(0)
        self.history.append(url)

        page_info = MOCK_PAGES.get(url, {"title": "Unknown Title"})
        self.metadata[url] = {"URL": url, "Title": page_info["title"]}

        return url

    def backtrack(self):
        if self.history:
            url = self.history.pop()
            return url
        return None

def load_seeds(filename="seeds.txt"):
    try:
        with open(filename, "r") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"{filename} not found. Using default seeds.")
        return list(MOCK_PAGES.keys())[:3]

def plot_memory_trends(q_sizes, s_sizes):

    steps = range(1, len(q_sizes) + 1)

    plt.figure(figsize=(10, 6))
    plt.plot(steps, q_sizes, marker='o', label='Discovery Variable Size', linewidth=2)
    plt.plot(steps, s_sizes, marker='s', label='History Size', linewidth=2)

    plt.xlabel("Crawl Step")
    plt.ylabel("Number of Items")
    plt.title("EchoSearch Crawler Memory Trends")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xticks(steps)
    plt.tight_layout()
    plt.show()

def main():
    print("--- ECHOSEARCH CRAWLER INITIALIZED ---")

    session = CrawlerSession()
    q_sizes = []
    s_sizes = []

    print("Loading seeds from seeds.txt...")
    seeds = load_seeds()
    for seed in seeds:
        session.add_url(seed)

    q_sizes.append(len(session.to_visit))
    s_sizes.append(len(session.history))

    for step in range(1, 6):
        url = session.crawl_next()
        if url is None:
            print("[Alert] No more URLs to visit.")
            break
        print(f"[Step {step}] Crawling: {url}")
        q_sizes.append(len(session.to_visit))
        s_sizes.append(len(session.history))


    if len(session.history) > 1:
        print("[Alert] History too deep. Backtracking...")
        last_url = session.backtrack()
        print(f"Returning from: {last_url}")
        q_sizes.append(len(session.to_visit))
        s_sizes.append(len(session.history))

    print("Crawl analysis complete. Displaying memory trends...")
    plot_memory_trends(q_sizes, s_sizes)

if __name__ == "__main__":
    main()