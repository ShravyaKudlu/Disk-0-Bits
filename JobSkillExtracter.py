import pickle
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
#from abc import JobSkillExtractor  

class JobSkillExtractor:
    def _extract_top_skills(self):
        # Function to extract top 20 skills for each job title
        def get_top_skills(group, n=20):
            all_skills = ' '.join(group['job_skills'].dropna())
            vectorizer = CountVectorizer(tokenizer=lambda x: x.split(','))
            skill_counts = vectorizer.fit_transform([all_skills])
            skill_count_df = pd.DataFrame(skill_counts.toarray(), columns=vectorizer.get_feature_names_out())
            return skill_count_df.sum().nlargest(n).index.tolist()

        # Extract top skills for each job title and store in a dictionary
        job_skill_map = self.df.groupby('job_title').apply(get_top_skills).to_dict()
        return job_skill_map

    def get_skills_by_title(self, job_title):
        # Retrieve top skills for a given job title
        return self.job_skill_map.get(job_title, [])

    def result(job_title):
        with open("job_skill_extractor.pkl", 'rb') as f:
            extractor = pickle.load(f)
        #job_title = 'Data Scientist'
        skills = extractor.get_skills_by_title(job_title)
        print(f"Top skills for {job_title}: {skills}")
    
jse = JobSkillExtractor
job_title='Software Developer'
jse.result(job_title)