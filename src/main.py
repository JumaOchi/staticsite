import os
import shutil
from markdown_to_htmlnode import markdown_to_html_node
import sys


def delete_contents(directory):
    """Deletes all files and folders inside the given directory, but keeps the directory itself."""
    if os.path.exists(directory):
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            if os.path.isdir(item_path):  
                shutil.rmtree(item_path)  # Remove entire folder
            else:  
                os.remove(item_path)  # Remove individual file


def copy_static_files_to_public(src, dest):
    """Recursively copy files and directories from src to dest"""
    if not os.path.exists(dest):
        os.mkdir(dest)  # Create destination directory if it doesn’t exist

    for item in os.listdir(src):  # List all files/folders inside src
        src_path = os.path.join(src, item)  # Full path in source
        dest_path = os.path.join(dest, item)  # Full path in destination

        if os.path.isdir(src_path):  # If it's a directory
            os.mkdir(dest_path)  # Create the same directory in destination
            copy_static_files_to_public(src_path, dest_path)  # Recursive call
        elif os.path.isfile(src_path):  # Check if it's a file before copying
            shutil.copy(src_path, dest_path)  # Copy the file
        #logging the files copied
        print(f"Copied {src_path} to {dest_path}")


def extract_title(markdown):
    """Extracts the title from the markdown file."""
    title = None
    for line in markdown.split("\n"):
        if line.startswith("# "):
            title = line.lstrip("# ").strip()
            break
        else : raise Exception("Title not found")
    return title

def generate_page(from_path, template_path, dest_path, basepath="/"):
    """Generates a new HTML page from a markdown file and a template."""
    with open(from_path, "r") as file:
        markdown = file.read()

    title = extract_title(markdown)
    html_node = markdown_to_html_node(markdown)

    with open(template_path, "r") as file:
        template = file.read()

    html = template.replace("{{title}}", title).replace("{{content}}", html_node.to_html())
    # Replace href and src to include basepath
    if basepath == "/":
        html.replace('href="/', 'href="').replace('src="/', 'src="')
    else:
        html = html.replace('href="/', f'href="{basepath.rstrip('/')}/').replace('src="/', f'src="{basepath.rstrip('/')}/')



    # Convert `.md` to `.html`
    if dest_path.endswith(".md"):
        dest_path = dest_path[:-3] + ".html"

    # Ensure the parent directory exists
    # Ensure the parent directory exists
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w") as file:
        file.write(html)
    
    print(f"Generated {dest_path}")


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath="/"):
    """Generates HTML pages for all markdown files in the given directory and subdirectories."""
    for item in os.listdir(dir_path_content):
        item_path = os.path.join(dir_path_content, item)
        dest_path = os.path.join(dest_dir_path, item)  

        if os.path.isdir(item_path):
            os.makedirs(dest_path, exist_ok=True)  # Ensure directories exist
            generate_pages_recursive(item_path, template_path, dest_path, basepath)
        elif item.endswith(".md"):
            generate_page(item_path, template_path, dest_path, basepath)  # `generate_page` handles .html conversion


def main():
    
    public_dir = "docs/"
    static_dir = "static/"

    delete_contents(public_dir)  # Clean ../public
    copy_static_files_to_public(static_dir, public_dir)  # Copy ../static -> ../public
    print("Static files Copy complete! Public directory  updated.")
    
    dir_path_content = "content/"
    template_path = "template.html"
    dest_dir_path = public_dir

    # Get the basepath from CLI, default to "/"
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    print(f"Using basepath: {basepath}")

    generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath)
    print("Index pages generated!")


if __name__ == "__main__":
    main()
