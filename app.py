"""TechOrigin company portfolio.

A single-page Flask site for TechOrigin, a technology and software
development company founded by Kamleshvar GV and M. Annamalai.
"""

from __future__ import annotations

import os
from datetime import datetime

from flask import Flask, render_template

app = Flask(__name__)
app.config.update(
    SITE_URL=os.environ.get("SITE_URL", "https://techorigin.online").rstrip("/"),
)

FOUNDER_EMAIL = "kamleshvarproject5@gmail.com"

FOUNDER = {
    "name": "Kamleshvar GV",
    "role": "Founder",
    "image": "images/founders/img.png",
    "image_width": 1400,
    "image_height": 786,
    "description": (
        "Founder of TechOrigin, working across full-stack development, "
        "cloud infrastructure and practical digital products."
    ),
    "email": FOUNDER_EMAIL,
    "github": "https://github.com/kamleshvar",
    "website": "https://kamleshvar.online",
    "instagram": [
        "https://instagram.com/kamleshvar0209",
        "https://instagram.com/kamleshvar2009",
    ],
    "contacts": [
        {
            "label": "GitHub",
            "value": "kamleshvar",
            "href": "https://github.com/kamleshvar",
            "icon": "github",
            "external": True,
        },
        {
            "label": "Email",
            "value": FOUNDER_EMAIL,
            "href": f"mailto:{FOUNDER_EMAIL}",
            "icon": "mail",
            "external": False,
        },
        {
            "label": "Instagram — Main",
            "value": "@kamleshvar0209",
            "href": "https://instagram.com/kamleshvar0209",
            "icon": "instagram",
            "external": True,
        },
        {
            "label": "Instagram — Secondary",
            "value": "@kamleshvar2009",
            "href": "https://instagram.com/kamleshvar2009",
            "icon": "instagram",
            "external": True,
        },
        {
            "label": "Personal Website",
            "value": "kamleshvar.online",
            "href": "https://kamleshvar.online",
            "icon": "globe",
            "external": True,
        },
    ],
    "foot_label": "Direct contact",
    "foot_note": "Direct lines to the founder.",
}

COFOUNDER = {
    "name": "M. Annamalai",
    "role": "Co-Founder",
    "image": "images/founders/annamalai.jpg",
    "image_width": 892,
    "image_height": 1200,
    "description": (
        "Co-Founder of TechOrigin, contributing to full-stack development "
        "and collaborative digital projects."
    ),
    "contacts": [
        {"label": "GitHub", "value": "Details to be added", "href": None, "icon": "github", "external": False},
        {"label": "Email", "value": "Details to be added", "href": None, "icon": "mail", "external": False},
        {"label": "Instagram", "value": "Details to be added", "href": None, "icon": "instagram", "external": False},
        {"label": "Website", "value": "Details to be added", "href": None, "icon": "globe", "external": False},
    ],
    "foot_label": "Contact details",
    "foot_note": "Will be added when available.",
}

