from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Uncomment the following line to use an example of a custom tool
# from presales_prep.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

@CrewBase
class PresalesPrepCrew():
	"""PresalesPrep crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def company_researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['company_researcher'],
			# tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
			verbose=True
		)

	@agent
	def topic_researcher(self) -> Agent:
	    return Agent(
            config=self.agents_config['topic_researcher'],
            verbose=True
        )

	@agent
	def executive_assistant(self) -> Agent:
		return Agent(
			config=self.agents_config['executive_assistant'],
			verbose=True
		)

	@task
	def company_research_task(self) -> Task:
		return Task(
			config=self.tasks_config['company_research_task'],
		)

	@task
	def topic_research_task(self) -> Task:
	   return Task(
				config=self.tasks_config['topic_research_task'],
        )

	@task
	def report_preparation_task(self) -> Task:
		return Task(
			config=self.tasks_config['report_preparation_task'],
			output_file='solution.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the PresalesPrep crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
