"""Site content: specialties, projects and shared copy.

Projects are defined once and listed by id on each specialty page, so a
project can appear under more than one specialty without duplicated text.
Text fields may contain inline HTML. Wrap owner-review notes in
<!--REVIEW--> ... <!--/REVIEW--> so the published build drops them.
"""

SITE_URL = "https://ameshack.github.io/amward-site/"
LINKEDIN = "https://www.linkedin.com/in/am-ward"

SPECIALTIES = {
    "brand": {
        "slug": "brand",
        "name": "Brand",
        "card": "Brand strategy, customer insight, integrated campaigns and creative direction.",
        "intro": "I translate customer insight into brand strategy, creative direction and integrated campaigns that build recognition and motivate action.",
        "capabilities": [
            "Brand strategy &amp; governance",
            "Customer research &amp; positioning",
            "Integrated campaigns &amp; creative leadership",
        ],
        "featured": ["delta-campaign", "reuse-sf", "sf-climate-action"],
        "supporting": [],
        "card_visual": {"img": "reuse.jpg", "alt": "REUSE SF campaign creative"},
        "title": "Brand strategy and campaigns",
        "description": "Brand strategy, customer research, integrated campaigns and creative direction by A.M. Ward, with work for Delta Air Lines and the City & County of San Francisco.",
    },
    "product-marketing": {
        "slug": "product-marketing",
        "name": "Product Marketing",
        "card": "Positioning, go-to-market strategy, product adoption and commercial growth.",
        "card_visual": {"img": "sfrecycles.jpg", "alt": "SF Recycles mobile web app", "phone": True},
        "title": "Product marketing",
        "description": "Product marketing by A.M. Ward: positioning, go-to-market strategy, adoption and growth.",
    },
    "communications": {
        "slug": "communications",
        "name": "Internal &amp; Executive Communications",
        "short": "Communications",
        "card": "Executive communications, organizational change and employee engagement.",
        "card_visual": {"img": "year-end-wrap-up.jpg", "alt": "", "position": "center 58%"},
        "title": "Internal and executive communications",
        "description": "Internal and executive communications by A.M. Ward: executive voice, change and AI adoption, and employee engagement.",
    },
    "leadership": {
        "slug": "leadership",
        "name": "Leadership &amp; Operations",
        "short": "Leadership",
        "card": "Team leadership, organizational strategy, resource allocation and operational excellence.",
        "card_visual": {"img": "strategic-plan.jpg", "alt": ""},
        "title": "Leadership and operations",
        "description": "Leadership and operations by A.M. Ward: executive partnership, team and agency leadership, and marketing operations.",
    },
}