PROJECTS = [
    {
        "number": "01",
        "slug": "erp",
        "name": "GV POWERS ERP",
        "category": "Business Management Software",
        "completed": "August 2026",
        "developer": "Kamleshvar GV",
        "developer_image": "images/founders/img.png",
        "url": "https://gvpowers.in",
        "description": (
            "A business ERP software project developed to support business "
            "operations through an integrated digital management system."
        ),
        "tags": ["Business Management Software", "ERP"],
        "image": "images/projects/erp-gvpowers.jpg",
        "image_alt": "GV POWERS ERP sign-in interface",
        "terminal_summary": (
            "An integrated ERP system built for GV POWERS to support business "
            "operations through a dedicated software platform."
        ),
        "terminal_highlights": [],
    },
    {
        "number": "02",
        "slug": "friendshare",
        "name": "Friendshare",
        "category": "Software Development",
        "completed": "September 2026",
        "developer": "Annamalai M",
        "developer_image": "images/founders/annamalai.jpg",
        "url": "https://friendshare.techorigin.online",
        "description": (
            "A document-sharing platform for study groups and friend circles, "
            "with private vault circles, subject-organised study rooms and "
            "built-in file conversion."
        ),
        "tags": ["Software Development", "Document Sharing", "Study Collaboration"],
        "image": "images/projects/friendshare.jpg",
        "image_alt": "Friendshare homepage interface",
        "terminal_summary": (
            "A document-sharing platform for study groups and friend circles."
        ),
        "terminal_highlights": [
            "Private vault circles for trusted groups.",
            "BTW study rooms with auto-organised subject folders.",
            "Built-in converter for PDF, DOCX, TXT, Markdown, CSV and images.",
            "Friend network and OTP-based account verification.",
        ],
    },
    {
        "number": "03",
        "slug": "timetable",
        "name": "Student Timetable Generator",
        "category": "Student Productivity",
        "completed": "October 2026",
        "developer": "Kamleshvar GV",
        "developer_image": "images/founders/img.png",
        "url": "https://tt.techorigin.online",
        "description": (
            "A personalised timetable-generation application for Class 12 "
            "students that organises study time around school, tuition, rest "
            "and daily routines, with a dedicated final 30-day revision schedule."
        ),
        "tags": ["Student Productivity", "Class 12", "Study Planning"],
        "image": "images/projects/timetable.jpg",
        "image_alt": "Student Timetable Generator sign-in interface",
        "terminal_summary": (
            "A personalised timetable generator for Class 12 students."
        ),
        "terminal_highlights": [
            "Collects wake-up, sleep, school and tuition timings.",
            "Generates a study plan around fixed daily commitments.",
            "Includes a 30-minute refreshments and break allowance.",
            "Switches to a dedicated final 30-day revision schedule.",
        ],
    },
]

ROADMAP = [
    {
        "date": "May 2026",
        "date_short": "May",
        "kind": "learning",
        "icon": "cloud",
        "status": "Completed",
        "title": "Learning Cloudflare Technology",
        "description": (
            "Started exploring and practising Cloudflare technologies, "
            "understanding how modern websites and applications can be "
            "connected, protected and managed through cloud infrastructure."
        ),
        "activities": [
            "Practising Cloudflare configuration.",
            "Exploring DNS management.",
            "Understanding domain and subdomain routing.",
            "Learning how Cloudflare supports web infrastructure.",
        ],
        "details": [],
    },
    {
        "date": "June 2026",
        "date_short": "June",
        "kind": "infrastructure",
        "icon": "server",
        "status": "Completed",
        "title": "Cloud Server Infrastructure",
        "description": (
            "Moved from learning cloud technologies to working with cloud "
            "server infrastructure, establishing the technical foundation for "
            "hosting and managing applications."
        ),
        "activities": [
            "Setting up a cloud server.",
            "Exploring server administration.",
            "Preparing application hosting environments.",
            "Learning deployment and infrastructure management.",
        ],
        "details": [],
    },
    {
        "date": "August 2026",
        "date_short": "August",
        "kind": "company",
        "icon": "building",
        "status": "Completed",
        "title": "TechOrigin Begins",
        "description": (
            "TechOrigin was started in August 2026 with the goal of building "
            "practical software solutions and developing modern digital products."
        ),
        "activities": [
            "Establishing the TechOrigin identity.",
            "Bringing together the founding team.",
            "Beginning software development projects.",
            "Turning technical ideas into working applications.",
        ],
        "details": [],
    },
    {
        "date": "August 2026",
        "date_short": "August",
        "kind": "project",
        "icon": "code",
        "status": "Completed",
        "title": "GV POWERS ERP Software",
        "description": (
            "Developed the first major TechOrigin project: an ERP software "
            "solution for GV POWERS, designed to support business operations "
            "through a dedicated software system."
        ),
        "activities": [],
        "details": [
            {"label": "Project", "value": "ERP Software for GV POWERS"},
            {
                "label": "Website",
                "value": "gvpowers.in",
                "href": "https://gvpowers.in",
            },
            {"label": "Completed", "value": "August 2026"},
            {"label": "Developer", "value": "Kamleshvar GV"},
            {"label": "Project number", "value": "01"},
        ],
    },
    {
        "date": "September 2026",
        "date_short": "September",
        "kind": "project",
        "icon": "share",
        "status": "Completed",
        "title": "Friendshare",
        "description": (
            "Friendshare is a document-sharing platform developed by Annamalai M "
            "for study groups and friend circles, with vault circles, "
            "subject-organised study rooms and built-in file conversion."
        ),
        "activities": [],
        "details": [
            {"label": "Project", "value": "Friendshare"},
            {
                "label": "Website",
                "value": "friendshare.techorigin.online",
                "href": "https://friendshare.techorigin.online",
            },
            {"label": "Completed", "value": "September 2026"},
            {"label": "Developer", "value": "Annamalai M"},
            {"label": "Project number", "value": "02"},
        ],
    },
    {
        "date": "October 2026",
        "date_short": "October",
        "kind": "project",
        "icon": "calendar",
        "status": "Completed",
        "title": "Student Timetable Generator",
        "description": (
            "Developed a timetable-generation application designed to help "
            "Class 12 students organise their daily routines, balance academic "
            "responsibilities and prepare for examinations."
        ),
        "activities": [],
        "details": [
            {"label": "Project", "value": "Student Timetable Generator"},
            {
                "label": "Website",
                "value": "tt.techorigin.online",
                "href": "https://tt.techorigin.online",
            },
            {"label": "Completed", "value": "October 2026"},
            {"label": "Developer", "value": "Kamleshvar GV"},
            {"label": "Target users", "value": "Class 12 students"},
            {"label": "Project number", "value": "03"},
        ],
    },
]

