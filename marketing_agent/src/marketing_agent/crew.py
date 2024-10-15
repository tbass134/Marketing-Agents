from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from marketing_agent.tools.custom_tool import Webscraper
from crewai_tools import EXASearchTool

import os

@CrewBase
class MarketingAgentCrew():
	"""MarketingAgent crew"""

	# AGENTS
	@agent
	def shop_owner(self) -> Agent:
		return Agent(
			config=self.agents_config['shop_owner'],
			llm=LLM(model=os.environ["MODEL"], base_url="http://localhost:11434"),
			verbose=True
		)
	
	@agent
	def researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['researcher'],
			llm=LLM(model=os.environ["MODEL"], base_url="http://localhost:11434"),
			tools=[EXASearchTool()],
			verbose=True
		)
	
	@agent
	def seo_specialist(self) -> Agent:
		return Agent(
			config=self.agents_config['seo_specialist'],
			llm=LLM(model=os.environ["MODEL"], base_url="http://localhost:11434"),
			verbose=True
		)
	
	@agent
	def content_creator(self) -> Agent:
		return Agent(
			config=self.agents_config['content_creator'],
			llm=LLM(model=os.environ["MODEL"], base_url="http://localhost:11434"),
			verbose=True
		)
	
	#TASKS
	@task
	def owner_task(self) -> Task:
		return Task(
			config=self.tasks_config['owner_task'],
		)
	

	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['research_task'],
		)
	

	@task
	def seo_task(self) -> Task:
		return Task(
			config=self.tasks_config['seo_task'],
		)
	
	@task
	def content_creator_task(self) -> Task:
		return Task(
			config=self.tasks_config['content_creator_task'],
			output_file='email.md'
		)
	
	
	@crew
	def crew(self) -> Crew:
		"""Creates the MarketingAgent crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)