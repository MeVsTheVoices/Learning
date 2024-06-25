from jinja2 import Environment, FileSystemLoader
max_score = 100
test_name = "Python Challenge"
students = [
    {"name" : "Billy", "score" : 100},
    {"name" : "Frank", "score" : 87},
    {"name" : "Jill", "score" : 92},
]

environment = Environment(loader = FileSystemLoader("templates/"))
results_filename = "students_results.html"
results_template = environment.get_template("mytemplate.html")
context = {
    "students" : students,
    "test_name" : test_name,
    "max_score" : max_score,
}
print(results_template.render(context))