CORE_POSITIONING = "Global-quality technology. Affordable pricing. Built for everyone."

CORE_PHILOSOPHY = [
    (
        "Technology should not be a luxury available only to large corporations. "
        "Students, educational institutions, small businesses, startups and "
        "independent developers should all have access to powerful, reliable and "
        "modern software at affordable prices."
    ),
    (
        "TechOrigin aims to bridge this gap by developing practical digital "
        "products, accessible software solutions and reliable technology "
        "infrastructure."
    ),
    (
        "Our ambition is to build an ecosystem where technology is powerful, "
        "pricing is transparent and innovation is accessible to everyone."
    ),
]

TARGET_MARKETS = [
    {
        "index": "01",
        "name": "Students & Education",
        "icon": "graduation",
        "accent": "edu",
        "audiences": [
            "School students",
            "College students",
            "Educational institutions",
            "Teachers and educators",
        ],
        "solutions": [
            "Timetable and study planner applications.",
            "Student productivity tools.",
            "School and college management software.",
            "Learning management platforms.",
            "Examination and assessment systems.",
            "Attendance and assignment management.",
            "Affordable student subscriptions.",
        ],
        "goal": (
            "Make quality educational technology accessible to students and "
            "institutions, without unnecessarily expensive software subscriptions."
        ),
    },
    {
        "index": "02",
        "name": "Businesses & Institutions",
        "icon": "building",
        "accent": "business",
        "audiences": [
            "Small businesses",
            "Medium-sized businesses",
            "Schools and colleges",
            "Startups",
            "Growing organisations",
        ],
        "solutions": [
            "ERP and business management systems.",
            "Billing and invoicing software.",
            "Inventory management.",
            "Customer relationship management (CRM).",
            "Business automation.",
            "Financial and operational reporting.",
            "Custom software development.",
            "Server and infrastructure setup.",
        ],
        "goal": (
            "Provide professional business software with flexible pricing, "
            "modular features and affordable implementation."
        ),
    },
    {
        "index": "03",
        "name": "Developers & Startups",
        "icon": "code",
        "accent": "dev",
        "audiences": [
            "Independent developers",
            "Freelancers",
            "Software development teams",
            "Startups",
            "Technology enthusiasts",
        ],
        "solutions": [
            "Affordable hosting and deployment.",
            "Developer platforms.",
            "API and integration services.",
            "Database management tools.",
            "Project deployment utilities.",
            "Cloud server management.",
            "Development productivity tools.",
        ],
        "goal": (
            "Make software development, deployment and infrastructure more "
            "accessible to independent developers and growing startups."
        ),
    },
]

