// Theme management
class ThemeManager {
    constructor() {
        this.theme = localStorage.getItem('theme') || 'light';
        this.init();
    }

    init() {
        document.documentElement.setAttribute('data-theme', this.theme);
        this.setupToggle();
    }

    setupToggle() {
        const toggle = document.getElementById('theme-toggle');
        if (toggle) {
            toggle.addEventListener('click', () => this.toggleTheme());
        }
    }

    toggleTheme() {
        this.theme = this.theme === 'light' ? 'dark' : 'light';
        document.documentElement.setAttribute('data-theme', this.theme);
        localStorage.setItem('theme', this.theme);
    }
}

// Blog post management
class BlogManager {
    constructor() {
        this.posts = [];
        this.init();
    }

    async init() {
        await this.loadPosts();
        this.displayRecentPosts();
    }

    async loadPosts() {
        try {
            // For now, we'll use sample data
            // In a real implementation, you'd fetch from a JSON file or API
            this.posts = [
                {
                    title: "Building a Minimalistic Portfolio",
                    date: "2024-01-15",
                    excerpt: "How I designed and built this portfolio website using vanilla HTML, CSS, and JavaScript with a focus on minimalism and performance.",
                    slug: "building-minimalistic-portfolio",
                    categories: ["Web Development", "Design", "Portfolio"]
                },
                {
                    title: "My Journey in Software Engineering",
                    date: "2024-01-10",
                    excerpt: "Reflections on my path from Rice University to becoming a software engineer, including key learnings and experiences.",
                    slug: "software-engineering-journey",
                    categories: ["Career", "Education", "Personal"]
                },
                {
                    title: "The Art of Clean Code",
                    date: "2024-01-05",
                    excerpt: "Principles and practices I follow to write maintainable, readable, and efficient code in my projects.",
                    slug: "clean-code-principles",
                    categories: ["Programming", "Best Practices", "Code Quality"]
                }
            ];
        } catch (error) {
            console.error('Error loading blog posts:', error);
            this.posts = [];
        }
    }

    displayRecentPosts() {
        const container = document.getElementById('blog-posts');
        if (!container) return;

        const recentPosts = this.posts.slice(0, 3);
        
        if (recentPosts.length === 0) {
            container.innerHTML = '<p class="loading">No posts available yet.</p>';
            return;
        }

        const postsHTML = recentPosts.map(post => `
            <article class="blog-post">
                <h3 class="blog-post-title">
                    <a href="blog/${post.slug}.html" style="color: inherit; text-decoration: none;">
                        ${post.title}
                    </a>
                </h3>
                <p class="blog-post-date">${this.formatDate(post.date)}</p>
                <p class="blog-post-excerpt">${post.excerpt}</p>
                <div class="blog-post-categories">
                    ${post.categories.map(category => `<span class="category-tag">${category}</span>`).join('')}
                </div>
            </article>
        `).join('');

        container.innerHTML = postsHTML;
    }

    formatDate(dateString) {
        const date = new Date(dateString);
        return date.toLocaleDateString('en-US', {
            year: 'numeric',
            month: 'long',
            day: 'numeric'
        });
    }
}

// Smooth scrolling
class SmoothScroller {
    constructor() {
        this.init();
    }

    init() {
        // Smooth scrolling is handled by CSS scroll-behavior: smooth
        // Additional smooth scrolling for anchor links if needed
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        });
    }
}

// Initialize everything when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new ThemeManager();
    new BlogManager();
    new SmoothScroller();
});

// Add some interactive features
document.addEventListener('DOMContentLoaded', () => {
    // Add hover effects for project cards
    const projectCards = document.querySelectorAll('.project-card');
    projectCards.forEach(card => {
        card.addEventListener('mouseenter', () => {
            card.style.transform = 'translateY(-4px)';
        });
        
        card.addEventListener('mouseleave', () => {
            card.style.transform = 'translateY(0)';
        });
    });

    // Add loading animation for blog posts
    const blogPosts = document.getElementById('blog-posts');
    if (blogPosts) {
        blogPosts.style.opacity = '0';
        setTimeout(() => {
            blogPosts.style.transition = 'opacity 0.5s ease';
            blogPosts.style.opacity = '1';
        }, 100);
    }
}); 