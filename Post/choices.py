from .models import Category

#Category_list = [
#    ('Lifestyle','Lifestyle'),
#    ('Design','Design'),
#    ('Photography','Photography'),
#    ('Health','Health'),
#    ('Management','Management'),
#    ('Gaming','Gaming'),
#    ('Entertainment','Entertainment'),
#    ('Sports','Sports'),
#    ('Coding','Coding'),
#    ('Nature','Nature'),
#]

Category_items = Category.objects.all().values_list('Name','Name')
Category_list = []

for item in Category_items:
    Category_list.append(item)