PRODUCT_DIVISIONS = [
    {
        "number": "01",
        "name": "TechOrigin Edu",
        "icon": "graduation",
        "badge": "High Priority",
        "badge_kind": "success",
        "accent": "edu",
        "summary": (
            "An educational technology ecosystem for students, schools and colleges."
        ),
        "items": [
            "Student timetable generator.",
            "Personal study planner.",
            "Attendance management.",
            "Assignment management.",
            "Examination management.",
            "School and college dashboards.",
            "Learning and productivity tools.",
        ],
        "goal": (
            "Create an integrated education platform that helps students manage "
            "their academic lives and enables institutions to manage their "
            "operations efficiently."
        ),
        "image": "images/projects/timetable.jpg",
        "image_alt": "Student Timetable Generator interface",
    },
    {
        "number": "02",
        "name": "TechOrigin Business",
        "icon": "building",
        "badge": "High Priority",
        "badge_kind": "success",
        "accent": "business",
        "summary": (
            "Affordable business software for small and medium-sized businesses."
        ),
        "items": [
            "ERP systems.",
            "Billing and invoicing.",
            "Inventory management.",
            "Customer relationship management.",
            "Employee management.",
            "Financial reporting.",
            "Business automation.",
        ],
        "goal": (
            "Provide modular business management software that organisations can "
            "adopt without the high implementation and licensing costs associated "
            "with traditional enterprise solutions."
        ),
        "image": "images/projects/erp-gvpowers.jpg",
        "image_alt": "GV POWERS ERP sign-in interface",
    },
    {
        "number": "03",
        "name": "TechOrigin Deploy",
        "icon": "server",
        "badge": "Strategic Opportunity",
        "badge_kind": "info",
        "accent": "deploy",
        "summary": "A developer-friendly deployment and infrastructure platform.",
        "items": [
            "Application hosting.",
            "Project deployment.",
            "Domain and subdomain management.",
            "Cloudflare integration.",
            "Server resource management.",
            "Application monitoring.",
            "Database management.",
            "Backup and deployment tools.",
        ],
        "goal": (
            "Simplify application deployment and infrastructure management for "
            "developers and startups."
        ),
        "image": None,
        "image_alt": None,
    },
    {
        "number": "04",
        "name": "TechOrigin AI",
        "icon": "spark",
        "badge": "Future Development",
        "badge_kind": "discovery",
        "accent": "ai",
        "summary": "An AI-powered technology division.",
        "items": [
            "AI-powered productivity tools.",
            "Business process automation.",
            "Document processing.",
            "Intelligent assistants.",
            "Data analysis tools.",
            "AI integrations for existing products.",
            "Workflow automation.",
        ],
        "goal": (
            "Integrate useful AI capabilities into real-world software products "
            "to improve productivity and reduce repetitive work."
        ),
        "image": None,
        "image_alt": None,
    },
    {
        "number": "05",
        "name": "TechOrigin Developer Tools",
        "icon": "terminal",
        "badge": "Future Development",
        "badge_kind": "info",
        "accent": "tools",
        "summary": (
            "A collection of tools and services for independent developers and "
            "development teams."
        ),
        "items": [
            "APIs and integrations.",
            "Database utilities.",
            "Developer dashboards.",
            "Project management utilities.",
            "Testing and debugging tools.",
            "Documentation tools.",
            "Affordable development resources.",
        ],
        "goal": (
            "Build an ecosystem that helps developers create, manage and deploy "
            "applications more efficiently."
        ),
        "image": None,
        "image_alt": None,
    },
]

