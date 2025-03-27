import os
import shutil
from markdown_to_htmlnode import markdown_to_html_node

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

def generate_page(from_path, template_path, dest_path) :
    """Generates a new HTML page from a markdown file and a template."""
    with open(from_path, "r") as file:
        markdown = file.read()
    title = extract_title(markdown)
    html_node = markdown_to_html_node(markdown)
    with open(template_path, "r") as file:
        template = file.read()
    html = template.replace("{{title}}", title).replace("{{content}}", html_node.to_html())
    with open(dest_path, "w") as file:
        file.write(html)
    print(f"Generated {dest_path}")

def main():
    public_dir = "public/"
    static_dir = "static/"

    delete_contents(public_dir)  # Clean ../public
    copy_static_files_to_public(static_dir, public_dir)  # Copy ../static -> ../public
    print("Static files Copy complete! Public directory  updated.")
    
    from_path = os.path.join("content", "index.md")
    template_path = "template.html"
    dest_path = os.path.join(public_dir, "index.html")
    generate_page(from_path, template_path, dest_path)
    print("Index page generated!")


if __name__ == "__main__":
    main()
