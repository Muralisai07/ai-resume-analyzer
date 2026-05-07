from flask import Flask, render_template, request
from utils.parser import (
    extract_text,
    extract_skills,
    match_score
)

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":

        file = request.files["resume"]
        job_desc = request.form["job_desc"]

        # Extract Resume Text
        text = extract_text(file)

        # Extract Skills
        skills = extract_skills(text)

        # ATS Score
        score, missing, matched = match_score(
            skills,
            job_desc
        )

        # Resume Feedback
        if score >= 80:
            feedback = (
                "Excellent ATS Match! "
                "Your resume is highly aligned "
                "with the job description."
            )

        elif score >= 60:
            feedback = (
                "Good ATS Match! "
                "Add some missing skills "
                "to improve your chances."
            )

        elif score >= 40:
            feedback = (
                "Average ATS Match. "
                "Improve technical skills "
                "and resume keywords."
            )

        else:
            feedback = (
                "Low ATS Match. "
                "Customize your resume "
                "according to the job description."
            )

        result = {
            "skills": skills,
            "score": score,
            "missing": missing,
            "matched": matched,
            "feedback": feedback
        }

    return render_template(
        "index.html",
        result=result
    )


if __name__ == "__main__":
    app.run(debug=True)