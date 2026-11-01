# Bootstrap Theme Collection

A collection of **17 visual themes** for Bootstrap 5, with a live component gallery for comparing and gradually modernising each stylesheet. This is an evolving style laboratory rather than a production-ready design system.

> **Live preview:** [GitHub Pages](https://vgarcan.github.io/botstrap-css-styles/) — published directly from `main` via the existing GitHub Pages configuration.
> **Project setup:** [GitHub Pages guide](docs/GITHUB_PAGES.md) · [Modernisation plan](docs/MODERNIZATION.md).

## 🎨 Available Themes

### **Modern**

#### 1. **Modern Gradient**
- **Style**: Modern gradients with glassmorphism effects
- **Colours**: Blues and purples with transparencies
- **Features**: Floating animations, glow effects, backdrop-filter
- **Ideal for**: Tech startups, SaaS applications, creative portfolios

#### 2. **Glassmorphism Pro**
- **Style**: Advanced glass and blur effects
- **Colours**: Transparencies with purple accents
- **Features**: Intense backdrop-filter, border morphism, shimmer effects
- **Ideal for**: Premium apps, futuristic interfaces, modern dashboards

#### 3. **Neumorphism Soft**
- **Style**: Soft design with realistic shadows
- **Colours**: Neutral greys with subtle gradients
- **Features**: Inner/outer shadows, pressure effects, smooth animations
- **Ideal for**: Mobile applications, touch interfaces, minimalist designs

### **Futuristic**

#### 4. **Cyberpunk Neon**
- **Style**: Futuristic aesthetic with neon effects
- **Colours**: Cyan, magenta, neon green on dark background
- **Features**: Neon flicker, glitch effects, scanlines, monospace typography
- **Ideal for**: Gaming, tech, futuristic applications, developer portfolios

#### 5. **Retrowave Synthwave**
- **Style**: Authentic 80s retrowave aesthetic
- **Colours**: Hot pink, electric blue, sunset gradients
- **Features**: Grid patterns, sunset effects, nostalgic vibes
- **Ideal for**: Music apps, creative portfolios, entertainment sites

### **Corporate**

#### 6. **Corporate Tech**
- **Style**: Clean, geometric, efficient
- **Colours**: Professional blues and greys
- **Features**: Minimal shadows, precise typography, subtle animations
- **Ideal for**: Technology companies, software platforms, B2B applications

#### 7. **Corporate Finance**
- **Style**: Conservative, reliable, premium
- **Colours**: Navy blues and gold accents
- **Features**: Professional typography, subtle shadows, trustworthy design
- **Ideal for**: Banking, finance, investment platforms

#### 8. **Corporate Legal**
- **Style**: Formal, traditional, authoritative
- **Colours**: Charcoal, burgundy, professional greys
- **Features**: Serif typography, formal layouts, conservative design
- **Ideal for**: Law firms, legal services, professional consultancy

#### 9. **Corporate Medical**
- **Style**: Clean, reliable, calming
- **Colours**: Medical blues and clean whites
- **Features**: Gentle animations, accessible design, trustworthy aesthetics
- **Ideal for**: Healthcare, pharmaceutical, medical services

### **Classic**

#### 10. **Minimalist Clean**
- **Style**: Clean and professional design
- **Colours**: Greys, subtle blues, lots of white space
- **Features**: Smooth transitions, subtle shadows, clear typography
- **Ideal for**: Corporate applications, dashboards, professional sites

#### 11. **Retro Vintage**
- **Style**: Nostalgia with vintage textures
- **Colours**: Browns, golds, creams with paper textures
- **Features**: Old paper effects, serif typography, decorative borders
- **Ideal for**: Historical sites, artistic portfolios, literary blogs

#### 12. **Art Deco Luxury**
- **Style**: Classic elegance with golden touches
- **Colours**: Black, gold, cream with geometric patterns
- **Features**: Art Deco patterns, shimmer effects, elegant typography
- **Ideal for**: Luxury sites, jewellery, premium hotels, exclusive events

### **Premium**

#### 13. **WWE Raw Elegant**
- **Style**: Premium metallic with red and gold
- **Colours**: Black, red, gold with metallic gradients
- **Features**: Metallic shine, elegant animations, premium feel
- **Ideal for**: Entertainment, premium brands, exclusive content

#### 14. **WWE SmackDown Chrome**
- **Style**: Chrome and steel aesthetic
- **Colours**: Blue, silver, chrome with metallic effects
- **Features**: Chrome reflections, steel textures, tech aesthetics
- **Ideal for**: Technology, automotive, industrial design

### **Children's**

#### 15. **Kids Friendly**
- **Style**: Soft, calming, safe for children (ages 3-8)
- **Colours**: Soft pastels - sky blue, soft pink, mint green, sunny yellow
- **Features**: Gentle animations, large rounded buttons, emoji decorations, Comic Sans typography
- **Ideal for**: Educational apps, children's websites, family services, learning platforms

#### 16. **Kids Vibrant Playground**
- **Style**: Energetic, vibrant, playful (ages 3-8)
- **Colours**: Electric blue, hot pink, lime green, bright orange, purple pop
- **Features**: Playful bounces, rainbow gradients, sparkle effects, Fredoka One typography
- **Ideal for**: Interactive games, playground apps, entertainment for children, activity platforms

### **Experimental**

#### 17. **Brutalist Bold**
- **Style**: Bold and uncompromising design
- **Colours**: Intense primary colours (yellow, red, blue, black)
- **Features**: Thick borders, hard shadows, bold typography, shake effects
- **Ideal for**: Digital art, experimental portfolios, impact sites

## 🚀 Installation and Usage

### Basic Installation

1. **Include Bootstrap 5 in your project:**
```html
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
```

2. **Add your desired theme after Bootstrap:**
```html
<!-- Example: Modern Gradient -->
<link rel="stylesheet" href="themes/modern-gradient.css">
```

3. **Include recommended fonts:**
```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Orbitron:wght@400;700;900&family=Poppins:wght@300;400;500;600;700&family=Playfair+Display:wght@400;700;900&family=Crimson+Text:wght@400;600&display=swap" rel="stylesheet">
```

### Dynamic Theme Switching

To enable dynamic theme switching:

```html
<!-- Default theme -->
<link id="theme-css" rel="stylesheet" href="themes/modern-gradient.css">

<script>
function changeTheme(themeName) {
    document.getElementById('theme-css').href = `themes/${themeName}.css`;
}
</script>
```

## 📁 Project Structure

```
/
├── themes/
│   ├── modern-gradient.css         # Modern gradients
│   ├── glassmorphism-pro.css       # Advanced glass effects
│   ├── cyberpunk-neon.css          # Futuristic cyberpunk aesthetic
│   ├── neumorphism-soft.css        # Soft realistic shadows
│   ├── minimalist-clean.css        # Clean professional design
│   ├── retro-vintage.css           # Nostalgic vintage style
│   ├── art-deco-luxury.css         # Art Deco elegance
│   ├── brutalist-bold.css          # Bold experimental design
│   ├── corporate-tech.css          # Technology corporate style
│   ├── corporate-finance.css       # Finance industry style
│   ├── corporate-legal.css         # Legal profession style
│   ├── corporate-medical.css       # Healthcare industry style
│   ├── retrowave-synthwave.css     # 80s retrowave aesthetic
│   ├── wwe-raw-elegant.css         # Premium red and gold
│   ├── wwe-smackdown-chrome.css    # Chrome and steel blue
│   ├── kids-friendly.css           # Soft children's theme
│   └── kids-vibrant-playground.css # Vibrant children's theme
├── index.html                      # Complete boilerplate with theme selector
├── docs/                           # Publishing and modernisation notes
└── README.md                       # Documentation
```

## 🎯 Technical Features

### Customisable CSS Variables
Each theme uses CSS variables that you can modify:

```css
/* Example: Modern Gradient */
:root {
  --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  --border-radius: 15px;
  --transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
}
```

### Unique Animations per Theme

**Modern Gradient:**
- `float`: Floating effect
- `glow`: Glow effect
- `slideInLeft`: Side entrance

**Glassmorphism Pro:**
- `floatGlass`: Floating with rotation
- `shimmer`: Shimmer effect
- `morphBorder`: Border morphism

**Cyberpunk Neon:**
- `neonFlicker`: Neon flicker
- `scanline`: Scan line
- `glitch`: Glitch effect
- `matrixRain`: Matrix rain

**Neumorphism Soft:**
- `neuPulse`: Soft pulsation
- `neuPress`: Pressure effect
- `neuFloat`: Neumorphic floating

**Brutalist Bold:**
- `brutalShake`: Intense vibration
- `brutalPop`: Visual explosion
- `brutalBlink`: Aggressive blinking

**Retrowave Synthwave:**
- `sunsetShimmer`: Sunset gradient animation
- `fadeInRetro`: Retro fade-in effect
- `scanlineSubtle`: Subtle scan line effect

**WWE Themes:**
- `chromeShine`: Metallic shine effect
- `elegantGlow`: Premium glow animation
- `steelFloat`: Industrial floating effect

**Kids Themes:**
- `gentleBounce`: Safe bouncing animation
- `playfulBounce`: Fun but controlled bounce
- `rainbowShimmer`: Rainbow text animation
- `colorShift`: Gentle hue rotation for special elements
- `sparkle`: Twinkling effect for decorative elements

### Theme-Specific Utility Classes

Each theme includes special classes:

```css
/* Modern Gradient */
.glass-effect, .animate-float, .animate-glow

/* Glassmorphism Pro */
.glass-light, .glass-heavy, .animate-morph

/* Cyberpunk Neon */
.neon-text, .glitch-effect, .matrix-bg

/* Neumorphism Soft */
.neu-pressed, .neu-raised, .animate-neu-pulse

/* Brutalist Bold */
.brutal-rotate-left, .brutal-shake, .brutal-blink

/* Retrowave Synthwave */
.retro-glow, .synthwave-text, .miami-gradient

/* WWE Raw Elegant */
.wwe-champion, .wwe-metal-shine, .wwe-elegant-float

/* WWE SmackDown Chrome */
.smackdown-chrome, .smackdown-steel-shine, .smackdown-glow

/* Kids Friendly */
.kids-rainbow-text, .kids-bounce, .kids-glow

/* Kids Vibrant Playground */
.kids-electric-text, .kids-magic-text, .playground-game
```

## 📱 Compatibility

- ✅ **Bootstrap 5.3.x** - Fully compatible
- ✅ **Modern Browsers** - Chrome, Firefox, Safari, Edge
- ✅ **Responsive Design** - Adaptable to all devices
- ✅ **Font Awesome 6.x** - Icons included
- ✅ **Google Fonts** - Optimised typography

## 🛠️ Advanced Customisation

### Change Primary Colours

```css
/* Override variables */
:root {
  --primary-color: #tu-color;
  --secondary-color: #tu-color;
}
```

### Modify Animations

```css
/* Speed up transitions */
:root {
  --transition: all 0.2s ease;
}

/* Disable animations */
* {
  animation: none !important;
}
```

### Create Variations

```css
/* Custom theme based on Modern Gradient */
.my-custom-card {
  background: var(--glass-primary);
  backdrop-filter: var(--blur-medium);
  /* Your modifications */
}
```

## 🎮 Interactive Demo

The boilerplate includes:

### **index.html - Complete Boilerplate:**
- **Real-time theme selector** with live preview
- **Comprehensive component library** - Navigation, forms, cards, tables, e-commerce
- **Dashboard components** - Stats cards, progress indicators, data tables
- **Professional layouts** - Hero sections, pricing cards, user management
- **Interactive elements** - Modals, offcanvas, accordions, carousels
- **Real theme downloads** - Fetch and download the actual selected CSS file
- **Theme persistence** - Remembers selected theme
- **Responsive design** - Optimised for all devices
- **Production-ready** - Professional components ready for use

### **Project documentation:**
- [GitHub Pages deployment and local preview](docs/GITHUB_PAGES.md)
- [Theme modernisation roadmap and acceptance criteria](docs/MODERNIZATION.md)

## 📊 Recommended Use Cases

| Theme | Best For | Industry |
|------|------------|-----------|
| Modern Gradient | SaaS Apps, Startups | Technology |
| Glassmorphism Pro | Premium Interfaces | Fintech, Luxury |
| Cyberpunk Neon | Gaming, Tech | Entertainment |
| Neumorphism Soft | Mobile Apps | Health, Wellness |
| Minimalist Clean | Dashboards | Corporate |
| Retro Vintage | Blogs, Portfolios | Art, Culture |
| Art Deco Luxury | Premium Sites | Luxury, Events |
| Brutalist Bold | Digital Art | Experimental |
| Corporate Tech | B2B Platforms | Technology |
| Corporate Finance | Banking Apps | Finance |
| Corporate Legal | Law Firms | Legal |
| Corporate Medical | Healthcare | Medical |
| Retrowave Synthwave | Music Apps | Entertainment |
| WWE Raw Elegant | Premium Brands | Entertainment |
| WWE SmackDown Chrome | Tech Products | Technology |
| Kids Friendly | Educational Apps | Children |
| Kids Vibrant Playground | Games | Children |

## 💾 Download System

### **Individual Theme Download:**
- Click **"Download [Theme Name]"** to get the current active theme
- Fetches the **actual CSS file** from `themes/` and uses a Blob for the browser download
- **No server required** - completely static
- **Instant download** with proper filename

### **Smart Button:**
- **Dynamic text** - Shows current theme name
- **Visual feedback** - Toast notifications for success/error
- **Future-proof** - Ready for full collection download feature

## 🤝 Contributing

Have ideas for new themes?

1. Fork the project
2. Create a new CSS file in `themes/`
3. Follow the existing variable structure
4. Include unique animations
5. Add documentation
6. Submit a Pull Request

## 📄 Licence

**MIT Licence** - Free use for personal and commercial projects.

## 🔗 Useful Links

- [Bootstrap 5 Documentation](https://getbootstrap.com/)
- [CSS Variables Guide](https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties)
- [Font Awesome Icons](https://fontawesome.com/)
- [Google Fonts](https://fonts.google.com/)
- [Marked.js Documentation](https://marked.js.org/) (for markdown parsing)

---

Enjoy creating incredible interfaces with this comprehensive Bootstrap theme collection! 🎨✨

**Need help?** Read the [Pages setup guide](docs/GITHUB_PAGES.md) or open an issue in the repository.