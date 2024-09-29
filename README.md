Jobly is Born The idea for Jobly began as a simple concept: an application that could take a student’s resume and, through intelligent analysis, provide recommendations for the skills and courses that would help them land their dream job. We envisioned Jobly as more than just a recommendation engine—it would become a comprehensive tool for students to plan their educational and professional development, with recommendations sourced from both universities and popular platforms like Coursera. Our vision was to help students: 1. Identify Gaps: Analyze their resumes and identify gaps in their skill set compared to industry demands. 2. Provide Courses: Recommend relevant university courses as well as online resources (such as Coursera) to bridge those gaps. 3. Improve Employability: Equip students with tailored insights on how to improve their profiles and become the ideal candidates for their desired job roles.




To run the jobly program clone the main repository.
1. create your environment
```bash
source myenv/bin/activate
```
2. install the requirements.txt
   ```bash
   pip3 install -r requirements.txt
   ```  
   
3.
  Down load this dataset for ml folder
  ```bash
    https://drive.google.com/file/d/1wbKIjaZx1zX0Tgv6dhTDzQiEkNe6p1Im/view?usp=sharing
     cd jobly
     python3 manage.py runserver 
  ```

4. Additionally 
bash```https://drive.google.com/file/d/1X_zOXx9439cIrSHi_R_mDHYZLJIKtfmv/view?usp=sharing```
Download the Model JobSkillExtracter from the above link and change the directory on the JobSkillExtracter.py.
Change the job_title to whatever title you want. For example: Software Developer, Sales, Marketing, Data Scientist etc. and find the 20 top most required skills for that job.
Use this top 20 skills in our Jobly app to curate results for your resume.
In the App, Upload your resume and enter the preferred job title/role and see our magic work to give you our top course recommmendations.
