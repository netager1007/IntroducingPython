import report as wr
from report import get_description as do_it

description = wr.get_description()
print("Today's weather: ", description)

description1 = do_it()
print("Today's weather: ", description1)
