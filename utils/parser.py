import pdfplumber

# Skills Database
SKILLS = [

    "python",
    "java",
    "sql",
    "html",
    "css",
    "javascript",
    "react",
    "node",
    "nodejs",
    "flask",
    "django",

    "machine learning",
    "deep learning",
    "artificial intelligence",
    "data analysis",

    "mongodb",
    "mysql",
    "postgresql",

    "git",
    "github",

    "docker",
    "aws",
    "linux",

    "numpy",
    "pandas",
    "opencv",
    "tensorflow",
    "pytorch",

    "c",
    "c++"
]


# Extract Text from PDF
def extract_text(file):

    text = ""

    try:

        with pdfplumber.open(file) as pdf:

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:
                    text += page_text + " "

    except Exception as e:

        print("PDF Error:", e)

    return text.lower()


# Extract Skills
def extract_skills(text):

    found = []

    for skill in SKILLS:

        if skill.lower() in text:
            found.append(skill.title())

    return sorted(list(set(found)))


# Match Score
def match_score(skills, job_desc):

    job_desc = job_desc.lower()

    required = []

    for skill in SKILLS:

        if skill.lower() in job_desc:
            required.append(skill.title())

    required = list(set(required))

    if len(required) == 0:
        return 0, [], []

    matched = list(
        set(skills) & set(required)
    )

    missing = list(
        set(required) - set(skills)
    )

    score = int(
        (len(matched) / len(required)) * 100
    )

    return score, missing, matched