FUTURE_ROADMAP = [
    {
        "year": "2026",
        "status": "Foundation Year",
        "state": "foundation",
        "theme": "Establishing the foundation.",
        "priorities": [
            "Establish the TechOrigin company identity.",
            "Build the founding team's technical capabilities.",
            "Develop the first software products.",
            "Establish cloud server infrastructure.",
            "Explore Cloudflare technologies and application deployment.",
            "Develop solutions for students and businesses.",
            "Build an initial product portfolio.",
        ],
        "focus": "Establish a strong technical and operational foundation.",
    },
    {
        "year": "2027",
        "status": "Planned",
        "state": "planned",
        "theme": "Turning projects into products.",
        "priorities": [
            "Expand TechOrigin Edu.",
            "Develop reusable ERP and business management software.",
            "Improve the Student Timetable Generator.",
            "Explore affordable developer hosting services.",
            "Begin developing TechOrigin Deploy.",
            "Improve product documentation and support.",
            "Introduce clear pricing plans.",
            "Build reusable software modules.",
        ],
        "focus": "Transform individual projects into structured, maintainable products.",
    },
    {
        "year": "2028",
        "status": "Planned",
        "state": "planned",
        "theme": "Building connected products.",
        "priorities": [
            "Develop an integrated TechOrigin product ecosystem.",
            "Expand educational software solutions.",
            "Introduce additional business management modules.",
            "Develop APIs and software integrations.",
            "Explore AI-powered applications.",
            "Introduce automation capabilities.",
            "Explore partnerships with educational institutions.",
            "Build a developer and user community.",
        ],
        "focus": "Connect products, services and infrastructure into a unified ecosystem.",
    },
    {
        "year": "2029",
        "status": "Planned",
        "state": "planned",
        "theme": "Reaching more customers.",
        "priorities": [
            "Expand beyond the initial Indian market.",
            "Explore international customers and opportunities.",
            "Improve software scalability and reliability.",
            "Explore multi-region hosting where commercially feasible.",
            "Develop international-ready product experiences.",
            "Expand institutional and business partnerships.",
            "Strengthen technical support and documentation.",
            "Build a broader technology community.",
        ],
        "focus": "Make TechOrigin products accessible to customers beyond the initial market.",
    },
    {
        "year": "2030",
        "status": "Long-Term Vision",
        "state": "vision",
        "theme": "Making technology accessible to everyone.",
        "priorities": [
            "Build a recognised affordable software ecosystem.",
            "Expand the TechOrigin Edu product family.",
            "Grow TechOrigin Business solutions.",
            "Strengthen developer infrastructure products.",
            "Expand useful AI-powered services.",
            "Develop scalable products for global users.",
            "Continue investing in product quality and accessibility.",
            "Build a sustainable technology company.",
        ],
        "focus": (
            "Become a technology company known for delivering professional, "
            "reliable and affordable digital solutions."
        ),
    },
]

PRICING_SEGMENTS = [
    {
        "name": "Students",
        "icon": "graduation",
        "accent": "edu",
        "items": [
            "Free or affordable entry-level plans.",
            "Student-friendly subscriptions.",
            "Essential features without unnecessary complexity.",
            "Affordable upgrades.",
        ],
    },
    {
        "name": "Schools & Colleges",
        "icon": "building",
        "accent": "business",
        "items": [
            "Flexible institutional licensing.",
            "Pricing based on institution requirements.",
            "Modular feature selection.",
            "Affordable deployment and support packages.",
        ],
    },
    {
        "name": "Small Businesses",
        "icon": "briefcase",
        "accent": "small",
        "items": [
            "Affordable monthly and yearly plans.",
            "Essential ERP and billing features.",
            "Modular upgrades.",
            "Transparent pricing.",
        ],
    },
    {
        "name": "Medium Businesses",
        "icon": "layers",
        "accent": "medium",
        "items": [
            "Customisable software packages.",
            "Additional modules as required.",
            "Flexible deployment options.",
            "Scalable infrastructure.",
        ],
    },
    {
        "name": "Developers & Startups",
        "icon": "code",
        "accent": "dev",
        "items": [
            "Low-cost entry-level hosting.",
            "Flexible resource-based pricing.",
            "Affordable deployment tools.",
            "Developer-friendly plans.",
        ],
    },
]

