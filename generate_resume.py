"""Generate Haikal-Fitri-Resume.pdf using reportlab."""

from pathlib import Path

from reportlab.lib.colors import HexColor, black
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import (
    HRFlowable,
    KeepTogether,
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
            "+60 111 449 1024 &nbsp;|&nbsp; "
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

    # Profile
    story.append(Paragraph("PROFILE", styles["section"]))
    story.append(
        Paragraph(
            "Infrastructure and IT operations engineer covering networking, endpoint security, Microsoft 365 "
            "and OT/SCADA support, with a compliance-first approach (ISO/IEC 27001:2022, CIS Benchmarks). "
            "Builds PowerShell and Python tooling to automate onboarding, auditing and monitoring.",
            styles["body"],
        )
    )

    # Experience
    story.append(Paragraph("EXPERIENCE", styles["section"]))

    story.append(Paragraph("Engineer, Digital Infrastructure Support", styles["role"]))
    story.append(Paragraph("Cypark Sdn Bhd &nbsp;&middot;&nbsp; 2025 – Present", styles["meta"]))
    story.append(
        bullets(
            [
                "Manage the Proxmox virtualisation environment and backup systems to keep the platform reliable.",
                "Maintain HPE and Aruba switching, VLAN segmentation and network documentation across HQ and remote "
                "sites, and configure Palo Alto (PAN-OS) firewall rules.",
                "Led the company-wide Splashtop remote access deployment, enrolling around 70 endpoints.",
                "Conduct SCADA vulnerability assessments and drafted the guideline for controlling automatic "
                "Windows Updates on plant OT PCs.",
                "Enforce ISO/IEC 27001:2022-aligned endpoint controls through Intune and Defender for Endpoint, "
                "including USB storage whitelisting and UAT of a Windows device rollout for about 30 users.",
                "Wrote a 137-control PowerShell audit script that maps Windows 11 hardening checks to CIS Benchmarks "
                "and ISO 27001:2022.",
                "Led incident response and staff awareness for a social-engineering malware attempt and a "
                "browser-notification scareware incident.",
                "Built a PowerShell automation suite for onboarding, server cleanup and disk monitoring, and automate "
                "IT workflows with Power Automate and Microsoft Graph.",
                "Administer Microsoft 365, Entra ID and SharePoint, including identity, licensing and collaboration workspaces.",
                "Evaluate vendor proposals for solar-farm CCTV and monitoring systems, weighing capex against "
                "managed-service options and flagging SLA and exit-clause risks.",
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
                "Analysed and reported on process flows for a Lean Six Sigma fuel-recoupment project, contributing to "
                "a 70% reduction in lead time and about 4,000 manhours saved.",
                "Managed reporting for the Vessel Tracking System (VTS), contributing to a 25% lead-time improvement "
                "and about 71,280 manhours saved.",
                "Led data integration for the Marine Intelligence System (MARSIS) to unify logistics data sources.",
                "Played a key role in User Acceptance Testing (UAT) of digital logistics tools prior to production rollout.",
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
                "Built web pages and forms with HTML, CSS and PHP, and managed the MySQL database for an internal web application.",
            ],
            styles["bullet"],
        )
    )

    # Education
    story.append(
        KeepTogether(
            [
                Paragraph("EDUCATION", styles["section"]),
                Paragraph("Bachelor of Information Systems (Hons.) — Intelligent Systems Engineering", styles["role"]),
                Paragraph(
                    "Universiti Teknologi MARA (UiTM) &nbsp;&middot;&nbsp; 2019 – 2023 &nbsp;&middot;&nbsp; CGPA 3.59 (First Class)",
                    styles["meta"],
                ),
                Paragraph("Malaysian Matriculation Programme", styles["role"]),
                Paragraph(
                    "Kolej Matrikulasi Kelantan &nbsp;&middot;&nbsp; 2018 – 2019 &nbsp;&middot;&nbsp; CGPA 3.13",
                    styles["meta"],
                ),
            ]
        )
    )

    # Technical Skills (kept together so the block never splits across pages)
    skills = [
        (
            "Infrastructure",
            "Proxmox, HPE / Aruba Switching, VLAN Design, Palo Alto PAN-OS, pfSense, Wireshark, "
            "Remote Access (Splashtop), SCADA / OT Networks, AWS (introductory)",
        ),
        (
            "Microsoft Platform",
            "Microsoft 365 Admin, Entra ID, Intune, Defender for Endpoint, Active Directory, "
            "SharePoint, Power Automate, Microsoft Graph",
        ),
        (
            "Security and Compliance",
            "ISO/IEC 27001:2022, CIS Benchmarks, PDPA, Incident Response, Endpoint Hardening",
        ),
        (
            "Automation and Data",
            "PowerShell, Python, SQL, Git, Power BI, Excel, HTML / CSS / JavaScript",
        ),
    ]
    skills_block = [Paragraph("TECHNICAL SKILLS", styles["section"])]
    for label, value in skills:
        skills_block.append(
            Paragraph(
                f'<font color="#0f4c75"><b>{label}:</b></font> {value}',
                styles["body"],
            )
        )
        skills_block.append(Spacer(1, 2))
    story.append(KeepTogether(skills_block))

    # Personal Projects
    story.append(Paragraph("PERSONAL PROJECTS", styles["section"]))
    story.append(
        bullets(
            [
                "<b>PC Health and Crash Analyzer</b> — Python/tkinter desktop tool packaged with PyInstaller for USB "
                "deployment; reads hardware specs and Event Logs, detects BSODs and hanging apps, checks Windows Update "
                "and BitLocker, and exports CSV/PDF.",
                "<b>Twitter Sentiment Analysis of Open Distance Learning (ODL)</b> — NLP, Pandas, RapidMiner, Power BI.",
            ],
            styles["bullet"],
        )
    )

    # Certifications
    story.append(Paragraph("CERTIFICATIONS AND TRAINING", styles["section"]))
    story.append(
        bullets(
            [
                "2024 &middot; PETRONAS Lean Six Sigma Yellow Belt.",
                "2024 &middot; PETRONAS Citizen Analytics Certificate.",
                "AWS Landing Zone workshop (two days) — Organizations, Control Tower, SCPs, IAM Identity Center.",
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
