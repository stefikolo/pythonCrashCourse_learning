import chapter_009.restaurant
from chapter_009.admin import Admin

kebab = chapter_009.restaurant.Restaurant('doner kebs', 'falafel and kebap')
kebab.describe_restaurant()

admin = Admin('@dm!n', 'Adm1n')
admin.desc_user()
admin.privilages.show_privileges()
