import pickle
import streamlit as st


# --------------------------------------------------
# Load TF-IDF Vectorizer
# --------------------------------------------------
@st.cache_resource
def load_vectorizer(vectorizer_path):
    with open(vectorizer_path, "rb") as file:
        vectorizer = pickle.load(file)

    return vectorizer


# --------------------------------------------------
# Load Trained Model
# --------------------------------------------------
@st.cache_resource
def load_model(model_path):
    with open(model_path, "rb") as file:
        model = pickle.load(file)

    return model


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Email Spam Detector",
    page_icon="📩",
    layout="centered"
)


# --------------------------------------------------
# UI
# --------------------------------------------------
st.title("📩 Email Spam Detection")

st.write(
    "Enter the email subject and content. "
    "The email will be converted into TF-IDF features and "
    "passed to the trained machine learning model."
)


# --------------------------------------------------
# Pickle File Paths
# --------------------------------------------------
model_path = "multinomial_naive_bayes_model.pkl"
vectorizer_path = "tfidf_vectorizer.pkl"


# --------------------------------------------------
# Load Model and Vectorizer
# --------------------------------------------------
try:
    model = load_model(model_path)
    vectorizer = load_vectorizer(vectorizer_path)

except FileNotFoundError as e:
    st.error(f"File not found: {e}")
    st.stop()

except Exception as e:
    st.error(f"Error loading pickle files: {e}")
    st.stop()


# --------------------------------------------------
# Email Input
# --------------------------------------------------
subject = st.text_input(
    "📌 Email Subject",
    placeholder="Enter email subject..."
)

content = st.text_area(
    "📝 Email Content",
    placeholder="Enter email content...",
    height=250
)


# --------------------------------------------------
# Prediction
# --------------------------------------------------
if st.button("🔍 Check Email", type="primary"):

    # Check empty input
    if not subject.strip() and not content.strip():
        st.warning("⚠️ Please enter the email subject or content.")
        st.stop()

    # Combine subject + content
    email_text = f"{subject} {content}".strip()

    # --------------------------------------------------
    # Convert text → TF-IDF vector
    # --------------------------------------------------
    features = vectorizer.transform([email_text])

    # st.write(
    #     f"TF-IDF Features: {features.shape[1]}"
    # )

    # --------------------------------------------------
    # Model Prediction
    # --------------------------------------------------
    prediction = model.predict(features)[0]

    # --------------------------------------------------
    # Prediction Probability
    # --------------------------------------------------
    confidence = None

    if hasattr(model, "predict_proba"):

        probabilities = model.predict_proba(features)[0]

        confidence = max(probabilities) * 100


    # --------------------------------------------------
    # Display Result
    # --------------------------------------------------

    # Your dataset uses:
    # 1 = Spam
    # 0 = Ham

    if prediction == 1:

        st.error("🚨 SPAM EMAIL")

        st.subheader("Prediction")
        st.write("This email is predicted as **SPAM**.")

    else:

        st.success("✅ HAM / NOT SPAM")

        st.subheader("Prediction")
        st.write("This email is predicted as **HAM (Not Spam)**.")


    # --------------------------------------------------
    # Confidence
    # --------------------------------------------------

    # if confidence is not None:

    #     st.info(
    #         f"🎯 Model Confidence: **{confidence:.2f}%**"
    #     )


    #---------------------------------------
    # Footer
    #---------------------------------------

st.info(
    "⚠️ Note: Predictions are based on the trained dataset and may not always "
    "be accurate. Please double-check important emails."
)