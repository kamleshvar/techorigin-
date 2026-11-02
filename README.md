# TechOrigin — Company Portfolio

A complete, responsive company portfolio for **TechOrigin**, a technology and software development company founded by **Kamleshvar GV** and **M. Annamalai**.

The site is built with Flask, handwritten HTML/CSS and lightweight vanilla JavaScript. It is a separate project and does not modify the existing personal portfolio.

## Project structure

```text
techorigin/
├── app.py
├── requirements.txt
├── README.md
├── templates/
│   ├── base.html
│   ├── index.html
│   └── 404.html
└── static/
    ├── css/
    │   └── style.css
    ├── js/
    │   └── main.js
    └── images/
        ├── founders/
        │   ├── img.png
        │   └── annamalai.jpg
        ├── companies/
        │   └── bridgethegap.png
        └── logo/
            ├── techorigin-logo.png
            ├── techorigin-logo-transparent.png
            ├── techorigin-mark.png
            └── techorigin-og.png
```

## Run locally

```bash
cd techorigin
pip install -r requirements.txt
python app.py
```

Open <http://127.0.0.1:5000>.

`SITE_URL` can be set as an environment variable for canonical and social URLs. It defaults to `https://techorigin.online`.

## Routes

| Route | Purpose |
| --- | --- |
| `/` | TechOrigin home page |
| Any missing route | Custom 404 page |

## Image sources

All founder photographs and logos are sourced from the existing portfolio assets:

- Founder — `Kamleshvar GV`: provided photograph `img.png` → `techorigin/static/images/founders/img.png`
- Co-founder — `M. Annamalai`: `portfolio/static/images/founders/annamalai/web/img.jpg` → `techorigin/static/images/founders/annamalai.jpg`
- TechOrigin wordmark: `portfolio/static/images/techorigin comapny/TechOrigin Gradient Tech Logo.png` → `techorigin/static/images/logo/techorigin-logo.png` (and a transparent version for the dark navigation)
- TechOrigin symbol: `portfolio/static/images/techorigin comapny/TO short logo.png` → `techorigin/static/images/logo/techorigin-mark.png`
- Bridge the Gap Robotics: `portfolio/static/images/companies/bridgethegap.png` → `techorigin/static/images/companies/bridgethegap.png`

The `og` image was composed from the original TechOrigin wordmark for social sharing previews.

## Sections

- Hero with a deployment-console visual and capability marquee
- About TechOrigin with working principles
- Founder and co-founder profile cards
- Vision and mission
- Eight capability cards
- Per-founder technology stacks with a shared foundation
- Infrastructure and Cloudflare architecture diagram
- Bridge the Gap Robotics roles
- Contact section with separate founder and co-founder panels
- Footer with dynamic copyright year

## Features

- Responsive desktop, tablet and mobile layouts
- Sticky glass navigation with active section tracking
- Mobile navigation with keyboard and backdrop dismissal
- Scroll-triggered reveal animations
- Subtle hero pointer tilt
- Scroll progress indicator
- Reduced-motion support
- Custom 404 and 500 handling
- Semantic HTML, skip link, focus styles and accessible labels
- Organization and website structured data

## Dependencies

- Flask 3.1+

## Notes

- The contact section uses the founder's provided GitHub, email, Instagram and website links. Co-founder contact details are intentionally shown as non-clickable placeholders and are not invented.
- Founder and co-founder contact data is defined in `app.py` for easy editing.
- No contact submission backend is implemented, and the site does not claim that a form works.
- No customer numbers, testimonials, awards or certifications are fabricated.
- Infrastructure capabilities are presented as hands-on technical experience, not service guarantees.


## Visual refinement

The stylesheet has been refined toward a more restrained, editorial company-site aesthetic:
- reduced decorative gradients, glow and glass effects
- more neutral dark surfaces and softer accent colours
- smaller corner radii and quieter shadows
- a simpler hero treatment while retaining the interactive terminal
- reduced decorative motion and improved reduced-motion handling

The Flask routes, page content, project records, founder details and terminal JavaScript were preserved.
