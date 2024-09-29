import requests

API_KEY = "fjCCyDMhfNO6dSvCvAylcLt4jkhKAD1GigcL3fQMMeeTYobf"
BASE_URL = "https://api.coursera.org/api/courses.v1"



class Coursera:
    def __init__(self,diff):
      self.diff = diff

    def search_courses(self,diff):
        headers = {
            'Authorization': f'Bearer {API_KEY}',
            'Accept': 'application/json'
        }

        all_courses = []  # List to hold all results

        for keyword in self.diff:
            params = {
                'q': 'search',
                'query': keyword
            }

            response = requests.get(BASE_URL, headers=headers, params=params)

            # Check if the response is OK
            if response.status_code == 200:
                courses = response.json().get('elements', [])
                courses = courses[:3]  # Limit to the first 5 results
                for course in courses:
                    title = course.get('name', 'No title available')
                    # Assuming video link is stored in 'previewLink' field
                    video_link = course.get('slug', False)
                    if video_link:
                        video_link = f"https://www.coursera.org/learn/{video_link}"

                    # Collecting title and video link
                    all_courses.append({
                        'title': title,
                        'video_link': video_link
                    })
            else:
                print(f"Error: {response.status_code} - {response.text}")

        return all_courses

