# Tolkien Fan Club - Static Site Generator

Welcome to the **Tolkien Fan Club** website! This project is a statically generated site powered by a custom-built Static Site Generator (SSG). The site celebrates J.R.R. Tolkien and his legendary works.

## 🌐 Live Demo
Check out the live site here: **[Tolkien Fan Club](https://jumaochi.github.io/staticsite/)**

---

##  About the Project
This project is a lightweight, markdown-based static site generator built in Python. It takes markdown files, processes them into HTML using a custom template, and outputs a fully static website.

###  Features
- Converts Markdown (`.md`) files into HTML.
- Supports hierarchical content structures.
- Includes automatic link generation and base path handling.
- Customizable templates for styling and layout.
- Compatible with GitHub Pages for easy deployment.

---

## 🚀 Getting Started
### 🔧 Prerequisites
Ensure you have **Python 3** installed on your machine.

### 🛠 Installation & Setup
Clone the repository:
```bash
git clone https://github.com/jumaochi/staticsite.git
cd staticsite
```

###  Local Development
To test the site locally before deploying:
```bash
chmod +x build.sh  # Make the script executable
./build.sh  # Build and serve the site
```
Then, open your browser and go to:
```
http://localhost:8888
```

###  Deploying to GitHub Pages
1. Push your changes to the `main` branch.
2. Ensure GitHub Pages is enabled in your repo settings.
3. The site will be available at:
   ```
   https://jumaochi.github.io/staticsite/
   ```

---

##  Basic Project Structure More files went into this such as tests
```
staticsite/
│── content/            # Markdown content files
│── static/             # Static assets (CSS, images, etc.)
│── template.html       # HTML template
│── docs/               # Generated site output (GitHub Pages deployment)
│── src/                # Static site generator script
│        
│── main.sh            # Build script
│── README.md           # Project documentation
```

---

## 🛠 Technologies Used
- **Python** for processing markdown and generating HTML
- **GitHub Pages** for hosting the site
- **Markdown** for content writing
- **Bash** Automation
---

##  Credits
Developed by **Juma Ochi** with a passion for static site generation.

If you like the project, feel free to star  the repo and contribute!

---

##  Contact
Got questions or suggestions? Reach out:
- GitHub: [jumaochi](https://github.com/jumaochi)
- Website: [jumaochi.github.io](https://jumaochi.github.io/juma.github.io/)

---

⚡ _“Not all those who wander are lost.” – J.R.R. Tolkien_ ⚡

