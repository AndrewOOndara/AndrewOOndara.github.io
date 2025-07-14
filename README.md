# Andrew Ondara - Portfolio Website

A minimalistic, modern portfolio website built with vanilla HTML, CSS, and JavaScript. Features a clean, art portfolio-style design with dark/light mode toggle, blog functionality, and Spotify integration.

## 🌟 Features

- **Minimalistic Design**: Clean, whitespace-heavy layout with elegant typography
- **Dark/Light Mode**: Toggle between themes with persistent preferences
- **Responsive**: Fully mobile-friendly and responsive design
- **Blog Support**: Simple blog system with markdown-style content
- **Spotify Integration**: Embedded Spotify player for "Now Playing" section
- **Fast Performance**: Vanilla technologies for optimal loading speeds
- **Accessible**: Semantic HTML and proper ARIA labels

## 📁 File Structure

```
├── index.html              # Main portfolio page
├── style.css               # Main stylesheet with CSS variables
├── script.js               # JavaScript functionality
├── favicon.png             # Site favicon
├── README.md               # This file
├── blog/                   # Blog directory
│   ├── index.html          # Blog listing page
│   ├── building-minimalistic-portfolio.html
│   ├── software-engineering-journey.html
│   └── clean-code-principles.html
└── images/                 # Image assets (existing)
```

## 🚀 Deployment

### GitHub Pages (Recommended)

1. Push your code to a GitHub repository
2. Go to repository Settings → Pages
3. Select source branch (usually `main` or `master`)
4. Your site will be available at `https://username.github.io/repository-name`

### Local Development

1. Clone the repository
2. Open `index.html` in your browser
3. Or use a local server:
   ```bash
   # Using Python
   python -m http.server 8000
   
   # Using Node.js
   npx serve .
   ```

## 🎨 Customization

### Colors and Themes

The site uses CSS custom properties for easy theming. Edit the variables in `style.css`:

```css
:root {
    --bg-primary: #ffffff;
    --text-primary: #1a1a1a;
    --accent-color: #3b82f6;
    /* ... more variables */
}
```

### Adding Blog Posts

1. Create a new HTML file in the `blog/` directory
2. Use the existing blog post template structure
3. Update the posts array in `script.js` to include your new post
4. Add the post to the blog index page

### Updating Content

- **About Section**: Edit the content in `index.html`
- **Projects**: Update the project cards in the projects section
- **Work Experience**: Modify the timeline items
- **Spotify Player**: Replace the iframe src with your preferred playlist

## 🛠️ Technologies Used

- **HTML5**: Semantic markup
- **CSS3**: Modern features (Grid, Flexbox, Custom Properties)
- **Vanilla JavaScript**: No frameworks, clean code
- **Inter Font**: Modern, readable typography
- **Spotify Embed**: For music integration

## 📱 Responsive Design

The site is built with a mobile-first approach and includes breakpoints for:
- Mobile: < 480px
- Tablet: 480px - 768px
- Desktop: > 768px

## 🔧 Performance Optimizations

- Minimal JavaScript bundle
- Optimized CSS with efficient selectors
- Lazy loading for non-critical resources
- Semantic HTML for better SEO
- Fast loading times with vanilla technologies

## 🎯 Future Enhancements

- [ ] Add search functionality to blog
- [ ] Implement proper markdown parsing
- [ ] Add analytics integration
- [ ] Optimize images with WebP format
- [ ] Add RSS feed for blog
- [ ] Implement comment system

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Feel free to fork this project and customize it for your own portfolio. If you find any bugs or have suggestions, please open an issue.

## 📞 Contact

- **Email**: aoo4@rice.edu
- **LinkedIn**: [Andrew Ondara](https://www.linkedin.com/in/andrewondara/)
- **GitHub**: [AndrewOOndara](https://github.com/AndrewOOndara)

---

Built with ❤️ by Andrew Ondara 