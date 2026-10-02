import streamlit as st
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()

st.set_page_config(
    page_title="AI Code Review Assistant",
    page_icon="🤖",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background-color: #0e1117;
}

.block-container {
    max-width: 1400px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

h1, h2, h3 {
    color: #f0f6fc;
}

.subtitle {
    color: #8b949e;
    font-size: 17px;
    margin-bottom: 28px;
}

section[data-testid="stSidebar"] {
    background-color: #0b0f14;
    border-right: 1px solid #30363d;
}

textarea {
    background-color: #0d1117 !important;
    color: #e6edf3 !important;
    border: 1px solid #30363d !important;
    border-radius: 10px !important;
    font-family: Consolas, monospace !important;
}

div[data-baseweb="select"] > div {
    background-color: #161b22;
    border-color: #30363d;
}

.stButton > button {
    border-radius: 8px;
    height: 44px;
    font-weight: 600;
}

.review-box {
    background-color: #161b22;
    border: 1px solid #30363d;
    border-radius: 12px;
    padding: 20px;
    margin-bottom: 16px;
}

.footer {
    text-align: center;
    color: #6e7681;
    margin-top: 35px;
    font-size: 13px;
}
</style>
""", unsafe_allow_html=True)

st.title("🤖 AI Code Review Assistant")

st.markdown(
    '<div class="subtitle">'
    'Review your code with AI and get practical suggestions for improving it.'
    '</div>',
    unsafe_allow_html=True
)

with st.sidebar:
    st.header("Review Settings")

    language = st.selectbox(
        "Programming Language",
        ["Java", "Python", "JavaScript", "C++"]
    )

    st.divider()

    st.write(
        "Analyze your code for bugs, security issues, "
        "code quality and possible improvements."
    )

    st.caption("Python • Streamlit • Gemini API")

left, right = st.columns(2, gap="large")

with left:
    st.subheader("💻 Your Code")

    code = st.text_area(
        "Code",
        height=500,
        placeholder="Paste your code here...",
        label_visibility="collapsed"
    )

    review_col, clear_col = st.columns(2)

    with review_col:
        review_button = st.button(
            "🔍 Review Code",
            use_container_width=True
        )

    with clear_col:
        clear_button = st.button(
            "🗑️ Clear",
            use_container_width=True
        )

if clear_button:
    st.session_state.pop("review", None)
    st.session_state.pop("code", None)
    st.session_state.pop("language", None)
    st.rerun()

with right:
    st.subheader("🤖 AI Review")

    if review_button:

        if not code.strip():
            st.warning("Please paste some code first.")

        else:

            prompt = f"""
You are an expert software code reviewer.

The programming language is strictly {language}.

Review the following {language} code.

Do not convert the code to another programming language.

Use exactly these sections:

## Summary
Give a short overall summary.

## Bugs and Errors
Find syntax, runtime, logical, or potential errors.
If there are none, say so.

## Security Issues
Identify security vulnerabilities or unsafe practices.
If there are none, say so.

## Code Quality
Review readability, naming, structure, maintainability, and best practices.

## Improvements
Give practical improvements the developer can make.

## Suggested Fix
Provide an improved version of the code in the SAME {language} programming language.
Do not convert it to Java, Python, JavaScript, C++, or any other language.

Keep the review concise and easy to understand.

Programming Language:
{language}

Code:
{code}
"""

            with st.spinner("AI is reviewing your code..."):

                try:
                    response = client.models.generate_content(
                        model="gemini-3.5-flash-lite",
                        contents=prompt
                    )

                    st.session_state.review = response.text
                    st.session_state.code = code
                    st.session_state.language = language

                except Exception as e:
                    st.error(
                        "Gemini is temporarily unavailable. Please try again."
                    )
                    st.caption(str(e))

    if "review" in st.session_state:

        st.markdown(
            '<div class="review-box">',
            unsafe_allow_html=True
        )

        st.markdown(st.session_state.review)

        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("### 🛠️ Fix My Code")

        fix_button = st.button(
            "✨ Generate Improved Code",
            use_container_width=True
        )

        if fix_button:

            selected_language = st.session_state.language
            original_code = st.session_state.code
            review = st.session_state.review

            fix_prompt = f"""
You are an expert {selected_language} developer.

You are given source code written in {selected_language}.

Your task is to fix and improve the code.

STRICT RULES:

1. The output MUST be written in {selected_language}.
2. NEVER convert the code to another programming language.
3. Preserve the original programming language.
4. Preserve the original functionality unless a change is required to fix a bug.
5. Fix the bugs and errors identified in the review.
6. Improve code quality where appropriate.
7. Do not add unnecessary features.
8. Return ONLY valid {selected_language} source code.
9. Do not include explanations.
10. Do not include Markdown code fences.
11. Do not write Java code unless the selected language is Java.
12. Do not write Python code unless the selected language is Python.
13. Do not write JavaScript code unless the selected language is JavaScript.
14. Do not write C++ code unless the selected language is C++.

Selected programming language:

{selected_language}

Original code:

{original_code}

AI review:

{review}

Return only the corrected {selected_language} code.
"""

            with st.spinner("Generating improved code..."):

                try:

                    fixed_response = client.models.generate_content(
                        model="gemini-3.5-flash-lite",
                        contents=fix_prompt
                    )

                    fixed_code = fixed_response.text.strip()

                    if fixed_code.startswith("```"):
                        lines = fixed_code.splitlines()

                        if lines and lines[0].startswith("```"):
                            lines = lines[1:]

                        if lines and lines[-1].strip() == "```":
                            lines = lines[:-1]

                        fixed_code = "\n".join(lines).strip()

                    st.markdown("### ✅ Improved Code")

                    st.code(
                        fixed_code,
                        language=selected_language.lower()
                    )

                except Exception as e:
                    st.error(
                        "Unable to generate improved code. Please try again."
                    )
                    st.caption(str(e))

    else:

        st.markdown(
            """
            <div class="review-box">
            <h3>Ready to review</h3>
            <p>Paste your code and click <b>Review Code</b>.</p>
            <p>The AI will analyze bugs, security,
            code quality and possible improvements.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

st.markdown(
    '<div class="footer">AI Code Review Assistant</div>',
    unsafe_allow_html=True
)