import os

def update_links(file_path, old_domain, new_domain):
    with open(file_path, 'r') as file:
        content = file.read()

    content = content.replace(old_domain, new_domain)

    with open(file_path, 'w') as file:
        file.write(content)

old_domain = 'https://www.austintexas.gov'
new_domain = 'https://apl-innovation-lab.github.io/AACHF'

for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.html'):
            update_links(os.path.join(root, file), old_domain, new_domain)
