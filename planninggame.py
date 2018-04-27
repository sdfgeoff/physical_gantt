import svgwrite
from svgwrite import cm, mm 

class Resource:
	def __init__(self, name):
		self.name = name
		self.tasks = []
		
	def create_task(self, task_name, task_duration):
		task = Task(task_name)
		task.duration = task_duration
		self.tasks.append(task)


class Task:
	def __init__(self, name):
		self.name = name
		self.duration = 0



class Render:
	def __init__(self, *args):
		self.resources = args
		
	def write(self, prefix):
		# Generate unique colors for each resource
		colors = ['red', 'blue', 'green', 'grey', 'pink']
			
		keycard = svgwrite.Drawing(filename=prefix+'-keycard.svg', size=(88*mm, 63*mm))
		for resource_id, resource in enumerate(self.resources):
			top = 12 * resource_id + 5
			keycard.add(keycard.rect(insert=(5*mm, top*mm), size=(10*mm, 10*mm), fill=colors[resource_id]))
			keycard.add(keycard.text(resource.name, insert=(17*mm, (top+6)*mm), fill='black', style="font-size:20"))
		keycard.save()
		
		for resource_id, resource in enumerate(self.resources):
			color = colors[resource_id]
			page = svgwrite.Drawing(filename=prefix+'-'+resource.name+'.svg', size=(297*mm, 210*mm))
			for task_id, task in enumerate(resource.tasks):
				top = task_id * 20 + 5
				for d in range(task.duration):
					left = 20 * d + 5
					page.add(page.rect(insert=(left*mm, top*mm), size=(20*mm, 20*mm), fill=colors[resource_id], stroke='black'))
				
				page.add(page.rect(insert=(7*mm, (top+3)*mm), size=((task.duration * 20 - 4)*mm, 14*mm), fill='white', opacity=0.8))
				page.add(page.text(task.name, insert=(8*mm, (top+11)*mm), fill='black', style="font-size:15"))
				
			page.save()
