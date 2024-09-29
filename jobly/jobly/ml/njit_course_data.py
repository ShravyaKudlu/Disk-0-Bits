import requests
from bs4 import BeautifulSoup
import re

URLS = [
    'https://catalog.njit.edu/graduate/computing-sciences/computer-science/#coursestext',
    'https://catalog.njit.edu/graduate/computing-sciences/information-systems/#coursestext',
    'https://catalog.njit.edu/graduate/computing-sciences/data-science/#coursestext'
]

class NJITCourseScraper:

  def __init__(self,diff):
      self.urls = URLS
      self.diff = diff
      

  # Function to scrape NJIT course catalog from a given URL
  def scrape_njit_courses(self):
      for url in self.urls:
        response = requests.get(url)

        if response.status_code != 200:
            print(f"Failed to retrieve the webpage: {url}")
            return None

        soup = BeautifulSoup(response.content, 'html.parser')
        course_section = soup.find('div', {'id': 'coursestextcontainer'})

        courses = []
        if course_section:
            course_titles = course_section.find_all('p', class_='courseblocktitle')
            course_descriptions = course_section.find_all('p', class_='courseblockdesc')

            for title, desc in zip(course_titles, course_descriptions):
                course_code_name = title.get_text(strip=True)
                course_description = desc.get_text(strip=True)
                courses.append({
                    'course_code_name': course_code_name,
                    'description': course_description
                })

      return courses

  def matches_skills(self,description, diff):
    # Normalize to lowercase for case-insensitive comparison
    normalized_description = description.lower()

    # Check if any of the skills are present in the description
    for skill in self.diff:
        if skill.lower() in normalized_description:
            return True
    return False


  # Function to filter courses with matching skills
  def filter_courses_with_skills(self,courses, diff):
      courses_with_skills = []

      for course in courses:
          course_description = course['description']
          if self.matches_skills(course_description, self.diff):
              courses_with_skills.append(course['course_code_name'])

      return courses_with_skills
    
  