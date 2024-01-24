import yaml
import csv
import urllib.request

# Get YAML file
url = 'https://github.com/cncf/landscape/raw/master/landscape.yml'
destination = 'input.yaml'
urllib.request.urlretrieve(url, destination)

# Open the YAML file
with open('input.yaml') as f:

    # Load YAML data
    data = yaml.safe_load(f)

# Specify the CSV file path
csv_file_path = 'output.csv'

# Open the CSV file for writing
with open(csv_file_path, 'w', newline='') as csvfile:
    # Define the CSV header
    fieldnames = ['Name', 'Homepage URL', 'Repo URL', 'Project Status', 'Logo', 'Twitter', 'Crunchbase', 'Date Joined', 'Extra']
    
    # Create the CSV writer
    csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    # Write the header to the CSV file
    csv_writer.writeheader()
    
    # Iterate through the data and write rows to the CSV file
    for category in data['landscape']:
        for subcategory in category['subcategories']:
            for item in subcategory['items']:
                csv_writer.writerow({
                    'Name': item['name'],
                    'Homepage URL': item['homepage_url'],
                    'Repo URL': item.get('repo_url', ''),
                    'Logo': item.get('logo', ''),
                    'Twitter': item.get('twitter', ''),
                    'Crunchbase': item.get('crunchbase', ''),
                    'Project Status': item.get('project', ''),
                    'Date Joined': item.get('joined', ''),
                    'Extra': item.get('extra', '')
                })

print(f'CSV file "{csv_file_path}" created successfully.')
