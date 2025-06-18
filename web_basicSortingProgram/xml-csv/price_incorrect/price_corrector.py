import re

# program to automatically rewrite all incorrect parts
with open("price_incorrect.xml", "r", encoding="utf-8") as file:
    xml_content = file.read()

corrected_content = re.sub(r"<symbol>(.*?)<symbol>", r"<symbol>\1</symbol>", xml_content)

with open("price.xml", "w", encoding="utf-8") as file:
    file.write(corrected_content)

print("program run sucessfully.")