"""Site content: specialties, projects, experience and credentials.

Projects are defined once and listed by id on each specialty page, so a
project can appear under more than one specialty without duplicated text.
Text fields may contain inline HTML; link to another page with
href="@slug/#anchor" and the build fills in the right relative path. Wrap owner-review notes in
<!--REVIEW--> ... <!--/REVIEW--> so the published build drops them.

Project fields: org, program (optional), title, image (optional; "layout":
"wide" stacks it above the text, "phone" frames a tall screenshot),
outcome (figure, label; an empty figure shows the label as a mandate),
challenge, role, details [(heading, html)], links [(label, url)].
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
        "projects": ["delta-campaign", "reuse-sf", "sf-climate-action"],
        "card_visual": {"img": "reuse.jpg"},
        "title": "Brand strategy and campaigns",
        "description": "Brand strategy, customer research, integrated campaigns and creative direction by Asia Meshack, with work for Delta Air Lines and the City & County of San Francisco.",
    },
    "product-marketing": {
        "slug": "product-marketing",
        "name": "Product Marketing",
        "card": "Positioning, go-to-market strategy, product adoption and commercial growth.",
        "intro": "I turn customer and competitive insight into product positioning, go-to-market strategies and scalable marketing capabilities that drive acquisition, adoption and growth.",
        "capabilities": [
            "Customer &amp; competitive insight",
            "Positioning &amp; go to market",
            "Acquisition, lifecycle &amp; enablement",
        ],
        "projects": ["sf-recycles", "cam-portal", "greener-life", "delta-suitcase"],
        # In reserve; add back to "projects" to publish: "rethink-disposable"
        "card_visual": {"img": "sfrecycles.jpg", "phone": True},
        "title": "Product marketing",
        "description": "Product marketing by Asia Meshack: positioning, go-to-market strategy, product adoption and growth, with work for Southern Company, Delta Air Lines and the City & County of San Francisco.",
    },
    "communications": {
        "slug": "communications",
        "name": "Internal &amp; Executive Communications",
        "short": "Communications",
        "card": "Executive communications, organizational change and employee engagement.",
        "intro": "I help leaders communicate strategy and change clearly, and help employees understand priorities and take action.",
        "capabilities": [
            "Executive voice &amp; counsel",
            "Change &amp; AI adoption",
            "Employee engagement &amp; measurement",
        ],
        "projects": ["microsoft-exec", "sf-internal-comms", "new-resource-bank"],
        # In reserve; add back to "projects" to publish: "microsoft-holiday"
        "card_visual": {"img": "year-end-wrap-up.jpg", "position": "center 52%"},
        "title": "Internal and executive communications",
        "description": "Internal and executive communications by Asia Meshack: executive voice, change and AI adoption, and employee engagement, with work for Microsoft and the City & County of San Francisco.",
    },
    "leadership": {
        "slug": "leadership",
        "name": "Leadership &amp; Operations",
        "short": "Leadership",
        "card": "Team leadership, organizational strategy, resource allocation and operational excellence.",
        "intro": "I build the strategy, teams and operating processes that help organizations deliver, including identifying where AI can improve workflows, developing practical tools and evaluating their effectiveness.",
        "capabilities": [
            "Executive partnership &amp; planning",
            "Team &amp; agency leadership",
            "Marketing operations &amp; change",
            "AI integration &amp; workflow development",
        ],
        "projects": ["executive-partnership", "team-leadership", "salesforce"],
        "card_visual": {"img": "strategic-plan.jpg"},
        "title": "Leadership and operations",
        "description": "Leadership and operations by Asia Meshack: executive partnership and planning, team and agency leadership, and marketing operations.",
    },
}

SF = "City &amp; County of San Francisco"

PROJECTS = {
    # ---------- Brand
    "delta-campaign": {
        "org": "Delta Air Lines", "program": "Sustainability brand campaign",
        "title": "National brand campaign",
        "image": {"src": "delta-ad.jpg", "w": 1100, "h": 612, "layout": "wide",
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
        "org": SF, "program": "REUSE SF",
        "title": "Integrated brand campaign and audience engagement",
        "image": {"src": "reuse.jpg", "w": 1100, "h": 558, "layout": "wide",
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
    "sf-climate-action": {
        "org": SF, "program": "SF Climate Action",
        "title": "Brand architecture and governance",
        "image": {"src": "climate-action-booth.jpg", "w": 1100, "h": 937,
                  "alt": "San Francisco Environment staff at a community outreach table branded with the San Francisco Climate Action 0 80 100 Roots identity"},
        "outcome": ("", "A unified climate brand system, and the citywide initiative built on it"),
        "challenge": "Bring the city’s environmental services and climate goals together under one coherent brand.",
        "role": "Expanded the city’s climate identity into a brand system, set its governance and created Climate Action Month to extend it.",
        "details": [
            ("Strategy and my role",
             "<p>Expanded the city’s “0/80/100/Roots” climate identity into a brand system connecting program identities, digital experiences, community outreach and executive communications. Established naming and messaging governance for new products and citywide initiatives.</p>"),
            ("Extending the brand",
             "<p>Created <a href=\"@product-marketing/#cam-portal\">Climate Action Month</a>, an annual citywide initiative that carried the brand to residents through an integrated partner strategy and a multilingual event-discovery experience.</p>"),
            ("Citywide context",
             "<ul><li>San Francisco was named to the CDP (formerly Carbon Disclosure Project) Cities A List for the fourth consecutive year in 2022, recognizing global leadership in environmental transparency and climate action</li>"
             "<li>The city reduced its carbon emissions while its population and economy grew, supported by the San Francisco Climate Action Plan and community engagement</li></ul>"
             "<p class=\"fine\">City-level results that the brand system and public engagement supported; they reflect the work of many departments and partners.</p>"),
        ],
        "links": [],
    },
    # ---------- Product Marketing
    "sf-recycles": {
        "org": SF, "program": "SF Recycles",
        "title": "Digital product launch and adoption",
        "image": {"src": "sfrecycles.jpg", "w": 420, "h": 2000, "layout": "phone",
                  "alt": "SF Recycles mobile web app: search box, popular searches, and recycle, compost and landfill bin guides"},
        "outcome": ("+495%", "year-over-year monthly active users"),
        "challenge": "Help residents of a city of 850,000 find the right way to recycle or dispose of everyday items.",
        "role": "As in-house product owner, directed customer research and agency delivery, and led go-to-market.",
        "details": [
            ("Strategy and my role",
             "<p>As in-house product owner, directed customer research and agency delivery to turn static guidance into a trilingual web application. Led go-to-market with product managers, engineers and UX.</p>"),
            ("Results",
             "<ul><li>+495% year-over-year monthly active users</li><li>The app and companion campaign contributed to 27% year-over-year growth in compliant use of an affiliated service</li><li>2018 Data &amp; Innovation Awards, first place, Users First</li></ul>"),
        ],
        "links": [],
    },
    "cam-portal": {
        "org": SF, "program": "Climate Action Month",
        "title": "Digital experience strategy and development",
        "image": {"src": "climate-action-month-portal.jpg", "w": 1000, "h": 765,
                  "alt": "April is Climate Action Month web page: Be the change in climate change banner, date and event-type filters, and event listings"},
        "outcome": ("+51%", "year-over-year page visits"),
        "challenge": "Make a citywide calendar of climate events and activities easy for residents to discover, navigate and explore.",
        "role": "Owned the digital experience from concept through launch, directing product requirements, UX, development and scalable content workflows.",
        "details": [
            ("Strategy and my role",
             "<p>Led the concept, requirements, design direction and development of a citywide event-discovery portal with web, UX and technical teams. Used audience research and feedback to guide navigation, filtering and multilingual access, while establishing standardized event-submission processes, content templates and editorial requirements.</p>"),
            ("Results",
             "<ul><li>+51% year-over-year page visits during the fourth annual Climate Action Month</li><li>Delivered a multilingual event-discovery portal with research-informed navigation and activity filtering</li><li>Established reusable event-submission templates and editorial workflows supporting contributions from community partners</li></ul>"),
        ],
        "links": [],
    },
    "greener-life": {
        "org": "Southern Company", "program": "Georgia Natural Gas Greener Life®",
        "title": "Subscription growth and lifecycle strategy",
        "image": {"src": "greener-life-offer.jpg", "w": 1100, "h": 738,
                  "alt": "Greener Life offer card: Get Greener Life free for a year and save, with Sign up for service and Add to my plan buttons"},
        "outcome": ("+11%", "subscribers in three months"),
        "challenge": "Grow a consumer subscription product in a competitive energy market.",
        "role": "Set vision, strategy and goals for the product and co-developed an integrated acquisition campaign.",
        "details": [
            ("Strategy and my role",
             "<p>Set vision, strategy and goals for a subscription product and co-developed an integrated acquisition campaign tied to a new feature and milestone.</p>"),
            ("Lifecycle and retention",
             "<p>Analyzed customer needs, competitive offerings and attrition drivers to identify acquisition and retention opportunities. Developed prioritized recommendations for customer journeys, messaging, product experience and loyalty initiatives.</p>"),
            ("Results",
             "<ul><li>+11% subscribers in three months</li><li>$1.7M in projected customer lifetime value from the subscriber gain</li></ul>"
             "<p class=\"fine\">Lifetime value is projected, not booked revenue.</p>"),
        ],
        "links": [],
    },
    "delta-suitcase": {
        "org": "Delta Air Lines", "program": "Upcycled suitcase",
        "title": "Consumer product positioning and commercialization",
        "image": {"src": "delta-suitcase.jpg", "w": 1110, "h": 419, "layout": "wide",
                  "alt": "Delta web feature: Suitcases made from Delta jets, showing the aluminum suitcase prototype"},
        "outcome": ("", "First-in-kind consumer product strategy and go-to-market planning"),
        "challenge": "Turn retired aircraft into a consumer product that strengthens the Delta brand and loyalty proposition.",
        "role": "Co-led product strategy and go-to-market planning with cross-functional teams and external partners.",
        "details": [
            ("Strategy and my role",
             "<p>Co-led development of a first-in-kind consumer product, an upcycled suitcase made from retired aircraft skin, including positioning, feature identification, partner selection, business case development and go-to-market planning with cross-functional teams and external partners.</p>"),
            ("Status",
             "<p>Delta introduced the suitcase publicly while it was still in development.</p>"),
        ],
        "links": [],
    },
    "rethink-disposable": {
        "org": SF, "program": "ReThink Disposable",
        "title": "Small-business acquisition and conversion",
        "image": None,
        "outcome": ("54%", "above enrollment goal, with 42% fewer prospect visits"),
        "challenge": "Enroll more small businesses in the program without adding field visits.",
        "role": "Used research-led targeting, field marketing, webinars and multilingual outreach.",
        "details": [
            ("Approach",
             "<p>Used research-led targeting, field marketing, webinars and multilingual outreach to improve small-business acquisition.</p>"),
            ("Results",
             "<p>Enrolled 77 businesses against a target of 50, at 11% lead conversion.</p>"),
        ],
        "links": [],
    },
    # ---------- Internal & Executive Communications
    "microsoft-exec": {
        "org": "Microsoft", "program": "Customer Success",
        "title": "Executive communications and AI adoption",
        "image": {"src": "year-end-wrap-up.jpg", "w": 1100, "h": 618, "layout": "wide",
                  "alt": "Title card from a year-end leadership video: Year-End Wrap-Up"},
        "outcome": ("", "Executive and employee communications for a 4,500+ person global organization"),
        "challenge": "Help a global organization understand strategic priorities, organizational change and new AI capabilities.",
        "role": "Developed executive messaging and a monthly leadership video series, and built AI tools for the communications team.",
        "details": [
            ("Strategy and my role",
             "<p>Developed executive messaging and a monthly leadership video series for Customer Success, translating strategic priorities, organizational transformation and AI capabilities into practical communications.</p>"),
            ("Executive voice",
             "<p>Authored and ghostwrote executive emails, scripts, presentations and posts across internal channels.</p>"),
            ("Applied AI",
             "<p>Built AI agents and workflows for drafting, editing and summarization while preserving executive voice and tone.</p>"),
        ],
        "links": [],
    },
    "microsoft-holiday": {
        "org": "Microsoft", "program": "Holiday Gratitude Campaign",
        "title": "Employee engagement and editorial strategy",
        "image": None,
        "outcome": ("+42%", "year-over-year engagement during the annual campaign"),
        "challenge": "Increase employee participation and recognition in an annual digital campaign.",
        "role": "Owned integrated communications strategy, editorial planning, channel governance and performance.",
        "details": [
            ("Strategy and my role",
             "<p>Owned integrated communications strategy, editorial planning, channel governance and performance for a campaign combining executive messaging, SharePoint and interactive employee recognition.</p>"),
            ("Results",
             "<ul><li>+42% year-over-year engagement during the annual campaign</li><li>Separately, average internal content views per post increased 61% within Customer Success through editorial planning, channel optimization and measurement</li></ul>"),
        ],
        "links": [],
    },
    "sf-internal-comms": {
        "org": SF, "program": "Environment Department",
        "title": "Building an internal communications function",
        "image": {"src": "our-values.png", "w": 1620, "h": 418, "layout": "wide",
                  "alt": "Our Values: Credibility, Innovation, Collaboration, Equity and Impact, each with an icon"},
        "outcome": ("+88%", "year-over-year employee understanding of mission and values"),
        "challenge": "Give employees a shared understanding of the department’s mission and how their work connects to it.",
        "role": "Created the department’s first internal communications function and an executive-sponsored mission-and-values strategy.",
        "details": [
            ("What I built",
             "<p>Created the department’s first internal communications function, including onboarding, an employee newsletter, Teams channels and a recurring leadership cadence. Originated an executive-sponsored mission-and-values strategy.</p>"),
            ("Results",
             "<ul><li>+88% year-over-year employee understanding of mission and values</li><li>+85% year-over-year understanding of how their work aligns with the mission</li></ul>"
             "<p class=\"fine\">Relative year-over-year increases from the annual employee experience survey.</p>"),
        ],
        "links": [],
    },
    "new-resource-bank": {
        "org": "New Resource Bank", "program": "Executive, investor &amp; impact communications",
        "title": "Executive and investor communications",
        "image": None,
        "outcome": ("", "Executive, investor and impact communications for a B Corp “Best for the World” bank"),
        "challenge": "Keep marketing and communications running during a leadership gap while explaining a core-system change to customers.",
        "role": "As Interim Marketing Director, developed executive and investor messaging and led the annual Impact Report.",
        "details": [
            ("Executive and investor messaging",
             "<p>Developed executive and investor messaging and financial-performance storytelling, working alongside the CFO and Investor Relations teams during the earnings cycle.</p>"),
            ("Impact Report",
             "<p>Led cross-team synthesis of business-impact and operational data, and authored and directed the annual print and digital Impact Report for customer, executive and stakeholder audiences.</p>"),
            ("Change communications",
             "<p>Directed multimedia customer outreach for a core-system transition, explaining operational impacts and the actions customers needed to take.</p>"),
            ("Context",
             "<p>Interim Marketing Director during the permanent Director’s leave. New Resource Bank was later acquired by Amalgamated Bank.</p>"),
        ],
        "links": [],
    },
    # ---------- Leadership & Operations
    "executive-partnership": {
        "org": SF, "program": "Executive leadership team",
        "title": "Executive operating partnership",
        "image": {"src": "strategic-plan.jpg", "w": 1100, "h": 481, "layout": "wide",
                  "alt": "Cover of the San Francisco Environment Department Strategic Plan 2021–2023"},
        "outcome": ("", "Organization-wide strategy, resource allocation and executive alignment"),
        "challenge": "Translate citywide priorities into a focused strategy, operating plan and budget for the department.",
        "role": "Served as senior operating partner to the department Director.",
        "details": [
            ("Strategy and my role",
             "<p>Served as senior operating partner to the department Director, translating citywide priorities into strategy, operating plans and executive communications.</p>"),
            ("Strategic plan",
             "<p>Led the 2021–2023 Strategic Plan and aligned organizational and board leaders on priorities and KPIs.</p>"),
            ("Budget and operating rhythm",
             "<p>Aligned budgets to strategy through forecasting and resource allocation; ran reviews and reporting that tracked milestones and prompted follow-up.</p>"),
        ],
        "links": [],
    },
    "team-leadership": {
        "org": SF, "program": "Communications center of excellence",
        "title": "Multidisciplinary team and agency leadership",
        "image": None,
        "outcome": ("", "Up to 7 direct reports, 24 indirect contributors and 10+ agency relationships"),
        "challenge": "Build a team able to serve a portfolio of 20+ services and technology products.",
        "role": "Restructured a team spanning marketing, content, community engagement, UX, web development, design and data.",
        "details": [
            ("What I changed",
             "<p>Restructured a team spanning marketing, content, community engagement, UX, web development, design and data. Clarified ownership, standardized workflows, rewrote roles and hired specialized talent.</p>"),
            ("Operations",
             "<p>Managed budgets, contracts and agency relationships while running distributed operations through more than two years of the pandemic.</p>"),
        ],
        "links": [],
    },
    "salesforce": {
        "org": SF, "program": "Salesforce CRM",
        "title": "Salesforce implementation and organizational adoption",
        "image": None,
        "outcome": ("", "Organization-wide CRM implementation and change leadership"),
        "challenge": "Give teams across the department a shared system for contacts, data and reporting.",
        "role": "Held accountability for the rollout and managed the project manager who delivered it.",
        "details": [
            ("Strategy and my role",
             "<p>Held accountability for a Salesforce rollout and managed the project manager who delivered it. Oversaw needs assessment, onboarding, training, change communications and workflow redesign.</p>"),
            ("Result",
             "<p>Enabled better contact and data management, cross-team information sharing and analytics reporting.</p>"),
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

# Homepage collage tile (kept separate from the SF Climate Action project image)
COLLAGE_CAM = {"src": "climate-action-month.jpg", "w": 714, "h": 720, "focus": "top",
               "alt": "Climate Action Month creative: Be the change in climate change, over the Golden Gate Bridge in fog"}

RECENT_WORK = ["Google", "Microsoft", "Delta Air Lines", "Southern Company"]

# ---------- About page
ABOUT_INTRO = ("I’ve led brand, product marketing, communications and operations for global companies, "
               "consulting clients and the City &amp; County of San Francisco, in the US and abroad. "
               "This page collects my experience, the technology I work with and my credentials.")

EXPERIENCE = [
    # (years, organization html, title, description, related specialty slugs)
    ("2026–now", "<b>Google</b>", "Strategic Marketing Consultant, AI",
     "Partner with engineering teams to translate expert marketing judgment into guidance, prompts and evaluation frameworks for reasoning in enterprise AI systems.", []),
    ("2025", "<b>Microsoft</b>", "Senior Communications Consultant",
     "Executive, employee and AI adoption communications for the global Customer Success organization. Built AI agents and workflows for drafting, editing and summarization while preserving executive voice and tone.",
     ["communications"]),
    ("2024", "<b>Southern Company</b>", "Senior Consultant, Brand &amp; Product Marketing",
     "Brand and product marketing for Georgia Natural Gas and its Greener Life® subscription product.", ["product-marketing"]),
    ("2023–24", "<b>Delta Air Lines</b>", "Senior Consultant, Brand &amp; Product Marketing",
     "National brand campaign, consumer research and new-product commercialization.", ["brand", "product-marketing"]),
    ("2017–22", "<b>City &amp; County of San Francisco, Environment Department</b>", "Head of Marketing, Product &amp; Community",
     "Owned brand, marketing, communications and community engagement across 20+ services and technology products, leading a multidisciplinary team.",
     ["brand", "product-marketing", "communications", "leadership"]),
    ("2017", "<b>New Resource Bank</b> (acquired by Amalgamated Bank)", "Interim Marketing Director",
     "Product positioning, customer communications through a core-system transition, and the annual Impact Report for a B Corp “Best for the World” bank.", ["communications"]),
    ("2012–16", "<b>Columbia University · Malaysia Ministry of Finance · World Wildlife Fund</b>", "Strategic communications, consulting and product roles",
     "Launched Columbia Housing and Transportation websites and the “Make It Your Home” brand; proposed a scalable microfinance model to the Ministry; co-launched a WWF practitioner learning platform.", []),
    ("2006–11", "<b>Putumayo World Music</b>", "Marketing Director (promoted from Coordinator and Manager)",
     "Brought on brand partners including South African Airways, Amnesty International, National Geographic and Intrepid Travel. A South African Airways sweepstakes generated 17K marketing-qualified leads, and Facebook followers grew from 3K to 55K in 15 months.", []),
]

TECH_INTRO = "I connect strategic judgment with practical AI capabilities to improve how teams research, develop ideas, solve problems and execute work."
TECH_ROWS = [
    ("AI &amp; agentic capabilities", "Agent design &amp; optimization · AI workflow development &amp; automation · Prompt design · AI evaluation frameworks · AI-assisted prototyping &amp; application development"),
    ("Select platforms &amp; models", "ChatGPT · Claude · Gemini · Gemini Notebook · Copilot"),
    ("Application development &amp; deployment", "Codex · GitHub · Vercel"),
]

AWARDS = [
    ("2022", "ADDY Award, Public Service Campaign", "REUSE SF ad campaign"),
    ("2022", "California Transportation Foundation, Operational Efficiency Award", "Essential Worker Ride Home program"),
    ("2020", "ADDY Award, Corporate Social Responsibility Film, Video &amp; Sound", "“Feeling Gassy” ad campaign"),
    ("2019", "Carbon Neutral Cities Alliance, Spotlight Award", "Campaign media leadership"),
    ("2018", "Carbon Neutral Cities Alliance, Bullhorn Award", "Social media leadership"),
    ("2018", "SF Data &amp; Innovation Awards, first place, Users First", "SF Recycles app"),
]
EDUCATION = [
    ("MBA, ISC Paris", ""),
    ("BA, Literature &amp; French, cum laude, New York University", "Minor in Communications · New York and Paris"),
    ("Pragmatic Institute, PMC Level I", "Foundations"),
    ("IBM Product Management Certificate", "In progress"),
]
LANGUAGES = "English, native · French, fluent · Spanish, elementary"
