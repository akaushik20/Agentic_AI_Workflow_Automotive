# 🔋 Agentic AI Workflow for EV Battery Health Monitoring

This project demonstrates an **autonomous Agentic AI workflow** for **predictive maintenance in electric vehicles (EVs)** using synthetic battery health data. Built using **LangGraph**, **Streamlit**, and optional **LLMs (Gemini)**, this proof-of-concept showcases how multi-agent systems can autonomously monitor, plan, and schedule service.

---

## 🚗 Project Overview

### ✳️ Agents in the Workflow

1. **BatteryInsightAgent**

   * Analyzes battery usage logs and degradation trends.

2. **ServicePlannerAgent**

   * Decides whether service is needed and recommends actions.

3. **SchedulerAgent**

   * Simulates booking an appointment with a service center.

4. **CommunicatorAgent**

   * Prepares user-facing messages. Optionally integrates LLM for enhanced explanation.

---

## 📁 Folder Structure

```
Agentic_AI_Workflow_Automotive/
├── agents/                  # Agent classes for battery, planning, scheduler, communication
├── langgraph/               # LangGraph orchestrator and shared state
├── data/                    # Synthetic dataset and generator
├── app.py                   # Streamlit front-end
├── README.md                # This file
└── requirements.txt         # Python dependencies
```

---

## 🧪 How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/akaushik20/Agentic_AI_Workflow_Automotive.git
cd Agentic_AI_Workflow_Automotive
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Generate Synthetic Battery Data (Optional)

```bash
python data/synthetic_data_generator.py
```

This will create a file called `battery_logs.csv`.

### 4. Run the Streamlit App

```bash
streamlit run app.py
```

### 5. Upload Data and Run Workflow

* Use the sidebar to upload `battery_logs.csv`
* Click **"🔁 Run Agentic AI Workflow"**
* View agent insights and final recommendations
* (Optional) Click **"🧠 Explain with AI"** for Gemini-generated explanation

### 6. (Optional) Use Gemini LLM

If you want to enable LLM-based explanations:

```bash
pip install google-generativeai
export GOOGLE_API_KEY=your_gemini_api_key_here
```

---

## 🌐 Tech Stack

* 🧠 LangGraph: Agent orchestration and state management
* 📊 Streamlit: Frontend for interactive UI
* 🤖 Gemini (optional): LLM explanation of recommendations
* 📁 Pandas/NumPy: Data handling and generation

---

## 📌 Key Highlights

* Modular, autonomous agents with clear responsibilities
* LangGraph-driven shared state and workflow
* Realistic synthetic EV battery logs
* Fully interactive UI with explainable AI option

---

## 📬 Future Enhancements

* Incorporate real-world EV datasets (Open Datasets, Fleet APIs)
* Add a memory layer or context preservation between runs
* Extend to other components: tires, brakes, drivetrain
* Plug into real service booking APIs

---

## 🤝 Contributions

Feel free to fork the repo and contribute! Pull requests are welcome.


---

**Built by [@akaushik20](https://github.com/akaushik20)** for academic research and industry prototyping.
