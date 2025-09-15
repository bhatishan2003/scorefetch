import requests
from bs4 import BeautifulSoup

class CricketMatchBrowser:
    def __init__(self):
        self.base_url = "https://www.cricbuzz.com"
        self.live_scores_url = "https://www.cricbuzz.com/cricket-match/live-scores"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/91.0.4472.124 Safari/537.36'
        }
        self.matches = []

    def get_page(self, url):
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            return response.content
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            return None

    def get_live_matches(self):
        content = self.get_page(self.live_scores_url)
        if not content:
            return []

        soup = BeautifulSoup(content, 'html.parser')
        matches = []
        match_containers = soup.find_all('a', class_='cb-lv-scrs-well')

        for container in match_containers:
            try:
                match_title = container.get('title', '').strip()
                match_url = self.base_url + container.get('href', '')

                score_info = {}
                team1_score = container.find('div', class_='cb-hmscg-bat-txt')
                team2_score = container.find('div', class_='cb-hmscg-bwl-txt')
                result_tag = (container.find('div', class_='cb-text-complete') or
                              container.find('div', class_='cb-text-live'))

                if team1_score and team2_score:
                    t1_name = team1_score.find('div', class_='cb-hmscg-tm-nm').get_text(strip=True)
                    t1_score = team1_score.find_all('div')[-1].get_text(strip=True)
                    t2_name = team2_score.find('div', class_='cb-hmscg-tm-nm').get_text(strip=True)
                    t2_score = team2_score.find_all('div')[-1].get_text(strip=True)
                    score_info = {t1_name: t1_score, t2_name: t2_score}

                if result_tag:
                    score_info['result'] = result_tag.get_text(strip=True)

                matches.append({
                    'title': match_title,
                    'url': match_url,
                    'score_info': score_info
                })
            except Exception:
                continue

        self.matches = matches
        return matches

    def get_match_details(self, match_url, score_info=None):
        content = self.get_page(match_url)
        if not content:
            return None

        soup = BeautifulSoup(content, 'html.parser')
        details = {}

        title_tag = soup.find('h1', class_='cb-nav-hdr')
        if title_tag:
            details['title'] = title_tag.get_text(strip=True)

        status_tag = (soup.find('div', class_='cb-text-live') or
                      soup.find('div', class_='cb-text-complete'))
        if status_tag:
            details['status'] = status_tag.get_text(strip=True)

        if score_info:
            for key, value in score_info.items():
                details[key] = value

        commentary = []
        items = soup.find_all('div', class_='cb-col cb-col-90 cb-dis-inline')[:5]
        for item in items:
            text = item.get_text(strip=True)
            if text:
                commentary.append(text[:100] + "..." if len(text) > 100 else text)
        if commentary:
            details['recent_commentary'] = commentary

        return details if details else None

    def display_matches(self):
        if not self.matches:
            print("No live matches found.")
            return
        print("\nLIVE MATCHES:")
        print("=" * 50)
        for i, match in enumerate(self.matches, 1):
            print(f"{i}. {match['title']}")

    def display_match_details(self, match_index):
        if not self.matches or match_index < 1 or match_index > len(self.matches):
            print("Invalid match number.")
            return
        selected_match = self.matches[match_index - 1]
        details = self.get_match_details(selected_match['url'], score_info=selected_match['score_info'])
        if not details:
            print("Could not load match details.")
            return

        print("\nMATCH DETAILS:")
        print("=" * 60)
        print(f"Match: {details.get('title', 'N/A')}")
        print(f"Status: {details.get('status', 'N/A')}")
        print("\nSCORES:")
        for key, value in details.items():
            if key not in ['title', 'status', 'recent_commentary']:
                print(f"{key}: {value}")
        if 'recent_commentary' in details:
            print("\nRECENT COMMENTARY:")
            for comment in details['recent_commentary']:
                print(f"• {comment}")
        print("=" * 60)
