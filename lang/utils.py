from bs4 import BeautifulSoup, NavigableString

def mark_text_for_translation(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    def mark_text_nodes(element):
        for idx, child in enumerate(element.children):
            if isinstance(child, NavigableString):
                original_text = child.strip()
                if original_text and not has_trans_tag(element):
                    new_tag = soup.new_tag('span')
                    new_tag.string = f'{{% trans "{original_text}" %}}'
                    element.insert(idx, new_tag)
                    child.extract()
            elif hasattr(child, 'children'):
                mark_text_nodes(child)
            elif child.name in ['script', 'style']:
                continue
            elif child.name == 'form':
                continue
            elif child.name == 'input':
                continue
            elif child.name == 'textarea':
                continue
            elif child.name == 'select':
                continue

    def has_trans_tag(element):
        return '{% trans' in str(element) or '{% blocktrans' in str(element)

    if soup.body:
        mark_text_nodes(soup.body)
    else:
        mark_text_nodes(soup)

    return str(soup)

def read_html_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def save_html_to_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
