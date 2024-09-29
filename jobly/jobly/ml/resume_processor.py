# resume_processor.py  
import fitz
import pandas as pd

class ResumeProcessor:
    def __init__(self,csv_file_path):
        self.csv_file_path = csv_file_path
        

    def read_pdf(self, file_path):
        """Read text from a PDF file."""
        document = fitz.open(file_path)
        text = ""

        for page in document:
            text += page.get_text()

        document.close()
        return text

    def match_skills_with_keywords(self,resume_text, skills_list):
        # Normalize the resume text to lower case for case-insensitive matching
        # print(resume_text)
        # resume_text = resume_text.lower()
        

        # Find and count skills present in the resume text
        matched_skills = [skill for skill in skills_list if skill.lower() in resume_text]
        return matched_skills
    
    def filter_data_by_title(self,title):

        data = pd.read_csv(self.csv_file_path)
        filtered_data = data[data['title'].str.contains(title, case=False, na=False)]
        return filtered_data

   