PROJECTS = {
    "delta-campaign": {
        "org": "Delta Air Lines",
        "title": "National brand campaign",
        "image": {"src": "delta-ad.jpg", "w": 1100, "h": 612,
                  "alt": "Closing frame of the Delta ad: Keep Climbing, Delta and SkyTeam logos, Learn more at delta.com/sustainability"},
        "outcome": ("#1", "Delta ad for brand difference and affinity"),
        "challenge": "Stand out with consumers nationally and deepen their affinity for the Delta brand.",
        "role": "Led strategy and execution, from consumer research through agency direction, paid media and measurement.",
        "details": [
            ("Strategy and my role",
             "<p>Led strategy and execution for a national omnichannel campaign, translating consumer research into creative briefs and agency direction.</p>"),
            ("Research",
             "<p>Led multiphase qualitative and quantitative consumer research and competitive analysis informing messaging, creative briefs and content strategy.</p>"),
            ("Execution",
             "<p>Directed agency coordination, paid-media investment, measurement and reporting.</p>"),
            ("Result",
             "<p>The #1 Delta ad for brand difference and affinity.</p>"),
        ],
        "links": [("Watch the Delta ad", "https://www.facebook.com/watch/?v=248379818072591")],
    },
    "reuse-sf": {
        "org": "City &amp; County of San Francisco",
        "title": "REUSE SF",
        "image": {"src": "reuse.jpg", "w": 1100, "h": 558,
                  "alt": "REUSE SF campaign creative: a model in yellow reclining with a reusable tote of produce"},
        "outcome": ("+51%", "intent to reuse, reported by the agency partner"),
        "challenge": "Persuade residents to choose reusable bags, cups and utensils over disposable ones.",
        "role": "Commissioned and directed the campaign, leading the agency, creative vendors and contractors.",
        "details": [
            ("Strategy and my role",
             "<p>Commissioned and directed a fashion-inspired campaign encouraging residents to choose reusable bags, cups and utensils over disposable alternatives. Led the agency, creative vendors and contractors across integrated advertising and community activations.</p>"),
            ("Execution",
             "<p>Combined advertising, professional-photo pop-ups, reusable giveaways, a pledge website and geotargeted digital promotion that drove attendance at neighborhood activations. Culturally relevant creative reached Spanish- and Chinese-speaking, lower-income and older residents.</p>"),
            ("Results",
             "<ul><li>+51% intent to reuse</li><li>Video engagement at 7× benchmark</li><li>Thousands of pledges and 4,000+ participant photos shared on social media</li><li>2022 ADDY Award, Public Service Campaign</li></ul>"
             "<p class=\"fine\">Campaign-level results reported by the agency partner. The 51% measures intent to reuse, not verified behavior.</p>"),
        ],
        "links": [("View the REUSE SF campaign", "https://www.reuse-sf.org/")],
    },
    "greener-life": {
        "org": "Southern Company · Georgia Natural Gas",
        "title": "Subscription growth and lifecycle strategy",
        "image": {"src": "greener-life.jpg", "w": 1100, "h": 363,
                  "alt": "Georgia Natural Gas Greener Life banner: A greener Georgia is on our minds"},
        "outcome": ("+11%", "subscribers in three months"),
        "challenge": "",
        "role": "Set vision, strategy and goals for a subscription product and co-developed an integrated acquisition campaign tied to a new feature and milestone.",
        "details": [],
        "links": [],
    },
    "delta-suitcase": {
        "org": "Delta Air Lines",
        "title": "Consumer product positioning and commercialization",
        "image": {"src": "delta-suitcase.jpg", "w": 1110, "h": 419, "focus": "left",
                  "alt": "Delta web feature: Suitcases made from Delta jets, showing the aluminum suitcase prototype"},
        "outcome": ("", "First-in-kind consumer product strategy and go-to-market planning"),
        "challenge": "",
        "role": "Co-led development of a first-in-kind consumer product, an upcycled suitcase made from retired aircraft skin.",
        "details": [],
        "links": [],
    },
    "sf-climate-action": {
        "org": "City &amp; County of San Francisco",
        "title": "SF Climate Action brand system",
        "image": {"src": "climate-action-month.jpg", "w": 714, "h": 720, "focus": "top",
                  "alt": "Climate Action Month creative: Be the change in climate change, over the Golden Gate Bridge in fog"},
        "outcome": ("+51%", "year-over-year web visits during the fourth annual Climate Action Month"),
        "challenge": "Bring the city’s environmental services and climate goals together under one coherent brand.",
        "role": "Expanded the city’s climate identity into a brand system and created Climate Action Month.",
        "details": [
            ("Strategy and my role",
             "<p>Expanded the city’s “0/80/100/Roots” climate identity into a brand system connecting program identities, digital experiences, community outreach and executive communications. Established naming and messaging governance for new products and citywide initiatives.</p>"),
            ("Climate Action Month",
             "<p>Created Climate Action Month, an annual citywide initiative that extended the brand through an integrated partner strategy.</p>"),
            ("Results",
             "<p>Web visits increased 51% year over year during the fourth annual Climate Action Month.</p>"),
        ],
        "links": [],
    },
}

PROOF_POINTS = [
    ("#1", "Delta Air Lines ad for brand difference and affinity", "Delta Air Lines"),
    ("+11%", "subscribers in three months; $1.7M projected customer lifetime value", "Southern Company"),
    ("+495%", "year-over-year monthly active users for a civic app", "City &amp; County of San Francisco"),
    ("+88%", "year-over-year employee understanding of mission and values (relative increase, annual survey)", "City &amp; County of San Francisco"),
]

RECENT_WORK = [
    "Google",
    "Microsoft",
    "Delta Air Lines",
    "Southern Company",
]
