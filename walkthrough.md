# Medical Expert System Implementation Walkthrough

The AI Medical Expert System is now fully implemented and functioning. It accurately demonstrates the key concepts from your Artificial Intelligence course through an interactive Python Streamlit application.

## System Features and AI Concepts Implemented

1. **Knowledge Representation (Unit V):** 
   - Found in `knowledge_base.py`.
   - The Knowledge Base (KB) is a structured dictionary mapping diseases to their `Core` and `Secondary` symptoms. It also includes recommendations (`Next Steps` and `Precautions`).

2. **Goal-Based Agent (Unit I):**
   - The inference engine (`engine.py`) acts as the agent. Its primary definition of success is a **Confidence Threshold >= 80%**. Once a target candidate hits this score, the agent stops querying the user and concludes the diagnosis.

3. **Forward Chaining (Unit V):**
   - Implemented as the first phase of the app. The user selects their initial symptoms (Percepts) which triggers the data-driven initial filter. The engine identifies any diseases that intersect with these symptoms and ranks them dynamically.

4. **Backward Chaining (Unit V):**
   - After ranking candidates in the first phase, the system identifies the "highest probability" diseases and switches to a hypothesis-driven approach. It looks up the missing symptoms required to confirm these high-probability diseases and asks targeted `Yes/No` questions to the user.

5. **State-Space Search (Unit II):**
   - When determining which question to ask next during Backward Chaining, the engine traverses the hypothesis space systematically: it exhausts checks for `Core` symptoms before it moves on to checking `Secondary` symptoms.
   - An **Explanation Module** is included at the bottom of the UI, giving a full trace of the reasoning tree right up to the goal state.

6. **Technical Constraints:**
   - Powered by Streamlit (`app.py`).
   - Uses `hashlib` to generate stable widget keys for dynamic `Yes/No` buttons to prevent session state resets.
   - Includes a permanent Educational Simulation Disclaimer.

## Testing and Verification

The system was verified using an automated browser workflow to test the accuracy of the rule firing and the user interface.

### Demonstration & Visuals

Here is an overview of the system reaching a successful diagnosis for COVID-19 by tracing the user's symptoms:

![Diagnostic App Completing a Goal Tree](/C:/Users/user/.gemini/antigravity/brain/fd1aaf36-3cd6-4bfa-b6b8-edae3ca4f803/medical_system_demo_1774778233282.webp)

And here is the final state showing the **Goal Reached**, the diagnosis, and the **Explanation Module** tracing the Forward and Backward chaining path:

![Diagnosis Completed Screenshot](/C:/Users/user/.gemini/antigravity/brain/fd1aaf36-3cd6-4bfa-b6b8-edae3ca4f803/diagnosis_reached_covid19_1774778451283.png)

## Running the Application

The application is already running locally on your machine at [http://localhost:8501](http://localhost:8501).
If you need to start it manually in the future, navigate to the `ai health` directory and run:

```bash
python -m streamlit run app.py
```
