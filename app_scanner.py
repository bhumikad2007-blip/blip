import streamlit as st

st.set_page_config(page_title="AI Notes Scanner", page_icon="📝", layout="centered")
st.title("📝 Smart Campus Notes Scanner & Flashcard Maker")
st.markdown("---")

st.subheader("📸 Step 1: Capture or Upload Notes")
captured_image = st.camera_input("Take a photo of your handwritten notes or textbook page")
uploaded_file = st.file_uploader("Or select a picture from your device storage gallery", type=["jpg", "png", "jpeg"])

active_image = captured_image if captured_image is not None else uploaded_file

if active_image is not None:
    st.success("✅ Image captured successfully!")
    st.image(active_image, caption="Uploaded Notes Processing View", use_container_width=True)
    
    st.markdown("---")
    st.subheader("🤖 Step 2: AI Automated Extraction & Summary")
    
    if st.button("Extract and Generate Flashcards"):
        with st.spinner("AI parsing image structures..."):
            extracted_text = "Sample Extracted Text: Quick sort uses a divide-and-conquer strategy. It picks an element as a pivot and partitions the array around it. The time complexity in the average case is O(n log n), and the worst case is O(n^2)."
            
            st.info("📊 Extracted Raw Text Data Layer")
            st.write(extracted_text)
            
            st.markdown("---")
            st.subheader("💡 Step 3: Generated Active-Recall Study Cards")
            
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("### ❓ Question 1")
                st.write("What core paradigm does the Quick Sort algorithm use?")
                if st.button("Reveal Answer 1"):
                    st.success("🎯 Divide and Conquer strategic partitioning.")
            
            with col2:
                st.markdown("### ❓ Question 2")
                st.write("What is the average-case runtime complexity?")
                if st.button("Reveal Answer 2"):
                    st.success("🎯 O(n log n) efficiency performance scale.")
else:
    st.info("💡 Open this portal on your phone or use your webcam to capture text records.")