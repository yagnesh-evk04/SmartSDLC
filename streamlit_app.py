import json
from utils import extract_json_from_codeblock
import streamlit as st
from utils import (
    ai_requirements_analysis,
    ai_design_suggestion,
    auto_code_generator,
    smart_test_automation,
    smart_deployment,
    predictive_maintenance
)


st.title("✨ Smart SDLC ")

project_input = st.text_area("Enter your project description:", height=150)

if st.button("Get Response"):
    if project_input.strip():
        st.info("SDLC is here...")

        # 1. Requirements
        requirements_raw = ai_requirements_analysis(project_input)
        with st.expander("🧾 Requirements"):
            try:
                cleaned = extract_json_from_codeblock(requirements_raw)
                st.json(json.loads(cleaned))
            except:
                st.write(requirements_raw)

        # 2. Architecture
        design_raw = ai_design_suggestion(requirements_raw)
        with st.expander("📐 Design"):
            try:
                cleaned = extract_json_from_codeblock(design_raw)
                st.json(json.loads(cleaned))
            except:
                st.write(design_raw)

        # 3. Code Output
        code = auto_code_generator(design_raw)
        with st.expander("💻 Code"):
            st.write(code)

        # 4. Test Results
        test_result = smart_test_automation(design_raw)
        with st.expander("✅ Testing"):
            st.write(test_result)

        # 5. Deployment & Maintenance
        test_result_lower = test_result.lower()
        with st.expander("🚚 Deployment"):
            st.success(smart_deployment(design_raw))
        with st.expander("🔧 Maintenance"):
            st.write(predictive_maintenance(design_raw))

        
    else:
        st.warning("Please enter a project description.")
