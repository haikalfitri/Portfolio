"""Generate Haikal-Fitri-Resume.pdf using reportlab."""

from pathlib import Path

from reportlab.lib.colors import HexColor, black
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import (
    HRFlowable,
    ListFlowable,
    ListItem,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
)

OUTPUT = Path(__file__).parent / "assets" / "Haikal-Fitri-Resume.pdf"

PRIMARY = HexColor("#0f4c75")
ACCENT = HexColor("#3282b8")
MUTED = HexColor("#555555")


def build_styles():
    base = getSampleStyleSheet()
    styles = {
        "name": ParagraphStyle(
            "name",
            parent=base["Title"],
            fontName="Helvetica-Bold",
            fontSize=20,
            textColor=PRIMARY,
            alignment=TA_LEFT,
            spaceAfter=2,
            leading=24,
        ),
        "title": ParagraphStyle(
            "title",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=11.5,
            textColor=ACCENT,
            spaceAfter=4,
            leading=14,
        ),
        "contact": ParagraphStyle(
            "contact",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=9,
            textColor=MUTED,
            spaceAfter=2,
            leading=12,
        ),
        "section": ParagraphStyle(
            "section",
            parent=base["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=11.5,
            textColor=PRIMARY,
            spaceBefore=10,
            spaceAfter=4,
            leading=14,
        ),
        "role": ParagraphStyle(
            "role",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=10.5,
            textColor=black,
            spaceAfter=1,
            leading=13,
        ),
        "meta": ParagraphStyle(
            "meta",
            parent=base["Normal"],
            fontName="Helvetica-Oblique",
            fontSize=9.5,
            textColor=MUTED,
            spaceAfter=3,
            leading=12,
        ),
        "bullet": ParagraphStyle(
            "bullet",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=9.5,
            textColor=black,
            leading=12.5,
            alignment=TA_JUSTIFY,
        ),
        "body": ParagraphStyle(
            "body",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=9.5,
            textColor=black,
            leading=12.5,
        ),
    }
    return styles


def bullets(items, style):
    return ListFlowable(
        [ListItem(Paragraph(item, style), leftIndent=6) for item in items],
        bulletType="bullet",
        bulletColor=ACCENT,
        bulletFontSize=7,
        leftIndent=12,
        spaceBefore=0,
        spaceAfter=2,
    )


def rule():
    return HRFlowable(
        width="100%",
        thickness=0.6,
        color=ACCENT,
        spaceBefore=1,
        spaceAfter=4,
    )


def build_story(styles):
    story = []

    story.append(Paragraph("Muhammad Haikal Fitri Bin Hassim @ Husain", styles["name"]))
    story.append(Paragraph("Engineer, Digital Infrastructure Support", styles["title"]))
    story.append(
        Paragraph(
            "+60 111 932 9198 &nbsp;|&nbsp; "
            '<a href="mailto:haikalfitri.hassim@gmail.com" color="#3282b8">haikalfitri.hassim@gmail.com</a> &nbsp;|&nbsp; '
            '<a href="https://www.linkedin.com/in/muhdhaikalfitri" color="#3282b8">linkedin.com/in/muhdhaikalfitri</a>',
            styles["contact"],
        )
    )
    story.append(
        Paragraph(
            "Subang Jaya / Kajang, Selangor &nbsp;|&nbsp; "
            '<a href="https://haikalfitri.github.io" color="#3282b8">haikalfitri.github.io</a>',
            styles["contact"],
        )
    )
    story.append(rule())

    # Experience
    story.append(Paragraph("EXPERIENCE", styles["section"]))

    story.append(Paragraph("Engineer, Digital Infrastructure Support", styles["role"]))
    story.append(Paragraph("Cypark Sdn Bhd &nbsp;&middot;&nbsp; 2025 – Present", styles["meta"]))
    story.append(
        bullets(
            [
                "Manages Proxmox virtualization environment and backup systems to ensure platform reliability.",
                "Conducts SCADA vulnerability assessments to safeguard operational technology networks.",
                "Manages firewalls, switches, and access points across the corporate network.",
                "Deployed Splashtop remote access to support distributed engineering and operations teams.",
                "Handles IT onboarding and end-user device provisioning across the organisation.",
                "Administers Microsoft 365 and SharePoint, including identity, licensing, and collaboration workspaces.",
                "Drives AI-driven workflow automation to streamline internal IT and business processes.",
            ],
            styles["bullet"],
        )
    )

    story.append(Spacer(1, 4))
    story.append(Paragraph("Business / System Analyst (GEES)", styles["role"]))
    story.append(Paragraph("PETRONAS Carigali Sdn Bhd &nbsp;&middot;&nbsp; Jul 2023 – Jul 2024", styles["meta"]))
    story.append(
        bullets(
            [
                "Led data integration for the Marine Intelligence System (MARSIS) to unify logistics data sources.",
                "Played a key role in User Acceptance Testing (UAT) of digital logistics tools prior to production rollout.",
                "Streamlined logistic digital tools, materially reducing manhours required for routine reporting.",
                "Implemented the HSE Assurance Program tracking workflow used across operational teams.",
                "Coordinated the Mentorship Program and a fuel benchmarking initiative applying Lean Six Sigma methods.",
                "Facilitated engagement and onboarding with over 40 contractors and external partners.",
            ],
            styles["bullet"],
        )
    )

    story.append(Spacer(1, 4))
    story.append(Paragraph("Web Developer Intern", styles["role"]))
    story.append(Paragraph("UiTM Technoventure &nbsp;&middot;&nbsp; Sep 2022 – Jan 2023", styles["meta"]))
    story.append(
        bullets(
            [
                "Conducted stakeholder interviews to gather and document system requirements.",
                "Developed flowcharts and process diagrams describing core system functionalities.",
                "Managed MySQL database operations including schema design, queries, and maintenance.",
                "Enhanced UI/UX design across internal web applications.",
                "Engineered web pages and forms using HTML, CSS, and PHP.",
            ],
            styles["bullet"],
        )
    )

    # Education
    story.append(Paragraph("EDUCATION", styles["section"]))
    story.append(
        Paragraph("Bachelor of Information Systems (Hons.) — Intelligent Systems Engineering", styles["role"])
    )
    story.append(
        Paragraph(
            "Universiti Teknologi MARA (UiTM) &nbsp;&middot;&nbsp; 2019 – 2023 &nbsp;&middot;&nbsp; CGPA 3.59 (First Class)",
            styles["meta"],
        )
    )
    story.append(Paragraph("Malaysian Matriculation Programme", styles["role"]))
    story.append(
        Paragraph(
            "Kolej Matrikulasi Kelantan &nbsp;&middot;&nbsp; 2018 – 2019 &nbsp;&middot;&nbsp; CGPA 3.13",
            styles["meta"],
        )
    )

    # Technical Skills
    story.append(Paragraph("TECHNICAL SKILLS", styles["section"]))
    skills = [
        (
            "Systems & IT",
            "Proxmox, Network Configuration, Network Security, Remote Access (Splashtop), "
            "Microsoft 365 Admin, SharePoint, SCADA Networks, AI Workflow Automation",
        ),
        (
            "Tools",
            "Wireshark, pfSense / Firewall, Power BI, Tableau, Excel, SQL Server, phpMyAdmin",
        ),
        ("Programming", "Python, SQL, R, Java, HTML, CSS, JavaScript"),
        ("Data Science", "Data Analysis, Machine Learning, NLP, Data Visualization"),
        (
            "Software Development",
            "Version Control, UAT, Data Integration, Database Management, Agile",
        ),
        (
            "Soft Skills",
            "Problem Solving, Adaptability, Collaboration, Integrity, Resilience, "
            "Continuous Learning, Attention to Detail",
        ),
    ]
    for label, value in skills:
        story.append(
            Paragraph(
                f'<font color="#0f4c75"><b>{label}:</b></font> {value}',
                styles["body"],
            )
        )
        story.append(Spacer(1, 2))

    # Personal Projects
    story.append(Paragraph("PERSONAL PROJECTS", styles["section"]))
    story.append(
        bullets(
            [
                "<b>Twitter Sentiment Analysis of Open Distance Learning (ODL)</b> — NLP, Pandas, RapidMiner, Power BI.",
                "<b>Monster Movie Analysis App with Predictive Modeling</b> — Shiny web app with predictive modelling.",
                "<b>FM24: Wonderkid Recruiting Analysis</b> — Statistical analysis and interactive dashboards.",
            ],
            styles["bullet"],
        )
    )

    # Certifications
    story.append(Paragraph("CERTIFICATIONS", styles["section"]))
    story.append(
        bullets(
            [
                "2024 &middot; PETRONAS Lean Six Sigma Yellow Belt.",
                "2024 &middot; PETRONAS Citizen Analytics Certificate.",
                "2023 &middot; Coursera — Foundations: Data, Data, Everywhere.",
            ],
            styles["bullet"],
        )
    )

    # References
    story.append(Paragraph("REFERENCES", styles["section"]))
    story.append(
        Paragraph(
            "<b>Loga Nathan Suppiah</b> — Manager, PETRONAS Carigali &nbsp;&middot;&nbsp; "
            '<a href="mailto:loganathan@petronas.com.my" color="#3282b8">loganathan@petronas.com.my</a>',
            styles["body"],
        )
    )
    story.append(Spacer(1, 2))
    story.append(
        Paragraph(
            "<b>Arthur L Arulananda Savarydass</b> — Specialist, PETRONAS Carigali &nbsp;&middot;&nbsp; "
            '<a href="mailto:arthur.savarydass@petronas.com.my" color="#3282b8">arthur.savarydass@petronas.com.my</a>',
            styles["body"],
        )
    )

    return story


def main():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(OUTPUT),
        pagesize=A4,
        leftMargin=1.6 * cm,
        rightMargin=1.6 * cm,
        topMargin=1.4 * cm,
        bottomMargin=1.4 * cm,
        title="Muhammad Haikal Fitri — Resume",
        author="Muhammad Haikal Fitri Bin Hassim @ Husain",
    )
    styles = build_styles()
    doc.build(build_story(styles))
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
