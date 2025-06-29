from utils import (
    ask_ibm,
    ai_requirements_analysis,
    ai_design_suggestion,
    auto_code_generator,
    smart_test_automation,
    smart_deployment,
    predictive_maintenance
)

def smart_sdlc_pipeline(project_description):
    print("🚀 Starting Smart SDLC Pipeline...\n")

    reqs = ai_requirements_analysis(project_description)
    print(f"🧾 Requirements:\n{reqs}\n")

    design = ai_design_suggestion(reqs)
    print(f"📐 Design:\n{design}\n")

    code_info = auto_code_generator(design)
    print(f"💻 Code:\n{code_info}\n")

    test_result = smart_test_automation()
    print(f"✅ Testing:\n{test_result}\n")

    if "passed" in test_result.lower():
        deploy_status = smart_deployment()
        print(f"🚚 Deployment:\n{deploy_status}\n")

        maintenance_tip = predictive_maintenance()
        print(f"🔧 Maintenance:\n{maintenance_tip}\n")
    else:
        print("❌ Tests failed. Fix issues before deploying.\n")

    print("✅ SDLC Pipeline Completed.")
