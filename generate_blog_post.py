#!/usr/bin/env python3
"""
Script: generate_blog_post.py
Description: Convert a Markdown file with metadata to a styled HTML blog post for your site.
Usage: python3 generate_blog_post.py my-new-post.md
"""
import sys
import os
import re
import markdown
from datetime import datetime

# --- Blog post HTML template (edit as needed) ---
BLOG_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Andrew Ondara Blog</title>
    <meta name="description" content="{excerpt}">
    <link rel="stylesheet" href="../style.css">
    <link rel="icon" type="image/png" href="../favicon.png">
</head>
<body>
    <div class="container">
        <header class="header">
            <div class="header-content">
                <h1 class="name">{title}</h1>
                <p class="title">{date}</p>
                <div class="blog-post-categories">
                    {category_tags}
                </div>
            </div>
        </header>
        <main class="main">
            <article class="blog-post">
                {content}
            </article>
        </main>
        <footer class="footer">
            <div class="footer-content">
                <div class="social-links">
                    <a href="https://github.com/AndrewOOndara" target="_blank" aria-label="GitHub">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg>
                    </a>
                    <a href="https://www.linkedin.com/in/andrewondara/" target="_blank" aria-label="LinkedIn">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
                    </a>
                    <a href="mailto:a.ondara14@gmail.com" aria-label="Email">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
                    </a>
                </div>
                <p class="footer-text">© 2024 Andrew Ondara. Built with ❤️</p>
                <a href="../" class="back-home">← Back to Home</a>
            </div>
        </footer>
    </div>
</body>
</html>
'''

# --- Helper functions ---
def slugify(title):
    """Convert a title to a URL-friendly slug."""
    return re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')

def parse_metadata(md_text):
    """Extract metadata (YAML front matter style) and content from Markdown text."""
    # Look for YAML front matter
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)', md_text, re.DOTALL)
    if match:
        import yaml
        meta = yaml.safe_load(match.group(1))
        content = match.group(2)
        return meta, content
    # Fallback: look for simple comments
    meta = {}
    lines = md_text.splitlines()
    content_start = 0
    for i, line in enumerate(lines):
        if line.startswith('Title:'):
            meta['title'] = line.split(':',1)[1].strip()
        elif line.startswith('Date:'):
            meta['date'] = line.split(':',1)[1].strip()
        elif line.startswith('Categories:'):
            meta['categories'] = [c.strip() for c in line.split(':',1)[1].split(',')]
        elif line.strip() == '':
            content_start = i+1
            break
    content = '\n'.join(lines[content_start:])
    return meta, content

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 generate_blog_post.py my-new-post.md")
        sys.exit(1)
    md_path = sys.argv[1]
    if not os.path.isfile(md_path):
        print(f"File not found: {md_path}")
        sys.exit(1)
    with open(md_path, 'r', encoding='utf-8') as f:
        md_text = f.read()
    meta, md_content = parse_metadata(md_text)
    # Required fields
    title = meta.get('title') or 'Untitled Post'
    date = meta.get('date') or datetime.now().strftime('%Y-%m-%d')
    categories = meta.get('categories') or ['General']
    excerpt = md_content.strip().split('\n')[0][:150]  # First line as excerpt
    # Convert Markdown to HTML
    html_content = markdown.markdown(md_content, extensions=['fenced_code', 'codehilite'])
    # Category tags HTML
    category_tags = ''.join(f'<span class="category-tag">{c}</span>' for c in categories)
    # Fill template
    html = BLOG_TEMPLATE.format(
        title=title,
        date=date,
        category_tags=category_tags,
        content=html_content,
        excerpt=excerpt
    )
    # Output path
    slug = slugify(title)
    out_path = os.path.join('blog', f'{slug}.html')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'✅ Blog post generated: {out_path}')

if __name__ == '__main__':
    main() 