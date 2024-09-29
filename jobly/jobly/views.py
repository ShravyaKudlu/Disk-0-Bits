import re
from typing import Counter
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import os
import pickle
import tempfile
from django.http import JsonResponse
from .ml.coursera import Coursera
from .ml.njit_course_data import NJITCourseScraper
from .ml.resume_processor import ResumeProcessor





SKILLS_LIST = [
    "Python", "Java", "SQL",
    "JavaScript", "C++", "HTML", "CSS",
    "Django", "React", "Node.js",
    "TensorFlow", "Tableau", "Kubernetes", "AWS", "Azure", "GCP",
    "Docker", "Angular Js", "Hadoop", "Terraform", "R Programming",
    "Linux", "Git", "RESTful APIs",
    "Microservices", "CI/CD", "NoSQL", "GraphQL", "Blockchain",
    "Flask", "Spring Boot", "Ruby on Rails", "ASP.NET", "Swift",
    "Kotlin", "Objective-C", "Perl",
    "TypeScript", "Vue.js", "Svelte", "Bootstrap", "Jenkins",
    "JIRA", "Confluence", "PostgreSQL", "MySQL", "MongoDB",
    "Cassandra", "Redis", "Elasticsearch", "Kibana", "Logstash",
]




def index(request):
  return render(request, 'index.html')

def about(request):
  return render(request, 'about.html')


def upload(request):
    
    if request.method == 'POST':
        resume = request.FILES.get('resume')  
        job_title = request.POST.get('job_title')  
        # if resume:
        #     # print(f'Received resume: {resume.name}')
        # if job_title:
        #     # print(f'Received job title: {job_title}')
        
        if resume and job_title:
            with tempfile.NamedTemporaryFile(delete=True) as temp_file:
                for chunk in resume.chunks():
                    temp_file.write(chunk)
                temp_file.flush()
                path = "/home/shravyashanbhogue/projects/Disk-O-Bits/jobly/jobly/ml/postings.csv"
                # Create an instance of ResumeProcessor
                
                processor = ResumeProcessor(path)
               
                pdf_text = processor.read_pdf(temp_file.name).lower()
                extracted_skills_resume = processor.match_skills_with_keywords(pdf_text,SKILLS_LIST)  
                print(extracted_skills_resume)  
                
                filtered_data = processor.filter_data_by_title(job_title)
                # print(filtered_data)
                item_counts = Counter()
                
                for index,row in filtered_data.iterrows():
                    job_description = row['description']  
                    extracted_skills_jobAd = processor.match_skills_with_keywords(job_description, SKILLS_LIST)

                    
                    item_counts.update(extracted_skills_jobAd)
                    print(extracted_skills_jobAd)

                top_3 = item_counts.most_common(5)
                top_skill=[]
                # Print the top 3 occurrences
                # print("Top 3 Occurrences:")
                for item, count in top_3:
                    top_skill.append(item)
                    # print(f"{item}: {count} occurrence(s)")                

                
                diff = list(set(top_skill)-set(extracted_skills_resume))
                print(diff)
                njit_course_scraper = NJITCourseScraper(diff)


      # Scrape courses from the current URL
                courses = njit_course_scraper.scrape_njit_courses()

                if courses:
          # Filter courses that match any of the predefined skills
                    courses_with_skills = njit_course_scraper.filter_courses_with_skills(courses,diff)

          # Print the courses with matching skills
                    print("\nCourses with matching skills:")
                    for course in courses_with_skills:
                        print(re.sub(r'\d+ credits?, \d+ contact hours?\.', '', course))
                else:
                    print("No courses found or unable to scrape data.")

                

                coursera = Coursera(diff)
                data1=coursera.search_courses(diff)
                for vids in data1:
                    print(f"Course: {vids['title']}, Video Link: {vids['video_link']}")
                print("\n")



            return JsonResponse({
                'diff': diff,
                'courses_with_skills': courses_with_skills,
                'data1': data1
            }, status=200)
