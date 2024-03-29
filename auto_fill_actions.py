import yaml,random

def generate_default_responses():
    list_text = [{'- text': 'Alright, I will take care of that.'},{'- text': "I'm currently processing your request."},{'- text':"I'm looking for the answer, I will reply to you as soon as possible"}]
    text = random.choice(list_text)
    return text

def auto_fill_actions(stories_file, domain_file):
    # Load stories.yml
    with open(stories_file, 'r', encoding='utf-8') as f:
        stories_data = yaml.safe_load(f)

    # Load domain.yml
    with open(domain_file, 'r', encoding='utf-8') as f:
        domain_data = yaml.safe_load(f)

    # Extract actions from stories.yml
    actions = set()
    for story in stories_data.get('stories', []):
        for step in story.get('steps', []):
            if 'action' in step:
                actions.add(step['action'])

    # Update responses in domain.yml
    for action in actions:
        if action not in domain_data['responses']:
            domain_data['responses'][action] = generate_default_responses()

    # Write updated domain.yml
    with open(domain_file, 'w') as f:
        yaml.dump(domain_data, f, default_flow_style=False)

# Usage example
auto_fill_actions('data/stories.yml', 'domain.yml')
