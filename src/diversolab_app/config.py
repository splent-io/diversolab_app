"""
Configuration for diversolab_app.

Each class extends the framework's base configuration. Only override
what your product needs — everything else is inherited automatically.
"""

from splent_framework.configuration.default_config import (
    DevelopmentConfig as BaseDev,
    TestingConfig as BaseTest,
    ProductionConfig as BaseProd,
)


class _SiteConfig:
    """Site-level configuration for DIVERSO LAB — consumed by the theme."""

    SITE_NAME = "DIVERSO LAB"
    SITE_TAGLINE = (
        "International computing research — developing technology to transform Andalucía."
    )
    SITE_NAV = [
        {"label": "Projects", "href": "/projects"},
        {"label": "Tools", "href": "/tools"},
        {"label": "Team", "href": "/team"},
    ]
    SITE_SOCIAL = [
        {"network": "GitHub", "href": "https://github.com/diverso-lab"},
        {"network": "Web", "href": "https://diversolab.us.es"},
    ]
    SITE_LOGO = "img/diverso-logo.png"
    SITE_HERO_EYEBROW = "Universidad de Sevilla · ETSII · Research group PRISMA (TIC-276)"
    SITE_HERO_ACTIONS = [
        {"label": "Our projects", "href": "/projects"},
        {"label": "Our tools", "href": "/tools", "class": "btn-ghost"},
    ]
    SITE_HIGHLIGHTS_TITLE = "Areas of expertise"
    SITE_HIGHLIGHTS = [
        {"icon": "🧩", "title": "Software Engineering",
         "text": "Variability-intensive systems, software product lines and automated analysis."},
        {"icon": "🤖", "title": "Artificial Intelligence",
         "text": "AI applied to software engineering and data-intensive systems."},
        {"icon": "🧠", "title": "Computational Thinking",
         "text": "Research and teaching on computational thinking."},
    ]
    SITE_SPONSORS_TITLE = "Funding & partners"
    SITE_SPONSORS = [
        "Universidad de Sevilla", "Junta de Andalucía",
        "Ministerio de Ciencia e Innovación", "ERDF / FEDER", "PRISMA · TIC-276",
    ]
    SITE_CTA = {
        "title": "Interested in our research?",
        "text": "Reach out — we collaborate on variability, AI and software engineering.",
        "button": "Meet the team",
        "href": "/team",
    }

    # i18n (native Flask-Babel support)
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_SUPPORTED_LOCALES = ["en", "es"]

    # Team section/role types and their order — declared per product.
    TEAM_GROUPS = [
        "Faculty",
        "PhD & Master Students",
        "Active Collaborators",
        "Technical Staff",
        "Former Members & Collaborators",
    ]


class DevelopmentConfig(_SiteConfig, BaseDev):
    pass


class TestingConfig(_SiteConfig, BaseTest):
    pass


class ProductionConfig(_SiteConfig, BaseProd):
    pass
