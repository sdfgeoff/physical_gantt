from planninggame import Resource, Render

hardware = Resource("Hardware Department")

hardware.create_task("This", 3)
hardware.create_task("That", 3)
hardware.create_task("The Other", 2)
hardware.create_task("", 10)
hardware.create_task("", 10)
hardware.create_task("", 10)

software = Resource("Software Department")

software.create_task("Snargle", 2)
software.create_task("Blarf", 4)

software.create_task("", 10) 
software.create_task("", 10) 
software.create_task("", 10) 


output = Render(hardware, software)
output.write("test")
