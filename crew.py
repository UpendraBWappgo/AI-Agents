from crewai import Crew,Process
from agents import blog_researcher,blog_writer
from task import research ,write


# Forming the tech-focused crew with some enhanced configurations
crew = Crew(
  agents=[blog_researcher, blog_writer],
  tasks=[research, write],
  process=Process.sequential,  # Optional: Sequential task execution is default
  memory=True,
  cache=True,
  max_rpm=100,
  share_crew=True
)

## start the task execution process with enhanced feedback
result=crew.kickoff(inputs={'topic':'No Need to visit Office for your Taxation and Legal works - Legal251'})
print(result)
