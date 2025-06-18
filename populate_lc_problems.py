from leetscrape import GetQuestion
from bs4 import BeautifulSoup
import re
import os

file_path = 'lc_list.txt'

output_dir = './problems'
solutions_dir = './solutions'


os.makedirs(output_dir, exist_ok=True)

with open(file_path, 'r') as file:
    lines = file.readlines()

for line in lines:
    slug, qid = line.strip().split(',')
    
    try:

        file_name = f"lc_{int(qid):04d}.py"
        file_path = os.path.join(output_dir, file_name)
        solution_path = os.path.join(solutions_dir, file_name)

        if(os.path.exists(solution_path)):
            print(f"skipping {qid} solution exists")
            continue

        if(os.path.exists(file_path)):
            print(f"skipping {qid} blank exists")
            continue

        print(f"Scraping question: {slug} (ID: {qid})")
        question = GetQuestion(titleSlug=slug).scrape()

        with open(file_path, 'w') as f:
            f.write(f"# {question.QID}. {question.title}\n\n")
            soup = BeautifulSoup(question.Body, 'html.parser')
            body_plaintext = soup.get_text(separator=" ", strip=True)



            # Print the body_plaintext for debugging
            # print("Original Body (plaintext):")
            # print(body_plaintext)


            # Handle the "Example" lines separately to prevent duplication
            body_plaintext = re.sub(r'(Example \d+:)', r'\n\1', body_plaintext)

            # Now split by periods followed by a space and a capital letter
            body_plaintext = re.sub(r'(?<=\.)\s+(?=[A-Z])', r'\n', body_plaintext)

            # Ensure we preserve any lines that begin with "Example"
            body_plaintext = re.sub(r'(?<=\n)(Example \d+:)', r'\n\1', body_plaintext)

            # Print the modified body for debugging
            # print("Modified Body (after regex):")
            # print(body_plaintext)

            # Split the body into lines after the replacements
            sentences = body_plaintext.split("\n")




            # f.write(f"# {question.Body}\n\n")  # Problem body
            # f.write(f"# {body_plaintext}\n\n")  # Problem body in plain text

            for sentence in sentences:
                if sentence.strip():  # Avoid writing empty lines
                    f.write(f"# {sentence.strip()}\n")
            f.write("\n")  # Add a newline between the description and the code stub

            
            f.write(f"{question.Code}")
            f.write(f"return\n")

            
        # print(f"Scraped question: {slug} saved as {file_name}!")

    except Exception as e:
        print(f"Error scraping question {qid}: {e}")
