import yaml
import csv

# Open the YAML file
with open('landscape.yml') as f:

    # Load YAML data
    data = yaml.safe_load(f)

# Specify the CSV file path
csv_file_path = 'output.csv'

# Open the CSV file for writing
with open(csv_file_path, 'w', newline='') as csvfile:
    # Define the CSV header
    fieldnames = ['name', 'homepage_url', 'repo_url', 'logo', 'twitter', 'crunchbase']
    
    # Create the CSV writer
    csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    # Write the header to the CSV file
    csv_writer.writeheader()
    
    # Iterate through the data and write rows to the CSV file
    for category in data['landscape']:
        for subcategory in category['subcategories']:
            for item in subcategory['items']:
                csv_writer.writerow({
                    'name': item['name'],
                    'homepage_url': item['homepage_url'],
                    'repo_url': item.get('repo_url', ''),
                    'logo': item.get('logo', ''),
                    'twitter': item.get('twitter', ''),
                    'crunchbase': item.get('crunchbase', '')
                })

print(f'CSV file "{csv_file_path}" created successfully.')