PRICING_PRINCIPLES = [
    "Transparent pricing.",
    "No unnecessary enterprise-level complexity.",
    "Flexible plans for different customer sizes.",
    "Essential features at accessible prices.",
    "Scalable upgrades as customers grow.",
    "Value-driven software development.",
]

GLOBAL_PILLARS = [
    {
        "name": "Accessibility",
        "icon": "globe",
        "text": "Technology that more people can afford.",
    },
    {
        "name": "Scalability",
        "icon": "layers",
        "text": "Products designed to grow with their users.",
    },
    {
        "name": "Innovation",
        "icon": "spark",
        "text": "Continuously improving through engineering and research.",
    },
]

GROWTH_PILLARS = [
    {
        "name": "Product-led Growth",
        "icon": "spark",
        "text": (
            "Build useful software products that solve real problems and improve "
            "through customer feedback."
        ),
    },
    {
        "name": "Affordable Technology",
        "icon": "tag",
        "text": (
            "Keep products accessible through efficient development, flexible "
            "plans and modular software."
        ),
    },
    {
        "name": "Infrastructure & Reliability",
        "icon": "server",
        "text": (
            "Invest in deployment, security, server management, backups and "
            "application performance."
        ),
    },
    {
        "name": "Community & Partnerships",
        "icon": "users",
        "text": (
            "Build relationships with students, developers, educational "
            "institutions and businesses."
        ),
    },
]

TERMINAL_PUBLIC_DATA = {
    "projects": [
        {
            "number": project["number"],
            "slug": project["slug"],
            "name": project["name"],
            "category": project["category"],
            "completed": project["completed"],
            "developer": project["developer"],
            "url": project["url"],
            "summary": project["terminal_summary"],
            "highlights": project["terminal_highlights"],
        }
        for project in PROJECTS
    ],
    "founder": {
        "name": FOUNDER["name"],
        "role": FOUNDER["role"],
        "email": FOUNDER["email"],
        "github": FOUNDER["github"],
        "website": FOUNDER["website"],
        "instagram": FOUNDER["instagram"],
    },
    "cofounder": {
        "name": COFOUNDER["name"],
        "role": COFOUNDER["role"],
    },
    "positioning": CORE_POSITIONING,
    "website": "https://techorigin.online",
    "skills": [
        "Python",
        "JavaScript",
        "HTML",
        "CSS",
        "SQL",
        "Flask",
        "Cloudflare",
        "Cloud server infrastructure",
    ],
}

INDEX_CONTEXT = {
    "founder": FOUNDER,
    "cofounder": COFOUNDER,
    "projects": PROJECTS,
    "journey": ROADMAP,
    "core_positioning": CORE_POSITIONING,
    "core_philosophy": CORE_PHILOSOPHY,
    "target_markets": TARGET_MARKETS,
    "product_divisions": PRODUCT_DIVISIONS,
    "future_roadmap": FUTURE_ROADMAP,
    "pricing_segments": PRICING_SEGMENTS,
    "pricing_principles": PRICING_PRINCIPLES,
    "global_pillars": GLOBAL_PILLARS,
    "growth_pillars": GROWTH_PILLARS,
    "terminal_data": TERMINAL_PUBLIC_DATA,
}


@app.context_processor
def inject_globals() -> dict[str, object]:
    """Expose values every template needs."""
    return {
        "current_year": datetime.now().year,
        "site_url": app.config["SITE_URL"],
    }


@app.get("/")
def index():
    """Render the TechOrigin home page."""
    return render_template("index.html", **INDEX_CONTEXT)


@app.errorhandler(404)
def page_not_found(_error):
    return render_template("404.html", error_code=404), 404


@app.errorhandler(500)
def internal_error(_error):
    return render_template("404.html", error_code=500), 500


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
