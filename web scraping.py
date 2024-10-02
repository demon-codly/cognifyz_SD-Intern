import requests
from bs4 import BeautifulSoup

# Step 1: Get the website URL from the user
def get_website_data():
    url = input("Enter the website URL: ")
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the website: {e}")
        return None

# Step 2: Scrape data from the website
def scrape_website(html_content, tag, class_name=None):
    soup = BeautifulSoup(html_content, 'html.parser')
    if class_name:
        elements = soup.find_all(tag, class_=class_name)
    else:
        elements = soup.find_all(tag)
    
    return elements

# Step 3: Present data in a user-friendly format
def present_data(elements):
    if not elements:
        print("No data found.")
        return

    print("\nScraped Data:")
    for idx, element in enumerate(elements, start=1):
        # We get the text from the HTML element and strip extra spaces
        print(f"{idx}. {element.get_text(strip=True)}")

# Step 4: Main function to test the program
def main():
    # Get website content
    html_content = get_website_data()
    if not html_content:
        return

    # Ask user what tag and (optionally) class they want to scrape
    tag = input("Enter the HTML tag you want to scrape (e.g., h2, p, div): ")
    class_name = input("Enter the class name (if applicable, otherwise press Enter): ").strip() or None

    # Scrape the website
    elements = scrape_website(html_content, tag, class_name)

    # Present the data
    present_data(elements)

# Run the scraper
if __name__ == "__main__":
    main()
