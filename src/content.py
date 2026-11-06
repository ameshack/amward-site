"""Site content: specialties, projects, experience and credentials.

Projects are defined once and listed by id on each specialty page, so a
project can appear under more than one specialty without duplicated text.
Text fields may contain inline HTML; link to another page with
href="@slug/#anchor" and the build fills in the right relative path. Wrap owner-review notes in
<!--REVIEW--> ... <!--/REVIEW--> so the published build drops them.

Project fields: org, program (optional), title, image (optional; "layout":
"wide" stacks it above the text, "phone" frames a tall screenshot),
outcome (figure, label; an empty figure shows the label as a mandate),
secondary (optional second metric), challenge, role_label ("My ownership"
where the owner had direct accountability, otherwise "My role"), role,
approach (optional strategic approach), details [(heading, html)],
links [(label, url)].
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
        "name": "Strategic Communications",
        "short": "Communications",
        "card": "Executive counsel, employee engagement, organizational change and external communications.",
        "intro": "I develop communications strategies that connect organizational priorities with the people they affect—from employees and executives to customers, partners and the public. My work spans executive counsel, employee engagement, organizational change, external communications and issues management, with an emphasis on clarity, credibility and measurable outcomes.",
        "capabilities": [
            "Executive voice &amp; counsel",
            "Change &amp; AI adoption",
            "Employee engagement &amp; measurement",
            "Media strategy &amp; issues management",
        ],
        "projects": ["microsoft-exec", "microsoft-editorial", "sf-internal-comms", "external-comms", "new-resource-bank"],
        "card_visual": {"img": "year-end-wrap-up.jpg", "position": "center 52%"},
        "title": "Strategic communications",
        "description": "Strategic communications by Asia Meshack: executive counsel, employee engagement, organizational change, external communications and issues management, with work for Microsoft, the City & County of San Francisco, Columbia University and New Resource Bank.",
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
        "outcome": ("#1", "tested Delta ad for driving consumer brand difference and affinity"),
        "secondary": ("Lift", "statistically significant lift in association with Delta’s net-zero-by-2050 commitment"),
        "challenge": "Stand out with consumers nationally and deepen their affinity for the Delta brand.",
        "role": "Led strategy and execution for a national omnichannel campaign, from consumer research and creative briefs through agency direction, paid media and measurement.",
        "approach": "Turned consumer research into creative briefs that spotlighted tangible changes to Delta’s operations, rather than distant climate goals.",
        "details": [
            ("Strategic insight",
             "<p>Consumer research reinforced the value of concrete, informative sustainability claims in building brand differentiation and affinity. By spotlighting tangible changes to Delta’s operations, the campaign made progress toward its long-term climate commitments more relatable, credible and memorable.</p>"),
            ("Research and execution",
             "<p>Led multiphase qualitative and quantitative consumer research and competitive analysis, translated the findings into creative briefs and agency direction, and oversaw paid-media investment, measurement and reporting.</p>"),
            ("Results",
             "<ul><li>The #1 tested Delta ad for driving consumer brand difference and affinity, in the emotive-testing phase of Delta consumer research</li>"
             "<li>Statistically significant lift in association with the message “We are committed to net zero carbon emissions by 2050,” per the media agency’s mid-campaign report</li></ul>"
             "<p class=\"fine\">Message association measures what viewers linked to Delta, not progress on emissions.</p>"),
            ("Ongoing content strategy",
             "<p>Separately, developed a research-backed evergreen content strategy built on four principles: spotlight current progress over distant commitments, feature the employees and partners behind it, connect progress to customer benefits, and share setbacks as openly as gains. It guided ongoing content planning, not the campaign ad.</p>"),
        ],
        "links": [("Watch the Delta ad", "https://www.facebook.com/watch/?v=248379818072591")],
    },
    "reuse-sf": {
        "org": SF, "program": "REUSE SF",
        "title": "Integrated brand campaign and audience engagement",
        "image": {"src": "reuse.jpg", "w": 1100, "h": 558, "layout": "wide",
                  "alt": "REUSE SF campaign creative: a model in yellow reclining with a reusable tote of produce"},
        "outcome": ("+51%", "reported increase in intent to reuse, per the agency partner"),
        "secondary": ("7×", "video engagement relative to benchmark"),
        "challenge": "Persuade residents to choose reusable bags, cups and utensils over disposable ones.",
        "role_label": "My ownership",
        "role": "Commissioned and directed the campaign, leading the agency, creative vendors and contractors.",
        "approach": "Framed reuse through fashion-inspired creative and invited residents to take part, through photo pop-ups, giveaways and a pledge, rather than only see ads.",
        "details": [
            ("Strategy and execution",
             "<p>Led integrated advertising, community activations, a pledge website and geotargeted digital promotion that drove attendance at neighborhood activations. User-generated-style video and culturally relevant creative reached Spanish- and Chinese-speaking, lower-income and older residents.</p>"),
            ("Results",
             "<ul><li>+51% reported increase in intent to reuse</li><li>Video engagement at 7× benchmark, driven by the user-generated-style creative</li>"
             "<li>Thousands of pledges and 4,000+ participant photos shared on social media, carrying the campaign into residents’ own channels</li>"
             "<li>2022 ADDY Award, Public Service Campaign</li></ul>"
             "<p class=\"fine\">Campaign-level results reported by the agency partner. The 51% measures intent to reuse, not verified behavior.</p>"),
        ],
        "links": [("View the REUSE SF campaign", "https://www.reuse-sf.org/")],
    },
    "sf-climate-action": {
        "org": SF, "program": "SF Climate Action",
        "title": "Brand architecture and governance",
        "image": {"src": "climate-action-booth.jpg", "w": 1100, "h": 937,
                  "alt": "San Francisco Environment staff at a community outreach table branded with the San Francisco Climate Action 0 80 100 Roots identity"},
        "outcome": ("+51%", "year-over-year website visits during the fourth annual Climate Action Month"),
        "challenge": "Bring the city’s environmental services and climate goals together under one coherent brand.",
        "role_label": "My ownership",
        "role": "Developed and governed the San Francisco Climate Action brand system, establishing shared identity, messaging and editorial standards across public-facing programs, campaigns and digital experiences.",
        "approach": "Extended the brand into Climate Action Month, a recurring citywide initiative, so residents met one consistent identity across programs, campaigns and events.",
        "details": [
            ("Brand system and governance",
             "<p>Expanded the city’s “0/80/100/Roots” climate identity into a brand system for city programs and public-facing communications, with naming, content strategy and governance for new products and citywide initiatives, coordinated across teams.</p>"),
            ("Extending the brand",
             "<p>Created Climate Action Month, an annual citywide initiative that brought the brand to residents through an integrated partner strategy. Its <a href=\"@product-marketing/#cam-portal\">event-discovery portal</a> is covered under Product Marketing.</p>"),
            ("Results",
             "<p>Website visits rose 51% year over year during the fourth annual Climate Action Month, reflecting the broader marketing and digital program rather than the brand system alone.</p>"),
            ("Broader context",
             "<ul><li>San Francisco was named to the CDP (formerly Carbon Disclosure Project) Cities A List for the fourth consecutive year in 2022, recognizing global leadership in environmental transparency and climate action</li>"
             "<li>The city reduced its carbon emissions while its population and economy grew, supported by the San Francisco Climate Action Plan and community engagement</li></ul>"
             "<p class=\"fine\">These citywide achievements show the public mission the communications supported; they aren’t outcomes of the brand system.</p>"),
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
        "role_label": "My ownership",
        "role": "As in-house product owner, led the transformation of static recycling guidance into a trilingual web application, directing user research, product development and go-to-market strategy.",
        "approach": "Used customer research to replace static lists with a searchable, item-by-item experience in English, Chinese and Spanish, and launched it with a companion outreach campaign.",
        "details": [
            ("Execution and collaboration",
             "<p>Directed customer research and digital agency delivery, and worked with product managers, engineers and UX to define and build a first-in-kind, mobile-accessible web application.</p>"),
            ("Results",
             "<ul><li>+495% year-over-year monthly active users</li>"
             "<li>Together with its companion campaign, the app contributed to 27% year-over-year growth in compliant use of an affiliated waste service</li>"
             "<li>2018 Data &amp; Innovation Awards, first place, Users First</li></ul>"
             "<p class=\"fine\">The 27% reflects the app and campaign together, not the app alone.</p>"),
        ],
        "links": [],
    },
    "cam-portal": {
        "org": SF, "program": "Climate Action Month",
        "title": "Digital experience strategy and development",
        "image": {"src": "climate-action-month-banner.jpg", "w": 1000, "h": 765,
                  "alt": "Climate Action Month web page: Be the change in climate change banner, Español and Chinese language links, date and event-type filters, and event listings"},
        "outcome": ("100+", "event submissions from organizers for the fourth annual Climate Action Month"),
        "secondary": ("+51%", "year-over-year website visits during the same event"),
        "challenge": "Make a citywide calendar of climate events and activities easy for residents to discover, navigate and explore.",
        "role_label": "My ownership",
        "role": "Led the portal from concept through launch, owning requirements and UX direction and partnering with web and design colleagues to develop a multilingual event-discovery experience informed by user research and behavior.",
        "approach": "Let audience research, behavior and feedback decide how residents find events: browsing by date and event type, multilingual presentation, and standard submissions so partner listings stayed consistent.",
        "details": [
            ("Context",
             "<p>Climate Action Month, an annual citywide initiative, gathered events and activities from community partners across San Francisco. The portal had to collect those listings and present them in one place.</p>"),
            ("Strategic decisions",
             "<p>Treated the calendar as a product rather than a list of links. Research, behavior and feedback on how residents browsed shaped the navigation, filters and event presentation, and Spanish and Chinese versions extended it beyond English speakers.</p>"),
            ("Execution and collaboration",
             "<p>Defined the concept and product requirements, set design and UX direction, and coordinated development with web, UX and technical colleagues. Established event-submission processes, content templates and editorial requirements so community partners could contribute listings consistently.</p>"),
            ("Results",
             "<ul><li>100+ event submissions from event organizers for the fourth annual Climate Action Month</li>"
             "<li>+51% year-over-year website visits during the fourth annual Climate Action Month</li></ul>"),
        ],
        "links": [],
    },
    "greener-life": {
        "org": "Southern Company", "program": "Georgia Natural Gas Greener Life®",
        "title": "Subscription growth and lifecycle strategy",
        "image": {"src": "greener-life-offer.jpg", "w": 1100, "h": 738,
                  "alt": "Greener Life offer card: Get Greener Life free for a year and save, with Sign up for service and Add to my plan buttons"},
        "outcome": ("+11%", "Greener Life® subscriptions in three months"),
        "secondary": ("$1.7M", "projected customer lifetime value"),
        "challenge": "Grow a consumer subscription product in a competitive energy market.",
        "role_label": "My role",
        "role": "Set the product vision, strategy and growth objectives, and co-developed an integrated acquisition campaign that helped increase subscriptions by 11% in three months.",
        "approach": "Grounded positioning in customer and competitive research, and timed an integrated acquisition campaign to a new product feature and milestone.",
        "details": [
            ("Strategic insight",
             "<p>Assessed competing carbon-offset and sustainability offerings, and managed the research agency behind the brand-health tracker, to sharpen positioning, messaging and product priorities.</p>"),
            ("Execution and collaboration",
             "<p>Co-developed the acquisition campaign across paid, owned and earned channels with internal teams and agency partners. Launched web personalization, weekly optimization sprints and A/B and format tests; recommendations for homepage placement and landing-page social proof were adopted. Authored sales and customer-service enablement materials.</p>"),
            ("Lifecycle and retention",
             "<p>Analyzed customer needs, competitive offerings and attrition drivers to identify acquisition and retention opportunities. Developed prioritized recommendations for customer journeys, messaging, product experience and loyalty initiatives.</p>"
             "<p class=\"fine\">Retention ideas such as a points-based loyalty concept and a cancellation-offer funnel were recommendations; no implemented retention result is claimed.</p>"),
            ("Results",
             "<ul><li>+11% Greener Life® subscriptions in three months</li><li>$1.7M in projected customer lifetime value from the subscriber gain</li></ul>"
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
        "role_label": "My role",
        "role": "Co-led development and commercialization planning for a first-in-kind Delta consumer product, including product features, positioning, partner selection, business case and go-to-market strategy.",
        "approach": "Built the proposition around product innovation, Delta SkyMiles objectives and brand credibility, and aligned product, loyalty, customer experience and external partners behind it.",
        "details": [
            ("Product development",
             "<p>Shaped the value proposition, positioning and feature recommendations for an upcycled aluminum suitcase made from retired Delta aircraft skin, and developed the business case.</p>"),
            ("Partners and go-to-market",
             "<p>Evaluated and recommended brand and manufacturing partners, and built go-to-market plans with cross-functional teams.</p>"),
            ("Status",
             "<p>This work covered development and prelaunch commercialization planning. Delta introduced the suitcase publicly while it was still in development.</p>"),
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
    # ---------- Strategic Communications
    "microsoft-exec": {
        "org": "Microsoft", "program": "Customer Success",
        "title": "Executive communications and organizational change",
        "image": {"src": "year-end-wrap-up.jpg", "w": 1100, "h": 618, "layout": "wide",
                  "alt": "Title card from a year-end leadership video: Year-End Wrap-Up"},
        "outcome": ("", "Executive and employee communications for a 4,500+ person global organization"),
        "challenge": "Help leaders communicate priorities, organizational change and emerging AI capabilities clearly and consistently across a global Customer Success organization of more than 4,500 employees.",
        "role": "Developed executive messaging and a recurring leadership communications program, translating organizational priorities, change initiatives and AI adoption into clear employee-facing communications.",
        "approach": "Partnered with senior leaders to clarify strategic intent, establish consistent executive messaging and coordinate communications across video, email, presentations and internal digital channels.",
        "details": [
            ("Executive partnership",
             "<p>Worked directly with senior leaders, including the Corporate Vice President of Customer Success, to clarify strategic intent during organizational transformation. Developed the CVP’s monthly leadership video, from scripting and editorial development through planning and distribution, and authored and ghostwrote executive emails, scripts, presentations and posts. Advised leaders on framing sensitive messages so they stayed clear and responsive to employee concerns.</p>"),
            ("Change and AI adoption",
             "<p>Translated AI capabilities and leadership priorities into practical communications across newsletters, presentations, video, email and digital channels, connecting what leaders were prioritizing to what employees needed to know and do.</p>"),
            ("Editorial governance and measurement",
             "<p>Established communications KPIs, operating plans and editorial processes that improved planning, performance visibility and consistency across internal channels.</p>"),
            ("Executive thought leadership and customer storytelling",
             "<p>Served as lead editor of customer success narratives for Microsoft’s Corporate Vice President of Customer Success, refining executive LinkedIn posts and stories about Microsoft Cloud and AI adoption to communicate customer outcomes, solution value and business impact.</p>"
             "<figure class=\"post\"><img src=\"@img/li-st-lukes.jpg\" alt=\"LinkedIn post from Microsoft’s Corporate Vice President of Customer Success about St. Luke’s University Health Network using Security Copilot agents\" width=\"664\" height=\"1200\" loading=\"lazy\" decoding=\"async\"><figcaption>Published LinkedIn post: St. Luke’s University Health Network and Security Copilot.</figcaption></figure>"
             "<details class=\"more-samples\"><summary>See two more posts</summary><div class=\"post-grid\">"
             "<figure class=\"post\"><img src=\"@img/li-dc-cfsa.jpg\" alt=\"LinkedIn post about Washington, DC Child and Family Services Agency modernizing with Microsoft Dynamics 365 and AI\" width=\"760\" height=\"1004\" loading=\"lazy\" decoding=\"async\"><figcaption>Washington, DC Child and Family Services Agency.</figcaption></figure>"
             "<figure class=\"post\"><img src=\"@img/li-project-cure.jpg\" alt=\"LinkedIn post about Project C.U.R.E. using Microsoft Dynamics 365, Power Platform, Power BI and Teams\" width=\"760\" height=\"1135\" loading=\"lazy\" decoding=\"async\"><figcaption>Project C.U.R.E.</figcaption></figure>"
             "</div></details>"),
            ("Supporting capability: AI workflows",
             "<p>Created AI agents and workflow automations for drafting, editing and summarization that made editorial work faster and more consistent while preserving executive voice and tone.</p>"),
        ],
        "links": [],
    },
    "microsoft-editorial": {
        "org": "Microsoft", "program": "Customer Success",
        "title": "Employee engagement and editorial strategy",
        "image": None,
        "compact": True,
        "outcome": ("+61%", "average internal content views per post within Customer Success"),
        "challenge": "Strengthen the relevance, consistency and reach of employee communications across a large, globally distributed Customer Success organization.",
        "role": "Led editorial planning, channel optimization and performance measurement for employee communications, developing repeatable processes and content strategies that improved visibility and engagement.",
        "approach": "Connected communications priorities to employee information needs, used performance data to refine editorial decisions and coordinated content across internal communications channels.",
        "details": [
            ("Results",
             "<p>Increased average internal content views per post by 61% through editorial planning, channel optimization and performance measurement.</p>"
             "<p class=\"fine\">Measured across internal content within the Customer Success organization, where average views per post rose from about 3,100 to about 5,000.</p>"),
            ("Holiday Gratitude Campaign",
             "<p>Developed and activated a multichannel year-end employee recognition campaign, combining executive messaging, a dedicated SharePoint experience and interactive Viva Engage content to encourage recognition, connection and participation. Owned its integrated strategy, editorial planning and channel governance.</p>"
             "<p class=\"fine\">The campaign was one part of the editorial program; the 61% reflects the program as a whole, not the campaign alone.</p>"),
        ],
        "links": [],
    },
    "sf-internal-comms": {
        "org": SF, "program": "Environment Department",
        "title": "Building an internal communications function",
        "image": {"src": "our-values.png", "w": 1620, "h": 418, "layout": "wide",
                  "alt": "Our Values: Credibility, Innovation, Collaboration, Equity and Impact, each with an icon"},
        "outcome": ("+88%", "relative year-over-year increase in employee understanding of mission and values"),
        "secondary": ("+85%", "relative year-over-year increase in understanding of how their work aligns with the mission"),
        "challenge": "Establish a cohesive internal communications function that strengthened employee understanding of organizational priorities, mission and values across a multidisciplinary public agency.",
        "role_label": "My ownership",
        "role": "Built the department’s internal communications function from the ground up, developing a mission-and-values strategy, executive messaging and employee communications programs designed to strengthen organizational understanding and alignment.",
        "approach": "Created a coordinated communications structure connecting leadership priorities with employee information needs through recurring editorial programming, internal channels, onboarding and organizational messaging.",
        "details": [
            ("What I built",
             "<p>Started from zero: employee onboarding, an internal newsletter, dedicated Teams channels and subchannels, and a recurring cadence for leadership updates. Together they gave leaders a dependable way to reach every team and gave employees one place to follow priorities.</p>"),
            ("Mission and values strategy",
             "<p>Originated an executive-sponsored mission-and-values strategy, embedded organizational purpose in onboarding, and directed physical and digital communications that connected it to employees’ day-to-day work.</p>"),
            ("Research and measurement",
             "<p>Used employee research to understand experience and readiness during digital and brand transformation, and tracked results through the annual employee experience survey.</p>"),
            ("Results",
             "<ul><li>+88% employee understanding of mission and values</li><li>+85% understanding of how their work aligns with the mission</li></ul>"
             "<p class=\"fine\">Relative year-over-year increases from the annual employee experience survey, not percentage-point changes.</p>"),
        ],
        "links": [],
    },
    "external-comms": {
        "org": SF + " · Columbia University",
        "title": "External communications, media strategy and issues management",
        "image": None,
        "outcome": ("", "Proactive earned media, issues response and sensitive institutional communications"),
        "challenge": "Navigate external communications needs ranging from public-awareness campaigns to media scrutiny and sensitive institutional incidents, balancing organizational priorities, public accountability and reputational considerations.",
        "role": "Directed proactive media strategy, supervised PR contributors, developed institutional messaging and coordinated external responses with program leaders, executive stakeholders and communications colleagues.",
        "approach": "Tailored communications strategies to the situation—from proactive storytelling and earned-media outreach to coordinated institutional responses requiring discretion, accuracy and message discipline.",
        "media": [
            {"img": "abc7-battery.jpg", "alt": "ABC7 studio segment on battery recycling with a red battery collection bucket",
             "label": "Proactive media · Bucket or Bin Top",
             "outlet": "ABC7 San Francisco", "date": "May 2018",
             "headline": "San Francisco official on how to dispose of old batteries",
             "url": "https://abc7news.com/post/sf-official-on-how-to-dispose-of-old-batteries/3421103/",
             "text": "Led communications strategy for the Bucket or Bin Top battery recycling campaign, establishing messaging and directing PR outreach that secured local ABC7 television coverage.",
             "extra": ("Department press release", "https://www.sfenvironment.org/press/beat-battery-waste-department-environment-launches-new-bucket-or-bin-top-recycling-campaign")},
            {"img": "abc7-bottlebank.jpg", "alt": "BottleBank mobile recycling tent and table in San Francisco, as shown in ABC7 coverage",
             "label": "Issues response · BottleBank",
             "outlet": "ABC7 San Francisco", "date": "February 2022",
             "headline": "San Francisco launches anticipated mobile recycling service, but not everyone is happy",
             "url": "https://abc7news.com/post/sf-bottlebank-mobile-recycling-service-san-francisco-app/11538522/",
             "text": "Coordinated institutional communications during public scrutiny of the BottleBank rollout, working with program leaders, partners and communications colleagues to determine responses, draft statements and support media-facing communications.",
             "extra": ("Follow-up coverage, February 2022", "https://abc7news.com/post/sf-bottlebank-mobile-recycling-service-san-francisco-app/11556375/")},
            {"label": "Sensitive institutional communications · Columbia University, 2012–2014",
             "headline": "Coordinated statements during sensitive campus housing incidents",
             "text": "Worked with Columbia Housing, university leadership and Central Public Affairs to develop and coordinate institutional statements during sensitive campus housing incidents, balancing timely communication, discretion and established university protocols."},
        ],
        "details": [
            ("How the work was divided",
             "<p>On proactive campaigns, set the strategy and messaging and supervised the PR specialist who carried out media outreach. On issues and incidents, worked with program leaders, executives and communications colleagues to decide on responses and draft statements, prioritizing accuracy, discretion and consistent messaging.</p>"),
            ("About the BottleBank coverage",
             "<p>The coverage reported residents’ concerns about the rollout. It’s included as evidence of the response work, not as favorable publicity.</p>"),
            ("Columbia University",
             "<p>Served as principal communications strategist for five university departments, including press and crisis communications, and managed rapid-response communications for campus incidents and urgent service updates.</p>"),
        ],
        "links": [],
    },
    "new-resource-bank": {
        "org": "New Resource Bank", "program": "Corporate communications",
        "title": "Executive and investor communications during organizational transition",
        "image": {"src": "nrb-impact-report.jpg", "w": 900, "h": 902,
                  "alt": "Cover of the New Resource Bank Impact Report: Well-being for people and the planet through banking"},
        "compact": True,
        "outcome": ("", "Executive, investor and impact communications for a B Corp “Best for the World” bank"),
        "challenge": "Maintain clear, credible communications with investors, customers and internal stakeholders during a period of organizational and leadership transition.",
        "role": "Led executive and customer communications and developed investor messaging, working alongside senior leadership, the CFO and Investor Relations to translate financial performance, organizational developments and impact priorities into clear stakeholder narratives.",
        "approach": "Connected financial and organizational information to audience-specific communications, including executive messaging, investor materials and the bank’s Impact Report.",
        "details": [
            ("Investor and executive messaging",
             "<p>Developed executive and investor messaging and financial-performance storytelling, working alongside the CFO and Investor Relations teams during the earnings cycle.</p>"),
            ("Impact Report",
             "<p>Led cross-team synthesis of business-impact and operational data, and authored and directed the annual print and digital Impact Report for customer, executive and stakeholder audiences.</p>"),
            ("Customer communications through change",
             "<p>Directed multimedia customer outreach for a core-system transition, explaining operational impacts and the actions customers needed to take.</p>"),
            ("Context",
             "<p>Served as Interim Marketing Director. New Resource Bank was later acquired by Amalgamated Bank.</p>"),
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
        "role_label": "My ownership",
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
        "role_label": "My ownership",
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
    ("#1", "tested Delta Air Lines ad for driving brand difference and affinity", "Delta Air Lines"),
    ("+11%", "subscribers in three months; $1.7M projected customer lifetime value", "Southern Company"),
    ("+495%", "year-over-year monthly active users for a civic app", "City &amp; County of San Francisco"),
    ("+88%", "year-over-year employee understanding of mission and values (relative increase, annual survey)", "City &amp; County of San Francisco"),
]

# Official logos from Wikimedia Commons; height in px balances their visual weight.
RECENT_WORK = [
    ("Google", "google.svg", 30),
    ("Microsoft", "microsoft.svg", 30),
    ("Delta Air Lines", "delta.svg", 24),
    ("Southern Company", "southern-company.svg", 42),
]

# ---------- About page
ABOUT_INTRO = ("I’ve led brand, product marketing, communications and operations for global companies, "
               "consulting clients and the City &amp; County of San Francisco, in the US and abroad. "
               "This page collects my experience, the technology I work with and my credentials.")

EXPERIENCE = [
    # (years, organization html, title, description, related specialty slugs)
    ("2026–now", "<b>Google</b>", "Strategic Marketing Consultant, AI",
     "Advise on strategic marketing and communications quality for Gemini, partnering with engineering to develop evaluation frameworks, expert judgment standards and AI agents across brand, positioning and go-to-market strategy.", []),
    ("2025", "<b>Microsoft</b>", "Senior Communications Consultant",
     "Executive, employee and AI adoption communications for the global Customer Success organization. Separately, created AI agents and workflow automations that made repeatable drafting, editing and summarization work faster and more consistent while preserving executive voice and tone.",
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
TECH_CAPABILITY = ("I build AI-enabled workflows, agents and practical tools that improve marketing and communications processes, streamline execution and make specialized expertise more scalable. "
                   "My experience spans hands-on development, workflow automation and collaboration with engineering teams to translate business requirements into AI capabilities.")
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
